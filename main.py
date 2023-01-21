from xml.dom import minidom

FILE_BARBATI="D:\\pythonProject\\GenerarePersoane\\PrenumeBaieti.txt"
FILE_FEMEI="D:\\pythonProject\\GenerarePersoane\\PrenumeFete.txt"
FILE_NUME_FAMILIE="D:\\pythonProject\\GenerarePersoane\\NumeFamilie.txt"

criteriu_lungime=lambda nume:len(nume)

def nrVocale(s):
    s=s.lower()
    kv=0
    vocale=['a','e','i','o','u','ă','î','â','y']
    for litera in s:
        if litera in vocale:
            kv=kv+1
    return kv

def nrConsoane(s):
    s = s.lower()
    kc=0
    consoane=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','ș','t','ț','v','w','x','z']
    for litera in s:
        if litera in consoane:
            kc=kc+1
    return kc

def nrDiacritice(s):
    s = s.lower()
    kd=0
    diacritice=[ord('ă'),ord('â'),ord('î'),ord('ș'),ord('ț')]
    for litera in s:
        if ord(litera) in diacritice:
            kd=kd+1
    return kd

def prenumeXMLGenerator():
    f1=open(FILE_BARBATI,'r',encoding="utf-8-sig")
    f2=open(FILE_FEMEI,'r',encoding="utf-8-sig")
    if f1==None or f2==None:
        raise Exception("Fisierul nu a putut fi deschis!!!")
    else:
        listaBarbati=[]
        for line in f1:
            listaBarbati.append(line.strip())
        f1.close()

        listaFemei=[]
        for line in f2:
            listaFemei.append(line.strip())
        f2.close()
        root=minidom.Document()
        listaPrenume=root.createElement("listaPrenume")
        root.appendChild(listaPrenume)
        listaBarbati=sorted(listaBarbati,key=criteriu_lungime)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=(lambda nume: nrDiacritice(nume)),reverse=True)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=(lambda v:nrVocale(v)),reverse=True)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=(lambda c:nrConsoane(c)),reverse=True)
        print(listaBarbati)
        for p in listaBarbati:
            e=root.createElement("prenume")
            e.setAttribute("lungime",str(len(p)))
            e.setAttribute("sex","M")
            e.setAttribute("consoane",str(nrConsoane(p)))
            e.setAttribute("vocale",str(nrVocale(p)))
            e.setAttribute("diacritice",str(nrDiacritice(p)))
            nodText=root.createTextNode(p)
            e.appendChild(nodText)
            listaPrenume.appendChild(e)
        for f in listaFemei:
            e=root.createElement("prenume")
            e.setAttribute("lungime",str(len(f)))
            e.setAttribute("sex","F")
            e.setAttribute("consoane",str(nrConsoane(f)))
            e.setAttribute("vocale",str(nrVocale(f)))
            e.setAttribute("diacritice",str(nrDiacritice(f)))
            nodText=root.createTextNode(f)
            e.appendChild(nodText)
            listaPrenume.appendChild(e)

        xml_str=root.toprettyxml(indent="\t")
        file="prenume.xml"
        with open(file,"w",encoding="utf-8-sig") as f:
            f.write(xml_str)
        f.close()

def numeFamilieXMLGenerator():
    f3=open(FILE_NUME_FAMILIE,'r',encoding="utf-8-sig")
    if f3==None:
        raise Exception("Fisierul nu a putut fi deschis!!!")
    else:
        listaNumeFamilie=[]
        for line in f3:
            listaNumeFamilie.append(line.strip())
        f3.close()
        root = minidom.Document()
        listafamilie = root.createElement("listaNumeFamilie")
    root.appendChild(listafamilie)
    for n in listaNumeFamilie:
        e = root.createElement("numeFamilie")
        e.setAttribute("lungime", str(len(n)))
        e.setAttribute("consoane", str(nrConsoane(n)))
        e.setAttribute("vocale", str(nrVocale(n)))
        e.setAttribute("diacritice", str(nrDiacritice(n)))
        nodText = root.createTextNode(n)
        e.appendChild(nodText)
        listafamilie.appendChild(e)

    xml_str = root.toprettyxml(indent="\t")
    file = "numeFamilie.xml"
    with open(file, "w", encoding="utf-8-sig") as f:
        f.write(xml_str)
    f.close()


n="Mihăiță"
x1=nrVocale(n)
x2=nrConsoane(n)
x3=nrDiacritice(n)
print(x1,x2,x3)
print(x1+x2==len(n))
prenumeXMLGenerator()
numeFamilieXMLGenerator()

