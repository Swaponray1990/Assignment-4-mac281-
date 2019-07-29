#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as ry
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#----------initialising the graph
M = ry.Graph()

m = ry.generators.small.krackhardt_kite_graph()

print("Nodes from krackhardt_kite_graph: ","\n",m.nodes(),"\n")
print("Edges from krackhardt_kite_graph: ","\n",m.edges())


person = {2:"Swapon" ,5:"Tapan", 7:"Ripon", 8:"Sumon", 9:"Bijoy", 6:"Shuvo", 4:"Artha", 1:"Nath", 3:"Champa", 0:"Suk"}
person

#--------------Creating the graph object
F1 =ry.Graph()
#---------------Creating the Edges from the graph
#---Option 1---
e1 = [(0,1), (0,2), (0,3), (0,5), (1,3), (1,4), (1,6), (2,3), (2,5),
     (3,4), (3,5), (3,6), (4,6), (5,6), (5,7), (6,7), (7,8), (8,9)]

#---Option 2---
e1 = m.edges()

#---------------Add all the edges to the graph object
F1.add_edges_from(e1)

print("Edges for named network","\n" ,F1.edges())

D = ry.relabel_nodes(F1, person)
print("----------------------\n")
print(" Nodes for named network: ", "\n", D.nodes())
print("----------------------\n")
print(" Edges for named network: ", "\n", D.edges())

ry.draw(D, with_labels =1)
plt.show()


# In[ ]:




