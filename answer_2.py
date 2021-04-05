s1=input(str('enter the string s1: '))
s2=input(str('enter the string s2: '))
a=list(s1)
b=list(s2)
c1=[]
d1=[]
c2=[]
d2=[]
for i in a:
    if i=='#':
        c1.append("e")
    else:
        c1.append(i)
    if i=='#':
        c2.append('f')
    else:
        c2.append(i)
for i in b:
    if i=='#':
        d1.append("e")
    else:
        d1.append(i)
    if i=='#':
        d2.append('f')
    else:
        d2.append(i)

def swap(c1,c2):
    c1[0],c1[1]=c1[1],c1[0]
    c2[0],c2[1]=c2[1],c2[0]
    #print(c1)
    if c1==d1 or c1==d2 or c2==d1 or c2==d2:
        print('MATCH')
    else:
        c1[2],c1[3]=c1[3],c1[2]
        c2[2],c2[3]=c2[3],c2[2]
        #print(c1)
        if c1==d1 or c1==d2 or c2==d1 or c2==d2:
            print('MATCH')
        else:
            print('DIFFERENT')
             
swap(c1,c2)
#print(c1, c2, d1, d2)