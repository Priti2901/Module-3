import os
import csv

py_poll=os.path.join('Resources','election_data.csv')

with open (py_poll) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)

    ballot_ids=[]
    counties=[]
    candidates=[]
    candidatenames=[]
    total_vote_can=[]
    result_per_can=[]
    total_can_per=[]

    line_count=0
    winnervotes=0
    loservote=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0


    for row in csvreader:
        ballot_id=row[0]
        county=row[1]
        candidate=row[2]
        ballot_ids.append(ballot_id)
        counties.append(county)
        candidates.append(candidate)
    line_count=len(ballot_ids)

candidatenames.append(candidates[0])

for loop1 in range (line_count -1):
    if candidates[loop1+1] !=candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

for loop2 in range (n):
    total_vote_can.append(candidates.count(candidatenames[loop2]))

loservotes=line_count

for loop3 in range(n):
    total_can_per.append(f'{round(total_vote_can[loop3]/line_count*100),4}%')
    if total_vote_can[loop3]>winnervotes:
        winner=candidatenames[loop3]
        winnervotes=total_vote_can[loop3]
    if total_vote_can[loop3]<loservotes:
        loser=candidatenames[loop3]
        loservotes=total_vote_can[loop3]

for loop4 in range(n):
    result_per_can.append(f'{candidatenames[loop4]}: {total_can_per[loop4]} {total_can_per[loop4]}')

resultlines='\n'.join(result_per_can)

analysis=f'\
Election Results\n\
-------------------\n\
Total Votes: {line_count}\n\
-------------------\n\
{resultlines}\n\
-------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
-------------------\n'

print(analysis)

file1 = open("./Analysis/pypoll.txt","w")
file1.writelines(analysis)
file1.close()


    


    

