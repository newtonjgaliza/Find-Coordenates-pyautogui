import pyautogui
import time

print("Mova o mouse até o elemento desejado.")
print("Você tem 5 segundos para se preparar...")

# Aguarda 5 segundos para dar tempo de preparar
time.sleep(5)

# Captura as coordenadas do mouse
x, y = pyautogui.position()

print(f"As coordenadas do mouse são: X={x}, Y={y}")
