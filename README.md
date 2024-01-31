# HarvardMedProjects
Projects Worked On while at Harvard Medical School

# Synapse_Automation Documentation
This file is designed to analyze and visualize neuron connectivity using the NetworkX library and visualize the results. The code performs the following tasks:

Reads a pre-saved network graph from a file (assumed to be in the GraphML format).
Loads a cell type database from a CSV file.
Defines functions to extract and analyze connections between neurons.
Provides functions to automate the process of checking and visualizing connections for specific neurons.
Requirements
Make sure you have the following libraries installed:

numpy
openpyxl
matplotlib
pandas
seaborn
networkx


# Usage
Loading Network Graph:

import networkx as nx
fname = 'db_mli_pc_231209_v2.gz'
G = nx.read_gpickle(fname)

Extracting and Displaying Node Information:
for nid in G.nodes:
    print(f'{nid}: {G.nodes(data=True)[nid]}')

Checking Connections:
all_connections_to('pc_16', True, 'mli')
Prints all connections to 'pc_16' filtered by cell type 'mli'.


Visualizing Connections:
neurons = ['interneuron_191', 'interneuron_188', ...]
check_all_connects(neurons, 'pc_16')
put_num_connections_df_violin(neurons, 'pc_16', 'Cell Type', 'Connections')
Visualizes connections for a list of neurons to 'pc_16' using a violin plot.

Automating Data Export to Excel:
automated_connections_list(neurons, 'pc_16', r'C:\Users\regehr2\Downloads\test-book.xlsx')
Automates the export of connection data to an Excel file.

Notes
Make sure to customize file paths and filenames according to your specific setup.
This script is provided as an example and may need modifications based on your data and requirements.
