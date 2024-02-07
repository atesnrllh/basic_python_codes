
input_file_path = 'write your input file path'
output_file_path = 'write your output file path'
with open(file_path) as input, open(output_file_path, 'w') as output:
    for line in input:
        if line.split('\t')[0] == '1':
            output.write(line)
