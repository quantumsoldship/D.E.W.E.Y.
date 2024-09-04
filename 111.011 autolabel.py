import os
import sys

def has_two_decimal_places(number):
    str_num = str(number)
    if '.' in str_num:
        decimal_part = str_num.split('.')[1]
        return len(decimal_part) == 2
    else:
        return False
    
def count_files_with_format(folder_path):
    count = 0
    for file_name in os.listdir(folder_path):
        if file_name[:3].isdigit():
            count += 1
    return count

def auto_label_file(file_path):
    folder_path = os.path.dirname(file_path)
    folder_name = os.path.basename(folder_path)
    reference_later = folder_name
    if '.' in folder_name:
        folder_name = folder_name[:5]
    else:
        folder_name = folder_name[:3]

    count = count_files_with_format(folder_path)
    original_file_name = os.path.basename(file_path)

    if reference_later[:5].count('.') > 0:
        if has_two_decimal_places(reference_later[:6]):
            new_file_name = reference_later[:6]  + str(count+1)
        elif count > 9:
            new_file_name = folder_name + str(count+1)
        else:
            new_file_name = folder_name + '0' + str(count+1)
    else:
        folder_name = folder_name.strip('0')
        new_file_name = folder_name + str(count+1)
        if reference_later.count('0') > 0:
            for i in range(reference_later.count('0') - 1):
                new_file_name = new_file_name + '0'
        else:
            if count > 8:
                new_file_name = folder_name + '.' + str(count+1)
            else:
                new_file_name = folder_name + '.' + '0' + str(count+1)

    path_of_file = os.path.join(folder_path, new_file_name + ' ' + original_file_name)

    os.rename(file_path, path_of_file)
    print('Success')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    auto_label_file(file_path)
