import csv
import random

try:
    with open('final.csv', 'w') as w:
        w.write('')
except Excetpion as e:
    print(e)

static =[

        "timestamp", "team_leader_name", "team_leader_email", "team_leader_mobile", 
        "org_name,member2_name", "member2_email", "member3_name", "member3_email", 
        "member4_name", "member4_email", "member5_name", "member5_email", "teacher_name", 
        "teacher_email", "teacher_mobile", "policyID", "password", "tname", "team_state"
]

NUM = 560

length = len(static)

with open('final.csv', 'a') as csvw:
            writer = csv.writer(csvw, delimiter=',')
            writer.writerow(static)



def randteam():
    alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
    ALPHA_NUM = list('0123456789'+ alpha)
    a = ''
    for i in range(6):
        a += random.choice(ALPHA_NUM)
    return a

amba = 0
with open('matha.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    temp = 0
    for row in reader:
        temp += 1  # Counter
        if temp == 2: 
            continue
        con = len(filter(lambda x: x!='', row))

        if con == 1:
            continue
        elif con == 0:
            break
        print('===============================')
        print('\n')
        data = [0]*length
        data[0] = ''
        data[1] = row[1]
        data[2] = row[4]
        data[3] = row[2]

        data[4] = row[0]
        data[5] = row[5]
        data[6] = row[6]
        data[7] = row[7]
        data[8] = row[8]
        data[9] = row[9]
        data[10] = row[10]
        data[11] = row[11]
        
        data[12] = ''
        data[13] = ''
        data[14] = ''
        data[15] = '2020POLICY'+randteam()
        data[16] = data[1].split()[0].lower() + '@123'
        data[17] = 'PolicyTest'+ str(NUM) + str(amba)
        data[18] = row[13]
        print(data)
        amba += 1

        with open('final.csv', 'a') as csvw:
            writer = csv.writer(csvw, delimiter=',')
            writer.writerow(data)
