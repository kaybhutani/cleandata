import re

def cleandata():
    fp1=open("cleanData.csv",'w')
    fp1.write("SN,IEC,Party Name,Address,IEC Allotment Date,Phone No,\
    e_mail,Exporter Type,BIN,Nature Of Concern,Directors,\n")

    clean_data=[]

    fp=open('data.csv',encoding="utf8", errors='ignore')
    sn=1
    i=0
    f1=""
    f2=""
    f3=""
    f4=""
    f5=""
    f6=""
    f7=""
    f8=""
    f9=""
    f10=""
    f11=""

    for line in fp:

        #line = fp.readline().strip()



        #print(line)

        if re.search("IEC,:,",line)!=None:
            f1=line.split(',')[2]
            i=i+1
            continue

        elif re.search("IEC Allotment Date,:,",line) != None:
            f2=line.split(',')[2]
            i=i+1
            continue

        elif re.search("Party Name and Address,:,",line) != None:
            f3=line.split(',')[2].replace('ÿ','')
            i=i+1
            #f4=fp.readline().strip() + ","
            #f4=f4 + fp.readline().strip()+ ","
            #f4=f4 + fp.readline().strip()+ ","
           # f4=f4 + fp.readline().strip()
           # f4=f4.replace(",,",",")
           # f4=f4.replace(",,",",")
           # f4=f4.replace(",,",",")
           # f4=f4.replace('"','')[:-1]
           # f4=f4.replace('Ã¿','')[1:]
            continue

        elif re.search("Phone No,:,",line) != None:
            f5=line.split(',')[2]
            i=i+1
            continue

        elif re.search("e_mail,:,",line) != None:
            f6=line.split(',')[2]
            i=i+1
            continue

        elif re.search("Exporter Type,:,",line) != None:
            f7=line.split(',')[2]
            i=i+1
            continue

        elif re.search("BIN",line) != None:
            f8=line.split(',')[2]
            i=i+1
            continue

        elif re.search("Nature Of Concern,",line) != None:
            f9=line.split(',')[2]
            i=i+1
            continue

        elif re.search("Directors:",line) != None:
            #f10=fp.readline().strip().split(',')[1].replace('Ã¿','')
            i=i+1
            continue


        if i==9:
            temp=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
            clean_data.append(temp)

            fp1.write(str(sn)+"\t"+f1+"\t"+f2+"\t"+f3+"\t"+f4+"\t"+f5+"\t"+f6+"\t"+f7\
                      +"\t"+f8+"\t"+f9+"\t"+f10+"\n")
            sn=sn+1
            i=0

    fp.close()
    fp1.close()
    return clean_data