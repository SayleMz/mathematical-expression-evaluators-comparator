def evaluate(expression: str):
    """
    Évalue une expression mathématique donnée sous forme de chaîne de caractères.
    
    Cette fonction gère les opérations de base (+, -, *, /) ainsi que les parenthèses pour 
    respecter les priorités des opérations. Elle utilise une approche basée sur une pile 
    pour stocker et évaluer les expressions.
    """

    def calculate(expression, it: int):
        """
        Fonction récursive interne pour analyser et calculer l'expression.

        Args:
            expression (str): L'expression mathématique à évaluer.
            it (int): Position actuelle dans la chaîne de caractères de l'expression.
        
        Returns:
            Tuple: Un tuple contenant la valeur calculée de l'expression et la position actuelle de l'itération.
        """
        stack = []  # Pile pour stocker les valeurs intermédiaires des calculs.
        current = 0  # Entier pour construire progressivement un nombre à partir de caractères.
        operator = '+'  # Opérateur actuel, initialisé à '+' par défaut.

        def update(stack, operator, value):
            """
            Applique l'opération spécifiée à la pile.

            Cette fonction utilise l'opérateur et la valeur actuels pour mettre à jour la pile
            avec le résultat de l'opération. Elle gère les quatre opérations de base.

            Args:
                stack (list): La pile utilisée pour stocker les valeurs.
                operator (char): L'opérateur à appliquer ('+', '-', '*', '/').
                value (int): La valeur à utiliser avec l'opérateur.
            """
            if operator == '+':
                stack.append(value)
            elif operator == '-':
                stack.append(-value)
            elif operator == '*':
                stack.append(stack.pop() * value)
            elif operator == '/':
                # Division entière pour éviter les problèmes de précision avec les flottants.
                stack.append(stack.pop() / value)

        while it < len(expression):
            if expression[it] == ' ':
                it += 1
                continue
            elif expression[it] in '+-*/':
                update(stack, operator, current)
                current = 0
                operator = expression[it]
            elif expression[it] == '(':
                # Traitement récursif des expressions entre parenthèses.
                current, it = calculate(expression, it + 1)
                it -= 1
            elif expression[it] == ')':
                update(stack, operator, current)
                # Retour de la somme des valeurs dans la pile et de l'index actuel.
                return sum(stack), it + 1
            else:
                # Construction du nombre actuel à partir des chiffres consécutifs.
                current = current * 10 + int(expression[it])
            it += 1

        update(stack, operator, current)
        return sum(stack)

    # Appel initial de la fonction de calcul.
    return calculate(expression, 0)
