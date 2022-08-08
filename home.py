
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
import webbrowser
import re
from ttkwidgets.autocomplete import AutocompleteEntry

class Graph:
    def __init__(self):
        #marking the metro lines and initializing the shortest distance associated with them as 0
        self.metro_lines = {19:0, 23:0, 50:0,51:0,26:0 ,47:0, 46:0, 48:0, 25:0, 27:0, 49:0, 33:0, 37:0}
        
        self.v = 56

        #initializing the incidence matrix
        self.edges = [[-1 for i in range(self.v)]
                      for j in range(self.v)]

        #list to record the explored nodes
        self.visited = []

    #method to add an edge to the graph
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    #returns the number of given location 



    def get_node(self,location):       

        pin_code=''
        area_name=''

        f1=open('area-hashtable.txt','r')

        while area_name!=location:
            line=f1.readline()
            

            if not line: 
                break

            line=line.strip("\n")

            pin_code,area_name=line.split(',')
        
        f1.close()

        return (int(pin_code))



    def get_location(self,pin):

        pin_code=''
        area_name=''

        f1=open('area_hashtable.txt','r')

        while pin_code!=pin:
            line=f1.readline()
            

            if not line: 
                break

            line=line.rstrip("\n")
            pin_code,area_name=line.split(',')
            pin_code = int(pin_code)

        f1.close()

        return (area_name)


    
    def createChennaiGraph(self):

        f2=open('chennai_map.txt','r')
        while True:
            line=f2.readline()
            if not line: 
                break
            line=line.strip("\n")
            src,dest,wt=line.split(',')
            wt=float(wt)
            s=self.get_node(src)
            d=self.get_node(dest)
            g=self.add_edge(s,d,wt)
        f2.close()



    def dijkstra(self, start_vertex):
        #initializing the distance to every vertex from start vertex as infinity
        D = {v: float('inf') for v in range(self.v)}
        #marking start vertex with 0 distance
        D[start_vertex] = 0
        #importing priority queue
        #pq = PriorityQueue()
        #priority queue will be usedto find the next minimum distance
        #pq.put((0, start_vertex))
        nearest=[]
        nearest.append([0,start_vertex])
        #obtaining the metro stations
        stations = list(self.metro_lines.keys())
        #for each metro station, find the least cost of travelling
        for station in stations:
            while station not in self.visited:
                
                
                mindist=nearest[0][0]
                current_vertex=nearest[0][1]
                flag = 0
                for i in range(len(nearest)):
                    if nearest[i][0]<mindist:
                        mindist=nearest[i][0]
                        current_vertex=nearest[i][1]
                        flag=i
                # print(nearest)
                # print(nearest[flag])                
                
                #(dist, current_vertex) = pq.get()  #dequeue the vertex with least distance
                self.visited.append(current_vertex)  #record the dequeued vertex
                del nearest[flag]
                #perform breadth first search on the dequeued vertex
                for neighbor in range(self.v):
                    if self.edges[current_vertex][neighbor] != -1:
                        #get the weight of the adjacent edges
                        distance = self.edges[current_vertex][neighbor]
                        if neighbor not in self.visited:
                            old_cost = D[neighbor]
                            new_cost = D[current_vertex] + distance
                            #find the minimum cost
                            if new_cost < old_cost:
                                #pq.put((new_cost, neighbor))
                                nearest.append([new_cost,neighbor])
                                D[neighbor] = new_cost  #update the new distance
            
            #recording the minimum distance achieved for each station
            self.metro_lines[station] = D[station]
        #finding the metro station with the least distance from start vertex
        distances = list(self.metro_lines.values())
        min_Dist = min(distances)
        min_dist_station_index = distances.index(min_Dist)
        min_dist_station = stations[min_dist_station_index]
        #resetting the record of processed nodes
        self.visited = []
        #returning the optimal metro station
        return (min_dist_station)


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("750x550+345+120")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Metro Navigation System")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Canvas1.configure(background="#8080ff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Canvas2 = tk.Canvas(self.Canvas1)
        self.Canvas2.place(relx=0.067, rely=0.091, relheight=0.818
                , relwidth=0.868)
        self.Canvas2.configure(background="#ffffff")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Canvas2)
        self.Label1.place(relx=0.131, rely=0.156, height=60, width=480)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Variable Small Light} -size 19 -weight bold -slant italic")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''CHENNAI METRO NAVIGATION SYSTEM''')

        self.Label2 = tk.Label(self.Canvas2)
        self.Label2.place(relx=0.422, rely=0.111, height=21, width=100)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI Variable Small Light} -size 13 -slant italic")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Welcome to''')

        self.Button1 = tk.Button(self.Canvas2)
        self.Button1.place(relx=0.307, rely=0.356, height=40, width=250)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#b7b7ff")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Variable Small Light} -size 13 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''')
        self.Button1.configure(command=self.search_form)

        self.Button1_1 = tk.Button(self.Canvas2)
        self.Button1_1.place(relx=0.307, rely=0.511, height=40, width=250)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#b7b7ff")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Segoe UI Variable Small Light} -size 13 -weight bold")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Map''')
        self.Button1_1.configure(command=self.map_redirect)

        self.Button1_1_1 = tk.Button(self.Canvas2)
        self.Button1_1_1.place(relx=0.307, rely=0.667, height=40, width=250)
        self.Button1_1_1.configure(activebackground="beige")
        self.Button1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1.configure(background="#b7b7ff")
        self.Button1_1_1.configure(compound='left')
        self.Button1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1.configure(font="-family {Segoe UI Variable Small Light} -size 13 -weight bold")
        self.Button1_1_1.configure(foreground="#000000")
        self.Button1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1.configure(highlightcolor="black")
        self.Button1_1_1.configure(pady="0")
        self.Button1_1_1.configure(text='''Exit''')
        self.Button1_1_1.configure(command=self.exit_home)

    def map_redirect(self):
        webbrowser.open('https://www.google.com/maps/d/embed?mid=1lbgJ_UsLSF-UCwvZME9fCS2QTXW-8ZA&ehbc=2E312F')

    def exit_home(self):
        msg=messagebox.askyesno("METRO NAVIGATION SYSTEM","Are you sure , you want to exit?")
        if (msg):
            exit()

    def search_form(self):
        root.destroy()
        search_start_up()

