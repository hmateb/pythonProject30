fajl=open("bolt.txt","r",encoding="utf-8")
next(fajl)
áfa={}
for sorok in fajl:
    sor=sorok.replace("\n","").split(" ")
    áfa.update({sor[0]:[int(sor[1]),int(sor[2])]})
print(len(áfa))
átlag=0
for i in áfa.values():
    átlag+=i[1]
print(átlag/len(áfa))
max=list(áfa.values())[0][0]
maxnev=list(áfa.keys())[0]
for i in áfa.keys():
    if max<áfa.get(i)[0]:
        max=áfa.get(i)[0]
        maxnev=i
c=0
for i in áfa.values():
    if i[0]<200:
        c+=1
print(c)
ki=open("olcso.txt","w",encoding="UTF-8")
ki.write("Horváth Máté boltjában kapható a 200 forint alatti termékék:\n")
for i in áfa.keys():
    if áfa.get(i)[0]<200:
        ki.write(f"{i}\n")
d=0
for i in áfa.values():
    if i[1]==27:
        d+=1
print(d)
petra=list()
for i in áfa.keys():
    if áfa.get(i)[0]==200:
        petra.append(i)
print(petra)