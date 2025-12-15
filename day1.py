
import math
def main():
    f = open("day1_input.txt", "r") 
    input_data = f.read()
    dial = 50
    passcode = 0
    for line in input_data.splitlines():
        direction = line[0]
        value = int(line[1:])
        if direction == "L":
            dial, passcode = turn_left(value, dial, passcode)
        elif direction == "R":
            dial, passcode = turn_right(value, dial, passcode)
    print(passcode)

def turn_left(input, dial,passcode):
    if input > 99:
        passcode += math.floor(input / 100)
        input = input % 100
    if dial - input < 0:
        if dial == 0:
            dial =  100 + (dial - input)
        else:
            passcode += 1
            dial =  100 + (dial - input)
    else:
        dial = dial - input
        if dial == 0:
            passcode += 1
    return dial,passcode

def turn_right(input, dial, passcode):
    if input > 99:
        passcode += math.floor(input / 100)
        input = input % 100
    if dial + input > 99:
        dial = (dial + input) - 100
        passcode += 1
    else:
        dial = dial + input
    return dial, passcode











if __name__ == "__main__":
    main()



