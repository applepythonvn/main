def homnaylathu(i):
        switcher={
                1:'Chủ nhật',
                2:'Thứ 2',
                3:'Thứ 3',
                4:'Thứ 4',
                5:'Thứ 5',
                6:'Thứ 6',
                7:'Thứ 7'
             }
        return switcher.get(i,"không có thứ mà bạn muốn")
print("-"*40)

print('1:Chủ nhật')

print("-"*40)

print('2:Thứ 2')

print("-"*40)

print('3:Thứ 3')

print("-"*40)

print('4:Thứ 4')

print("-"*40)

print('5:Thứ 5')

print("-"*40)

print('6:Thứ 6')

print("-"*40)

print('7:Thứ 7')

print("-"*40)

i = int(input("Hôm nay là thứ mấy? "))
print(homnaylathu(i))
