# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Functions
"""
def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

def read_file(file_name):
    file = open(file_name, "r")
    return file

def parse_lines(content):
    parsed = []
    lines = content.readlines()
    for line in lines:
        p_line = line.split()
        parsed.append(p_line)
    return parsed

def create_dict(parsed):
    dict = {}
    for key_value in parsed:
        if len(key_value) == 2:
            key = key_value[0]
            dict[int(key)] = key_value[1]
    return dict

def get_pyramid(dict):
    nums = list(dict.keys())
    nums.sort()
    pyramid = create_staircase(nums)
    return pyramid

def get_numbers(pyramid):
    values = []
    for element in pyramid:
        number = element[-1]
        values.append(number)
    return values

def build_sentence(numbers, key_values):
    words = []
    for number in numbers:
        words.append(key_values[number])
    sentence = " ".join(words)
    return sentence
    
"""
Program
"""
file = read_file("file_for_coding_test.txt")
parsed = parse_lines(file)
pairs = create_dict(parsed)
pyramid = get_pyramid(pairs)
numbers = get_numbers(pyramid)
sentence = build_sentence(numbers, pairs)
print(sentence)