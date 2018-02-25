'''
###########
Code1: dates transformation
input: a list of strings
output: new list of dates in form of YYYYMMDD
example:
change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"]) 
should return the list ["20100330", "20161215", "20121115"]
###########
'''
import re

def change_date_format(list):
    list = file.readline()
    #print(list)
    dates = re.split(', ',list.replace('"',""))#to avoid empty string, split "," and space
    #dates = re.split('"',dates)
    #print(dates) 

    for n in range(len(dates)):
        #print(dates[i])
        if "-" in dates[n]:
            dates[n] = re.split('\-', dates[n])
            #print(dates[n])
            dates[n] = dates[n][2]+dates[n][0]+dates[n][1]
            #print(dates[n])
        elif "/" in dates[n]:
            dates[n] = re.split('\/', dates[n])
            if len(dates[n][0]) > 2:
                dates[n] = dates[n][0]+dates[n][1]+dates[n][2]
                #print(dates[n])
            else:
                dates[n] = dates[n][2]+dates[n][1]+dates[n][0]
                #print(dates[n])
        else:
            #Use del to remove an element by index, 
            #pop() to remove it by index if you need the returned value, 
            #and remove() to delete an element by value. 
            #The latter requires searching the list, 
            #and raises ValueError if no such value occurs in the list
            del dates[n]
    #print(dates)
    return dates

    
file = open("dates.txt", "r")
print(change_date_format(file))
file.close()


