# HarvardMedProjects
Projects Worked On while at Harvard Medical School<br /><br />
**Authors**:

Sean Ediger<br />
Cole Gaynor<br />

# Synapse_Automation Documentation
This file is designed to analyze and visualize neuron connectivity using the NetworkX library and visualize the results. The code performs the following tasks:

Reads a pre-saved network graph from a file (assumed to be in the GraphML format).
Loads a cell type database from a CSV file.
Defines functions to extract and analyze connections between neurons.
Provides functions to automate the process of checking and visualizing connections for specific neurons.
Requirements
Make sure you have the following libraries installed:<br />
<br />
**numpy**<br />
**openpyxl**<br />
**matplotlib**<br />
**pandas**<br />
**seaborn**<br />
**networkx**<br />


### Usage
**Loading Network Graph**:<br />

import networkx as nx<br />
fname = 'db_mli_pc_231209_v2.gz'<br />
G = nx.read_gpickle(fname)<br />
<br />
**Extracting and Displaying Node Information**:<br />
for nid in G.nodes:<br />
    print(f'{nid}: {G.nodes(data=True)[nid]}')<br />
<br />
**Checking Connections**:<br />
all_connections_to('pc_16', True, 'mli')<br />
Prints all connections to 'pc_16' filtered by cell type 'mli'.<br />
<br />

**Visualizing Connections**:<br />
neurons = ['interneuron_191', 'interneuron_188', ...]<br />
check_all_connects(neurons, 'pc_16')<br />
put_num_connections_df_violin(neurons, 'pc_16', 'Cell Type', 'Connections')<br />
Visualizes connections for a list of neurons to 'pc_16' using a violin plot.<br />
<br />
**Automating Data Export to Excel**:<br />
automated_connections_list(neurons, 'pc_16', r'C:\Users\regehr2\Downloads\test-book.xlsx')<br />
Automates the export of connection data to an Excel file.<br />
<br />
**Notes**:<br />
Make sure to customize file paths and filenames according to your specific setup.<br />
This script is provided as an example and may need modifications based on your data and requirements.<br />
