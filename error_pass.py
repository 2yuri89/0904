try:
    f = open("나 없는 파일", 'r')
except FileNotFoundError:   # 파일이 없더라도 오류가 발생하지 않고 통과
    pass
