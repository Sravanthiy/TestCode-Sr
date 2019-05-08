import re
import datetime as dt


def fieldSortAndTop(data, h, col=10):
    # produce a list sorted by Current Rent in ascending order .
    ##Obtain the first 5 items from the resultant list and  output to the console.
    list1 = []
    for j in range(1, len(data), 1):
        try:
            list1.append(float(data[j][h[col]]))
        except:
            print("Error converting Current Rent to float on line", j, "\n", data[j])
    list1 = sorted(set(list1))
    top5 = list1[0:5]
    print('\n', '\033[1m' + "Top 5 " + '\033[4m', h[col].strip(), '\033[0m', "are", '\033[0m', top5)
    return list1


def filterOnLeaseYears(data, h, y=25, col=9):
    # From the list of all mast data create new list of mast data with Lease Years = 25 years.
    # Output the list to the console, include all data fields.
    # Output the total rent for all items in this list to the console

    # initialise variable
    totalrent = 0
    # printing header
    print('\n', '\033[1m', "Data where", '\033[4m', h[col], '\033[0m', "=", y, '\033[0m', '\n')
    print('\033[1m', ", ".join(h), '\033[0m')

    # iterate, filter, create new list and print data
    newmastdata = []
    for i in range(1, len(data), 1):
        if int(data[i][h[col]]) == y:
            newmastdata.append(data[i])
            print(", ".join(list(data[i].values())))
            try:
                totalrent += float(data[i][h[col]])
            except:
                print("Error converting Current Rent to float on line", i, "\n", data[i])

    print('\n', '\033[1m', "Total rent is", '\033[0m', totalrent)
    return newmastdata, totalrent


def groupByField(data, h, col=6):
    ##Requirement:
    # Create a dictionary containing tenant name and a count of masts for each tenant.
    # Output the dictionary to the console in a readable form.

    # Create a unique tenants name list
    tenants = []
    for j in range(1, len(data), 1):
        tenants.append(data[j][h[col]])
    tenants = sorted(set(tenants))

    print('\n', '\033[1m', '\033[4m', "Data Grouped by", h[col], '\033[0m')

    # Iterate over data to count the number of masts and create a dictionary
    dtnt = {}
    for i in range(0, len(tenants), 1):
        mastcount = 0
        for j in range(1, len(data), 1):
            if data[j][h[col]] == tenants[i]:
                mastcount += 1
        dtnt[tenants[i]] = mastcount
        # Output in readable format
        print(tenants[i], ":", mastcount)
    return dtnt


def filterOnLeaseSD(data, h, col=7, d1='01 Jun 1999', d2='31 Aug 2007'):
    # Requirement:
    # List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
    # Output the data to the console with dates formatted as DD/MM/YYYY
    ##

    # printing header
    print('\n', '\033[1m', "Data filtered on", '\033[4m', h[col], "between", d1, d2, '\033[0m', '\n')
    print('\033[1m', ", ".join(h), '\033[0m')

    # formatting input strings to dates
    d1 = dt.datetime.strptime(d1, "%d %b %Y")
    d2 = dt.datetime.strptime(d2, "%d %b %Y")
    newmastdata = []
    # filtered in on dates
    for i in range(1, len(data), 1):
        lstartd = dt.datetime.strptime(data[i][h[col]], "%d %b %Y")

        if d1 <= lstartd <= d2:
            lendd = dt.datetime.strptime(data[i][h[col + 1]], "%d %b %Y")
            # reformatting dates
            data[i][h[col]] = lstartd.strftime('%d/%m/%Y')
            data[i][h[col + 1]] = lendd.strftime('%d/%m/%Y')
            print(", ".join(list(data[i].values())))
            newmastdata.append(data[i])
    return newmastdata


def all(data, h):
    fieldSortAndTop(data, h)
    filterOnLeaseYears(data, h)
    groupByField(data, h)
    filterOnLeaseSD(data, h)


def choice():
    # Choice text
    print('\033[1m' + "\n\nChoose the operation you would like to perform" + '\033[0m')
    print("1: Produce a list sorted by Current Rent in ascending order and Obtain the first 5 items from the "
          "resultant list.")
    print("2: From the list of all mast data create new list of mast data with Lease Years = 25 years and include "
          "total rent")
    print("3: Create a dictionary containing tenant name and a count of masts for each tenant.")
    print("4. List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007. Resultant "
          "dates formatted as DD/MM/YYYY.")
    print("5. Do all of these.")
    print("6. Exit.")


def extraComma(line, h):
    string = re.findall(r'\"(.+?)\"', line)[0]
    newstring = re.sub(r',', '', string)
    newline = line.replace(string, newstring)
    if len(newline.split(",")) == len(h):
        return newline
    else:
        print("Error formatting line", line)


def processData(file):
    infile = file.readlines()
    headers = infile[0].strip().split(",")
    datadict = list(range(1, len(infile) + 1, 1))

    for j in range(1, len(infile), 1):
        list1 = infile[j].strip().split(",")
        if len(list1) == len(headers):
            pass
        else:   
            new = extraComma(infile[j].strip(), headers)
            list1 = new.split(",")

        datadict[j] = {}
        for i in range(0, len(headers), 1):
            datadict[j][headers[i]] = list1[i]
    return headers, datadict


if __name__ == "__main__":
    # Reading the csv file
    file1 = open("Mobile Phone Masts.csv", "r")

    header, data = processData(file1)
    while True:
        choice()
        var1 = input("Input choice:\t")
        if var1 in ['6', 6, 'none', 'exit', 'Exit']:
            break
        elif var1 in ["1", 1]:
            fieldSortAndTop(data, header)
        elif var1 in ["2", 2]:
            filterOnLeaseYears(data, header)
        elif var1 in ["3", 3]:
            groupByField(data, header)
        elif var1 in ["4", 4]:
            filterOnLeaseSD(data, header),
        elif var1 in ["5", 5, "all"]:
            all(data, header)
        else:
            print('\033[1m', "Incorrect Choice", '\033[0m')
