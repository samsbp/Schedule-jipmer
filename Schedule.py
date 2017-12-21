__author__="rohit"
# Dictionary Format : year_of_join, name,p_unit,current_unit, sem, micu, hdu, ems, gastro, neph, neuro, cardio
# We need a new Excel Sheet Format for the sake of simple program
#that should be in the above format
#class Definition
class Doctor:
    def __init__(self,doc_dict): #subjected to key errors if not carefull
        self.mydict=doc_dict
        self.year_of_join = doc_dict['YEAR OF JOIN']
        self.name = doc_dict['NAME']
        self.current_unit = doc_dict['CURRENT UNIT']
        self.p_unit =doc_dict['PARENT UNIT']
        self.sem = doc_dict['SEM']
        self.micu = doc_dict['MICU']
        self.hdu = doc_dict['HDU']
        self.ems = doc_dict['EMS']
        self.gastro = doc_dict['GASTRO']
        self.nephro = doc_dict['NEPHROLOGY']
        self.neuro = doc_dict['NEUROLOGY']
        self.cardio = doc_dict['CARDIO']
        self.not_avail_micu = False
        self.hidden=False
    def __str__(self):
        return (self.name+str(self.current_unit))
    def update(self):
        self.mydict['YEAR OF JOIN']=self.year_of_join
        self.mydict['NAME']=self.name
        self.mydict['CURRENT UNIT']= self.current_unit
        self.mydict['PARENT UNIT']= self.p_unit
        self.mydict['SEM']= self.sem
        self.mydict['MICU']=self.micu
        self.mydict['HDU']=self.hdu
        self.mydict['EMS']=self.ems
        self.mydict['GASTRO']= self.gastro
        self.mydict['NEPHROLOGY']= self.nephro
        self.mydict['NEUROLOGY']=self.neuro
        self.mydict['CARDIO']= self.cardio

def get_ems(i,j,emplist,count=0): #note that ems_i and ems_j should be global or should be passed by reference
    found = False
    print("Entry")
    if count==3:
        print("-----------------FINISHED------------------")
    for k in range(len(unit[i])):
        if unit[i][k].ems==0 and unit[i][k].sem==2:
            emplist.append(unit[i][k])
            unit[i][k].ems=1
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            flag=False
            if unit[j][k].ems == 0 and unit[j][k].sem==2:
                flag=True
                print("ko")
                emplist.append(unit[j][k])
                unit[j][k].ems =1
                unit[j][k].hidden =True
                print((i+2)%6,(j+2)%6)
                return ((i+2)%6,(j+2)%6,emplist,count)    #end stage for recursion
  
    if not found:  # for 1 shift
        i = (i + 1) % 6
        j = (j + 1) % 6
        return get_ems(i, j,emplist,count+1)
        # 1shift = when you dont find a doctor availale
        # 2shift = next month iteration
# gastro
#worng code to be corrected -----------here---------
def get_gst(i,j,glist,count=0): #note that ems_i and ems_j should be global or should be passed by reference
    found = False
    print("Entry")
    if count==3:
        print("-----------------FINISHED------------------")
    for k in range(len(unit[i])):
        if unit[i][k].gastro==0 and unit[i][k].sem==3:
            glist.append(unit[i][k])
            unit[i][k].gastro=1
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            if unit[j][k].gastro== 0 and unit[j][k].sem==3:
                print("ko")
                glist.append(unit[j][k])
                unit[j][k].gastro =1
                unit[j][k].hidden =True
                print((i+2)%6,(j+2)%6)
                return ((i+2)%6,(j+2)%6,glist,count)    #end stage for recursion

    if not found:  # for 1 shift
        i = (i + 1) % 6
        j = (j + 1) % 6
        return get_gst(i, j,glist,count+1)
#nephro 
def get_neph(i,j,nephlist,count=0): #note that ems_i and ems_j should be global or should be passed by reference
    found = False
    print("Entry")
    if count==3:
        print("-----------------FINISHED------------------")
    for k in range(len(unit[i])):
        if unit[i][k].nephro==0 and unit[i][k].sem==4:
            nephlist.append(unit[i][k])
            unit[i][k].nephro=1
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            flag=False
            if unit[j][k].nephro== 0 and unit[j][k].sem==4:
                flag=True
                print("ko")
                nephlist.append(unit[j][k])
                unit[j][k].nephro =1
                unit[j][k].hidden =True
                print((i+2)%6,(j+2)%6)
                return ((i+2)%6,(j+2)%6,nephlist,count)    #end stage for recursion

    if not found:  # for 1 shift
        i = (i + 1) % 6
        j = (j + 1) % 6
        return get_neph(i, j,nephlist,count+1)
