
input_file_path = 'write your input file path'
output_file_path = 'write your output file path'
with open(file_path) as old, open(output_file_path, 'w') as new:
    for line in old:
        if line.split('\t')[0] == '1':
            new.write(line)
