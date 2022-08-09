for tc in range(10):
    tc_num = int(input())
    search_data = str(input())
    data = str(input())

    result = 0

    for i in range(len(data) - len(search_data) + 1):
        if data[i:i+len(search_data)] == search_data:
            result += 1

    print('#{} {}'.format(tc_num, result))