#neuro
def get_neuro(i,j,nulist,count=0): #note that ems_i and ems_j should be global or should be passed by reference
    found = False
    print("Entry")
    if count==3:
        print("-----------------FINISHED------------------")
        return
    for k in range(len(unit[i])):
        if unit[i][k].neuro==0 and unit[i][k].sem==4:
            nulist.append(unit[i][k])
            unit[i][k].neuro=1
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            flag=False
            if unit[j][k].neuro== 0 and unit[j][k].sem==4:
                flag=True
                print("ko")
                nulist.append(unit[j][k])
                unit[j][k].neuro =1
                unit[j][k].hidden =True
                print((i+2)%6,(j+2)%6)
                return ((i+2)%6,(j+2)%6,nulist,count)    #end stage for recursion
   
    if not found:  # for 1 shift
        i = (i + 1) % 6
        j = (j + 1) % 6
        return get_neuro(i, j,nulist,count+1)

#cardio
def get_cardio(i,j,cardlist,count=0): #note that ems_i and ems_j should be global or should be passed by reference
    found = False
    print("Entry")
    if count==3:
        print("-----------------FINISHED------------------")
        return
    for k in range(len(unit[i])):
        if unit[i][k].cardio==0 and unit[i][k].sem==5:
            cardlist.append(unit[i][k])
            unit[i][k].cardio=1
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            flag=False
            if unit[j][k].cardio== 0 and unit[j][k].sem==5:
                flag=True
                print("ko")
                cardlist.append(unit[j][k])
                unit[j][k].cardio =1
                unit[j][k].hidden =True
                print((i+2)%6,(j+2)%6)
                return ((i+2)%6,(j+2)%6,cardlist,count)    #end stage for recursion
    

    if not found:  # for 1 shift
        i = (i + 1) % 6
        j = (j + 1) % 6
        return get_cardio(i, j,cardlist,count+1)


#end of class definition
def get_input(filename):
    import pandas as pd
    unit = [[], [], [], [], [], []]
    xf = pd.ExcelFile(filename)

    sheet1 = xf.parse(0)

    for i in range(len(sheet1)):  # if a student has discontinued  we need to load a name='blank' in the excel sheet
        dic = dict(sheet1.iloc[i])  # NOT iMPLEMENTED ERROR WILL OCCOUR IF iloc(i) use iloc[i]
        doc = Doctor(dic)
        # combine doc=Doctor(dict(sheet1.iloc(i)))
        unit[int(doc.current_unit) - 1].append(doc)
        # by the end of this loop we can get unit[0],unit[1]...each as a list of Doctor objects
        # now we can operate only on units
    for i in range(len(unit)):
        for k in unit[i]:
            print(k,k.sem)
    return unit
def write():
    import pandas as pd
    list1 = []
    for i in range(len(unit)):
        for j in range(len(unit[i])):
            unit[i][j].update()#update the doctor scedule to latest value
            list1.append(unit[i][j].mydict)
    df = pd.DataFrame(list1)
    df = df.reindex_axis(df.columns, axis=1)
    writer = pd.ExcelWriter("C:\\Users\\Rohit Mapakshi\\Desktop\\output.xlsx")
    df.to_excel(writer, 'Sheet1')
    writer.save()



if __name__ == '__main__':

    filename="C:\\Users\\Rohit Mapakshi\\Desktop\\TEMPLATE.xlsx"
    unit = get_input(filename)
    output="C:\\Users\\Rohit Mapakshi\\Desktop\\output.xlsx"
    (m1,m2,gt1,gt2,n1,n2,ne1,ne2,c1,c2)=(0,1,2,3,4,5,0,1,2,3)
    for count in range(0,5):#for 5 months
        print("=============iteration=======",count+1)
       
        (l1,l2,l3,l4,l5)=([],[],[],[],[])
        
        (m1,m2,l1,c)=get_ems(m1,m2,l1,0)
        print("ems ppl")
        for k in l1:
            print(k)
    
        
        (gt1,gt2,l2,c)=get_gst(gt1,gt2,l2,0)
        print("gastro ppl")
        for k in l2:
            print(k)
      

        
        (n1,n2,l3,c)=get_neph(n1,n2,l3,0)
        print("neph ppl")
        for k in l3:
            print(k)
       

      
        (ne1,ne2,l4,c)=get_neuro(ne1,ne2,l4,0)
        print("neuro ppl")
        for k in l4:
            print(k)
 
            
    
        (c1,c2,l5,c)=get_cardio(c1,c2,l5,0)
        print("cardio ppl")
        for k in l5:
            print(k)

  
    
        #write output at each end of cycle and read again to avoid errors





  















