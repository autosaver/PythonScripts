import pyautogui
from tqdm import tqdm
import time
import random

def sleep_with_progress(seconds):
    for _ in tqdm(range(seconds), desc="Waiting to start....", ncols=100):
        time.sleep(random.uniform(0.8, 1.2))  # Random sleep in the range of 0.8 to 1.2 seconds

sleep_with_progress(5)

start_time = time.time()

scroll_amount = 300

while time.time() - start_time < 30:  # Run for up to 30 seconds
    try:
        box_pos = pyautogui.locateCenterOnScreen("follow_button.png")

        if box_pos is not None:
            follow_x, follow_y = box_pos
            print("Current button position: ", follow_x, follow_y)
            pyautogui.moveTo(follow_x, follow_y, random.uniform(0.8, 1.5))  # Move to the button in a random time between 0.8 and 1.5 seconds
            pyautogui.leftClick()  # Click on the button
        else:
            print("Button not found. Scrolling down")
            for _ in range(scroll_amount // 50):  # for slow scrolling
                pyautogui.scroll(-50)
                time.sleep(random.uniform(0.08, 0.15))  # Random sleep between 0.08 and 0.15 seconds

    except pyautogui.ImageNotFoundException:
        print("Image not found. Scrolling down...")
        for _ in range(scroll_amount // 50):  # Slow scroll in case of exception
            pyautogui.scroll(-50)
            time.sleep(random.uniform(0.08, 0.15))  # Random sleep between 0.08 and 0.15 seconds

    time.sleep(random.uniform(0.4, 0.6))  # Random sleep between 0.4 and 0.6 seconds after each iteration

print("Script Complete. Exiting...")
