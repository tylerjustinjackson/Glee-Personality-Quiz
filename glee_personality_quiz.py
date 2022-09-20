import time                             #import time to add delays

def main():                             #greeting
    print("")
    name = input("Hello! You are about to take the Glee personality quiz. What's your name? ").strip().title()
    print(f"""
Hello {name}, please only input alphabetical values""")
    time.sleep(0.75)

def intro_vs_extro():                    #determines is user is introert of extrovert
    try:
        if intro >= extro:
            introcharacterdetermine()
        elif extro > intro:
            extrocharacterdetermine()
    except:
        error()

def extrocharacterdetermine():           #if extrovert determines work ethic and maturity
    try:
        if mature > immature:
            if ethic_high > ethic_low:
                print("Congrats! Your Character is Will Schuester!")
            else:
                print("Congrats! Your Character is Santana Lopez")
        elif mature < immature:
            if ethic_high > ethic_low:
                print("Congrats! Your Character is Rachel Berry!")
            else:
                print("Congrats! Your Character is Noah Puckerman!")
    except:
        error()

def introcharacterdetermine():           #if introvert, determines maturity
    try:
        if mature > immature:
            print("Congrats! Your character is Finn Hudson!")
        else:
            print("Congrats! Your character is Britany S. Pierce!")
    except:
        error()

def error():
    print("Your submission is invalid. Please retake the quiz")

main()              #start of active code sequence, calls greeting 
    
intro = 0           #preset values for later personality calculations
extro = 0
mature = 0
immature = 0
ethic_high=0
ethic_low=0
success_high=0
success_low=0

#sequence of 10 questions to gauge personality traits
#question 1
while True:
    time.sleep(0.3)
    print("""
Question 1...
On a Friday night, would you rather:
A) Go to Breadstix with friends
B) Watch reruns of shows at home""")
    q1=input("Answer: ").strip().lower()
    if "b" == q1 or "watch reruns of shows at home" == q1:
        intro += 1
        break
    elif "a" == q1 or "go to Breadstix with friends" == q1:
        extro+=1
        break
    else:
        print("invalid response...")
        continue


#question 2
while True:   
    time.sleep(0.3)
    print("""
Question 2...
If Mercedes Jones demanded a solo due to Rachel Berry taking them all, would you:
A) Demand the whole group get a fair shot
B) Demand she get a solo""")
    q2=input("Answer: ").strip().lower()
    if "a" == q2 or "demand the whole group get a fair shot" == q2:
        immature += 1
        break
    elif "b" == q2 or "demand she get a solo" == q2:
        mature+=1
        break
    else:
        print("invalid response...")
        continue

#question 3
while True:    
    time.sleep(0.3)
    print("""
Question 3...
In the choir room, would you rather:
A) Sing the sectionals solo
B) Perform choreo with the group""")
    q3=input("Answer: ").strip().lower()
    if "b" == q3 or "perform choreo with the group" == q3:
        intro += 1
        break
    elif "a" == q3 or "sing the sectionals solo" == q3:
        extro+=1
        break
    else:
        print("invalid response...")
        continue

#question 4
while True:     
    time.sleep(0.3)
    print("""
Question 4...
During audition season, would you
A) Practice relentlessly to get the perfect audition number
B) Practice a little but mainly let the audience feel the raw emotion""")
    q4=input("Answer: ").strip().lower()
    if "a" == q4 or "practice relentlessly" in q4:
        ethic_high += 1
        break
    elif "b" == q4 or "practice a little" == q4:
        ethic_low+=1
        break
    else:
        print("invalid response...")
        continue

#question 5
while True:     
    time.sleep(0.3)
    print("""
Question 5...
Would you prefer to be the
A) Duet partner
B) Lead singer""")
    q5=input("Answer: ").strip().lower()
    if "b" == q5 or "lead singer" == q5:
        extro += 1
        break
    elif "a" == q5 or "duet partner" == q5:
        intro+=1
        break
    else:
        print("invalid response...")
        continue

#question 6
while True:     
    time.sleep(0.3)
    print("""
Question 6...
If someone says something mean to you, would you
A) Let it roll off your back
B) Confront them about their behavior""")
    q6=input("Answer: ").strip().lower()
    if "a" == q6 or "roll off" in q6:
        mature += 1
        break
    elif "b" == q6 or "confront" in q6:
        immature+=1
        break
    else:
        print("invalid response...")
        continue

#question 7    
while True:
    time.sleep(0.3)
    print("""
Question 7...
What are you better at?
A) Making tough decisions
B) Being a creative spirit""")
    q7=input("Answer: ").strip().lower()
    if "a" == q7 or "tough decision" in q7:
        intro += 1
        break
    elif "b" == q7 or "creative spirit" in q7:
        extro+=1
        break
    else:
        print("invalid response...")
        continue

#question 8
while True:
    time.sleep(0.3)
    print("""
Question 8...
In ten years, do you see yourself
A) Being wildly successful in your career in a big city
B) Staying close to home while still having impact on your field of study""")
    q8=input("Answer: ").strip().lower()
    if "a" == q8 or "city" in q8 or "wildly successful" in q8:
        success_high += 1
        break
    elif "b" == q8 or "home" in q8 or "close" in q8 or "impact" in q8:
        success_low+=1
        break
    else:
        print("invalid response...")
        continue

#question 9    
while True:  
    time.sleep(0.3)
    print("""
Question 9...
What is your favorite color?
A) Yellow
B) Pink
C) Black
D) Blue""")
    q9=input("Answer: ").strip().lower()
    if "a" == q9 or "b"==q9 or "yellow"==q9 or "pink"==q9:
        extro += 1
        break
    elif "c" == q9 or "d" == q9 or "black"==q9 or "blue"==q9:
        intro+=1
        break
    else:
        print("invalid response...")
        continue
    
#question 10    
while True:      
    time.sleep(0.3)
    print("""
Question 10...
Who would you rather vote into office?
A) Oprah Winfrey
B) Spongebob""")
    q10=input("Answer: ").strip().lower()
    if "a" == q10 or "ophrah winfrey" == q10 or "ophrah" == q10 or "winfrey" ==q10:
        mature += 1
        break
    elif "b" == q10 or "spongebob" == q10:
        immature+=1
        break
    else:
        print("invalid response...")
        continue

for _ in range(4):
    time.sleep(0.1)                     #starts calculation process and lets user wait a couple seconds
print("""
DONE!

Findng character match...""", end="")
time.sleep(2.5)
print("Results...")
time.sleep(1.1)
intro_vs_extro()