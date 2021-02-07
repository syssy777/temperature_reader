def Temp_Reader():
    weekList = []

    def daily_temp():
        print('--------- Enter your daily temperature for the week --------------')
        print('')
        for i in range(1, 8):
            daily_ = float(input(f'Enter the temperature of day {i} for the week: '))
            print(daily_)
            weekList.append(daily_)

    daily_temp()

    def avg_temp():
        myList = [i for i in weekList]
        avg = sum(myList) / len(weekList)
        print()
        print(f'Average temperature of the week: {avg :.2f}')
        print()
        print('-----------Day wise analysis-----------')
        print()

        for i in range(len(weekList)):
            if weekList[i] == avg:
                print(f'Temperature on day {i + 1} is Equal to Average')
            elif weekList[i] > avg:
                print(f'Temperature on day {i + 1} is Above Average')
            else:
                print(f'Temperature on day {i + 1} is Below Average')

    avg_temp()
    # exit()


Temp_Reader()
