status = (100,500)
match status:
    case (x,y):
        print(f"X and Y are: {x}, {y}")
    case x:
        print(x)

status = 42
match status:
    case (x,y):
        print(f"X and Y are: {x}, {y}")
    case x:
        print(x)