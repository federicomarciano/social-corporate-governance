"""
Parish Dataset - Federico Marciano - 01/30/2022



Aim: 
     
 Associate each Parish with years when an incinerator was active.
 
 
 
Variables:
     
 - parish is the Parish of interest.
 
 - year indicates a year when an active incinerator was in the Parish of interest.
 
 - uncertain takes value 0 when the information provided is certain, value 1 
   when I have some doubts, value 2 when I have information on a plant only 
   through the spreadsheet by the Danish Energy Agency and I do not know whether 
   the plant was open before 1994 (when the spreadsheet starts); usually the 
   spreadsheet specifies the opening year of a facility, but there are exceptions.
   
 - sector takes value 0 when the plant is for public heating/electricity and value
   1 when the plant is used for manufacturing/residential purposes. 


 
Notes:
     
 - our sample starts in 1980 and ends in 2018. 
 
 - the most reliable information is from 1994 onward, because we have the spreadsheet
   by the Danish Energy Agency.
   
 - the raw data from which I come up with this code are stored in Incinerators.xlsx, 
   saved in the shared folder. In that file, the column called note is devoted to justifying 
   my decisions and approximations. 
   
 - the spreadsheet returned by this code is named ParishDataset.xlsx and saved in 
   the shared folder.
"""

import pandas as pd 
df = pd.DataFrame(columns=['year', 'parish', 'uncertain', 'sector'])
                  
