import os
import shutil
import time
def main():
    deleted_folder_count=0
    deleted_file_count=0
    path='/path to delete'
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folders,files in os.walk(path):
        if seconds>=getFileOrFolderAge(rootFolder):
            removeFolder(rootFolder)
            deleted_folder_count+=1
            break
        else:
            for folder in folders:
                folder_path=os.path.join(rootFolder,folder)
                if seconds>=getFileOrFolderAge(folder_path):
                    removeFolder(folder_path)
                    deleted_folder_count+=1
    for file in files:
        file_path=os.path.join(rootFolder,file)
        if seconds>=getFileOrFolderAge(file_path):
            removeFile(file_path)
            deleted_file_count+=1
    def removeFolder(path):
        if not shutil.rmt(path):
            print ('path is removed successfully')
        else:
            print ('unable to remove the path')
    def removeFile(path):
        if not os.rmt(path):
            print ('path is removed successfully')
        else:
            print ('unable to remove the path')
    def getFileOrFolderAge(path):
        ctime=os.stat(path).st_ctime
        return ctime
    main()
    input('Enter to exit')










    