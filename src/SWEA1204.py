test_case = int(input())

for _ in range(test_case):
    tc = int(input())
    nums = list(map(int, input().split()))

    num_max = max(nums)
    num_cnt = [0 for _ in range(num_max + 1)]

    for i in nums:
        num_cnt[i] += 1

    result = 0
    result_data = 0
    for i in range(len(num_cnt)):
        if num_cnt[i] >= result_data:
            result = i
            result_data = num_cnt[i]

    print('#{} {}'.format(tc, result))
