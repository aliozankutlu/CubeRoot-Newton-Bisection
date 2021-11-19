def find_cube_root(x):
    for a in range(0, abs(x)+1):
        if a**3 >= abs(x):
            break
    if a**3 != abs(x):
        return 0
    else:
        if x < 0:
            a = -a
    return a       

def bisection(x):
    epsilon = 0.01
    step = epsilon**3
    numGuesses = 0
    ans = 0.0
    while abs(ans**3 - x) >= epsilon and ans <= x:
        ans += step
        numGuesses += 1

    if abs(ans**3 - x) >= epsilon:
        return 0
    else:
        return ans



def newtonRapson(x):
    epsilon = 0.01
    guess = x/2.0
    while abs(guess**3 - x) >= epsilon:
        guess = guess - (((guess**3) - x) / (guess**3))
        
    return guess


print(find_cube_root(64))
print(bisection(64))
print(newtonRapson(64))
