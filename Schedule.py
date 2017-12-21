__author__="rohit"
import pandas as pd
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

#get_list is a common function for retreiving the selected two people from 2 consecutive units
#the arguments of the get_list should contain
#i,j-start of the consecutive units in integer
#pherilist-the list that contains the selected doctor for pheripheral unit
#pheripheral - the unit in which the current function should be acted upon
#sem- semester(ems-3rd sem,gastro-4th sem)
def get_list(i,j,pheripheral,sem,count=0,pherilist=[]): #note that ems_i and ems_j should be global or should be passed by reference
    if(count==0):
        pherilist=[]
    found = False
    print("Entry")
    if count==3:
        print("-----------------FINISHED------------------")
        return
    for k in range(len(unit[i])):
        if eval("unit[i][k]."+pheripheral+"==0") and unit[i][k].sem==sem:
            pherilist.append(unit[i][k])
            exec("unit[i][k]."+pheripheral+'=1')
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            flag=False
            if eval("unit[j][k]."+pheripheral+"==0") and unit[j][k].sem==sem:
                flag=True
                print("ko")
                pherilist.append(unit[j][k])
                exec("unit[j][k]."+pheripheral+'=1')
                unit[j][k].hidden =True
                print((i+2)%6,(j+2)%6)
                return ((i+2)%6,(j+2)%6,pherilist,count)    #end stage for recursion
          


        
    

    if not found:  # for 1 shift
        i = (i + 1) % 6
        j = (j + 1) % 6
        return get_list(i, j,pheripheral,sem,count+1,pherilist)    




#end of class definition
def get_input(filename):
   
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
        print("UNIT--------",i)
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
    writer = pd.ExcelWriter("C:\\Users\\sam\\Desktop\\output.xlsx")
    df.to_excel(writer, 'Sheet1')
    writer.save()



if __name__ == '__main__':

    filename="C:\\Users\\Sam\\Desktop\\jipmer\\Schedule-jipmer-master\\TEMPLATE_.xlsx"
    unit = get_input(filename)
    output="C:\\Users\\Rohit Mapakshi\\Desktop\\output.xlsx"
    (m1,m2,gt1,gt2,n1,n2,ne1,ne2,c1,c2)=(0,1,2,3,4,5,0,1,2,3)
    for count in range(0,5):#for 5 months
        print("=============iteration=======",count+1)
       
        (l1,l2,l3,l4,l5)=([],[],[],[],[])
        
        (m1,m2,l1,c)=get_list(m1,m2,"ems",2)
        print("ems ppl")
        for k in l1:
            print(k)
    
        
        (gt1,gt2,l2,c)=get_list(m1,m2,"gastro",3)
        print("gastro ppl")
        for k in l2:
            print(k)
      

        
        (n1,n2,l3,c)=get_list(m1,m2,"nephro",4)
        print("neph ppl")
        for k in l3:
            print(k)
       

      
        (ne1,ne2,l4,c)=get_list(m1,m2,"neuro",4)
        print("neuro ppl")
        for k in l4:
            print(k)
 
            
    
        (c1,c2,l5,c)=get_list(m1,m2,"cardio",5)
        print("cardio ppl")
        for k in l5:
            print(k)

  
    
        #write output at each end of cycle and read again to avoid errors





  















