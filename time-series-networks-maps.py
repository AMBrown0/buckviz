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
# Build a dataframe with 4 connections
df = pd.DataFrame({'source':['A', 'B', 'C','A'], 
'target':['D', 'A', 'E','C']})
# Build your graph
G=nx.from_pandas_edgelist(df, 'source', 'target')
# plot with spring layouts
nx.draw(G, with_labels=True, node_size=1000, pos=nx.spring_layout(G))
plt.show()


# Build a dataframe with 4 connections
df = pd.DataFrame({'source':['A', 'B', 'C','A'], 
'target':['D', 'A', 'E','C']})
# Build your directed graph using DiGraph
G=nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.DiGraph())

# plot with spring layouts
nx.draw(G, arrows=True, arrowsize=20, with_labels=True, node_size=1000, pos=nx.spring_layout(G))
plt.show()


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