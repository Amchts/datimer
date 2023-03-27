import time
import datetime
import re

#get input and fix/read it
userInput = input("Enter timer amount:\n")
userInput = userInput.lower()
ptn1 = bool(re.search(":", userInput))
ptn2 = bool(re.search("\D+", userInput))
ptn3 = userInput.count(" and ")

#define functions
def countdown(totalsec):
    while totalsec > 0:
        totalsec = totalsec - 1
        actualtimer = datetime.timedelta(seconds = totalsec)
        print(actualtimer, end="\r")
        time.sleep(1)
    print("That's it. It's been: " + answer)

def numberversion():
    x = userInput
    splitTxt = x.split(":")  
    totalinsec = (((int(splitTxt[0])) * 3600) + ((int(splitTxt[1])) * 60) + (int(splitTxt[2])))
    # totalinsec = int((((splitTxt[0]) * 3600) + ((splitTxt[1]) * 60) + (splitTxt[2])))
    countdown(totalinsec)

def wordversion():
    answer = userInput
    arethereanynumbers = bool(re.search("\d+", answer))
    if arethereanynumbers is True:
        splittxt = answer.split()  
        numberportion = int(splittxt[0])
        unitportion = str(splittxt[1])
        if "hour" in unitportion:
            totalsec = (numberportion * 3600)
        elif "min" in unitportion:
            totalsec =  (numberportion * 60)
        elif "sec" in unitportion:
            totalsec = numberportion
        else:
            print("did you spell it wrong?")
            exit()
        countdown(totalsec)
    else:
        print("there are no numbers. try again")

def andfunction():
  if ptn3 == 1:
    x = userInput.split(" and ")
    a = x[0].split()
    b = x[1].split()
    firstnumberportion = int(a[0])
    firstunitportion = str(a[1])
    secondnumberportion = int(b[0])
    secondunitportion = str(b[1])
    if "hour" in firstunitportion:
      totalsec1 = (firstnumberportion * 3600)
    if "min" in firstunitportion:
      totalsec1 =  (firstnumberportion * 60)
    if "sec" in firstunitportion:
      totalsec1 = firstnumberportion
    if "hour" in secondunitportion:
      totalsec = (totalsec1 + (secondnumberportion * 3600))
    if "min" in secondunitportion:
      totalsec =  (totalsec1 + (secondnumberportion * 60))
    if "sec" in secondunitportion:
      totalsec = (totalsec1 + secondnumberportion)
  elif ptn3 == 2:
    x = userInput.split(" and ")
    a = x[0].split()
    b = x[1].split()
    c = x[2].split()
    firstnumberportion = int(a[0])
    firstunitportion = str(a[1])
    secondnumberportion = int(b[0])
    secondunitportion = str(b[1])
    thirdnumberportion = int(c[0])
    thirdunitportion = str(c[1])
    if "hour" in firstunitportion:
      totalsec1 = (firstnumberportion * 3600)
    if "min" in firstunitportion:
      totalsec1 =  (firstnumberportion * 60)
    if "sec" in firstunitportion:
      totalsec1 = firstnumberportion
    if "hour" in secondunitportion:
      totalsec2 = (totalsec1 + (secondnumberportion * 3600))
    if "min" in secondunitportion:
      totalsec2 =  (totalsec1 + (secondnumberportion * 60))
    if "sec" in secondunitportion:
      totalsec2 = (totalsec1 + secondnumberportion)
    if "hour" in thirdunitportion:
      totalsec = (totalsec2 + (thirdnumberportion * 3600))
    if "min" in thirdunitportion:
      totalsec =  (totalsec2 + (thirdnumberportion * 60))
    if "sec" in thirdunitportion:
      totalsec = (totalsec2 + thirdnumberportion)
  countdown(totalsec)

#The actual running functions part
if ptn1 is True:
    numberversion()
elif ptn2 is True and ptn3 == 0:
    wordversion()
elif ptn3 > 0:
    andfunction()