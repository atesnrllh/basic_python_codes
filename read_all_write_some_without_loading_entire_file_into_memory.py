
file_path = '/home/nuri/Downloads/HEXA-main_fine/x_small/dev.txt'
# with open(file_path, "r") as file1:
#     with open("file2.txt", "w") as file2:
#         x= file1.read()
#         print()

# import fileinput
#
# with open("dev.pos.txt", "w") as file_out:
#     for line in fileinput.input(file_path, inplace=True):
#         line_to_list = line.split('\t')
#         if line_to_list[0] == "1":
#             file_out.write(line)
#         print()


with open(file_path) as old, open('newtest', 'w') as new:
    for line in old:
        if line.split('\t')[0] == '1':
            new.write(line)

print()
