import csv
import os
from csv import writer
from csv import reader
import numpy as np
import pandas as pd
os.system('cls')
# os.system('clear')


try:
    with open('octant_input.csv', 'r') as read_obj, \
            open('output.csv', 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            csv_writer.writerow(row)
except:
    print("octant_input.csv is not found")
#  creating a new list for average value


u1=[]
v1=[]
w1=[]

try:
    with open('output.csv', 'r',newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u1.append(row['U'])
            v1.append(row['V'])
            w1.append(row['W'])
except:
    print("output.csv not found")
    
u2=[eval(x) for x in u1]
v2=[eval(x) for x in v1]
w2=[eval(x) for x in w1] 
u1_avg=sum(u2)/len(u2);
v1_avg=sum(v2)/len(v2);
w1_avg=sum(w2)/len(w2);
 
df = pd.read_csv("output.csv")  
# adding the values for avarage
df.at[0,'u_avg']=u1_avg
df.at[0,'v_avg']=v1_avg
df.at[0,'w_avg']=w1_avg

#  finding the values of "V'=V - V avg" and insert in outfile using" db.at" function
for i in range(0,len(u2)):
    df.at[i,'U_avg=U - U avg']=u2[i]-u1_avg
for i in range(0,len(v2)):
    df.at[i,'V_avg=V - V avg']=v2[i]-v1_avg
for i in range(0,len(w2)):
    df.at[i,'W_avg=W - W avg']=w2[i]-w1_avg

n=len(u2)
octant_list=[]



# finding the value of octant ans insert in output file
try:
    for i in range(0,n):
        if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']>0):
            df.at[i,"Octant"]=1
            octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']<0):
            df.at[i,'Octant']=-1
            octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']>0):
            df.at[i,'Octant']=2
            octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']<0):
            df.at[i,'Octant']=-2
            octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']>0):
            df.at[i,'Octant']=3
            octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']<0):
                df.at[i,'Octant']=-3
                octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']>0):
            df.at[i,'Octant']=4
            octant_list.append(df.at[i,'Octant'])
            
        if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']<0):
                df.at[i,'Octant']=-4
                octant_list.append(df.at[i,'Octant'])
except:
    print("Octant_list not found")    


# adding a coummn for user input ans overall count    
df.at[2,' '] ='User input'      
df.at[0,'Octant ID']='Overall Count'   

         
#   inserting the feequency data
df.at[0,'1']=octant_list.count(1)
df.at[0,'-1']=octant_list.count(-1)
df.at[0,'2']=octant_list.count(2)
df.at[0,'-2']=octant_list.count(-2)
df.at[0,'3']=octant_list.count(3)
df.at[0,'-3']=octant_list.count(-3)
df.at[0,'4']=octant_list.count(4)
df.at[0,'-4']=octant_list.count(-4)









# function for split the list into equal parts
def list_split(listA, n):
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n+x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                [None for y in range(n-len(every_chunk))]
        yield every_chunk
        
    
    
# main function for creating frequency in a  given range  and inserting  in csv file     
try:
    def octact_identification(mod):
        start=0;
        i=3
        df.at[2,'Octant ID']="Mod "+str(mod)
        try:
          lis=list(list_split(octant_list, mod))
        except:
            print("The function List_split not found")
        lis_size=len(lis)
        i=3
        for x in lis:
            if(i-2==lis_size):
                df.at[i,'Octant ID']=str(start)+"-"+str(n-1)
            else:
                df.at[i,'Octant ID']=str(start)+"-"+str(start+mod-1)
            df.at[i,'1']=x.count(1)
            df.at[i,'-1']=x.count(-1)
            df.at[i,'2']=x.count(2)
            df.at[i,'-2']=x.count(-2)
            df.at[i,'3']=x.count(3)
            df.at[i,'-3']=x.count(-3)
            df.at[i,'4']=x.count(4)
            df.at[i,'-4']=x.count(-4)
            i+=1
            start=start+mod
except:
    print("The function octact_identification is not found ")


# mod=int(input("Enter your value of Mod: "))
mod=5000
try:
  octact_identification(mod)
except:
    print("The function octact_identification is not found")


# saving the csv file
df.to_csv("output.csv",index=False)

