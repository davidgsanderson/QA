import math

#function to add two times - converts to minutes and then back to time
def addTime(time1, time2) :
    minutes1 = timeToMinutes(time1)
    minutes2 = timeToMinutes(time2)
    allMinutes = minutes1 + minutes2
    timeResult = convertTime(allMinutes)
    return timeResult

#function to minus two times - converts to minutes and back to time (ensures can't be negative)
def minusTime(time1, time2) :
    minutes1 = timeToMinutes(time1)
    minutes2 = timeToMinutes(time2)
    allMinutes = minutes1 - minutes2
    if allMinutes < 0 :
        allMinutes *= -1
    timeResult = convertTime(allMinutes)
    return timeResult

#function to convert time (DD:HH:MM) to minutes (used in most other functions)
def timeToMinutes(time) :
    allMinutes = (time[0] * 1440) + (time[1] * 60) + time[2]
    return allMinutes

#function to convert time (DD:HH:MM) to hours. converts time to minutes and then minutes to hours.
def timeToHours(time) :
    minutes = timeToMinutes(time)
    hours = minsToHours(minutes)
    return hours

#function to convert minutes to hours, rounds to two decimals
def minsToHours(minutes) :
    hours = minutes/60
    hours = round(hours, 2)
    return hours

#function to convert hours to days, round to two decimals
def hoursToDays(hours) :
    days = hours/24
    days = round(days, 2)
    return days

#function to convert from minutes back to time (DD:HH:MM)
def convertTime(minutes) :
    time = []
    days = math.floor(minutes / 1440)
    remainderMins = minutes % 1440
    hours = math.floor(remainderMins / 60)
    mins = minutes - (days*1440) - (hours*60)
    time.append(days)
    time.append(hours)
    time.append(mins)
    time = castStr(time)
    return time

#helper function to cast input time into list or integers
def castInt(time) :
    time[0] = int(time[0])
    time[1] = int(time[1])
    time[2] = int(time[2])
    return time

#helper function to cast time back into string format for output
def castStr(time) :
    time[0] = str(time[0])
    time[1] = str(time[1])
    time[2] = str(time[2])

    result = time[0] + ":" + time[1] + ":"  + time[2]
    
    return result

#Function to receive two Time string
def getTwoInputs() :
    time1 = []
    time2 = []
    while len(time1) != 3 :
        inputTime1 = input("input first time in this format DD:HH:MM - ")
        time1 = (inputTime1.split(":"))
        time1 = castInt(time1)
    while len(time2) != 3 :
        inputTime2 = input("input second time in this format DD:HH:MM - ")
        time2 = (inputTime2.split(":"))
        time2 = castInt(time2)
        return(time1,time2)

#Function to receive and return a single integer
def getOneInput(operation) :
    if operation == 3 or operation == 4 :
        inputTime = input("input time in this format DD:HH:MM -  ")
        time = (inputTime.split(":"))
        time = castInt(time)
        return(time)
    elif operation == 5 or operation == 6 :
        inputTime = input("input time as a whole number - ")
        time = int(inputTime)
        return(time)



def main() :
    working = False

    while working == False :

        working = True
        operation =-1

        print(" ")
        print("Time Calculator")
        print("1- Add 2 times")
        print("2- Find the difference between 2 times")
        print("3- Convert to Hours")
        print("4- Convert to Minutes")
        print("5- Convert Minutes to hours")
        print("6- Convert Hours to days")
        print("7- Exit")
        print("")

        #loops until option 1-7
        while operation < 1 or operation > 7 :
            operation = int(input("\t Enter an option: "))
    

        #Main if statement for each option - gets input(s), calls relevant function and then prints
        if operation == 1 :
            inputs = getTwoInputs()
            time1 = inputs[0]
            time2 = inputs[1]
            time = addTime(time1, time2)
            print(time)
        elif operation == 2 :
            inputs = getTwoInputs
            time1 = inputs[0]
            time2 = inputs[1]
            time = minusTime(time1, time2)
            print(time)
        elif operation == 3 :
            time = getOneInput(operation)
            hours = timeToHours(time)
            print("\n" + str(hours) + " hours.")
        elif operation == 4 :
            time = getOneInput(operation)
            minutes = timeToMinutes(time)
            print("\n" + str(minutes) + " minutes.")
        elif operation == 5 :
            time = getOneInput(operation)
            hours = minsToHours(time)
            print("\n" + str(hours) + " hours.")
        elif operation == 6 :
            time = getOneInput(operation)
            days = hoursToDays(time)
            print("\n" + str(days) + " days.")
        else :
            print("Thank you for using the time Calcualtor")
            exit(0)

        operation = -1
        working = False

main()


    



    


        










