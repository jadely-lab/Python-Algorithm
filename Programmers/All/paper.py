
def solution(numbers):
    numbers = sorted(numbers)
    n = 0
    add = 0
    for a in range(0,10):
        print("a=",a)
        if n == len(numbers):
            break
        elif numbers[n] == a:
            print(n,"th is", a)
            n += 1
        else:
            print(a, add)
            add += a
    return add

numbers = [1,2,3,4,6,7,8,0]
solution(numbers)