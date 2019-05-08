import pandas as pd
import datetime as dt


def fieldSortAndTop(data, field="Current Rent", top=5):
    # produce a list sorted by Current Rent in ascending order .
    ##Obtain the first 5 items from the resultant list and  output to the console.
    try:
        newdata = data.sort_values([field]).head(top)
        print('\n' + '\033[1m' + '\033[4m' + "Sorting Data by", field, "and displaying top", top, "rows" + '\033[0m')
        print(newdata)
        return newdata
    except:
        print("Encountered an exception. Please verify input")



def filterOnLeaseYears(data, i=25):
    # From the list of all mast data create new list of mast data with Lease Years = 25 years.
    # Output the list to the console, include all data fields.
    # Output the total rent for all items in this list to the console
    try:
        i = int(i)
        newdata = data[data["Lease Years"] == i]
        if len(newdata) > 0:
            print('\n' + '\033[1m' + '\033[4m' + "Mast data where Lease years =", i, '\033[0m')

            print(newdata)
            print()
            print("Total Rent on all Masts where Lease Years are ", i, " is", newdata["Current Rent"].sum())
            print()
            return newdata
        else:
            print("No such records")
            return None
    except:
        print("Please provide the right input")


def groupByField(data, comment=""):
    ##Requirement:
    # Create a dictionary containing tenant name and a count of masts for each tenant.
    # Output the dictionary to the console in a readable form.
    #

    # Grouping data
    newdata = data.groupby(["Tenant Name"])["Property Name"].count().rename("count").reset_index()

    # Initialising and assigning values to Dictionary
    newdict = {}
    for i in range(len(newdata)):
        newdict[newdata.iloc[i]["Tenant Name"]] = newdata.iloc[i]["count"]

    # Displaying output
    print('\n' + '\033[1m' + '\033[4m' + "Grouped by Tenant Name", comment, '\033[0m')
    for key in newdict.keys():
        print(key, ":", newdict[key])
    return newdict


def groupByFieldCaseInsenstve(data):
    data["Tenant Name"] = data["Tenant Name"].str.upper()
    groupByField(data, "(Case Insensitive)")



def filterOnLeaseSD(data):
    # Requirement:
    # List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
    # Output the data to the console with dates formatted as DD/MM/YYYY
    ##

    # Converting Date strings to date formats
    data["LeaseSD"] = list(map(lambda x: dt.datetime.strptime(x, "%d %b %Y"), data["Lease Start Date"]))
    data["LeaseED"] = list(map(lambda x: dt.datetime.strptime(x, "%d %b %Y"), data["Lease End Date"]))
    # Filtering data as per requirement
    newdata = data[(data["LeaseSD"] >= '1 June 1999') & (data["LeaseSD"] <= '31 Aug 2007')]
    # formatting output
    newdata["Lease Start Date"] = newdata["LeaseSD"].dt.strftime('%d/%m/%Y')
    newdata["Lease End Date"] = newdata["LeaseED"].dt.strftime('%d/%m/%Y')
    newdata.drop(["LeaseSD", "LeaseED"], inplace=True, axis=1)
    # displaying output
    print('\n' + '\033[1m' + '\033[4m' + "Data filtered on Lease Start Date" + '\033[0m')
    print(newdata)
    return newdata


# filterOnLeaseSD(data)
def all(data):
    fieldSortAndTop(data)
    filterOnLeaseYears(data)
    groupByField(data)
    filterOnLeaseSD(data)


if __name__ == "__main__":
    # Reading the csv file
    inputdata = pd.read_csv("Mobile Phone Masts.csv")


    def choice():
        # Choice text
        print("\n\nChoose the operation you would like to perform")
        print("1:Produce a list sorted by Current Rent in ascending order and Obtain the first 5 items from the "
              "resultant list.") 
        print("2: From the list of all mast data create new list of mast data with Lease Years = 25 years and include "
              "total rent") 
        print("3: Create a dictionary containing tenant name and a count of masts for each tenant.")
        print("4. List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007. Resultant "
              "dates formatted as DD/MM/YYYY.") 
        print("5. Do all of these.")
        print("6. Exit")


    while True:
        choice()
        inputvar = input("Input choice:\t")

        if inputvar in ['6', 6, 'none', 'exit', 'Exit']:
            break
        elif inputvar in ["1", 1]:
            fieldSortAndTop(inputdata)
        elif inputvar in ["2", 2]:
            filterOnLeaseYears(inputdata)
        elif inputvar in ["3", 3]:
            groupByField(inputdata)
        elif inputvar in ["4", 4]:
            filterOnLeaseSD(inputdata),
        elif inputvar in ["5", 5, "all"]:
            all(inputdata)
        else:
            print("Incorrect Choice")
