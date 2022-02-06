######### import the required libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
import os,cv2
import time 
import matplotlib.pyplot as plt
######### create the root window
root = tk.Tk()
root.title('Puzzle Solver')
root.resizable(True, True)
root.geometry('1920x1080')
#root.config(bg='yellow')

my_frame = Frame(root, width=576, height=324,bg='black')
my_frame.pack(fill="both", expand=True)

img = ImageTk.PhotoImage(file="Images/bg.jpg")
label = Label(
    my_frame,
    image=img
)
label.place(x=0, y=0)



#global filename,destfn

############# global &/ initialisations
filename = "Images/puzzle.jpg" # initial source for input image
#destfn = "/home/ksv/Documents/UI/puzzle.jpg" # initial outputted image
destfn = "Images/puzzle.jpg" # initial outputted image
size = 55 # initial piece size: 55 X 55
gen,pop = 10,500 # total generations to run and initial population for genetic algo
in1_img = 0
start,stop = 0,0 # variables to store start and end times
img_t,text_t,text_t2 = 0,0,0

def select_file(): 
############## helper function to select files

    filetypes = (
        ('Image files', '*.jpg'),('Image files', '*.jpeg'),('Image files', '*.png'),
        ('All files', '*.*')
    )

    global filename # referring to earlier created global variable
    filename = fd.askopenfilename(
        title='Open a file',
#        initialdir='/home/ksv/Pictures/', # initial default directory to show in dialogue box
        initialdir='~/', # initial default directory to show in dialogue box
        filetypes=filetypes)

#    showinfo(title='Selected File',message=filename)
    print(filename)
    if (len(filename)): # only if an image is selected
# Create a photoimage object of the image in the path
        in_img = Image.open(filename) #open the image
        test = ImageTk.PhotoImage(in_img.resize((750,750), Image.ANTIALIAS)) #0.6*(1920,1080)
        label1 = tk.Label(image=test) 
        label1.image = test
        label1.place(x=50,y=50)
#    print("Sel:"+filename)
#    destfn = filename

def rand():
################ helper function to randomise the selected input image
#    size = 48
#    print("Calc:"+filename)
    global destfn,size,filename
#    print(size)
    destfn = filename # filename shouldn't contain any spaces
    command = "create_puzzle " + filename + " --size=" + str(size) + " --destination=Images/puzzle.jpg" # puzzled image will be stored in directory where this code is present
#    print(command)
    stream = os.popen(command) # execute this is terminal and print the response.
    output = stream.read() # these commands execute our create_script function which creates puzzles
#    print(output)
    in_img = Image.open("Images/puzzle.jpg") # displays the resulting puzzle
    test = ImageTk.PhotoImage(in_img.resize((750,750), Image.ANTIALIAS)) #display the image in 750 X 750 frame
    label2 = tk.Label(image=test)
    label2.image = test
    label2.place(x=1010,y=50)
#    calc() # place a call to the genetic algorithm solver for solving the puzzle
    
def plots():
############### plot for fitness function
    img_cv = cv2.imread('Images/fit_plot.png')
    plt.imshow(img_cv)
    plt.axis('off')
    plt.show()

def calc(): 
############### final solver
#    gen = 20
#    pop = 600
#    gaps --image=puzzle.jpg --generations=20 --population=600 --size=
    global in1_img, start, stop, text_t2
    start = time.time()
    command = "gaps --image=Images/puzzle.jpg" + " --generations=" + str(gen) + " --population=" + str(pop) + " --size=" + str(size) + " --verbose"

    stream = os.popen(command)
    output = stream.read() # these place a request in the shell and triggers the gaps program.
    stop = time.time()
    print(output) # gaps is our genetic algo solver.
#    stream = os.popen("pwd")
#    print(stream.read())
    in1_img = Image.open("Images/temp.jpg") # final solved image is stored locally as temp.jpg which is opened
    test1 = ImageTk.PhotoImage(in1_img.resize((750,750), Image.ANTIALIAS)) #0.6(1920,1080)
    label2 = tk.Label(image=test1)
    label2.image = test1
    label2.place(x=1010,y=50) # position of the image frame
    timer = float(int(100*(stop-start))/100)
    text_t2 = "Execution time="+str(timer) + " sec" # find the execution time
    L5.config(text=text_t2)# update the execution time
#    stop()
#    label2.place(x=1010,y=50)

