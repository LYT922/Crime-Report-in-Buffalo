
def read_file(data_filename):
    teststring = ''
    with open(data_filename, 'r') as file:
        for line in file:
            teststring = teststring + line
    return teststring

def getstring():
    return read_file('Crime_Incidents.csv')

def getlists():
    incidentnumber = []
    dateandtime = []
    crimetype = []
    parentincident = []
    hourofday = []
    dayofweek = []
    address = []
    city = []
    state = []
    count1 = 1
    item = getstring().split('\n') 
    while count1 < len(item) - 2:
        if len(item[count1].split(',')[1]) == 22:
            if int(item[count1].split(',')[1][6:10]) >= 2009:
                incidentnumber.append(item[count1].split(',')[0])
                dateandtime.append(item[count1].split(',')[1])
                crimetype.append(item[count1].split(',')[3])
                parentincident.append(item[count1].split(',')[5])
                hourofday.append(item[count1].split(',')[6])
                dayofweek.append(item[count1].split(',')[7])
                address.append(item[count1].split(',')[8])
                city.append(item[count1].split(',')[9])
                state.append(item[count1].split(',')[10]) 

        count1+=1
    return [incidentnumber, dateandtime, crimetype, parentincident, hourofday, dayofweek, address, city, state]

data = getlists()
print(data[0])