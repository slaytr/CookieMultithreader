import threading
import time

# Simple multithreading example in python
def cook_a_cookie(number, letter):
    while number < 1000:
        print("Cookie #{} Batch #{}".format(number, letter))
        number += 1

Cookie_Cooker_One = threading.Thread(target=cook_a_cookie, args=(0, "A"))
Cookie_Cooker_Two = threading.Thread(target=cook_a_cookie, args=(3, "B"))
Cookie_Cooker_Two.start()
Cookie_Cooker_One.start()
time.sleep(5)

Cookie_Cooker_One.join()
Cookie_Cooker_Two.join()