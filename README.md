# TestCode-Sr

PreRequisites:
  Expects Data file and Code to be on the same path.

Data file name: Mobile Phone Masts.csv

Code to be executed: Main.py
Description:
Code has the following functions:
  1.Choice to print the choice text
  2. processData(file) returns a header list and data in dictionary format.
  3. extraCommas takes input as a line and removes one extra comma within double quotes
  4.fieldSortAndTop(data, header,col) produces a list of top 5 items in column col. Defaulted to column Tenant name
  5. groupByField(data, header, col) Create a dictionary containing tenant name and a count of masts for each tenant. col number is defaulted to tenant name
  6. filterOnLeaseSD(data,header,col,startdate,enddate): Lists the data for rentals with col values between start date and end date. Defaulted to Lease start date between 1 Jun 1999 and 31 Aug 2007.
  7. all(data, header):	calls the functions fieldSortAndTop,filterOnLeaseYears, groupByField,filterOnLeaseSD(data)
  8. Main:Takes the choice which includes performing all the functions or none and exit.
