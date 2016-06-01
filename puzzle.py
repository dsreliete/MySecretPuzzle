import os

def rename_file(directory, old, new):
    new_names_list = old
    if new in new_names_list: #verify if there is a remaned file with the new name
        break
    else:
    old_file = directory + '/' + old
    new_file = directory + '/' + new
    if os.path.exists(old_file): #rename a file that really exists
        os.rename(old_file, new_file)
    

def change_name(directory):
    numbers_list = ['0','1','2','3','4','5','6','7','8','9']
    for old_name in os.listdir(directory):
        i = 0
        tam = len(old_name)
        while(i < tam):
            c = old_name[i]
            if c in numbers_list:
                new_name = old_name[i+1:tam]
            i += 1
        rename_file(directory, old_name, new_name)
    print('file renamed')
        
PATH = 'C:/Users/eliete/Desktop/UdacityProjects/python/puzzle'
change_name(PATH)

