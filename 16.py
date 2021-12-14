chieucao = float(input("Bạn cao bao nhiêu m: "))
cannang = float(input("Bạn nặng bao nhiêu Kg: "))
BMI = cannang / (chieucao * chieucao)

print('-'*40)
print("Chỉ số BMI đối với người trên 20 tuổi được phân loại và diễn giải theo bảng sau:\n")
print("BMI < 16: Gầy cấp độ III")
print("16 <= BMI < 17:  Gầy cấp độ II")
print("17<= BMI < 18.5: Gầy cấp độ I")
print("18.5 <= BMI < 25: Bình thường")
print('25 <= BMI < 30: Thừa cân')
print('30 <= BMI < 35 : Béo phì cấp độ I')
print('35 <= BMI < 40: Béo phì cấp độ II')
print('BMI > 40: Béo phì cấp độ III')
print('-'*40)

print("CHỈ SỐ BMI CỦA BẠN LÀ: ",int(BMI))

if BMI < 16:
    print("Gầy cấp độ III")
elif 16 <= BMI < 17:
    print("Gầy cấp độ II")
elif 17 <= BMI < 18.5:
    print("Gầy cấp độ I")
elif 18.5 <= BMI < 25:
    print("Bình thường")
elif 25 <= BMI < 30:
    print("Thừa cân")
elif 30 <= BMI < 35:
    print("Béo phì cấp độ I")
elif 35 <= BMI < 40:
    print("Béo phì cấp độ II")
elif BMI > 40:
    print("Béo phì cấp độ III")