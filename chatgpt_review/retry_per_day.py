import datetime

from main1_get_data import convertTimeFromString, run


def readFile(filename):
    errorTime = []
    with open(filename, 'r') as f:
        for line in f :
            errorTime.append(line)
    return errorTime

def delayHour(errorTime):
    newErrorTimes = []
    for time in errorTime:
        newErrorTimes.append(time)
    return newErrorTimes

def main():
    errorTime = readFile("errors_per_day.txt")

    for i in errorTime:
        print(i)
        start = convertTimeFromString(i)
        end = start + datetime.timedelta(days=1)
        print(start)
        print(end)

        run(str(start), str(end),'day')

if __name__ == '__main__':
    main()
