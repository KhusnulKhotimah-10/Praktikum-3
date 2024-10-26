# Input number of elements
N = int(input("Masukkan jumlah bilangan: "))

# Initialize maximum value to 0
max_val = 0

# Loop through N times to get the numbers
for i in range(1, N + 1):
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    # Check if the current number is greater than max_val
    if bilangan > max_val:
        max_val = bilangan

# Display the maximum number
print(f"Bilangan terbesar adalah: {max_val}")