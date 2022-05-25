from contextvars import Token
import dropbox
class TransferData:
    def __init__(self,token):
        self.token=token

    def uploadFile(self,file1,file2):
        dbx=dropbox.Dropbox(self.token)
        f=open(file1,'rb')

        dbx.files_upload(f.read(),file2)


def main():
    token='sl.BH9N3KU7DC_4xO5OtEYfrXGBS9r6qv-YrEN8WlTIdCQ5zkorwo8sIdi4Gb8s4BZTEuu4a4hdCPjDggdTgfFI4Uz1mWvu8fIm5WvAyUM6vHDgejovoHB6xIpUwCnoOUxAlkiALpI'
    backup=TransferData(token)
    file1=input('enter the file path to transfer =>')
    file2=input('enter the name of the file for dropbox =>')
    backup.uploadFile(file1,file2)
    print('file successfully transferred')

main()