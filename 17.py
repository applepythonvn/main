import turtle as tt

tt.bgcolor('black')
tt.pensize(2)
tt.speed(100)

# Lặp lại tổng cộng sáu lần
for i in range(6):

    # Chọn sự kết hợp màu của bạn
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        tt.color(color)
         
        
        # Vẽ một vòng tròn với kích thước đã chọn, 100 ở đây
        tt.circle(105)
         
        
        # Di chuyển 10 pixel sang trái để vẽ một vòng tròn khác
        tt.left (10)
     
    # Ẩn con trỏ (hoặc con rùa) đã vẽ vòng tròn
    tt.hideturtle ()
input()