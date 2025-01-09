def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    top_rows = []
    bottom_rows = []
    dashes = []
    answers = []


    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and one operator."
        
        num1, operator, num2 = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if len(num1) > 4  or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        if operator == '+':
            answer = str(int(num1) + int(num2))
        else:
            answer = str(int(num1) - int(num2))

        width = max(len(num1), len(num2)) + 2
        top_row = ' ' * (width - len(num1)) + num1
        bottom_row = operator + ' ' + ' ' * (width - len(num2) - 2) + num2
        dash = '-' * width
        answer_row = ' ' * (width - len(answer)) + answer

        top_rows.append(top_row)
        bottom_rows.append(bottom_row)
        dashes.append(dash)
        answers.append(answer_row)

        arranged_problems = '    '.join(top_rows) + '\n' + \
                        '    '.join(bottom_rows) + '\n' + \
                        '    '.join(dashes)

        if show_answers:
            arranged_problems += '\n' + '    '.join(answers)
    return arranged_problems


result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(result)