# 입력된 숫자 목록에서 가장 많이 나온 숫자와 그 횟수를 찾는 프로그램
# 예시) [1, 2, 3, 2, 1, 3, 1, 4, 2, 1] 이 주어졌을 때,
# - 가장 많이 나온 숫자는 1이고
# - 1이 나온 횟수는 4번임을
# 인쇄하는 함수!


def find_most_frequent_number_naive(numbers):
    """입력된 숫자 목록에서 가장 많이 나온 숫자와 그 횟수를 찾는 프로그램(O(N^2))"""
    max_count = 0  # 입력된 숫자 목록에서 가장 많이 나온 숫자의 횟수
    most_frequent = None  # 가장 많이 나온 숫자

    for number in numbers:

        current_count = 0  # 현재 반복문 내에서 숫자 count

        for current_num in numbers:
            if current_num == number:
                current_count += 1

        if current_count > max_count:
            max_count = current_count
            most_frequent = number

    return most_frequent, max_count


def find_most_frequent_number_optimal(numbers):
    count_dict = {}

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    max_count = 0
    most_frequent = None

    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent = num

    return most_frequent, max_count


# 실행 결과:
# 입력된 숫자 목록: [1, 2, 3, 2, 1, 3, 1, 4, 2, 1]
#
# 첫 번째 방법(느린 방법)의 결과:
# 가장 많이 나온 숫자는 1이고, 4번 나왔어요!
#
# 두 번째 방법(빠른 방법)의 결과:
# 가장 많이 나온 숫자는 1이고, 4번 나왔어요!

numbers = [1, 2, 3, 2, 1, 3, 1, 4, 2, 1]
print("입력된 숫자 목록:", numbers)
print("\n첫 번째 방법(느린 방법)의 결과:")
number, count = find_most_frequent_number_naive(numbers)
print(f"가장 많이 나온 숫자는 {number}이고, {count}번 나왔어요!")

print("\n두 번째 방법(빠른 방법)의 결과:")
number, count = find_most_frequent_number_optimal(numbers)
print(f"가장 많이 나온 숫자는 {number}이고, {count}번 나왔어요!")
