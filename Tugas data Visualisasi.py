#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# reading the database
data = pd.read_csv("DataSales3.csv", delimiter = ";")

# printing the top 10 rows
display(data.head(20))


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("DataSales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.scatter(data['Category'], data['Quantity'])

# Adding Title to the plot
plt.title("Data Profit")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')

plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("DataSales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.bar(data['Category'], data['Quantity'])

# Adding Title to the plot
plt.title("Test")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('bar.png', dpi=300, bbox_inches='tight')

plt.show()


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("DataSales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.hist(data['Segment'])


# Adding Title to the plot
plt.title("Data Segment")

# Save the plot as a PNG file
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')

plt.show()


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("DataSales3.csv", delimiter = ";")

# Scatter plot w day against tip
sales = ['Category', 'Quantity']
datasales = [23, 10]

plt.pie(datasales, labels=sales)

plt.title("Sales Data")

# Save the plot as a PNG file
plt.savefig('pie.png', dpi=300, bbox_inches='tight')

plt.show()


# In[ ]:




