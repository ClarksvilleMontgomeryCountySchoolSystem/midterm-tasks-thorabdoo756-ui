# Halloween Candy Sharing

# Given Variables
people = 2  # friends who went trick-or-treating
bagA = 23
bagB = 17
bagC = 19

# Part 1: Combine the haul
total_candy = bagA + bagB + bagC
print("Total candy collected:", total_candy)

# Part 2: Fair sharing (include yourself)
people = people + 1  # include yourself
share = total_candy // people
leftover = total_candy % people
print("Each person gets:", share)
print("Leftover candy:", leftover)

# Part 3: Include the sick friend
people = people + 1  # include sick friend
share = total_candy // people
leftover = total_candy % people
print("Each person gets:", share)
print("Leftover candy:", leftover)
