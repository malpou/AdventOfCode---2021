with open("C:/Users/malth/OneDrive - IT Afdelingen/Dokumenter/AdventOfCode/Dec 1/Data.txt") as file:
    measurements = file.readlines()
    measurements = [line.rstrip() for line in measurements]

    # Part 1
    increases = 0
    for i in range(len(measurements) - 1):
        if int(measurements[i]) < int(measurements[i + 1]):
            increases += 1
    print(increases)

    # Part 2
    windows = []
    for i in range(len(measurements) - 2):
        # loop that itereates 3 times
        windows.append(int(measurements[i]) + int(measurements[i + 1]) + int(measurements[i + 2]))

    windowIncrease = 0
    for i in range(len(windows) - 1):
        if windows[i] < windows[i + 1]:
            windowIncrease += 1
    print(windowIncrease)
