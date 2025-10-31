"""
Mathematical Expression Evaluator
A simple program that reads math problems from a file, solves them using stack magic,
and writes the answers to another file.
"""

def create_stack():
    """Make a new empty stack (just a simple list)"""
    return []

def push(stack, item):
    """Put an item on top of the stack"""
    stack.append(item)

def pop(stack):
    """Take the top item off the stack"""
    if not is_empty(stack):
        return stack.pop()
    return None

def peek(stack):
    """Look at the top item without removing it"""
    if not is_empty(stack):
        return stack[-1]
    return None

def is_empty(stack):
    """Check if the stack has nothing in it"""
    return len(stack) == 0

def get_operator_importance(operator):
    """Some math operators are more important than others"""
    if operator in ['+', '-']:
        return 1
    elif operator in ['*', '/']:
        return 2
    return 0

def convert_to_computer_friendly(expression):
    """
    Convert normal math expression to computer-friendly format
    (This is called 'postfix' notation - computers understand it better)
    """
    operator_stack = create_stack()
    output_tokens = []
    
    for character in expression:
        if character.isdigit() or character == '.':
            # Handle numbers with multiple digits and decimals
            if output_tokens and (output_tokens[-1].isdigit() or output_tokens[-1][-1] == '.'):
                output_tokens[-1] += character
            else:
                output_tokens.append(character)
        elif character in '+-*/':
            # Handle math operators based on their importance
            while (not is_empty(operator_stack) and 
                   get_operator_importance(peek(operator_stack)) >= get_operator_importance(character)):
                output_tokens.append(pop(operator_stack))
            push(operator_stack, character)
        elif character == '(':
            push(operator_stack, character)
        elif character == ')':
            while not is_empty(operator_stack) and peek(operator_stack) != '(':
                output_tokens.append(pop(operator_stack))
            pop(operator_stack)  # Remove the '('
        
        # Add space to separate numbers and operators
        if output_tokens and not character.isdigit() and character != '.' and output_tokens[-1] != ' ':
            output_tokens.append(' ')
    
    # Add any remaining operators
    while not is_empty(operator_stack):
        output_tokens.append(' ')
        output_tokens.append(pop(operator_stack))
    
    return ''.join(output_tokens).strip()

def solve_computer_friendly(expression):
    """Solve the computer-friendly expression using stack magic"""
    number_stack = create_stack()
    parts = expression.split()
    
    for part in parts:
        if part.replace('.', '').isdigit():  # It's a number (either whole or decimal)
            push(number_stack, float(part))
        else:
            # It's an operator - we need two numbers to work with
            if len(number_stack) < 2:
                return "Oops! This math doesn't make sense"
            
            number2 = pop(number_stack)
            number1 = pop(number_stack)
            
            if part == '+':
                result = number1 + number2
            elif part == '-':
                result = number1 - number2
            elif part == '*':
                result = number1 * number2
            elif part == '/':
                if number2 == 0:
                    return "Can't divide by zero!"
                result = number1 / number2
            else:
                return f"Unknown operator: {part}"
            
            push(number_stack, result)
    
    if len(number_stack) != 1:
        return "Something's wrong with this math problem"
    
    final_result = pop(number_stack)
    # Return nice-looking result (whole number if possible, otherwise decimal)
    return int(final_result) if final_result == int(final_result) else round(final_result, 2)

def solve_math_problem(problem):
    """Solve a single math problem"""
    try:
        # Clean up the problem by removing spaces
        problem = problem.replace(' ', '')
        if not problem:
            return "Empty problem"
        
        # Make sure only valid characters are used
        allowed_characters = set('0123456789+-*/.() ')
        if any(char not in allowed_characters for char in problem):
            return "Invalid characters in the problem"
        
        # Convert and solve
        computer_friendly_version = convert_to_computer_friendly(problem)
        answer = solve_computer_friendly(computer_friendly_version)
        return answer
    except Exception as error:
        return f"Error: {str(error)}"

def process_math_file(input_filename='input.txt', output_filename='output.txt'):
    """Read math problems from file, solve them, and write answers"""
    try:
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()
        
        answers = []
        
        for line in lines:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            elif line == '---':  # This is just a separator
                answers.append('---')
            else:
                # Solve this math problem
                answer = solve_math_problem(line)
                answers.append(str(answer))
        
        # Write all answers to the output file
        with open(output_filename, 'w') as output_file:
            for answer in answers:
                output_file.write(answer + '\n')
        
        print(f" All done! Check {output_filename} for your answers!")
        
    except FileNotFoundError:
        print(f" Couldn't find {input_filename}")
    except Exception as error:
        print(f" Something went wrong: {str(error)}")

def main():
    """The main function that runs our math solver"""
    print(" Welcome to the Math Problem Solver!")
    print("=" * 40)
    
    # Process the input file automatically
    process_math_file()
    
    # Let users try their own problems
    print("\n Want to try some problems yourself?")
    print("Type a math problem or 'bye' to exit")
    
    while True:
        user_problem = input("\n➡  Enter a math problem: ").strip()
        
        if user_problem.lower() in ['bye', 'exit', 'quit']:
            print(" Thanks for using the Math Solver!")
            break
        elif user_problem:
            answer = solve_math_problem(user_problem)
            print(f" Answer: {answer}")

# This makes the program run when we execute the file
if __name__ == "_main_":
    main()