# import necessary packages 
import pandas as pd 
import matplotlib.pyplot as plt 

# create a dataframe 
Marks = pd.DataFrame({'Raju': [8, 10, 7, 7, 10],
					'Hari': [6, 4, 6, 7, 6]})

# plot marks of each student
plt.plot(Marks['Raju'], label="Raju Marks", color="Red")
plt.plot(Marks['Hari'], label="Hari Marks", color="Blue")

# labelling the axes
plt.xlabel("Tests")
plt.ylabel("Marks")

# reordering the labels
handles, labels = plt.gca().get_legend_handles_labels()

# specify order
order = [ 1, 0]

# pass handle & labels lists along with order as below
plt.legend([handles[i] for i in order], [labels[i] for i in order])
plt.show() 
