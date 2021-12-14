num = int(input("Số tiền bạn muốn chi: "))

if num >= 150:
	print("Giảm giá còn: ", num - 50)
elif num >= 100:
	print("Giảm giá còn: ", num - 25)
elif num >= 75:
	print("Giảm giá còn: ", num - 15)
else:
    print("Không được giảm giá: ", num)