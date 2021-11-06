'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    from itertools import permutations
    ans = []
    def forlen(len):
        global nums
        nums = [''.join(p) for p in permutations(numbers,len)]
        for num in nums:
            num = int(num)
            ans.append(num)
        
    for i in range(len(numbers)):
        forlen(i+1)
        
    ans = sorted(set(ans))
    answer = []
    
    def isit(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    for one in ans:
        if isit(one) == True:
            answer.append(one)
        
    return len(answer)