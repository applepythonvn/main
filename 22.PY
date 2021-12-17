#The 21 Game

# trả về bội số gần nhất với 4
def gannhat(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near
  
def lose1():
    print ("\n\nYOU LOSE !")
    print("Chúc may mắn lần sau !")
    exit(0)
      
# kiểm tra xem các số có liên tiếp không
def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True
  
# bắt đầu trò chơi
def start1():
    xyz = []
    last = 0
    while True:
        print ("Nhập 'F' để có cơ hội đầu tiên. ")
        print("Nhập 'S' để có cơ hội thứ hai.")
        chance = input('> ')
          
        # người chơi có cơ hội đầu tiên
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print ("\nLượt của bạn.")
                    print ("\nBạn muốn nhập bao nhiêu số?")
                    inp = int(input('> '))
                      
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print ("Nhập sai. Bạn bị loại khỏi trò chơi.")
                        lose1()
              
                    i, j = 1, 1
  
                    print ("Bây giờ hãy nhập các giá trị")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i = i + 1
                      
                    # lưu trữ phần tử cuối cùng của xyz.
                    last = xyz[-1] 
                      
                    ## kiểm tra xem đầu vào
                    # số liên tiếp
                    if check(xyz) == True: 
                        if last == 21:
                            lose1()
                              
                        else:
                            # "Đến lượt máy tính."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Thứ tự các đầu vào sau lượt của máy tính là: ")
                            print (xyz)
                            last = xyz[-1]
                    else:
                        print ("\nBạn đã không nhập các số nguyên liên tiếp.")
                        lose1()
                          
        #người chơi có cơ hội thứ hai
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                # "Đến lượt máy tính"
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print ("Thứ tự các đầu vào sau lượt của máy tính là: ")
                print (xyz)
                if xyz[-1] == 20:
                    lose1()
                      
                else:
                    print ("\nLượt của bạn.")
                    print ("\nBạn muốn nhập bao nhiêu số?")
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print ("Nhập giá trị của bạn")
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i = i + 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        # print (xyz)
                        near = gannhat(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        # nếu đầu vào không liên tiếp
                        # tự động bị loại
                        print ("\ nBạn không nhập các số nguyên liên tiếp.")
                        # print ("Bạn bị loại khỏi trò chơi.")
                        lose1()
            print ("\n\nXIN CHÚC MỪNG !!!")
            print ("YOU WON !")
            exit(0)
              
        else:
            print ("sự lựa chọn sai lầm")
                          
          
game = True    
while game == True:
        print ("Trình phát 2 là Máy tính.")
        print ("Bạn có muốn chơi trò chơi số 21 không? (Có / Không)")
        ans = input ('>')
        if ans == 'có':
            start1()
        else:
            print ("Bạn có muốn thoát khỏi trò chơi không? (có / không)")
            nex = input ('>')
            if nex == "có":
                print ("Bạn đang thoát khỏi trò chơi ...")
                exit (0)
            elif nex == "không":
                print ("Đang tiếp tục ...")
            else:
                print ("Lựa chọn sai")