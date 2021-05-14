import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

""" 
Run time for the program to call the api, create a dataframe, append dataframes, export as excel file, create a boxplot, on average is around 140 seconds from start to finish
"""


# Creating an empty dataframe
dataFrame = pd.DataFrame()
# Opens the data to read
with open('/Users/milnessam/PycharmProjects/vis-data-science-diagnostic-exercise/data/uniprot_ids.csv', 'r') as op:
    reader = csv.reader(op)
    data = ""
    # loop to read through every line in the data file
    for row in reader:
        # if a line from the file contains an invalid character such as '|', skip over that line
        if row[0] == '|':
            pass
        else:
            # else, assign each line's id to the string variable 'data', which then gets passed into the url variable to get the full url for the API call
            data = row[0]
        # Creates the full url with each unique uniprot ID
        url = 'https://www.uniprot.org/uniprot/' + data + '.tab'
        # Creates a dataframe for each specific ID by calling the api
        df = pd.read_table(url, sep="\t")
        # Combines each ID dataframe together by appending
        dataFrame = dataFrame.append(df, ignore_index=True)
        # Manipulates the data frame and drop's the columns not needed
        newFrame = dataFrame.drop(columns=['Status', 'Entry name'])
        # Manipulates the data frame and renames needed columns
        finalDataFrame = newFrame.rename(columns={'Entry': 'Uniprot ID', 'Gene names': 'Gene', 'Protein names': 'Protein'})

# Exports the  finalDataFrame as an excel file
dfToExcel = finalDataFrame.to_excel('/Users/milnessam/PycharmProjects/vis-data-science-diagnostic-exercise/data/unprot1.xlsx')


"""
    - Creates a boxplot using matplotlib and seaborn packages
    - Creates the x variable as the 'organism' column, which compares the two types of organisms in the data, humans vs. mouse
    - Creates the y variable as the 'length' column, which compares the two different organisms protein length
"""
x = finalDataFrame['Organism']
y = finalDataFrame['Length']
plt.figure(figsize=(7, 7))
ax = sns.boxplot(x=x, y=y, data=finalDataFrame).set_title('Human vs. Mouse Protein Length')
print(plt.show())
