import os
import csv

py_bank=os.path.join('Resources','budget_data.csv')

with open (py_bank) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)
    
    months=[]
    profit_losses=[]
    
    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

     
    for row in csvreader:
        month=row[0]
        profit_loss=row[1]

        months.append(month)
        profit_losses.append(profit_loss)

    m_count = len(months)

for loop1 in range (m_count):
    total = total + int(profit_losses[loop1])

for loop2 in range(m_count-1):
    a_change = a_change + (float(profit_losses[loop2+1]) - float(profit_losses[loop2]))

    m_change = (float(profit_losses[loop2 +1 ])-float(profit_losses[loop2])) 

    if m_change>delta1:
        delta1 = m_change
        delta_line1 = loop2
    else:
        delta2 = delta2

analysis = f'\
Financial Analysis\n\
------------------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Averag Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1 + 1]} (${int(delta1)})\n\
Greatest Decrease in profits: {months[delta_line2 + 1]} (${int(delta2)})\n'

print(analysis)

file1 = open("./Analysis/pybank.txt","w")
file1.writelines(analysis)
file1.close()

