from tkinter import *
import os

import csv
import sample_data
from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function
def next_page():
    irrelevant_values_data_main.destroy()
    import classification
def read_data_set():
    TableMargin = Frame(irrelevant_values_data_main, width=500)
    TableMargin.place(x=50, y=110,width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(
        "customerID", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines"
        , "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV"
        , "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges"
        , "TotalCharges", "Churn"), height=400, selectmode="extended", yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('customerID', text="customerID", anchor=W)
    # tree.heading('gender', text="gender", anchor=W)
    # tree.heading('SeniorCitizen', text="SeniorCitizen", anchor=W)
    tree.heading('Partner', text="Partner", anchor=W)
    tree.heading('Dependents', text="Dependents", anchor=W)
    tree.heading('tenure', text="tenure", anchor=W)
    tree.heading('PhoneService', text="PhoneService", anchor=W)
    tree.heading('MultipleLines', text="MultipleLines", anchor=W)
    tree.heading('InternetService', text="InternetService", anchor=W)

    tree.heading('OnlineSecurity', text="OnlineSecurity", anchor=W)
    tree.heading('OnlineBackup', text="OnlineBackup", anchor=W)
    tree.heading('DeviceProtection', text="DeviceProtection", anchor=W)
    tree.heading('TechSupport', text="TechSupport", anchor=W)
    tree.heading('StreamingTV', text="StreamingTV", anchor=W)
    tree.heading('StreamingMovies', text="StreamingMovies", anchor=W)
    tree.heading('Contract', text="Contract", anchor=W)
    tree.heading('PaperlessBilling', text="PaperlessBilling", anchor=W)
    tree.heading('PaymentMethod', text="PaymentMethod", anchor=W)
    tree.heading('MonthlyCharges', text="MonthlyCharges", anchor=W)
    tree.heading('TotalCharges', text="TotalCharges", anchor=W)
    tree.heading('Churn', text="Churn", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=100)
    tree.column('#9', stretch=NO, minwidth=0, width=100)
    tree.column('#10', stretch=NO, minwidth=0, width=100)
    tree.column('#11', stretch=NO, minwidth=0, width=100)
    tree.column('#12', stretch=NO, minwidth=0, width=100)
    tree.column('#13', stretch=NO, minwidth=0, width=100)
    tree.column('#14', stretch=NO, minwidth=0, width=100)
    tree.column('#15', stretch=NO, minwidth=0, width=100)
    tree.column('#16', stretch=NO, minwidth=0, width=100)
    tree.column('#17', stretch=NO, minwidth=0, width=100)
    tree.column('#18', stretch=NO, minwidth=0, width=100)
    tree.column('#19', stretch=NO, minwidth=0, width=100)
    # tree.column('#20', stretch=NO, minwidth=0, width=100)
    # tree.column('#21', stretch=NO, minwidth=0, width=100)



    tree.pack()
    ob=sample_data
    file="data_set/irrelevant.csv"
    with open(file) as f, open('data_set/feature.csv', 'w',encoding='utf-8',newline='') as csvfile:

        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(
            ['customerID',  'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines'
                , 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV'
                , 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges'
                , 'TotalCharges', 'Churn'])
        for row in reader:
            #print row
            t1 = row['customerID']
            # t2 = row['gender']
            # t3 = row['SeniorCitizen']
            t4 = row['Partner']
            t5 = row['Dependents']
            t6 = row['tenure']
            t7 = row['PhoneService']
            t8 = row['MultipleLines']
            t9 = row['InternetService']

            t10 = row['OnlineSecurity']
            t11 = row['OnlineBackup']
            t12 = row['DeviceProtection']
            t13 = row['TechSupport']
            t14 = row['StreamingTV']

            t15 = row['StreamingMovies']
            t16 = row['Contract']
            t17 = row['PaperlessBilling']
            t18 = row['PaymentMethod']
            t19 = row['MonthlyCharges']

            t20 = row['TotalCharges']
            t21 = row['Churn']
            # print(t18)
            if ((t18 == "normal")):
                dd=0
            else:
                tree.insert("", 0, values=(t1,  t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17,t18,t19,t20,t21))
                filewriter.writerow([t1, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18,t19,t20,t21])

############################################################
irrelevant_values_data_main = Tk()
w=750
h=550
ws = irrelevant_values_data_main.winfo_screenwidth()
hs = irrelevant_values_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
irrelevant_values_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
irrelevant_values_data_main.title(sample_data.student.title)
irrelevant_values_data_main.resizable(False, False)
irrelevant_values_data_main.configure(background=sample_data.student.background)
########################################################### Element design


message = Label(irrelevant_values_data_main, text=sample_data.student.titlec,fg="#FFF",bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(irrelevant_values_data_main, text="Attribute Extraction",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)
resust_dataset = Button(irrelevant_values_data_main,command=next_page , text="Next",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

irrelevant_values_data_main.mainloop()
