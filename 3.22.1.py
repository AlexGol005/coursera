class Man:
    surname = ''
    name = ''
    school_num = 0
    middle_grade = 0

def manKey(man):
    return (man.surname, man.name, man.school_num, man.middle_grade)

n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.height = int(tempManData[0])
    man.name = tempManData[1]
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.height, man.name)


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')



inFile.close()
outFile.close()