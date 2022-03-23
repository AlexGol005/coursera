class Man:
    surname = ''
    name = ''
    sch_num = 0
    middle_grade = 0


def manKey(man):
    return (man.surname, man.name, man.sch_num, man.middle_grade)


peopleList = []
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
for line in inFile:
    tempManData = line.split()
    man = Man()
    man.surname = tempManData[0]
    man.name = tempManData[1]
    man.sch_num = tempManData[2]
    man.middle_grade = tempManData[3]
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.surname, man.name, man.sch_num, man.middle_grade, file=outFile)

inFile.close()
outFile.close()
