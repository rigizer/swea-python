# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD

from collections import deque

for tc in range(10):
    tc_num = int(input())

    queue = deque([i for i in list(map(int, input().split()))])
    idx = 1
    while True:
        idx = 1 if idx > 5 else idx

        data = queue.popleft() - idx
        if data <= 0:
            queue.append(0)
            break

        queue.append(data)
        idx += 1

    t = [str(queue.popleft()) + ' ' for _ in range(8)]
    print('#{} {}'.format(tc_num, ''.join(t)))
