from random import random
from typing import List

def main():
    for i in range(10):
        input = random_path(6)
        print('Path: ' + input)
        (result, path) = dino(input)
        print(result)
        if result:
            print(path)
        print()

def dino(input: str) -> (bool, List[int]):
    path = [(0,1,1)] # (position, next_step, next_distance)
    while(len(path) > 0):
        position, next_step, next_distance = path.pop()
        if(position < len(input) and next_step < 2):
            terrain = input[position]
            if(terrain == 'F'):
                out_path = [i for (i,_,_) in path]
                out_path.append(position)
                return (True, out_path)
            if(terrain != 'L'):
                path.append((position, next_step + 1, next_distance + 1))
                position += next_distance
                next_step = (-1 if next_distance > 1 else 0)
                next_distance = next_distance + next_step
                path.append((position, next_step, next_distance))
    return (False, [])

def random_path(length:int) -> str:
    path = 'B'
    for i in range(length):
        path += ('R' if random() > 0.3 else 'L')
    path += 'F'
    return path

if __name__ == "__main__":
    main()
