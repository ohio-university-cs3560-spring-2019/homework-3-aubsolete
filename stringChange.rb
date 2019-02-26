#
# Name: Aubree Dix
# Date: 2/25/19
# Assignment: HW 6, Ruby
# Class: CS 3560
#

input = gets.chomp    # get input from user
input.downcase!       # in case input has cap-letters, set lowercase
i = 0                 # initialize counter

while i < input.length  # set while loop to iterate through string
  # if first letter in string is f, replace with gh
  if i == 0 && input[i] == 'f'
    input[i] = 'g'
    input.insert(1, 'h')
  end
  # if middle letter is i, replace with o
  if i != 0 && i < input.length - 1 && input[i] == 'i'
    input[i] = 'o'
  end
  # if last two letters are sh, replace with ti
  if i == (input.length - 2) && input[i] == 's' && input[i+1] == 'h'
    input[i] = 't'
    input[i+1] = 'i'
  end
  i = i + 1   # increment counter (i)
end

puts input    # see result