def start_up():
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    app = Toplevel1(root)
    root.mainloop()

lista=['Navalur', 'Thazhambur', 'Semmanjeri', 'Kovilancheri', 'Perumbakkam', 'Sholinganallur', 'Medavakkam', 'Tambaram', 'Pallikaranai', 'Kovilambakkam', 'Thoraipakkam', 'Chromepet', 'Perungudi', 'Madipakkam', 'Pammal', 'Nanganallur', 'Velachery', 'Thandalam', 'Gerugambakkam', 'Guindy', 'Adyar', 'Poonamallee', 'Porur', 'T.Nagar', 'Nungambakkam', 'Koyambedu', 'Chennai Central', 'Anna Nagar', 'Ayappakkam', 'Ambattur', 'Puthagaram', 'Perambur', 'Royapuram', 'Tondiarpet', 'Madhavaram', 'Kadirvedu', 'Mathur', 'Tiruvottyur', 'Manali', 'Graniteline', 'Padanallur', 'Perungavoor', 'Vichoor', 'Edayanchavadi','Ennore', 'Athipatttu', 'Kilpauk', 'Egmore', 'Vadapalani', 'Mannady', 'Nandanam', 'Gopalapuram', 'Selaiyur', 'Thiruvanmiyur', 'Adyar', 'Besant Nagar']


