#!/usr/bin/env python

import os

file_path = '/Users/marisaalves/Downloads/toys-datasets/diabetes.data'
if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, program will crash')

file = open('/Users/marisaalves/Downloads/toys-datasets/diabetes.data')

corrected_file = []
i = 0
for line in file.readlines():
	clean_line = line.replace("\t",' ').strip()
	line_values = clean_line.split(' ')
	corrected_line = []
	print(line_values)
	if i > 0:
		for value in line_values:
			if (float(value)).is_integer():
				corrected_line.append(int(value))	 
			else:
				corrected_line.append(float(value))
			print(corrected_line)
		corrected_file.append(corrected_line)
	else:
		corrected_file.append(line_values)
	i = i+1
print(corrected_file)

corrected_list = list(map(list,zip(*corrected_file)))
print(corrected_list)


file.close()
