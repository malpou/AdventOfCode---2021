class Command:
    direction = ""
    distance = 0

    def __init__(self, command):
        self.direction = command.split()[0]
        self.distance = int(command.split()[1])


with open("C:/Users/malth/OneDrive - IT Afdelingen/Dokumenter/AdventOfCode/Dec 2/Data.txt") as file:
    commandsStr = file.readlines()
    commandsStr = [line.rstrip() for line in commandsStr]

    # Part 1
    horizontal = 0
    depth = 0

    for commandStr in commandsStr:
        command = Command(commandStr)
        match command.direction:
            case "forward":
                horizontal += command.distance
            case "up":
                depth -= command.distance
            case "down":
                depth += command.distance
    print("result: " + str(horizontal * depth))

    # Part 2
    horizontal = 0
    depth = 0
    aim = 0

    for commandStr in commandsStr:
        command = Command(commandStr)
        match command.direction:
            case "forward":
                horizontal += command.distance
                depth += aim * command.distance
            case "up":
                aim -= command.distance
            case "down":
                aim += command.distance
    print("result: " + str(horizontal * depth))
    