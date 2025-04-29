"""
Allana Picana
ICS 173 
Github Project
05/04/25
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

my_file = "https://raw.githubusercontent.com/lannicollene/ICS173/main/Communication.csv"
# Load dataset
df = pd.read_csv(my_file, index_col=0)

# Check the structure
print(df.head())

sns.countplot(data=df,
              x="Communication Preference",        
              hue="Age",                        
              palette="crest",                    
              dodge=True)

# save visualization as png
plt.savefig('visualization/communication_pref_by_age.png')

plt.show()

