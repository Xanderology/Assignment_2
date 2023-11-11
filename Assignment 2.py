#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:21:27 2023

@author: xanderology
"""

#1.	In the first assignment, you downloaded the sequence for chr1_GL383518v1_alt. Write a Python program to read the complete sequence from the file. 
    # a.	Print the 10th letter of this sequence.
    # b.	Print the 758th letter of this sequence.
    

import os
os.path.join(os.path.dirname(__file__))


# Define the file path
file_name = "chr1_GL383518v1_alt.fa"

try:
    # Open the file for reading'
    with open(file_name, "r") as file:
        # Read the entire sequence from the file
        header = file.readline()
        # Read the sequence replacing each new line with nothing
        genome = (file.read().replace("\n","")).upper()

        # Check if the sequence has at least 758 letters
        if len(genome) >= 758:
            # Print the 10th letter (index 11 because indexing starts at 0)
            print("10th letter:", genome[9])

            # Print the 758th letter (index 757 because indexing starts at 0)
            print("758th letter:", genome[757])
        else:
            print("The sequence does not have enough letters.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print("An error occurred:", e)


# 2.	Write a Python program to create the reverse complement of the encoded DNA molecule used in Part 1. Remember to reverse the sequence, and substitute the bases with their Watson-Crick-Franklin pair.
    #a.	Print the 79th letter of this sequence.
    #b.	Print the 500th through the 800th letters of this sequence. 
        

# Create a dictionary to map bases to their complements
complement_dict = {'A':'T','T':'A','C':'G','G':'C'}

# Reverse the sequence and create the complement
reverse_complement_sequence = ''.join([complement_dict[base] for base in reversed(genome)])

# Print the 79th letter (index 78 because indexing starts at 0)
print("Part 2: 79th letter:", reverse_complement_sequence[78])

# Print the 500th to 800th letters (index 500 to 801)
print("Part 2: 500th to 800th letters:", reverse_complement_sequence[500:801])


#3.	Write a Python program that asks the user for a number, and generates a list of numbers that contains that many terms of the Fibonacci numbers.
#a.	Use your generated list of Fibonacci numbers to make a second list of numbers, where the first number is 1, and each subsequent number is quotient of the corresponding Fibonacci number and the previous Fibonacci number.
#b.	Use your second list of numbers to make a third group of numbers, where the first two elements are 0, and each subsequent element is the difference of the corresponding element in the second list and the previous element in the list group.

# Function to generate a list of Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list

# Function to calculate the quotient list
def calculate_quotients(fib_list):
    quotient_list = [1]  # Start with 1 as the first value
    for i in range(1, len(fib_list)):
        if fib_list[i - 1] == 0:
            quotient_list.append(0)
        else:
            quotient = fib_list[i] / fib_list[i - 1]
            quotient_list.append(quotient)
    return quotient_list

# Function to calculate the third group
def calculate_third_group(quotient_list):
    third_group = []
    for i in range(1, len(quotient_list)):
        product = quotient_list[i] * quotient_list[i - 1]
        third_group.append(product)
    return third_group

try:
    # Ask the user for the number of terms in the Fibonacci sequence
    n = int(input("Enter the number of Fibonacci terms: "))

    # Generate the Fibonacci list
    fibonacci_list = generate_fibonacci(n)

    # Calculate the quotient list
    quotient_list = calculate_quotients(fibonacci_list)

    # Calculate the third group
    third_group = calculate_third_group(quotient_list)

    # Print the generated lists
    print("Fibonacci List:", fibonacci_list)
    print("Quotient List:", quotient_list)
    print("Third Group List:", third_group)

except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print("An error occurred:", e)
    
    
#4.	Write a Python program that uses nested loops to create a 10 by 10 matrix from nested lists that contains consecutive odd numbers starting at 1.
#a.	Calculate the trace of this matrix using list index positions. Store it as a variable.
#b.	Display the trace with the sentence “The trace of your matrix is X”, where X is the variable containing the calculated trace.
#c.	Calculate the sum of all elements in the upper triangle of the matrix. Store it as a variable.
#d.	Display the sum of all elements in the upper triangle of the matrix with the sentence “The sum of upper triangular elements in your matrix is X.”, where X is the variable containing the calculated sum of upper triangular elements.
#e.	Calculate the sum of all elements in the lower triangle of the matrix. Store it as a variable.
#f.	Display the sum of all elements in the upper triangle of the matrix with the sentence “The sum of lower triangular elementsin your matrix is X.”, where X is the variable containing the calculated sum of lower triangular elements.

# Create a 10x10 matrix of consecutive odd numbers
# Initialize an empty 10x10 matrix
matrix = []

# Initialize the first odd number
odd_number = 1

# Loop through rows (10 rows)
for _ in range(10):
    # Initialize a row for the matrix
    row = []
    
    # Loop through columns (10 columns)
    for _ in range(10):
        # Append the current odd number to the row
        row.append(odd_number)
        
        # Increment the odd number by 2 to get the next odd number
        odd_number += 2
    
    # Append the row to the matrix
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)

# Initialize a variable to store the trace
trace = 0

# Calculate the trace by summing the values along the main diagonal
for i in range(10):
    trace += matrix[i][i]

# Display the trace
print("The trace of your matrix is", trace)

# Initialize a variable to store the sum of upper triangular elements
upper_sum = 0

# Calculate the sum of elements in the upper triangle
for i in range(10):
    for j in range(i + 1, 10):
        upper_sum += matrix[i][j]

# Display the sum of upper triangular elements
print("The sum of upper triangular elements in your matrix is", upper_sum)

lower_sum = 0

# Calculate the sum of elements in the lower triangle
for i in range(10):
    for j in range(i):
        lower_sum += matrix[i][j]

# Display the sum of lower triangular elements with the sentence
print("The sum of lower triangular elements in your matrix is", lower_sum)


#5.	Write a Python program to read the sequence used in Part 1.
#a.	Create a nested dictionary that contains the number of times each letter appears in the downloaded sequence, as a function of which kilobase of the sequence you are looking at.
#HINT: “my_dict”[5000] should contain a dictionary that has a separate key for each of the different nucleotides. And “my_dict”[5000][“A”] should contain the number of times each A appears in the sequence between position 5000 and position 6000.
    
# Function to count nucleotide occurrences in a given sequence
def count_nucleotides(sequence):
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
    return nucleotide_counts


file_path = "/Users/xanderology/Desktop/Bioinformatics Masters/INFO-B 573 Programming for Science Informatics FA23/chr1_GL383518v1_alt.fa"

# Read the sequence from the file
with open(file_path, 'r') as file:
    #Read the entire sequence from the file
    sequence = file.read().replace("\n","").upper()
    
# Create a nested dictionary to store counts
kilobase_counts = {}

# Define the kilobase step size
kilobase_step = 1000

# Loop through the sequence in kilobase steps
for start in range(0, len(sequence), kilobase_step):
    end = start + kilobase_step
    sub_sequence = sequence[start:end]
    nucleotide_count = count_nucleotides(sub_sequence)
    
    # Store the counts in the nested dictionary
    kilobase_counts[start] = nucleotide_count

# Print the nested dictionary
for start, counts in kilobase_counts.items():
    print(f'Kilobase {start}-{start+kilobase_step-1}: {counts}')



import sys
print(sys.version)
