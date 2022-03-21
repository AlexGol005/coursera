dict_ = {}
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
for line in inFile:
    line = line.split()
    if int(line[2]) not in dict_:
        dict_[int(line[2])] = [int(line[3])]
    else:
        dict_[int(line[2])].append(int(line[3]))

print(dict_)

inFile.close()
outFile.close()