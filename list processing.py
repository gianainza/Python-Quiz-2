# 5. List Processing
print("List Processing\n")
numbers = []
 
for i in range(5):
    num = int(input(f"Input number {i + 1}: "))
    numbers.append(num)
 
numbers.sort(reverse=True)
 
print("Numbers sorted from highest to lowest:")
print(numbers)