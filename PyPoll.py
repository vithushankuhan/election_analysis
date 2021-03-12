# The Data we need to retreive.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular votes.

# Import datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
timeNow = dt.datetime.now()
# Print the present time
print("The time right now is ", timeNow)    

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis.
    print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
    # Close the file
    election_data.close()

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using outfile open the file 
outfile = open(file_to_save, "w")
# Write three counties to the file
outfile.write("Counties in the Election\n------------------------\nArapahoe\nDener\nJefferson")
# Close the file
outfile.close()
