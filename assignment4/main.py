# import string_operations
# sample =  "hello World"

# print(string_operations.reverse_string(sample))
# print(string_operations.capitalize_string(sample))
# print(string_operations.lowercase_string(sample))
# print(string_operations.uppercase_string(sample))

from utilities import calculator,string_operation 

print("Using calculator.py:")
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))

sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", string_operation.reverse_string(sample_string))
print("Capitalized:", string_operation.capitalize_string(sample_string))
print("Lowercase:", string_operation.lowercase_string(sample_string))
print("Uppercase:", string_operation.uppercase_string(sample_string))