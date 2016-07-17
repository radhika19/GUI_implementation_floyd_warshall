#!/usr/bin/python
import numpy as np 
import Tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import tkMessageBox
ver=input("enter the vertices")
from_node=0
to_node=0
root = tk.Tk()
root.title('adjacency matrix for flyod warshall')
new = {}
def floyd_warsh(adj,f,t):
    flag=1
    for i in range(0,ver):
            for j in range(0,ver):
                    for k in range(0,ver):
                       adj[i][k]= min(adj[i][k],adj[i][j]+adj[j][k])
                       flag=1
    for i in range(0,ver):
            if(adj[i][k]<0):
                    tkMessageBox.showinfo("OUTPUT","consists of negative cycle")

                    
                    flag=0
    if(flag==1):
            if(adj[f-1][t-1]==999999999):
                    tkMessageBox.showinfo("OUTPUT","no connection")
            else:
                    short=adj[f-1][t-1]
                    tkMessageBox.showinfo("OUTPUT","shortest distance %d" %short)
def create_adj(new):
    adj=np.ones((ver,ver))
    
    for row in range(1,ver+1):
            for col in range(1,ver+1):
                    n= "%s%s" %(row,col)
        
                    if n in new.keys():
                       print n
                       if(new[n]=='-'):
                          adj[row-1][col-1]=999999999   
                       else:
                          adj[row-1][col-1]= new[n]
    
    return adj
def draw_graph(graph):
    #no=np.arange(1,ver+1)
    G=nx.DiGraph()
    #G.add_nodes_from(no)
    mat=[]
    
    #print graph
    # add edges
    for row in range(0,len(graph)):
            for col in range(0,len(graph)):
		    
		    n=graph[row][col]
                    
                    if(n==999999999):
                       
                       n=0
                    mat.append(row+1)
                    mat.append(col+1)
                    mat.append(n)
    graph2=np.reshape(mat,(-1,3))
    
    G.add_weighted_edges_from(graph2)

    
    
    pos=nx.shell_layout(G) 
    nx.draw(G,pos)
    nx.draw_networkx_edge_labels(G,pos)
    plt.show()
def key_r(event, cell):
    data = dict[cell].get() 
    new[cell]=data
    
def fields():
    name1= "%s" % e1.get()
    name2 = "%s" % e2.get()
    global from_node 
    from_node=int(name1)
    global to_node 
    to_node= int(name2)
dict = {}
w = 20
h = 1
 

for row in range(0,ver+1):
    for col in range(0,ver+1):
            if col == 0:
    
		    label1 = tk.Label(root, width=3, text=str(row))
		    label1.grid(row=row, column=col, padx = 2, pady=2)
            elif row == 0:
    
		    label1 = tk.Label(root, width=w, text=str(col))
		    label1.grid(row=row, column=col, padx = 2, pady=2)
            else:
  
		    entry1 = tk.Entry(root, width=w)
		   
		    entry1.grid(row=row, column=col) 
		   
		    cell = "%s%s" % (row, col)
		    dict[cell] = entry1
                    entry1.bind('<Tab>', lambda e, cell=cell: key_r(e, cell))
		    
                    
b2=tk.Button(root, text='Submit', command=root.destroy)
b2.grid(row=row+1,columnspan=col)
dict['11'].focus()
root.mainloop()
nodes = tk.Tk()
tk.Label(nodes, text="from node").grid(row=0)
tk.Label(nodes, text="to node").grid(row=1)
e1 = tk.Entry(nodes)
e2 = tk.Entry(nodes)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(nodes, text='confirm', command=nodes.destroy).grid(row=3, column=0,  pady=4)
tk.Button(nodes, text='Select', command=fields).grid(row=3, column=1,  pady=4)
nodes.mainloop( )
matrix=create_adj(new)
print from_node
print to_node
print matrix
draw_graph(matrix)
val=floyd_warsh(matrix,from_node,to_node)






 

           
