# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:57:52 2020

@author: andy
"""

# install networkx in Anaconda prompt
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

df = pd.DataFrame({'source':['A', 'B', 'C','A'], 
'target':['D', 'A', 'E','C'],
'weight':[12,40,52,33]})
# Build your graph
G=nx.from_pandas_edgelist(df, 'source', 'target', edge_attr=True)
# plot with spring layouts
pos1=nx.spring_layout(G)
nx.draw(G, with_labels=True, node_size=1000, pos=pos1)
# plot weights as edges labels
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, edge_labels=labels, pos=pos1)