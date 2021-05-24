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

def quiz_1():
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
if __name__ == "__main__":
    quiz_1()