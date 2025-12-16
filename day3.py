
""" Advent of Code 2025 - Day 3

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
In 818181911112111, the largest joltage you can produce is 92.
The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
"""
testbanks = "987654321111111"
def find_max_joltage(bank):
	first = 0
	second = 0
	possible_first = 0
	next_best = 0
	for battery in bank:
		print(f'First: {first}, Second: {second}, Battery: {battery}')
		battery = int(battery)
		if second > first:
			first = second
			second = battery
		if battery > second:
			second = battery
	max_jotage = first*10 + second
	return max_jotage


def main():
	f = open("day3_input.txt", "r") 
	input_data = f.read()
	sum_max_jotage = 0
	for line in input_data.splitlines():
		max_jolt = find_max_joltage(line)
		sum_max_jotage += max_jolt

	print(find_max_joltage(testbanks)) 
	print(sum_max_jotage)



if __name__ == "__main__":
	main()