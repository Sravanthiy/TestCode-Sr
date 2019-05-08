# TestCode-Sr

PreRequisites:
  Expects Data file and Code to be on the same path.

Data file name: Mobile Phone Masts.csv

Code to be executed: Main.py

Description: 
    Code has the following functions:
    
       1. Main:Reads data file. Calls the process data function and Takes the user input which includes performing all the functions or none and exit.
        
       2. All(data, header):	calls the functions fieldSortAndTop,filterOnLeaseYears, groupByField,filterOnLeaseSD(data)
      
       3.Choice to print the choice text. Called to only print the choice text for user
       
       4. processData(file) returns a header list and data in dictionary format. Used to process the input file into a dictionary
       
       5. extraCommas takes input as a line and removes one extra comma within double quotes. This is used by processData function
       
       6.fieldSortAndTop(data, col) produces a list of top 5 items in column col. Defaulted to column Tenant name.
       
       7. groupByField(data,  col) Create a dictionary groupng by col and a count of masts for each value. col name is defaulted to tenant name.
       
       8. filterOnLeaseSD(data,header,col,startdate,enddate,formatcolumns): Lists the data for rentals with col values between start date and end date. Defaulted to Lease start date between 1 Jun 1999 and 31 Aug 2007.
       
       9. filterOnLeaseYears(data, h, y, col,s): where 'col' value is 'y' and sums the amount in column 's'. Defaults y=25, col='Lease Years',s='Current Rent'
       

      
