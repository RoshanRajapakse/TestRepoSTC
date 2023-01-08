# Function to print the star pattern
def print_star_pattern(n):
  # Loop through the rows
  for i in range(1, n+1):
    # Print n-i spaces followed by i stars
    print(' '*(n-i) + '*'*i)

# Test function
print_star_pattern(5)

#r1
