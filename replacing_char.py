#question1 is the file name
f=open("question1","r+")
c=f.read()
l=0
for i in c:
    # 16 is the lenght of one row including the spaces between each character.It will differ from text to text
    if l==16:
        print(i)
        print("\n")
        l=0
    else:
        print(i,end=" ")
        l+=1
print("*************************************")
# using replace to replace the char we want
c=c.replace("0","1")
for i in c:
    if l==16:
        print(i)
        print("\n")
        l=0
    else:
        print(i,end=" ")
        l+=1
