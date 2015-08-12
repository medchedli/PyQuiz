 # -*- coding: utf-8 -*-
import random
print "WELCOME:"
print "-------------------------------------------------------------------------------"
print "This project was done on the 2k15 Summer Camp organized by AJST"
print "-------------------------------------------------------------------------------"
print "The work was done, in collaboration, by Habib Debaya, Neirouz Aljene, and Jassem Ben Jaber"
print "-------------------------------------------------------------------------------"
h=raw_input("Click enter to continue")
print "-------------------------------------------------------------------------------"
print "This project consists of a small Quiz determining your knowledge in many"
print "different areas."
print "-------------------------------------------------------------------------------"
print "We will now start the test."
print "-------------------------------------------------------------------------------"
h=raw_input("Click enter to continue")
print "-------------------------------------------------------------------------------"
print "You get extra 10 points for each correct answer. Play carefully and try reaching"
print "a perfect score of 100 to get a small prize."
print "-------------------------------------------------------------------------------"
print "Don't forget that also, if you at least get 5 right answers, you'll be rewarded"
print "with a small game."
print "-------------------------------------------------------------------------------"
print "You will also get the option to ask for a correction at the end of the test."
print "-------------------------------------------------------------------------------"
print "May the odds be ever in your favor."
print "-------------------------------------------------------------------------------"
h=raw_input("Click enter to continue")
##Used Variables
y=0
n=0
z=0
f=0
qf1=0
qf2=0
qf3=0
qf4=0
qf5=0
qf6=0
qf7=0
qf8=0
qf9=0
qf10=0
##Used Functions
def false(f):
    if f==0:
        print "(_)\n/|\ \n |\n/ \ "
    if f==1:
        print "\n \n \n \n \n \n _____|_____"
    if f==2:
        print "     |\n     |\n     |\n     |\n     |\n     |\n_____|_____"
    if f==3:
        print "      _______\n     |/\n     |\n     |\n     |\n     |\n     |\n_____|_____"
    if f==4:
        print "      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |\n     |\n     |\n_____|_____"
    if f==5:
        print "      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |      / \ \n     |\n_____|_____"
        print "Bob is dead"
        print "All is done"
        print "Bob will forever haunt you."
        print "Bob will live in your dreams."
        print "Bob is everywhere."
def wrong(n):
        if n==1:
                print "First Wrong Answer"
                print "Oh, it looks like you're starting to make mistakes :/"
        if n==2:
                print "Second Wrong Answer"
                print "Come on, one mistake is bad enough but TWO ??!!"
        if n==3:
                print "Third Wrong Answer"
                print "THREE MISTAKES ? How wrong can your answers be?"
        if n==4:
                print "Fourth Wrong Answer"
                print "I guess this answers the last question. Four mistakes? I hope you're taking this test seriously."
        if n==5:
                print "Fifth Wrong Answer"
                print "Good job, you've now failed half of this test."
        if n==6:
                print "Sixth Wrong Answer"
                print "I can't believe your winning percentage is going to be under 50% ... Get your stuff together."
        if n==7:
                print "Seventh Wrong Answer"
                print "7 FREAKING MISTAKES ... There's no going back now."
        if n==8:
                print "Eighth Wrong Answer"
                print "Okay, I am starting to give up on you :("
        if n==9:
                print "Ninth Wrong Answer"
                print "You only have one more chance to get something done."
        if n==10:
                print "Tenth Wrong Answer"
                print "I regret giving you this test :("
def right(z, y):
        if y==1:
                print "First Right Answer"
                print "Good job, at least you got yourself a 10% winrate."
        if y==2:
                print "Second Right Answer"
                print "A 2nd correct answer. I think you're getting the hang of this game."
        if y==3:
                print "Third Right Answer"
                print "3 right answers is something you should always be proud of."
        if y==4:
                print "Fourth Right Answer"
                print "We could say you've covered all 4 corners of this test."
        if y==5:
                print "Fifth Right Answer"
                print "Another correct answer! High Five!"
        if y==6:
                print "Sixth Right Answer"
                print "I hope you keep this pace and get to 7 right answers!"
        if y==7:
                print "Seventh Right Answer"
                print "7 is the magic number. You got this in the bag !"
        if y==8:
                print "Eighth Right Answer"
                print "80% win rate? Amazing."
        if y==9:
                print "Ninth Right Answer"
                print "Almost there!!"
        if y==10:
                print "Tenth Right Answer"
                print "A perfect score!! Here is a small game for you!!"
                i = 1
                a = random.randint(1,100)
                print "-------------------------------------------------------------------------------"
                print "In this game, you're going to try guessing a number between 1 and 100"
                print "-------------------------------------------------------------------------------"
                print "Each time you enter your guess, we will tell you if it's greater or lesser than the wanted number"
                print "-------------------------------------------------------------------------------"
                n = input("Choose a number between 1 and 100 : ")
                while n != a :
                    if n < a :
                        n=input("Too small, try a greater number! ")
                        i+=1
                    elif n > a :
                        n=input("Too big, try a lesser number! ")
                        i+=1
                print "Game Over"
                print "Bravo :), You've cracked two games in a row !!"
                print "You managed to do it in", i ,"tries"