class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("750x750+370+118")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Search menu")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Canvas1.configure(background="#8080ff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Canvas2 = tk.Canvas(self.Canvas1)
        self.Canvas2.place(relx=0.067, rely=0.091, relheight=0.818
                , relwidth=0.868)
        self.Canvas2.configure(background="#ffffff")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Canvas2)
        self.Label1.place(relx=0.346, rely=0.1, height=40, width=200)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#dfdfff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Variable Small Light} -size 15 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''         SEARCH''')

        self.Label2 = tk.Label(self.Canvas2)
        self.Label2.place(relx=0.215, rely=0.235, height=25, width=100)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#bfbfff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI Variable Small Light} -size 9 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Source:''')

        self.Label2_1 = tk.Label(self.Canvas2)
        self.Label2_1.place(relx=0.215, rely=0.335, height=25, width=100)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#bfbfff")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Segoe UI Variable Small Light} -size 9 -weight bold")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Destination:''')

        arealst=['Navalur'
        ,'Thazhambur'
        ,'Semmanjeri'
        ,'Kovilancheri'
        ,'Perumbakkam'
        ,'Sholinganallur'
        ,'Medavakkam'
        ,'Tambaram'
        ,'Pallikaranai'
        ,'Kovilambakkam'
        , 'Thoraipakkam'
        ,'Chromepet'
        ,'Perungudi'
        ,'Madipakkam'
        ,'Pammal'
        ,'Nanganallur'
        ,'Velachery'
        ,'Thandalam'
        ,'Gerugambakkam'
        ,'Guindy'
        ,'Adyar'
        ,'Poonamalle'
        ,'Porur'
        ,'T.Nagar'
        ,'Nungambakkam'
        ,'Koyambedu'
        ,'Chennai Central'
        ,'Anna Nagar'
        ,'Ayappakkam'
        ,'Ambattur'
        ,'Puthagaram'
        ,'Perumbur'
        ,'Royapuram'
        ,'Tondiarpet'
        ,'Madhavaram'
        ,'Kadirvedu'
        ,'Mathur'
        ,'Tiruvottyur'
        ,'Manali'
        ,'Graniteline'
        ,'Padinallur'
        ,'Perungavoor'
        ,'Vichoor'
        ,'Edayanchavadi'
        ,'Ennore'
        ,'Athipatttu'
        ,'Kilpauk'
        ,'Egmore'
        ,'Vadapalani'
        ,'Mannady'
        ,'Nandanam'
        ,'Gopalapuram'
        ,'Selaiyur'
        ,'Thiruvanmiyur'
        ,'Adyar'
        ,'Besant Nagar']
        self.srcclick = tk.StringVar()
        self.srcclick.set("Choose source")
        self.srcdrop = tk.OptionMenu(root1 , self.srcclick , *arealst)
        self.srcdrop.place(relx=0.461, rely=0.275, height=40, width=250)
        self.srcdrop.configure(background="#b7b7ff")

        self.destclick = tk.StringVar()
        self.destclick.set("Choose destination")
        self.destdrop = tk.OptionMenu(root1 , self.destclick , *arealst)
        self.destdrop.place(relx=0.461, rely=0.35, height=40, width=250)
        self.destdrop.configure(background="#b7b7ff")
    

