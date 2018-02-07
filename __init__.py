
file_path1 = 'archive.7z'
file_path2 = 'archive_password.7z'
file_password = 'P@ssw0rd!'
file_out1 = './unzipped1/'
file_out2 = './unzipped2/'


#########################################################
# Use p7zip and subprocess library
#########################################################
# prerequisites:
# install globally this library http://p7zip.sourceforge.net/
# download, extract archive and launch with sudo install.sh
from subprocess import Popen, check_output
import os

# 7za x archive_password.7z -pP@ssw0rd! -o./unzipped/
def extract_archive(filepath, out_dir = None, password = None):
    password = '-p' + password if password is not None else None
    out_dir = '-o' + os.path.dirname(out_dir) if out_dir is not None else None
    args = ('7za', 'x', filepath, password, out_dir, '-bt', '-y')
    args = tuple(x for x in args if x is not None) # remove 'None' values from args list

    proc = Popen(args)
    proc.communicate()

    return proc.returncode


extract_archive(file_path1, file_out1)
extract_archive(file_path2, file_out2, file_password)
extract_archive(file_path2, password=file_password)