def points(z):
        print "Your score is now", z, "."
print "-------------------------------------------------------------------------------"
print "Q1 : What is the capital of Greece ?"
print "A = Thessaloniki   B = Athens   C = Chalcis"
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("B","b"):
        n+=1
        qf1=1
        wrong(n)
        break
while x in ("B", "b"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q2 : What is a baby lion called ?"
print "A = A Calf    B = A Pup   C = A Cub"
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("C","c"):
        n+=1
        qf2=1
        wrong(n)
        break
while x in ("C", "c"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q3 : Larry's father has five sons named Ten, Twenty, Thirty, Forty...Guess what would be the name of the fifth ?"
print "A = Fifty   B = Larry   C = Jacob"
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("B","b"):
        n+=1
        qf3=1
        wrong(n)
        break
while x in ("B", "b"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q4 : Which one of these animals' brain weighs the same as a human's ?"
print "A = Dolphin   B = Monkey   C = Elephant "
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("A","a"):
        n+=1
        qf4=1
        wrong(n)
        break
while x in ("A", "a"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q5 : How many animators does the energy section have ?"
print "A = 1 Animators   B = 2 Animators   C = 3 Animators "
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("C","c"):
        n+=1
        qf5=1
        wrong(n)
        break
while x in ("C", "c"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q6 : Which came first, Apple, Microsoft or Samsung ?"
print "A = Microsoft   B = Samsung   C = Apple "
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("B","b"):
        n+=1
        qf6=1
        wrong(n)
        break
while x in ("B", "b"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q7 : How many hairs does a human have ?"
print "A = 1.000.000   B = 100.000   C = 10.000 "
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("B","b"):
        n+=1
        qf7=1
        wrong(n)
        break
while x in ("B", "b"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q8 : When did Tunisia sign its independence treaty ?"
print "A = 20 Mars 1956   B = 5 Mars 1956   C = 5 December 1952 "
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("A","a"):
        n+=1
        qf8=1
        wrong(n)
        break
while x in ("A", "a"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q9 : Who started the GNU project ?"
print "A = Richard Stallman   B = Linus Torvalds    C = Bill Gates"
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("A","a"):
        n+=1
        qf9=1
        wrong(n)
        break
while x in ("A", "a"):
        z+=10
        y+=1
        right(z, y)
        break
points(z)
print "-------------------------------------------------------------------------------"
print "Q10 : How much wood would a woodchuck chuck if a woodchuck could chuck wood ?"
print "A = None   B = 532 kg   C = As much wood as a woodchuck could chuck if a"
print "                            woodchuck could chuck wood."
x=raw_input("Please write the letter corresponding to the correct answer >>> ")
while x not in ("C", "c"):
        n+=1
        qf10=1
        wrong(n)
        break
while x in ("C", "c"):
        z+=10
        y+=1
        points(z)
        right(z, y)
        break
print "-------------------------------------------------------------------------------"
if y<10:
        print "You've made", n, "mistakes"
m=raw_input("Write 'Correction' to get answers for the questions you failed to answer correctly, or write 'No' if you want to skip the correction \n")
if m in ("Correction", "correction") and y<=9:
    print "-------------------------------------------------------------------------------"
    print "Here are the corrections to the questions you failed to answer correctly"
    print "-------------------------------------------------------------------------------"
    if qf1==1:
            print "Correction to the first question: "
            print "Q1 : What is the capital of Greece ?"
            print "B = Athens"
            print "-------------------------------------------------------------------------------"
    if qf2==1:
            print "Correction to the second question: "
            print "Q2 : What is a baby lion called ?"
            print "C = A Cub"
            print "-------------------------------------------------------------------------------"
    if qf3==1:
            print "Correction to the third question: "
            print "Q3 : Larry's father has five sons named Ten, Twenty, Thirty, Forty...Guess what would be the name of the fifth ?"
            print "B = Larry"
            print "-------------------------------------------------------------------------------"
    if qf4==1:
            print "Correction to the fourth question: "
            print "Q4 : Which one of these animals' brain weighs the same as a human's ?"
            print "A = Dolphin"
            print "-------------------------------------------------------------------------------"
    if qf5==1:
            print "Correction to the fifth question: "
            print "Q5 : How many animators does the energy section have ?"
            print "C = 3"
            print "-------------------------------------------------------------------------------"
    if qf6==1:
            print "Correction to the sixth question: "
            print "Q6 : Which came first, Apple, Microsoft or Samsung ?"
            print "B = Samsung"
            print "-------------------------------------------------------------------------------"
    if qf7==1:
            print "Correction to the seventh question: "
            print "Q7 : How many hairs does a human have ?"
            print "B = 100.000"
            print "-------------------------------------------------------------------------------"
    if qf8==1:
            print "Correction to the eighth question: "
            print "Q8 : When did Tunisia sign its independence treaty ?"
            print "A = 20 Mars 1956"
            print "-------------------------------------------------------------------------------"
    if qf9==1:
            print "Correction to the nineth question: "
            print "Q9 : Who started the GNU project ?"
            print "A = Richard Stallman"
            print "-------------------------------------------------------------------------------"
    if qf10==1:
            print "Correction to the tenth question: "
            print "Q10 : How much wood would a woodchuck chuck if a woodchuck could chuck wood ?"
            print "C = As much wood as a woodchuck could chuck if a woodchuck could chuck wood."
if y>=5 and y<=9:
        print "-------------------------------------------------------------------------------"
        print "Since you've succefully answered more than 5 questions, you will be rewarded"
        print "with a small game"
        print "-------------------------------------------------------------------------------"
        print "Bob got mad because you answered his questions wrong so he decided to ask  for your help yet again but this time you need to win in order to save his life"
        print "-------------------------------------------------------------------------------"
        print "In this game, we will provide you with words that are missing some of their letters"
        print "and your job is to try and guess them"
        print "-------------------------------------------------------------------------------"
        g=raw_input("Write 'GO' to play \n")
        if g in ("Go", "GO", "go", "gO"):
            print "-------------------------------------------------------------------------------"
            print "LET'S GO"
            print "-------------------------------------------------------------------------------"
            print "Ob*iv**us"
            x=raw_input("Guess the missing characters by rewriting the whole word \n")
            print "-------------------------------------------------------------------------------"
            if x in ("Oblivious", "oblivious"):
                    print "Bob is going to get to live for another day thanks to you!"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            else:
                    f+=1
                    print "You guessed wrong."
                    print "The word is Oblivious."
                    print "Don't let Bob lose hope in you"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            print "-------------------------------------------------------------------------------"
            print "En***on***t"
            x=raw_input("Guess the missing characters by rewriting the whole word \n")
            print "-------------------------------------------------------------------------------"
            if x in ("Environment", "environment"):
                    print "Bob is yet again being saved from suicide"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            else:
                    f+=1
                    print "You guessed wrong."
                    print "The word is Environment."
                    print "Bob is getting even closer to death"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            print "-------------------------------------------------------------------------------"
            print "Sus**ci**s"
            x=raw_input("Guess the missing characters by rewriting the whole word \n")
            print "-------------------------------------------------------------------------------"
            if x in ("Suspicious", "suspicious"):
                    print "Good job, Bob is almost safe!"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            else:
                    f+=1
                    print "You guessed wrong."
                    print "The word is Suspicious."
                    print "Don't give up on Bob, save him !!"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            print "-------------------------------------------------------------------------------"
            print "Se**ibi***y"
            x=raw_input("Guess the missing characters by rewriting the whole word \n")
            print "-------------------------------------------------------------------------------"
            if x in ("Sensibility", "sensibility"):
                    print "Good job, you might actually do this!"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            else:
                    f+=1
                    print "You guessed wrong."
                    print "The word is Sensibility."
                    print "Avoid doing mistakes. You gotta save Bob"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            print "-------------------------------------------------------------------------------"
            print "An**y**us"
            x=raw_input("Guess the missing characters by rewriting the whole word \n")
            print "-------------------------------------------------------------------------------"
            if x in ("Anonymous", "anonymous"):
                    print "Such a nice way to end this small game"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            else:
                    f+=1
                    print "You guessed wrong."
                    print "The word is Anonymous."
                    print "Horrible ending but you can play this game again by getting the same score"
                    print "in the Quiz one more time :D"
                    print "-------------------------------------------------------------------------------"
                    false(f)
            if f<=4:
                print "-------------------------------------------------------------------------------"
                print "You only made", f, "mistakes"
                print "-------------------------------------------------------------------------------"
                print "Bob is safe"
                print "Bob is happy"
                print "(_)\n/|\ \n |\n/ \ "
raw_input()
