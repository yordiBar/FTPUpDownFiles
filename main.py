# use ftplib library
from ftplib import FTP
import os

# create an ftp object with your ftp path, login details and source folder name
ftp = FTP('ftp.yourPath.com')
ftp.login('username', 'password')
srcFolder = '/SrcFolderName/'


ftp.cwd(srcFolder)

# return file names from directory
files = ftp.nlst()
for fileName in files:
    # isFile() makes sure to read a file not a directory
    if os.path.isfile(fileName):
        print("Downloading")
        ftp.retrbinary("RETR %s" % fileName, open(fileName, 'wb').write())

# close connection
ftp.close()
