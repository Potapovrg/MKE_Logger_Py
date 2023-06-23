import pyautogui
import time

prev_x, prev_y = pyautogui.position()
last_move_time = time.time()

while True:
    x, y = pyautogui.position()
    if (x, y) != (prev_x, prev_y):
        current_time = time.time()
        time_diff = round((current_time - last_move_time) * 1000)
        diff_x, diff_y = x - prev_x, y - prev_y
        print(f"Текущие координаты мышки: x={x}, y={y}, перемещение: dx={diff_x}, dy={diff_y}, время: {time_diff} мс")
        prev_x, prev_y = x, y
        last_move_time = current_time