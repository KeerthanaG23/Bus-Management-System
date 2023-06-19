import csv
clean_data = []

with open("data_miniproj1.csv", "r") as f:
    reader = csv.reader(f)
    counter = 0
    for i in reader:
        if i[0] != '':
            clean_data += [[]]
            clean_data[counter] += [i[0]]
            temp = ''
            try:
                for j in i[3:i.index('')]:
                    temp += j + ','

            except:
                for j in i[3:]:
                    temp += j + ','

            clean_data[counter] += [temp[:-1]]
            counter += 1
            print(i)
with open("RAW.csv", 'w') as g:
    writer = csv.writer(g)
    writer.writerows(clean_data)
