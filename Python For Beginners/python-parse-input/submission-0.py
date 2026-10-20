from typing import List

def read_integers() -> List[int]:
    user_input = input()
    user_input = user_input.split(',')
    ints = [int(i) for i in user_input]
    return ((ints))

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
