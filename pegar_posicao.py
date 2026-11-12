import time
import pyautogui

# utilitario para descobrir a posicao (x, y) de um campo na tela
print("Coloque o mouse em cima do campo e deixe parado.")
for segundos in range(10, 0, -1):
    print(f"Pegando a posicao em {segundos}...")
    time.sleep(1)

print("Posicao do mouse:", pyautogui.position())
