"""
Allana Picana
ICS 173 
Github Project
05/04/25
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Path of the .csv file to read
my_file = "https://raw.githubusercontent.com/lannicollene/ICS173/main/Communication.csv"

# Read the file into a variable df
df = pd.read_csv(my_file, index_col=0)

# Check the structure: print the first five rows of the data
print(df.head())

# Visualize data by creating plot
sns.countplot(data=df,
              x="Communication Preference",        
              hue="Age",                        
              palette="crest",                    
              dodge=True)

# save visualization as png
##plt.savefig("ICS173/visualization/communication_pref_by_age.png")

plt.show()

# Visualize data by creating plot
comm = sns.catplot(data=df,
                x="Communication Preference",
                hue="Gender",
                col="College Degree", 
                palette="pastel",
                kind="count",
                height=5,
                aspect=1,
                dodge=False)

comm.set_titles("College: {col_name}")
comm.set_axis_labels("Communication Preference", "Count")

# save visualization as png
##plt.savefig("ICS173/visualization/communication_pref_by_gender_degree.png")
plt.show()