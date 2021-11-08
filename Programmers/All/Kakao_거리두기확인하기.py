'''
개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

대기실은 5개이며, 각 대기실은 5x5 크기입니다.
거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

예를 들어,
위 그림처럼 자리 사이에 파티션이 존재한다면 맨해튼 거리가 2여도 거리두기를 지킨 것입니다.
위 그림처럼 파티션을 사이에 두고 앉은 경우도 거리두기를 지킨 것입니다.
위 그림처럼 자리 사이가 맨해튼 거리 2이고 사이에 빈 테이블이 있는 경우는 거리두기를 지키지 않은 것입니다.

응시자가 앉아있는 자리(P)를 의미합니다.	빈 테이블(O)을 의미합니다.	파티션(X)을 의미합니다.
5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
'''
def solution(places):
    global count
    count = 0
    answer = []
    def checkit(list):
        for one in list:
            if one == 0:
                return 0
        return 1
    def seeifr(place,i,j,count):
        if j != 4:
            if place[i][j+1]=='P':      # 사람이 있으면 안 됨
                count = 0
                return 0
            elif place[i][j+1]=='X':    # 파티션은 프리패스
                count = 0
                return 1
            elif count == 0:
                count += 1
                total = []
                total.append(seeifr(place,i,j+1,1))
                total.append(seeifb(place,i,j+1,1))
                total.append(seeift(place,i,j+1,1))
                return checkit(total)
            else:
                count = 0
                return 2
        return 3
    def seeifl(place,i,j,count):
        if j != 0:
            if place[i][j-1]=='P':      # 사람이 있으면 안 됨
                return 0
            elif place[i][j-1]=='X':    # 파티션은 프리패스
                return 1
            elif count == 0:
                total = []
                total.append(seeifl(place,i,j-1,1))
                total.append(seeifb(place,i,j-1,1))
                total.append(seeift(place,i,j-1,1))
                return checkit(total)
            else:
                return 2
        return 3
    def seeifb(place,i,j,count):
        if i != 4:
            if place[i+1][j]=='P':      # 사람이 있으면 안 됨
                return 0
            elif place[i+1][j]=='X':    # 파티션은 프리패스
                return 1
            elif count == 0:
                total = []
                total.append(seeifb(place,i+1,j,1))
                total.append(seeifr(place,i+1,j,1))
                total.append(seeifl(place,i+1,j,1))
                return checkit(total)
            else:
                return 2
        return 3
    def seeift(place,i,j,count):
        if i != 0:
            if place[i-1][j]=='P':      # 사람이 있으면 안 됨
                return 0
            elif place[i-1][j]=='X':    # 파티션은 프리패스
                return 1
            elif count == 0:
                total = []
                total.append(seeift(place,i-1,j,1))
                total.append(seeifr(place,i-1,j,1))
                total.append(seeifl(place,i-1,j,1))
                return checkit(total)
            else:
                return 2
        return 3
    def find(place,i,j):
        allcounts = []
        allcounts.append(seeifr(place,i,j,0))
        allcounts.append(seeifl(place,i,j,0))
        allcounts.append(seeifb(place,i,j,0))
        allcounts.append(seeift(place,i,j,0))
        return checkit(allcounts)

    def room(place):
        check = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    check.append(find(place,i,j))
                elif i==4 and j==4:
                    check.append(1)
        return checkit(check)
                
    for place in places:
        answer.append(room(place))

    return answer