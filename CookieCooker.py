import threading
import time


cookies_list = []

# Simple multithreading example in python
def cook_a_cookie(number, letter):
    while number < 1000:
        finished_cookie = "Cookie #{} Batch #{}".format(number, letter)
        cookies_list.append(finished_cookie)
        number += 1
        print(finished_cookie)

def print_mixed_cookies(cookie_list):
    j = 'Placeholder Cookie Batch #0'
    batch_a = 0
    batch_b = 0
    for i in cookie_list:
        if i.split(" ")[3] != j.split(" ")[3]:
            print("{} and {} don't mix".format(i,j))
        elif j.split(" ")[3] == "#A":
            batch_a += 1
        else:
            batch_b +=1
        j=i
    print("Clustered Batch A's {} Clustered Batch B's {}".format(batch_a, batch_b))

Cookie_Cooker_One = threading.Thread(target=cook_a_cookie, args=(0, "A"))
Cookie_Cooker_Two = threading.Thread(target=cook_a_cookie, args=(3, "B"))
Cookie_Cooker_Two.start()
Cookie_Cooker_One.start()
time.sleep(5)

Cookie_Cooker_One.join()
Cookie_Cooker_Two.join()

print_mixed_cookies(cookies_list)