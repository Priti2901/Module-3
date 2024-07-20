import os
import csv

py_bank=os.path.join('Resources','budget_data.csv')

Date=[]
Profit_Losses=[]
pl_in_cm=[]
pl_in_nm=[]
A_C=[]

with open (py_bank) as csvfile:
    csvreader=csv.reader(py_bank,delimiter=',')

    csv_header=next(py_bank)
    print(f"Header:{csv_header}")

    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(row[1])
        pl_in_cm.append((row[1]).pop(-1))
        pl_in_nm.append((row[1]).pop(0))
        A_C.append(pl_in_nm-pl_in_cm)
  

        def print (py_bank_data):
            Date=str(Date)
            Profit_Losses=int(Profit_Losses)
            pl_in_cm=int(pl_in_cm)
            pl_in_nm=int(pl_in_nm)
            A_C=int(A_C)
        
        Total_Months=len(Date)
        Total = sum(Profit_Losses)
        Average_Changes=sum(A_C)/len(A_C)
        Greatest_Increase_in_Profits = max(A_C)
        Greast_Decrease_in_Profits =min(A_C)

    print("Financial Analysis")






        



        
        

    

 





