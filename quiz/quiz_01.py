# Q1
# 파이썬 문자열을 다루는 퀴즈입니다
# 파일명은 quiz01_1.py로 저장합니다
# 다음과 같이 문자열이 담긴 변수가 있습니다.
# str = "Life is too short, You need Python"
# 이 문장에 총 몇 개의 알파벳 글자가 사용되었는지 판별해 봅시다.
# Instruction:
#







str = "Life is too short, You need Python"
# 이 문자열 내의 글자를 모두 소문자로 변경합니다.
def quiz_1():
    print(str.upper())
# 이 문자열 내의 공백과 ,를 제거합니다.
def quiz_2():
    str_1 = str.replace(" ", "").replace(",","")
    print(str_1)
# 이 문자열을 list로 형변환한 후 lst 변수에 담아 봅니다.
def quiz_3():
    str_2 = list(str)
    print(str_2)
# lst를 set로 형변환하여 chars 변수에 담아 봅시다.
# chars를 화면에 출력해 봅시다.
def quiz_4():
    str_2 = list(str)
    global chars
    chars = set(str_2)
    print(chars)

# chars를 다시 list로 형변환하여 lst에 담아 봅시다.
def quiz_5():
    global lst
    lst = list(chars)
    print(lst)
# lst를 알파벳 순으로 정렬하고, 길이를 출력해 봅시다.
def quiz_6():
    sort_lst = sorted(lst)
    print(sort_lst)
    print(len(sort_lst))
# 리스트와 사전을 다루는 퀴즈입니다.
# 파일명은 quiz01_3.py로 저장합니다
# 다음과 같이 사전을 포함한 리스트가 선언되어 있습니다.
#
# 두 학생의 kor, eng, math 합계 점수와 평균을 사전 데이터에 "total", "average" 키값으로 넣어 봅시다.

students = [
    {
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]

def quiz_1_3():
    # print(students.values())
    print(len(students))

    for i in range(len(students)):
        dict_total = 0
        count = 0
        for n,s in students[i].items():
            if isinstance(s, int):
                count += 1
                dict_total += s

        students[i].update({"total": dict_total})
        students[i].update({"average": round(dict_total/count,2)})
    print(students)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def quiz_1_2():
    slice = lst[3:7]
    slice.reverse()
    lst[3:7] = slice

    print(lst)


if __name__ == "__main__":
    quiz_1()
    quiz_2()
    quiz_3()
    quiz_4()
    quiz_5()
    quiz_6()
    quiz_1_2()
    quiz_1_3()