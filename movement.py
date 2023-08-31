from turtle import Turtle, Screen

tim = Turtle()

# Hareket fonksiyonlarını tanımla
def move_forward():
    tim.forward(10)  # İleri gitmek için belirli bir mesafe (örneğin 10 birim)

def move_backward():
    tim.backward(10)  # Geri gitmek için belirli bir mesafe

def turn_left():
    tim.left(10)  # Sola dönme açısı

def turn_right():
    tim.right(10)  # Sağa dönme açısı

# Ekranı dinleme moduna al
screen = Screen()

# Tuşlara basıldığında ilgili hareket fonksiyonunu çağır
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")

# Tuş dinlemeyi başlat
screen.listen()

# Ekranı kapatmak için tıklanmayı bekler
screen.exitonclick()