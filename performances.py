if __name__ == '__main__':
    from recursive import evaluate as eval_recursive
    from iterative import evaluate as eval_iterative
    from os import listdir
    from time import time

    directory = './testcases'
    competitors = {
        'built-in': eval,
        'recursive': eval_recursive,
        'iterative': eval_iterative
    }

    for filename in listdir(directory):
        with open(f'{directory}/{filename}') as file:
            print(f'Running on {filename}: ', end='\n\t')
            testcase = file.read()
            reference = None
            for competitor, function in competitors.items():
                print(competitor, end=': ')
                t = time()
                answer = function(testcase)
                print(f'{(time() - t):.5f}ms | ', end='')
                if reference is not None:
                    if reference != answer:
                        print('Provided answers do not match:')
                        print(f'ref: {reference} & ans: {answer}')
                        exit()
                    reference = answer
            print() # append newline