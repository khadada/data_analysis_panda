import pandas
# Reading the csv file
data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# Get the len of each series [grey] [black] [red] and save it in the variables
gray = len(data[data['Primary Fur Color'] == 'Gray'])
black = len(data[data['Primary Fur Color'] == 'Black'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# Create object from this values
data_dict = {
    'Primary Fur Color': ['gray', 'black', 'red'],
    'Count': [gray, black, red]
}
# Create data frame from the object above
data_frame = pandas.DataFrame(data_dict)
# Covert that data frame to csv file
data_frame.to_csv('data_Squirrel_Count.csv')