import shutil
from tkinter import *
import os

import csv
from tkinter.filedialog import askopenfilename

import sample_data

##################################################################   read dataset
def read_first_data():
    a=0

    csv_file_path = askopenfilename()

    fpath= os.path.dirname(os.path.abspath(csv_file_path))
    fname=(os.path.basename(csv_file_path))
    fsize=os.path.getsize(csv_file_path)
    txt.delete(0,END)
    txt.insert(0,fpath)
    txt2.insert(0,fname)
    with open(csv_file_path, 'r') as csvFile:
        i=0
        reader = csv.reader(csvFile)
        for row in reader:
            i+=1
        s=sample_data
        s.total_record=i
        s.total_record1=i
        s.f_filepath=csv_file_path
        s.f_path=fpath
        print(csv_file_path)
        txt3.insert(0,i)
################################################################## Next page
def next_page():
    folder = 'data_set'
    if not os.path.exists('data_set'):
        os.makedirs('data_set')
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    root.destroy()
    import read_data_set

##################################################################    main loop
root = Tk()
w=750
h=550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.title(sample_data.student.title)
root.resizable(False, False)
root.configure(background=sample_data.student.background)
################################################################## components design
message = Label(root, text=sample_data.student.titlec,fg="#FFF",bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=20)
#######
lbl = Label(root,justify=CENTER, text="PATH", width=20,bg=sample_data.student.background, height=2, fg="#FFF", font=('times', 15, ' bold '))
lbl.place(x=100, y=150)
lbl2 = Label(root,justify=RIGHT, text="DATA SET", width=20, fg="#FFF",bg=sample_data.student.background,  height=2, font=('times', 15, ' bold '))
lbl2.place(x=100, y=225)
lbl3 = Label(root,justify=RIGHT, text="VALUES", width=20, fg="#FFF",bg=sample_data.student.background,  height=2, font=('times', 15, ' bold '))
lbl3.place(x=100, y=300)
#######
txt = Entry(root, validate="key", width=20, font=('times', 25, ' bold '))
txt.place(x=300, y=150)

txt2 = Entry(root, width=20, font=('times', 25, ' bold '))
txt2.place(x=300, y=225)

txt3 = Entry(root, width=20, font=('times', 25, ' bold '))
txt3.place(x=300, y=300)
######## button with command function
compare_dataset = Button(root, text="Select Data",width=15,command=read_first_data  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=250, y=400)
resust_dataset = Button(root, text="Next",width=15  ,height=1,command=next_page,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

root.mainloop()
