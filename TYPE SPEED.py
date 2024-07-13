from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay, 2)
    speed = len(userinput) / time_roundoff
    return round(speed)

while True:
    check = input("Are you ready for the test -----> (Yes / No) : ")
    if check == "Yes":
        test = [
            "My name is Lakshay Verma", 
            "I am a BUDDING SOFTWARE ENGINEER",
            "I am a student of B.Tech in COMPUTER SCIENCE & ENGINEERING",
            "I am currently pursuing my engineering from KCC INSTITUTE OF TECHNOLOGY & MANAGEMENT",
            "I am a student of 3rd year",
            "TECHNOLOGIES I KNOW : HTML, CSS, JavaScript, C - Language, Python, JAVA, MySQL",
            "I am a good learner and I am always ready to learn new things",
            "I am a good team player and I always try to help my team members",
            "I am a good listener and I always try to understand the problem before solving it",
            "I am a good problem solver and I always try to find the best solution for the problem",
            "I am a good communicator and I always try to communicate with my team members",
            "I am a good leader and I always try to lead my team members",
            "I am a good follower and I always try to follow my team members",
            "I am a good decision maker and I always try to make the best decision for the team",
            "I am a good time manager and I always try to manage my time efficiently",
            "I am a good multitasker and I always try to do multiple tasks at the same",
        ]
        test1 = r.choice(test)
        print("<----- Typing Speed ----->")
        print(test1)
        print()
        print()

        time_1 = time()
        testinput = input(" Enter : ")
        time_2 = time()

        print(" Speed : ", speed_time(time_1, time_2, testinput),"w/sec")
        print(" Mistakes : ", mistake(test1, testinput))

    elif check == "No":
        print("Bye, Good day :->")
        break

    else:
        print("Invalid Input")
