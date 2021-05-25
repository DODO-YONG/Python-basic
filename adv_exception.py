def handling_exception():
    """


    :return:
    """
    try:
        lst = list()
        # lst[3] = 1
        # 4/0
        # int("String")
        print(int("12345"))
    except ValueError as e:
        print("정수로 변환 불가")
        print(e, type(e))
    except IndexError as e:
        print("인덱스에 접근 불가")
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.")
        print(e, type(e))
    except Exception as e:
        print("Error")
        print(e, type(e))
    else: # try이 블럭에서 예외없을 때 한 번 실행
        print("예외없음")
    finally:
        print("예외처리 종료")

def raise_exception():
    """
    예외 위임
    :return:
    """
    def beware_dog(animal):
        if animal == "dog":
            raise RuntimeError("강아지는 출입을 제한합니다.")
        else:
            print(animal, "어서오세요!")
    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))

    print("end of code")
if __name__ == "__main__":
    # handling_exception()
    raise_exception()