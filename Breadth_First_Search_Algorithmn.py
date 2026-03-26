# Breadth First Search Algorithm

# This algorithm is used to generate all combinations of well-formed parentheses given a number of pairs. It uses a queue to explore all possible combinations level by level, ensuring that the generated parentheses are valid at each step.
def gen_parentheses(pairs):
    if not isinstance(pairs, int): # Check if the input is an integer
        return 'The number of pairs should be an integer'
    if pairs < 1: # Check if the number of pairs is at least 1
        return 'The number of pairs should be at least 1'
    
    queue = [('', 0, 0)] # Initialize the queue with an empty string and counts of open and close parentheses used
    result = [] # Initialize the result list to store valid combinations
    while queue: # Continue until the queue is empty
        current, opens_used, closes_used = queue.pop(0)
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    
    return result

print(gen_parentheses(3))


## Output:['((()))', '(()())', '(())()', '()(())', '()()()']