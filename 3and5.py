#
#   Name: Aubree Dix
#   Assignment: Euler #1 in Python
#   Date: February 13, 2019
#

sum = 0;
counter = 0;
iterate = 1000;
while counter < iterate:
    if counter % 3 == 0 or counter % 5 == 0:
        print(counter);
        sum += counter;
    counter += 1;
print(sum);
