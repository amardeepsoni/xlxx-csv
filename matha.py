import csv
import random

try:
    with open('final.csv', 'w') as w:
        w.write('')
except Excetpion as e:
    print(e)

static =[

        "timestamp", "team_leader_name", "team_leader_email", "team_leader_mobile", 
        "org_name", "member2_name", "member2_email", "member3_name", "member3_email", 
        "member4_name", "member4_email", "member5_name", "member5_email", "teacher_name", 
        "teacher_email", "teacher_mobile", "policyID", "password", "tname", "team_state"
]

NUM = 509

length = len(static)

with open('final.csv', 'a') as csvw:
            writer = csv.writer(csvw, delimiter=',')
            writer.writerow(static)



amba = 0
with open('matha.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    temp = 0
    for row in reader:
        temp += 1  # Counter
        if temp == 2: 
            continue
        con = len(list(filter(lambda x: x!='', row)))

        if con == 1:
            continue
        elif con == 0:
            break
        print('===============================')
        print('\n')
        data = [0]*length
        data[0] = ''
        data[1] = row[1].strip()
        data[2] = row[4].strip()
        data[3] = row[2].strip()

        data[4] = ' '.join(row[0].split(',')).strip()
        data[5] = row[5].strip()
        data[6] = row[6].strip()
        data[7] = row[7].strip()
        data[8] = row[8].strip()
        data[9] = row[9].strip()
        data[10] = row[10].strip()
        data[11] = row[11].strip()
        data[12] = row[12].strip()
        
        data[13] = ''
        data[14] = ''
        data[15] = ''
        
        data[16] = '2020POLICYIRSC'+ str(NUM + amba).strip()
        data[17] = (data[1].split()[0].lower() + '@123').strip()
        data[18] = ('PolicyTeam'+ str(NUM + amba)).strip()
        data[19] = row[13].strip()
        print(data[4])
        amba += 1

        with open('final.csv', 'a') as csvw:
            writer = csv.writer(csvw, delimiter=',')
            writer.writerow(data)

