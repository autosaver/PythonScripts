import pyautogui
from tqdm import tqdm
import time
import random

def sleep_with_progress(seconds):
    for _ in tqdm(range(seconds), desc="Waiting to start....", ncols=100):
        time.sleep(random.uniform(0.8, 1.2))  # Random sleep in the range of 0.8 to 1.2 seconds

sleep_with_progress(5)

start_time = time.time()
clicks_count = 0
failure_count = 0
scroll_amount = random.randint(300,500)

while failure_count<=5 and time.time() - start_time < random.randint(300,600):  # Run for up to x seconds
    try:
        box_pos = pyautogui.locateCenterOnScreen("follow_button.png")

        if box_pos is not None:
            follow_x, follow_y = box_pos
            print("Current button position: ", follow_x, follow_y)
            pyautogui.moveTo(follow_x, follow_y, random.uniform(0.05, 0.45))  # Move to the button in a random time between 0.8 and 1.5 seconds
            pyautogui.leftClick()  # Click on the button
            clicks_count+=1
            failure_count=0
        else:
            print("Button not found. Scrolling down")
            for _ in range(scroll_amount // 50):  # for slow scrolling
                pyautogui.scroll(-50)
                time.sleep(random.uniform(0.05, 0.12))  # Random sleep between 0.08 and 0.15 seconds

    except pyautogui.ImageNotFoundException:
        print("Image not found. Scrolling down...")
        for _ in range(scroll_amount // 50):  # Slow scroll in case of exception
            pyautogui.scroll(-50)
            time.sleep(random.uniform(0.05, 0.12))  # Random sleep between 0.08 and 0.15 seconds

    time.sleep(random.uniform(0.05, 0.30))  # Random sleep between 0.4 and 0.6 seconds after each iteration
    failure_count+=1

if failure_count <= 5:
    print("Script Complete. Total Clicks: ", clicks_count)
    pyautogui.alert("Script Complete. Total Clicks: " + str(clicks_count))
else:
    print("Script failed to complete. Total Clicks: ", clicks_count)
    pyautogui.alert("Script failed to complete. Total Clicks: " + str(clicks_count))
