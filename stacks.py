def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets[closing_brackets.index(char)] != stack.pop():
                return False

    return not stack
        