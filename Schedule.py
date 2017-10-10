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
    def __str__(self):
        return (self.name+str(self.current_unit))


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
            print(i)















