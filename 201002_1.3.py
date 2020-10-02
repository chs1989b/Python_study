shirt_size = ['xs', 's', 'm', 'l', 'xl', 'xxl', 's', 'm', 'l', 'xl']

def solution(shirt_size):
    answer = [0 for _ in range(6)]
    for ss in shirt_size:
        if ss == 'xs':
            answer[0] += 1
        if ss == 's':
            answer[1] += 1
        if ss == 'm':
            answer[2] += 1
        if ss == 'l':
            answer[3] += 1
        if ss == 'xl':
            answer[4] += 1
        if ss == 'xxl':
            answer[5] += 1
    return answer

print(solution(shirt_size))