def merg_file(file_list, final_file):
    list_len_lines = []
    dict_line = {}
    dict_file = {}
    for file in file_list:
        with open(file, 'rt', encoding = 'utf-8') as open_file:
            lines = open_file.readlines()
            list_len_lines.append(len(lines))
            str_lines = ''.join(lines)
            dict_line[file] = str_lines
        for num_lines in list_len_lines:
            continue
        dict_file[num_lines] = file  
        list_len_lines.sort()
    
    with open(final_file, 'a', encoding = 'utf-8') as write_file:
        write_file.write(f'{dict_file[min(list_len_lines)]}\n{min(list_len_lines)}\n{dict_line[dict_file[min(list_len_lines)]]}')
        list_len_lines.remove(min(list_len_lines))

        write_file.write(f'\n{dict_file[min(list_len_lines)]}\n{min(list_len_lines)}\n{dict_line[dict_file[min(list_len_lines)]]}')
        list_len_lines.remove(min(list_len_lines))

        write_file.write(f'\n{dict_file[min(list_len_lines)]}\n{min(list_len_lines)}\n{dict_line[dict_file[min(list_len_lines)]]}')
        list_len_lines.remove(min(list_len_lines))
   
merg_file(['1.txt', '2.txt', '3.txt'], 'final_file.txt')