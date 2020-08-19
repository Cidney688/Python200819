scores=[]
namelist=[]
maxscores=0
minscores=100
total=0

for i in range(5):
    n=int(input("成績:"))
    a=str(input("name:"))
    scores.append(n)
    namelist.append(a)
    
    if n>maxscores:
        maxscores=n
        maxname=a
        
    if n<minscores:
        minscores=n
        minname=a
    total=total+n
    
s=total/len(scores)
print('總分:',total) 
print('平均:',s)
print('最高分:',maxscores,maxname)
print('最低分:',minscores,minname)