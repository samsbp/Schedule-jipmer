__author__="rohit"
# Dictionary Format : year_of_join, name,p_unit,current_unit, sem, micu, hdu, ems, gastro, neph, neuro, cardio
# We need a new Excel Sheet Format for the sake of simple program
#that should be in the above format
#class Definition
class Doctor:
    def __init__(self,doc_dict): #subjected to key errors if not carefull
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
def get_ems(i,j,emplist): #note that ems_i and ems_j should be global or should be passed by reference
    found = False
    for k in range(len(unit[i])):
        if unit[i][k].ems==0 and unit[i][k].sem==2:
            emplist.append(unit[i][k])
            unit[i][k].ems=1
            unit[i][k].hidden=True
            found=True
            break
    if found:
        for k in range(len(unit[j])):
            if unit[j][k].ems == 0 and unit[j][k].sem==2:
                emplist.append(unit[j][k])
                unit[j][k].ems =1
                unit[j][k].hidden =True
                return (i,j)
                break                      #end stage for recursion
    if not found:  # for 1 shift
        i = i + 1 % 6
        j = j + 1 % 6
        get_ems(i, j,emplist)

# 1shift = when you dont find a doctor availale
# 2shift = next month iteration




#end of class definition

if __name__ == '__main__':
    import pandas as pd
    unit=[[],[],[],[],[],[]]
    xf=pd.ExcelFile("M:\Project Files\Scheduling\P1\Book1.xlsx")
    sheet1=xf.parse(0)
    for i in range(len(sheet1)):   #if a student has discontinued  we need to load a name='blank' in the excel sheet
        dic=dict(sheet1.iloc[i]) #NOT iMPLEMENTED ERROR WILL OCCOUR IF iloc(i) use iloc[i]
        doc=Doctor(dic)
        #combine doc=Doctor(dict(sheet1.iloc(i)))
        unit[int(doc.current_unit)-1].append(doc)
    #by the end of this loop we can get unit[0],unit[1]...each as a list of Doctor objects
    #now we can operate only on units
    for j in range(len(unit)):
        print(j)
        for i in unit[j]:
            if not i.hidden:
                print(i)
    list1=[]
    get_ems(0,1,list1)
    print("ems ppl")
    for k in list1:
        print(k)

#def schedule():

















