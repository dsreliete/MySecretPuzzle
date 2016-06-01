import os


def rename_file(directory, old, new):
    if new in os.listdir(directory):
        print('this name was already added')
        return
    else:
        old_file = directory + '/' + old
        new_file = directory + '/' + new
        
    if os.path.exists(old_file): #rename a file that really exists
        os.rename(old_file, new_file)
        print('file renamed')
    

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
        
PATH = 'C:/Users/eliete/Desktop/UdacityProjects/python/puzzle/prank'
change_name(PATH)