#Aalborg
for i in range(1980, 2019): 
    values_to_add={'year':i, 'parish':8371, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Aars 
for i in range(1985, 2019): 
    values_to_add={'year':i, 'parish':8269, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Albertsund
for i in range(1980, 1993): 
    values_to_add={'year':i, 'parish':9134, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Aarhus 1
for i in range(1980, 2019): 
    values_to_add={'year':i, 'parish':8127, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Aarhus 2 
for i in [2002, 2003, 2004, 2005, 2006, 2007, 2008]: 
    values_to_add={'year':i, 'parish':8114, 'uncertain':2, 'sector':1}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Aarhus 3 
values_to_add={'year':1994, 'parish':7039, 'uncertain':2, 'sector':0}
row_to_add=pd.Series(values_to_add)
df=df.append(row_to_add, ignore_index=True)

#Brondby 
for i in range(1980, 1993): 
    values_to_add={'year':i, 'parish':7144, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Copenhagen  
for i in range(1980, 2019): 
    values_to_add={'year':i, 'parish':7082, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Esbjerg 1
for i in range(2003, 2019): 
    values_to_add={'year':i, 'parish':8908, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Esbjerg 2 
for i in range(2008, 2010): 
    values_to_add={'year':i, 'parish':8906, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Ferikshavn
for i in range(1994, 2019): 
    values_to_add={'year':i, 'parish':8430, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Gerlev 
for i in range(1980, 1986): 
    values_to_add={'year':i, 'parish':7453, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Glostrup 
for i in range(1980, 2019): 
    values_to_add={'year':i, 'parish':7147, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Graested
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':7432, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1994, 1996): 
    values_to_add={'year':i, 'parish':7432, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Grenaa 
for i in range(1981, 2019): 
    values_to_add={'year':i, 'parish':8231, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Haderslev 
for i in range(1980, 1993): 
    values_to_add={'year':i, 'parish':8965, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1993, 2014): 
    values_to_add={'year':i, 'parish':8965, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Hadsund 
for i in range(1984, 2006): 
    values_to_add={'year':i, 'parish':9191, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Hammel 
for i in range(1980, 1986): 
    values_to_add={'year':i, 'parish':8022, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1986, 2019): 
    values_to_add={'year':i, 'parish':8022, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Herning 
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':8803, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1994, 2011): 
    values_to_add={'year':i, 'parish':8803, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Hjorring 
for i in range(1980, 1986): 
    values_to_add={'year':i, 'parish':7448, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1986, 2019): 
    values_to_add={'year':i, 'parish':7448, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Hobro
for i in range(1984, 2018): 
    values_to_add={'year':i, 'parish':8198, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Holstebro 
for i in range(1980, 1993): 
    values_to_add={'year':i, 'parish':8814, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1993, 2019): 
    values_to_add={'year':i, 'parish':8814, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Horsens 
for i in range(1992, 2019): 
    values_to_add={'year':i, 'parish':9077, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Hosholm 
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':9145, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1994, 2019): 
    values_to_add={'year':i, 'parish':9145, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Jerslev Sjaelland 
for i in range(1994, 1995): 
    values_to_add={'year':i, 'parish':7219, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Kolding 1
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':7929, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Kolding 2
for i in range(1982, 2019): 
    values_to_add={'year':i, 'parish':7933, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Korsor 
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':7348, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Magleby 
for i in range(1980, 1986): 
    values_to_add={'year':i, 'parish':7495, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Mariager 
for i in range(1999, 2001): 
    values_to_add={'year':i, 'parish':8199, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Middelfart 
for i in range(1980, 1984): 
    values_to_add={'year':i, 'parish':7823, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1984, 2007): 
    values_to_add={'year':i, 'parish':7823, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)   

#Naestved 
for i in range(1983, 2019): 
    values_to_add={'year':i, 'parish':7511, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Nyborg 1
for i in range(1980, 1983): 
    values_to_add={'year':i, 'parish':7724, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1983, 2019): 
    values_to_add={'year':i, 'parish':7724, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Nyborg 2 
for i in range(1994, 1997): 
    values_to_add={'year':i, 'parish':7197, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Nykobing F 
for i in range(1983, 2019): 
    values_to_add={'year':i, 'parish':7578, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Norre Alslev 
for i in range(1991, 1994): 
    values_to_add={'year':i, 'parish':7613, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1995, 2019): 
    values_to_add={'year':i, 'parish':7613, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Odense 
for i in range(1996, 2019): 
    values_to_add={'year':i, 'parish':7782, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Padborg 
values_to_add={'year':2013, 'parish':9029, 'uncertain':2, 'sector':0}
row_to_add=pd.Series(values_to_add)
df=df.append(row_to_add, ignore_index=True)

#Rodekro 
for i in range(1995, 2004): 
    values_to_add={'year':i, 'parish':9011, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Ronne 
for i in range(1991, 2019): 
    values_to_add={'year':i, 'parish':7553, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Roskilde 
for i in range(1981, 2019): 
    values_to_add={'year':i, 'parish':7156, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Sindal 
for i in range(1980, 1986): 
    values_to_add={'year':i, 'parish':8428, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Skagen 
for i in range(1980, 2018): 
    values_to_add={'year':i, 'parish':8480, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Skanderborg 
for i in range(1984, 2019): 
    values_to_add={'year':i, 'parish':9166, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Skive 
for i in range(1984, 2001): 
    values_to_add={'year':i, 'parish':9085, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Slagelse 
for i in range(1981, 1983): 
    values_to_add={'year':i, 'parish':9144, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1983, 2018): 
    values_to_add={'year':i, 'parish':9144, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Sonderborg 1
for i in range(1996, 2019): 
    values_to_add={'year':i, 'parish':8992, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Sonderborg 2 
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':8988, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1994, 1996): 
    values_to_add={'year':i, 'parish':8988, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Svendborg 
for i in range(1980, 1994): 
    values_to_add={'year':i, 'parish':9238, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1994, 1996): 
    values_to_add={'year':i, 'parish':9238, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1999, 2019): 
    values_to_add={'year':i, 'parish':9238, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Saeby 
for i in range(1997, 2002): 
    values_to_add={'year':i, 'parish':7293, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Thisted 
for i in range(1980, 1991): 
    values_to_add={'year':i, 'parish':8721, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1991, 2019): 
    values_to_add={'year':i, 'parish':8721, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Taastrup 
for i in range(1989, 1994): 
    values_to_add={'year':i, 'parish':7152, 'uncertain':1, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
for i in range(1994, 2005): 
    values_to_add={'year':i, 'parish':7152, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)
    
#Terndrup 
for i in range(1994, 1999): 
    values_to_add={'year':i, 'parish':9217, 'uncertain':2, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Thyholm 
values_to_add={'year':2003, 'parish':8657, 'uncertain':2, 'sector':0}
row_to_add=pd.Series(values_to_add)
df=df.append(row_to_add, ignore_index=True)

#Vejen 
for i in range(1990, 2011): 
    values_to_add={'year':i, 'parish':8931, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

#Videbaek 
for i in range(1981, 1994): 
    values_to_add={'year':i, 'parish':8769, 'uncertain':0, 'sector':0}
    row_to_add=pd.Series(values_to_add)
    df=df.append(row_to_add, ignore_index=True)

    
writer=pd.ExcelWriter('ParishDataset.xlsx')
df.to_excel(writer, index=False)
writer.save()


