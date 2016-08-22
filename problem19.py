def getdaysinmonth(month, year):
    if month == 2:
        if year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0):
            return 29
        else:
            return 28
    else:
        if month in (9, 4, 6, 11):
            return 30
        else:
            return 31


def incrementdayofweek(day):
    if day == "Saturday":
        return "Sunday"
    else:
        return days[days.index(day) + 1]


def incrementday(day):
    days_month = getdaysinmonth(day[1], day[2])
    day = (day[0] + 1, day[1], day[2])
    if day[0] == days_month + 1:
        day = (1, day[1] + 1, day[2])
    if day[1] == 13:
        day = (day[0], 1, day[2] + 1)
    return day

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
currentDayOfWeek = "Tuesday"
currentDay = (1, 1, 1901)
countSundays = 0

while True:
    currentDay = incrementday(currentDay)
    currentDayOfWeek = incrementdayofweek(currentDayOfWeek)
    if currentDay[0] == 1 and currentDayOfWeek == "Sunday":
        # print "Sunday found on {}/{}/{} ".format(currentDay[1], currentDay[0], currentDay[2])
        countSundays += 1
    if currentDay[0] == 31 and currentDay[1] == 12 and currentDay[2] == 2000:
        break
print countSundays
