from os import listdir, rename
# from os.path import isfile

def rename_file(_dir):
    # Get the file name from folder
    lists =  listdir(_dir)
    # print(lists)
    for name in lists:
        trantab = name.maketrans("0123456789","          ","0123456789")
        new_name = name.translate(trantab)
        old_path = _dir +'/'+name
        new_path = _dir +'/'+new_name
        try:
            rename(old_path,new_path)
        except Exception as e:
            pass
        

    lists_after = listdir(_dir)

if __name__ == '__main__':
    _dir = './data'
    rename_file(_dir)
