try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(f"발생한 예외: {type(e).__name__}")
    print(f"예외 메시지: {e}")