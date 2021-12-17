def cach1():
    try:
        n = int(input("Nhập 1 số từ 1-9: "))
        if n<1 or n>9:
            print("Chi tinh duoc bang cuu chuong 1 den 9 thoi!")
        else:
            print("-"*50)
            print("Bẳng cửu chuong ",n)    
            for i in range(1, 10):
                print("{} x {} = {}".format(n, i, n*i))
    except:
        print("Dinh dang dau vao khong hop le!")

def cach2():
    n = int(input("Nhập 1 số: "))
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n*i))
cach2()