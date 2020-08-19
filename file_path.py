import os.path
if os.path.isfile('q.txt'):
    print('exist')
    file=open('q.txt','a')
    file.write('file 94 exist')
    file.close()

else:
    print('not exist')
    file=open('q.txt','w')
    file.write('new')
    file.close()

