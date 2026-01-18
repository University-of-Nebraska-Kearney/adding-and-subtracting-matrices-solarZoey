# Author: Nova Solarz (it/they/she)
# Date of Creation: 2026-01-15
# Date of Last Edit: 2026-01-17
# Program Directive: 
    # get_martix(): creates and returns a matrix from user input such that the size and dimension is determined by the user. This should be a hybrid of the fixed-sized and the sentinel model we discussed in class. The user should be prompted for the number or rows and columns before entering values to fill the matrix.
    # add_matrix(matrix1, matrix2): takes two matrices as parameters, verifies that they can be added together, adds them together, and returns the sum.

from numpy import max as npmax # well-optimized way get the maximum element from a multidimensional array

def main():
	print("~ 始 ~")
	print()
	A = get_matrix()
	print()
	B = get_matrix()
	print()
	print_matrix(A)
	print("+")
	print_matrix(B)
	print("=")

	C = add_matrix(A, B)
	if C:
		print_matrix(C)
	else:
		print("matrix addition failed!")

	print("~ 完 ~")


def get_matrix() -> list[list]:
	# creates and returns a matrix from user input 
	# such that the size and dimension is determined by the user. 

	# get size from user
	valid = False
	while not valid:
		row_entry = input("Enter row size: ")
		try:
			row_entry = int(row_entry)
			valid = True
		except ValueError:
			print("Entry is not a number! Must be an integer. Try again.")
	valid = False
	while not valid:
		column_entry = input("Enter column size: ")
		try:
			column_entry = int(column_entry)
			valid = True
		except ValueError:
			print("Entry is not a number! Must be an integer. Try again.")

	print(f"You have specified {row_entry} row{"s" if row_entry > 1 else ""} and {column_entry} column{"s" if column_entry > 1 else ""} for your matrix.")

	# loop for element inputs
	matrix = []
	for r in range(row_entry):
		
		matrix.append([])

		for c in range(column_entry):

			valid = False
			while not valid:
				try:
					element_entry = input(f"Enter a value for element ({r+1},{c+1}): ")
					element_entry = int(element_entry)
					valid = True
				except ValueError:
					print("Entry is not a number! Must be an integer. Try again.")

			matrix[r].append(element_entry)

	return matrix


def add_matrix(matrix1, matrix2) -> list[list]|int:
	# takes two matrices as parameters, 
	# verifies that they can be added together, 
	# adds them together, 
	# and returns the sum.
	# NOTE: if the matrices are of incompatable dimensions, this will return 0 (false)

	# verify sizes
	if len(matrix1) != len(matrix2):
		print("matrices have incongruent row sizes!")
		return 0
	elif len(matrix1[0]) != len(matrix2[0]):
		print("matrices have incongruent column sizes!")
		return 0
	else:
		# calculate
		result = []
		for r in range(len(matrix1)):
			result.append([])

			for c in range(len(matrix1[0])):
				result[r].append(matrix1[r][c] + matrix2[r][c])

		return result


def print_matrix(M:tuple[tuple]):
	# prints a matrix in a pretty manner

	# get number of digits from maximum value in the matrix for padding purposes
	highest = npmax(M)
	highest = str(highest)
	digits = len(highest)

	# construct main body of the string to print
	out = []
	for r in M:
		txt = "│"
		for c in r:
			c = str(c)
			c += ","
			txt += f"{c:^{digits+2}}" # format string for padding
		txt = txt.replace(',',' ')
		txt = txt[:-1]
		txt += "│\n"
		out.append(txt)

	# add cap and tail to brackets
	space = " "
	out.insert(0, f"┌{space*(len(out[0])-3)}┐\n")
	out.append(f"└{space*(len(out[0])-3)}┘\n")

	# print the matrix string
	for i in out:
		print(i, end="")


if __name__ == '__main__':
	main()