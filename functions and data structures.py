# 4. Functions & Data Structures
print("Functions & Data Structures\n")
def calculate_area(length, width):
    return length * width
 
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
 
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}\n")