#self.Entry1 = tk.Entry(self.Canvas2)
#self.Entry1.place(relx=0.461, rely=0.378, height=25, relwidth=0.307)
#self.Entry1.configure(background="#cacaff")
#self.Entry1.configure(disabledforeground="#a3a3a3")
#self.Entry1.configure(font="-family {Segoe UI Variable Small Light} -size 10")
#self.Entry1.configure(foreground="#000000")
#self.Entry1.configure(insertbackground="black")
#
#self.Entry1_1 = tk.Entry(self.Canvas2)
#self.Entry1_1.place(relx=0.461, rely=0.489, height=25, relwidth=0.307)
#self.Entry1_1.configure(background="#cacaff")
#self.Entry1_1.configure(disabledforeground="#a3a3a3")
#self.Entry1_1.configure(font="-family {Segoe UI Variable Small Light} -size 10")
#self.Entry1_1.configure(foreground="#000000")
#self.Entry1_1.configure(highlightbackground="#d9d9d9")
#self.Entry1_1.configure(highlightcolor="black")
#self.Entry1_1.configure(insertbackground="black")
#self.Entry1_1.configure(selectbackground="#c4c4c4")
#self.Entry1_1.configure(selectforeground="black")

        
        self.Listbox1 = tk.Listbox(self.Canvas2)
        self.Listbox1.place(relx=0.192, rely=0.4, relheight=0.35
                , relwidth=0.614)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Segoe UI Variable Small Light} -size 10")
        self.Listbox1.configure(foreground="#000000")


        self.Button1 = tk.Button(self.Canvas2)
        self.Button1.place(relx=0.307, rely=0.85, height=25, width=80)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#cacaff")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Variable Small Light} -size 11 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''')
        self.Button1.configure(command=self.result_startup)

        self.Button1_1 = tk.Button(self.Canvas2)
        self.Button1_1.place(relx=0.568, rely=0.85, height=25, width=80)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#cacaff")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Segoe UI Variable Small Light} -size 11 -weight bold")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Home''')
        self.Button1_1.configure(command=self.go_home)
    
    def go_home(self):
        root1.destroy()
        start_up()

    def result_startup(self):
        self.find_route()
        # root1.destroy()
        #start_up_result()

    def find_route(self):

        start=self.srcclick.get()
        end=self.destclick.get()
        
        
        g = Graph()  #create graph of 56 vertices
        g.createChennaiGraph()
        #read the source and destination
        #start = input("Enter your current location: ")
        start=g.get_node(start)
        #end = input("Enter your destination: ")
        end=g.get_node(end)
        metros = list(g.metro_lines.keys())
        #check if the locations have a metro station already
        if start in metros and end in metros:
            self.Listbox1.insert(1,"\nYou have a direct Route:")
            self.Listbox1.insert(2,"1) From your location, go to the metro station in your area")
            self.Listbox1.insert(3,"2) Drop off at the metro station at your destination area")
            output_no=3
        elif start in metros:
            #find nearest metro station from destination location
            station2 = g.dijkstra(end)
            station2 = g.get_location(station2)
            self.Listbox1.insert(1,"\nYour Route:")
            self.Listbox1.insert(2,"1) Go to the metro station at your current area")
            self.Listbox1.insert(3,"2) Drop off at the %s metro station "%(station2))
            self.Listbox1.insert(4,"3) Go to your destination")
            output_no=4
        elif end in metros:
            #find nearest metro station from source location
            station1 = g.dijkstra(start)
            station1=g.get_location(station1)
            self.Listbox1.insert(1,"\nYour Route:")
            self.Listbox1.insert(2,"1) From your location, go to the %s  metro station "%(station1))
            self.Listbox1.insert(3,"2) Drop off at the metro station in your destination area")
            output_no=3
        else:
            #find nearest metro station from source location
            station1 = g.dijkstra(start)
            station1=g.get_location(station1)
            #find nearest metro station from destination location
            station2 = g.dijkstra(end)
            station2 = g.get_location(station2)
            if station1 == station2:
                #notify user with optimal solution
                self.Listbox1.insert(1,"\nThe closet metro to both locations is the %s metro station"%(station1))
                self.Listbox1.insert(2,"Traveling in metro is not advised.")
                output_no=2
            else:
                self.Listbox1.insert(1,"\nYour Route:")
                self.Listbox1.insert(2,"1) From your location, go to the %s metro station"%(station1))
                self.Listbox1.insert(3,"2) Drop off at the %s metro station at"%(station2))
                self.Listbox1.insert(4,"3) Go to your destination")
                output_no=4

output=[]
output_no=0

def search_start_up():
    '''Main entry point for the application.'''
    global root1
    root1 = tk.Tk()
    root1.protocol( 'WM_DELETE_WINDOW' , root1.destroy)
    # Creates a toplevel widget.
    app1 = Toplevel2(root1)
    root1.mainloop()

class Toplevel3:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("750x550+370+118")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("result")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Canvas1.configure(background="#8080ff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Canvas2 = tk.Canvas(self.Canvas1)
        self.Canvas2.place(relx=0.067, rely=0.091, relheight=0.818
                , relwidth=0.868)
        self.Canvas2.configure(background="#ffffff")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Canvas2)
        self.Label1.place(relx=0.346, rely=0.133, height=40, width=200)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#dfdfff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Variable Small Light} -size 15 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SEARCH RESULT''')

        global Listbox1
        self.Listbox1 = tk.Listbox(self.Canvas2)
        self.Listbox1.place(relx=0.192, rely=0.278, relheight=0.556
                , relwidth=0.614)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Segoe UI Variable Small Light} -size 10")
        self.Listbox1.configure(foreground="#000000")

        for i in range(1,output_no+1):
            self.Listbox1.insert(i,output[i])

        self.Button1 = tk.Button(self.Canvas2)
        self.Button1.place(relx=0.422, rely=0.844, height=40, width=100)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#9595ff")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Variable Small Light} -size 13 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Home''')
        self.Button1.configure(command=self.go_back_home)
    
    def go_back_home(self):
        root2.destroy()
        start_up()

def start_up_result():
    '''Main entry point for the application.'''
    global root2
    root2 = tk.Tk()
    root2.protocol( 'WM_DELETE_WINDOW' , root2.destroy)
    # Creates a toplevel widget.
    app3=Toplevel3(root2)
    root2.mainloop()

if __name__ == '__main__':
    start_up()