def on_change(sizei): # get() values entered in the entries
    global size
    size = int(sizei.widget.get())
    img_t = cv2.imread(filename)
    text_t = "Total puzzle Pieces="+str(img_t.shape[0]//size)+"X"+str(img_t.shape[1]//size)
    L4.config(text=text_t)
    print("change in size:",size)

def on_change1(geni): # retrieve the generation values entered
    global gen
    gen = geni.widget.get()
    print("change in gen:",gen)
def on_change2(popi): # retrieve the population values entered
    global pop
    pop = popi.widget.get()
    print("change in pop:",pop)

def savefile(): # helper function to save the obtained image
    filenamer = fd.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filenamer:
        return
    in1_img.save(filenamer)

#def update_progress_label():
#    return f"Current Progress: {pb['value']}%"

#def progress():
#    if pb['value'] &lt == 100:
#        pb['value'] += 20
#        value_label['text'] = update_progress_label()
#    else:
#        showinfo(message='The progress completed!')

#def stop():
#    pb.stop()
#    value_label['text'] = update_progress_label()

# Position image
#    label1.place(x=100, y=100)
    #return filename


# open button 1 ======> button for Input image
open_button_1 = Button(root, highlightcolor='red', text='Input Image',bg='black', fg='white', command=select_file )
#open_button_1 = ttk.Button(my_frame,text='Input Image')
open_button_1.pack(expand=True)
open_button_1.place(x=400, y=900) #338,400

# open button 2 ======> solve button
open_button_2 = Button(root,bg='black', fg='white', text='Solve',command=calc)
open_button_2.pack(expand=True)
open_button_2.place(x=903, y=485) #1238,400

# open button 4 ======> puzzle button
open_button_4 = Button(root,bg='black', fg='white', text='Puzzle',command=rand)
open_button_4.pack(expand=True)
open_button_4.place(x=900, y=450) #1238,400

# open button 5 ======> plot button
open_button_4 = Button(root,bg='black', fg='white', text='Plot',command=plots)
open_button_4.pack(expand=True)
open_button_4.place(x=907, y=520) #1238,400

# open button 3 =======> save button
open_button_3 = Button(root, text='Save Image',bg='black', fg='white', command=savefile)
#open_button_1 = ttk.Button(my_frame,text='Input Image')
open_button_3.pack(expand=True)
open_button_3.place(x=1360, y=900) #338,400


# entry for pieces size =====
L1 = Label(root, text="Piece size\nbetween\n16-128",fg='black',bg='white')
L1.pack( side = LEFT)
L1.place( x = 815,y=350)
sizei=Entry(root, text="This is Entry Widget", bd=2,textvariable=size)
#sizei.insert(0, "28-64") #for default entry
sizei.pack()
sizei.place(x=900, y=350,width = 85, height=30)
sizei.bind("<Return>",on_change)

# entry for generations =====
L2 = Label(root, text="Enter Gen\nvalue",fg='black',bg='white')
L2.pack( side = LEFT)
L2.place( x = 815,y=250)
geni=Entry(root, text="This is Entry Widget", bd=2,textvariable=gen)
geni.pack()
geni.place(x=900, y=250,width = 85, height=30)
geni.bind("<Return>",on_change1)

# entry for pop size =====
L3 = Label(root, text="Enter pop \nvalue",bg='white',fg='black')
L3.pack( side = LEFT)
L3.place( x = 815,y=150)
popi=Entry(root, text="This is Entry Widget", bd=2,textvariable=pop)
#popi.insert(0, pop) #for default entry
popi.pack()
popi.place(x=900, y=150,width = 85, height=30)
popi.bind("<Return>",on_change2)

pie = 10
# label for no of pieces =====

L4 = Label(root, text=text_t,bg='white',fg='black') #,textvariable=pie)
L4.pack( side = LEFT)
L4.place( x = 815,y=650)

# Execution time =====

L5 = Label(root, text=text_t2,bg='white',fg='black') #,textvariable=pie)
L5.pack( side = LEFT)
L5.place( x = 815,y=700)

#popi.insert(0, pop) #for default entry

# progress bar
#pb = ttk.Progressbar(root1,orient='horizontal',mode='determinate', length=280)
#pb.grid(column=900, row=600, columnspan=2, padx=10, pady=20)
#value_label = ttk.Label(root1, text=update_progress_label())
#value_label.grid(column=0, row=1, columnspan=2)

#root.attributes('-transparentcolor', "white")
# run the application
root.mainloop()

