import math
""" testcases 11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121."""
testcases = "11-22,95-115,998-1012,1188511880-1188511890, 222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
def main():
	f = open("day2_input.txt", "r") 
	input_data = f.read()
	ranges = input_data.split(",")
	print(ranges[0])
	count = 0
	for r in ranges:
		low, high = r.split("-")
		print(f"Low: {low}, High: {high}")
		count += find_repeating_sequence(low, high)
	#find_repeating_sequence("","1000000000")
	print(f"Count: {count}")



"""
To find all invalid numbers where the id repeats twice in the range, e.g., 1234 is vallid but 1212 is not.
Input: low and high eg 726 and 1031
Known, all numbers with odd number of digits are valid.
Fact: ignore the numbers with odd number of digits. increase the low to the next even digit number.

pattern: 11,22,33,44,55,66,77,88,99,1010,1111,1212,1313,1414,1515,1616,1717,1818,1919,2020,2121


Part2: all numbers with a sequence repeating at least twice are invalid. eg., 999, 1212, 123123, 4545, 121212 are invalid.
possible solution: try the first sequence length from 1 to n/2 and check if the number can be formed by repeating that sequence.
"""
def is_a_sequence(number):
	value = False
	num_str = str(number)
	half_len = len(num_str)//2
	for i in range(1, half_len+1):
		seq = num_str[:i]
		mult = len(num_str)//len(seq)
		if seq * mult == num_str:
			print(f"Found repeating sequence in number: {number}. Sequnce: {seq}")
			value = True
			break
	return value

def find_repeating_sequence(low,high):
	count = 0
	#make low even digits
	low = int(low)
	high = int(high)
	for i in range(low, (high+1)):
		
		if is_a_sequence(i):
			count += i
			

	return count


if __name__ == "__main__":
	main()