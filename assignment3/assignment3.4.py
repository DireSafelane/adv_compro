numbers = [1,2,3,4,5]
modified_numbers = [i*10 if i%2==0 else i-1 for i in numbers]
print(modified_numbers)