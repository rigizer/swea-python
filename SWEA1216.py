MATRIX_SIZE = 100
TEST_CASE = 10

result = 0

def search_palindrome(arr):
    global result
    for i in range(MATRIX_SIZE):
        for n in range(result, MATRIX_SIZE):
            for j in range(MATRIX_SIZE - n + 1):
                if arr[i][j:j + n] == arr[i][j:j + n][::-1] and result < n:
                    result = n
                    break


def arr_matrix(arr):
    # 전치행렬 초기값 생성
    temp_arr = [[0 for r in range(MATRIX_SIZE)] for c in range(MATRIX_SIZE)]

    # 기존 행렬에 바로 집어넣으면 데이터를 절반까지 못 넣기 때문에
    # 전치행렬에 대한 임시변수를 선언한 다음
    # 기존 행렬을 탐색하며 전치한 좌표에 대해 전치행렬에 값을 삽입한다
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            temp_arr[j][i] = arr[i][j]

    return temp_arr


# 테스트케이스 10회
for tc in range(TEST_CASE):
    tc_num = int(input())
    arr = [list(input()) for _ in range(MATRIX_SIZE)]

    # 가로 탐색
    search_palindrome(arr)

    # 전치행렬화
    arr = arr_matrix(arr)

    # 세로 탐색
    search_palindrome(arr)

    # 데이터 출력
    print('#{} {}'.format(tc_num, result))

    result = 0
