def evaluate(expression: str):
    """
    Évalue une expression mathématique donnée sous forme de chaîne de caractères.

    Cette fonction, comme la précédente, gère les opérations de base et les parenthèses.
    Elle utilise une liste de listes pour gérer les différentes profondeurs des parenthèses.

    Args:
        expression (str): L'expression mathématique à évaluer.
    """

    current = 0  # Nombre actuel en cours de construction
    operator = '+'  # Opérateur actuel, initialisé à '+'
    depth = [[]]  # Liste de listes représentant les différentes profondeurs de l'expression
    n = len(expression)  # Longueur de l'expression

    for i in range(n + 1):
        # Traitement des caractères spéciaux ou fin de l'expression
        if i == n or expression[i] in '-+*/)':
            # Applique l'opérateur actuel au nombre actuel et le stocke dans la profondeur appropriée
            if operator == '+':
                depth[-1].append(current)
            elif operator == '-':
                depth[-1].append(-current)
            elif operator == '*':
                depth[-1].append(depth[-1].pop() * current)
            elif operator == '/':
                depth[-1].append(depth[-1].pop() / current)
            
            if i == n:
                break  # Fin de l'expression

            # Gestion des parenthèses fermantes
            if expression[i] == ')':
                current = sum(depth.pop())  # Calcule la somme à la profondeur actuelle
                operator = depth[-1].pop()  # Récupère l'opérateur précédent
            else:
                operator = expression[i]  # Mise à jour de l'opérateur
                current = 0  # Réinitialisation du nombre actuel

        # Gestion des parenthèses ouvrantes
        elif expression[i] == '(':
            depth[-1].append(operator)  # Sauvegarde l'opérateur associé à la profondeur actuelle actuel
            operator = '+'  # Réinitialisation de l'opérateur
            depth.append([])  # Ajout d'une nouvelle profondeur
        else:
            # Construction du nombre actuel
            current = current * 10 + int(expression[i])

    return sum(depth[-1])  # Retourne la somme des nombres à la profondeur la plus externe
