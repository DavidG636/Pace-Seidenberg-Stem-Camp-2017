# The chunk of code below imports many modules which are used in the program
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import scipy as sp
from scipy import stats

# The chunk of code below reads the csv files for each month on your desktop. I fyou have the csv files on your desktop and it doesn't work, change the word after username to your username for Windowns.
september = pd.read_csv('pathTo/september data.csv', header=0)
october = pd.read_csv('pathTo/october data.csv', header=0)
november = pd.read_csv('pathTo/november data.csv', header=0)
december = pd.read_csv('pathTo/december data.csv', header=0)
januaryToJuly = pd.read_csv('pathTo/jan-july data.csv', header=0)

# The chunk of code below transposes the data
september = september.T
october = october.T
november = november.T
december = december.T
januaryToJuly = januaryToJuly.T

# The chunk of code below cleans up the csv files to make them be set up easier and easier to work with
september.columns = september.iloc[0]
october.columns = october.iloc[0]
november.columns = november.iloc[0]
december.columns = december.iloc[0]
januaryToJuly.columns = januaryToJuly.iloc[0]
september = september.iloc[1:]
october = october.iloc[1:]
november = november.iloc[1:]
december = december.iloc[1:]
januaryToJuly = januaryToJuly.iloc[1:]

data2016 = pd.concat([september,october,november,december,januaryToJuly],axis = 1) # all the csv files for each month is concatenated into one dataframe

# The chunk of code below sorts through all the data in data2016 and extracts only the oyster measurements and the pH levels
avgs = data2016['Average']
avg_sizes = data2016['Average size of all live oysters (mm)']
avg_sizes.columns = ['a', 'b', 'c','d', 'Avgsizes']
avgs.columns = ['a', 'b', 'c','d', 'AvgpH']
avg_sizes['sizes'] = avg_sizes['Avgsizes'].astype(float)
avgs['pH'] = avgs['AvgpH'].astype(float)

# The two lines of code below puts the oyster measurements and pH levels below 14 into one data frame
temp = pd.DataFrame({'pH': avgs['pH'], 'size': avg_sizes['sizes']})
temp = temp[temp['pH'] <= 14.0]

# The chunk of code below seperates the acidic pH's from the basic pH's into two different variables. It then finds the mean of the acidic and basic pH's and sets them to two variables
acidic_pH = temp[temp['pH'] < 7.0]
basic_pH = temp[temp['pH'] > 7.0]
acidic_pH_average = acidic_pH.mean()
basic_pH_average = basic_pH.mean()

# The function below shows you the averages in pH and size
def averages():
  time.sleep(2)
  print("")
  print("Acidic: " + str(acidic_pH_average).replace("dtype: float64",""))
  time.sleep(2)
  print("Basic: " + str(basic_pH_average).replace("dtype: float64",""))

# The chunck of code below is the untro to the program
print("Welcome to Team Four's Data Science Project!")
time.sleep(2)
print("")
q1 = input("Would you like to see our 'averages',our 'pie chart', or our 'scatter plot' Type the word or words in the single quotes to see that thing. ") # This code asks the user what they want to see

# The chunk of code below checks what the user wanted to see and outputs what they wanted to see
if(q1 == "averages"):
  averages() # This calls on the averages function
elif(q1 == "scatter plot"):
    y_pos = np.arange(len(pH_objects))
    plt.scatter(temp['pH'], temp['size'])
    plt.xlabel('pH Level')  # labels x axis
    plt.ylabel('Oyster Size')  # labels y axis
    plt.title('Oysters Vs. PH')  # title name
    plt.show()
elif (q1 == "pie chart"):
    labels = 'Acidic', 'Basic' # Lables the pieces of the pie charts
    sizes = [acidic_pH_average[1], basic_pH_average[1]]
    colors = ['red', 'blue']
    explode = (0.1, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
