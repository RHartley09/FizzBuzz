# I like appending the result into a new list, because it prints the list, and not a bunch of strings.
# Give it a try: print(fizzBuzzBetter([_insert your list of integers here_]))

def fizzBuzzBetter(intArray):
    placeHere = []
    for n in intArray:
        if n % 3 == 0 and n % 5 == 0:
            placeHere.append("FizzBuzz")
        elif n % 3 == 0:
            placeHere.append("Fizz")
        elif n % 5 == 0:
            placeHere.append("Buzz")
        else:
            placeHere.append(n)
    return placeHere