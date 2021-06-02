import gzip
import os
import shutil

path = input('Input abs path.\n')
filelists = os.listdir(path)
for i in filelists:
    if os.path.isdir(os.path.join(path,i)):
        dirpath = os.path.join(path,i)
        gzfile = os.listdir(dirpath)[0]
        with gzip.open(os.path.join(dirpath,gzfile), 'rb') as f_in:
            writefile = gzfile.replace('.gz','.pdb')
            with open(os.path.join(dirpath,writefile), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
