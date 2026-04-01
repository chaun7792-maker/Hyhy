import turtle
import math
import random

# ==========================================
# CẤU HÌNH HỆ THỐNG
# ==========================================
def setup_canvas():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor("#0a0a0a")  # Đen sâu thẳm
    screen.title("TERRA PROJECT - THE ULTIMATE VISION")
    screen.tracer(0)  # Tăng tốc độ vẽ tối đa
    return screen

def draw_star(t, x, y):
    """Vẽ các tinh thể ánh sáng xung quanh"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    color = random.choice(["#DAA520", "#FFFFFF", "#8B4513"])
    t.color(color)
    size = random.randint(1, 3)
    for _ in range(4):
        t.forward(size)
        t.backward(size)
        t.left(90)

# ==========================================
# THÂN MÁY CHÍNH CỦA SIÊU PHẨM
# ==========================================
def create_masterpiece():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    
    # 1. Vẽ nền tinh thể (Ambient Stars)
    for _ in range(100):
        draw_star(t, random.randint(-600, 600), random.randint(-400, 400))

    # 2. Thuật toán vẽ cấu trúc Terra (Lõi Đất Vĩnh Cửu)
    # Kết hợp màu sắc: Nâu đất, Vàng đồng, Hổ phách và Trắng bạc
    palette = ["#4B2E1E", "#8B4513", "#CD853F", "#DAA520", "#FFD700", "#FFFFFF"]
    
    for i in range(400):
        t.pencolor(palette[i % 6])
        
        # Công thức toán học tạo hình xoắn ốc đa chiều
        phi = i * (math.pi * (3 - math.sqrt(5)))  # Golden angle
        distance = i * 0.8
        x = distance * math.cos(phi)
        y = distance * math.sin(phi)
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        t.setheading(i * 1.5)
        t.forward(i / 4)
        t.left(45)
        t.width(i / 100 + 1)
        
        # Tạo hiệu ứng hào quang sau mỗi 50 bước
        if i % 60 == 0:
            t.stamp()

    # 3. Chữ nghệ thuật (Typography)
    t.penup()
    t.goto(0, -320)
    t.color("#DAA520")
    t.write("T  E  R  R  A", align="center", font=("Verdana", 40, "bold"))
    
    t.goto(0, -370)
    t.color("white")
    t.write("VỮNG NHƯ THẠCH - BẢN LĨNH TIÊN PHONG", align="center", font=("Courier", 15, "italic"))

# ==========================================
# THI ĐIỂM CHẠY
# ==========================================
if __name__ == "__main__":
    scr = setup_canvas()
    create_masterpiece()
    scr.update() # Cập nhật toàn bộ hình ảnh một lần để tạo hiệu ứng bất ngờ
    print("Siêu phẩm đã sẵn sàng diện kiến!")
    scr.exitonclick()
