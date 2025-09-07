import pyautogui
import time

rizzler = input("auto clicker or [blank]? ")
def main():
    skibidi = input("whats amount of clicks do you want?")
    skibidii = input("whats the interval between clicks?")

    try:
        print("Starting in 3 seconds...")
        time.sleep(1)
        print("3..")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1..")
    except KeyboardInterrupt():
        print("Process interrupted before start.")
        exit()

    try:
        for i in range(int(skibidi)):
            pyautogui.click()
            time.sleep(int(skibidii))
    except KeyboardInterrupt:
        print("Process interrupted by user.")
        exit()
    if KeyboardInterrupt:
        print("Done!")


if rizzler == "auto clicker":
    main()
else:
    print("no")
    exit()

