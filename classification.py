import operator
from tkinter import messagebox

import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function
import sample_data
from sample_data import student

def clustering(type,churn,OnlineSecurity,DeviceProtection,StreamingMovies,Contract,PaymentMethod):
    sample_data.student.input_data.append(churn.lower())
    if type.lower()=="dsl":
        xx=sample_data.student.total_DSL_dict[churn.lower()]
        xx+=1
        sample_data.student.total_DSL_dict[churn.lower()]=xx
    elif type.lower()=="fiber optic":
        xx = sample_data.student.total_Fiber_dict[churn.lower()]
        xx += 1
        sample_data.student.total_Fiber_dict[churn.lower()] = xx
    elif type.lower() == "no":
        xx = sample_data.student.total_No_dict[churn.lower()]
        xx += 1
        sample_data.student.total_No_dict[churn.lower()] = xx
    #################OnlineSecurity
    data=OnlineSecurity.lower()
    if data=="yes":
        xx = sample_data.student.OnlineSecurity_yes[churn.lower()]
        xx += 1
        sample_data.student.OnlineSecurity_yes[churn.lower()] = xx
    elif data=="no":
        xx = sample_data.student.OnlineSecurity_no[churn.lower()]
        xx += 1
        sample_data.student.OnlineSecurity_no[churn.lower()] = xx
    else:
        xx = sample_data.student.OnlineSecurity_no_internet[churn.lower()]
        xx += 1
        sample_data.student.OnlineSecurity_no_internet[churn.lower()] = xx
    #################DeviceProtection
    data1 = DeviceProtection.lower()
    if data1=="yes":
        xx = sample_data.student.DeviceProtection_yes[churn.lower()]
        xx += 1
        sample_data.student.DeviceProtection_yes[churn.lower()] = xx
    elif data1=="no":
        xx = sample_data.student.DeviceProtection_no[churn.lower()]
        xx += 1
        sample_data.student.DeviceProtection_no[churn.lower()] = xx
    else:
        xx = sample_data.student.DeviceProtection_no_internet[churn.lower()]
        xx += 1
        sample_data.student.DeviceProtection_no_internet[churn.lower()] = xx
    #################StreamingMovies
    data2 = StreamingMovies.lower()
    if data2 == "yes":
        xx = sample_data.student.StreamingMovies_yes[churn.lower()]
        xx += 1
        sample_data.student.StreamingMovies_yes[churn.lower()] = xx
    elif data2 == "no":
        xx = sample_data.student.StreamingMovies_no[churn.lower()]
        xx += 1
        sample_data.student.StreamingMovies_no[churn.lower()] = xx
    else:
        xx = sample_data.student.StreamingMovies_no_internet[churn.lower()]
        xx += 1
        sample_data.student.StreamingMovies_no_internet[churn.lower()] = xx
    #################Contract
    data3 = Contract.lower()
    if data3 == "month-to-month":
        xx = sample_data.student.Contract_Month_to_month[churn.lower()]
        xx += 1
        sample_data.student.Contract_Month_to_month[churn.lower()] = xx
    elif data3 == "one year":
        xx = sample_data.student.Contract_One_year[churn.lower()]
        xx += 1
        sample_data.student.Contract_One_year[churn.lower()] = xx
    else:
        xx = sample_data.student.Contract_Two_ear[churn.lower()]
        xx += 1
        sample_data.student.Contract_Two_ear[churn.lower()] = xx
    #################PaymentMethod
    data4 = PaymentMethod.lower()
    if data4 == "electronic check":
        xx = sample_data.student.PaymentMethod_electronic_check[churn.lower()]
        xx += 1
        sample_data.student.PaymentMethod_electronic_check[churn.lower()] = xx
    elif data4 == "mailed check":
        xx = sample_data.student.PaymentMethod_electronic_mailed_check[churn.lower()]
        xx += 1
        sample_data.student.PaymentMethod_electronic_mailed_check[churn.lower()] = xx
    elif data4=="bank transfer (automatic)":
        xx = sample_data.student.PaymentMethod_electronic_bank_transfer[churn.lower()]
        xx += 1
        sample_data.student.PaymentMethod_electronic_bank_transfer[churn.lower()] = xx
    elif data4=="credit card (automatic)":
        xx = sample_data.student.PaymentMethod_electronic_credit_card[churn.lower()]
        xx += 1
        sample_data.student.PaymentMethod_electronic_credit_card[churn.lower()] = xx


def clustering_result():
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt1
    import numpy as np
    features, true_labels = make_blobs( n_samples=200, centers=3,cluster_std=2.75,random_state=42)
    features[:5]
    true_labels[:5]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    scaled_features[:5]
    kmeans = KMeans(init="random",n_clusters=3,n_init=10,max_iter=300,random_state=42)
    kmeans.fit(scaled_features)
    kmeans.inertia_
    kmeans.cluster_centers_
    kmeans.n_iter_
    kmeans.labels_[:5]
    kmeans_kwargs = {"init": "random","n_init": 10,"max_iter": 300,"random_state": 42,}
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(scaled_features)
        sse.append(kmeans.inertia_)
    Marks1 = pd.DataFrame({'Yes':
                              [0,
                                sample_data.student.total_DSL_dict['yes'],
                                sample_data.student.total_Fiber_dict['yes'],
                                sample_data.student.total_No_dict['yes'],
                                sample_data.student.OnlineSecurity_yes['yes'],
                                sample_data.student.OnlineSecurity_no['yes'],
                                sample_data.student.DeviceProtection_yes['yes'],
                                sample_data.student.DeviceProtection_no['yes'],
                                sample_data.student.StreamingMovies_yes['yes'],
                                sample_data.student.StreamingMovies_no['yes'],
                                sample_data.student.Contract_Month_to_month['yes'],
                                sample_data.student.Contract_One_year['yes'],
                                sample_data.student.Contract_Two_ear['yes'],
                                sample_data.student.PaymentMethod_electronic_check['yes'],
                                sample_data.student.PaymentMethod_electronic_mailed_check['yes'],
                                sample_data.student.PaymentMethod_electronic_bank_transfer['yes'],
                                sample_data.student.PaymentMethod_electronic_credit_card['yes'],
                                 ]})
    plt1.plot(Marks1['Yes'][1:], label="1.InternetService_DSL_yes"
                                 "\n2.InternetService_Fiber_yes"
                                 "\n3.InternetService_No_yes"
                                 "\n4.OnlineSecurity_yes"
                                 "\n5.OnlineSecurity_no"
                                 "\n6.DeviceProtection_yes"
                                 "\n7.DeviceProtection_no"
                                 "\n8.StreamingMovies_yes"
                                 "\n9.StreamingMovies_no"
                                 "\n10.Contract_Month_to_month"
                                 "\n11.Contract_One_year"
                                 "\n12.Contract_Two_ear"
                                 "\n13.PaymentMethod_electronic_check"
                                 "\n14.PaymentMethod_electronic_mailed_check"
                                 "\n15.PaymentMethod_electronic_bank_transfer"
                                 "\n16.PaymentMethod_electronic_credit_card"
             , color="Red")
    Marks = pd.DataFrame({'no':
                              [0,
                               sample_data.student.total_DSL_dict['no'],
                               sample_data.student.total_Fiber_dict['no'],
                               sample_data.student.total_No_dict['no'],
                               sample_data.student.OnlineSecurity_yes['no'],
                               sample_data.student.OnlineSecurity_no['no'],
                               sample_data.student.DeviceProtection_yes['no'],
                               sample_data.student.DeviceProtection_no['no'],
                               sample_data.student.StreamingMovies_yes['no'],
                               sample_data.student.StreamingMovies_no['no'],
                               sample_data.student.Contract_Month_to_month['no'],
                               sample_data.student.Contract_One_year['no'],
                               sample_data.student.Contract_Two_ear['no'],
                               sample_data.student.PaymentMethod_electronic_check['no'],
                               sample_data.student.PaymentMethod_electronic_mailed_check['no'],
                               sample_data.student.PaymentMethod_electronic_bank_transfer['no'],
                               sample_data.student.PaymentMethod_electronic_credit_card['no'],
                               ]})
    plt.plot(Marks['no'][1:], label="1.InternetService_DSL_yes"
                                    "\n2.InternetService_Fiber_yes"
                                    "\n3.InternetService_No_yes"
                                    "\n4.OnlineSecurity_yes"
                                    "\n5.OnlineSecurity_no"
                                    "\n6.DeviceProtection_yes"
                                    "\n7.DeviceProtection_no"
                                    "\n8.StreamingMovies_yes"
                                    "\n9.StreamingMovies_no"
                                    "\n10.Contract_Month_to_month"
                                    "\n11.Contract_One_year"
                                    "\n12.Contract_Two_ear"
                                    "\n13.PaymentMethod_electronic_check"
                                    "\n14.PaymentMethod_electronic_mailed_check"
                                    "\n15.PaymentMethod_electronic_bank_transfer"
                                    "\n16.PaymentMethod_electronic_credit_card"
             , color="blue")
    plt1.xlabel("Clustering")
    plt1.ylabel("Count")
    plt1.title("Clustering")
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Clustering')
    handles, labels = plt1.gca().get_legend_handles_labels()
    order = [0]
    plt_2 = plt.figure(figsize=(6, 4))
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Clustering Labels')
    plt1.legend([handles[i] for i in order], [labels[i] for i in order])
    ##################################################

    plt1.show()

def clustering_result1():
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt1
    import numpy as np
    features, true_labels = make_blobs( n_samples=200, centers=3,cluster_std=2.75,random_state=42)
    features[:5]
    true_labels[:5]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    scaled_features[:5]
    kmeans = KMeans(init="random",n_clusters=3,n_init=10,max_iter=300,random_state=42)
    kmeans.fit(scaled_features)
    kmeans.inertia_
    kmeans.cluster_centers_
    kmeans.n_iter_
    kmeans.labels_[:5]
    kmeans_kwargs = {"init": "random","n_init": 10,"max_iter": 300,"random_state": 42,}
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(scaled_features)
        sse.append(kmeans.inertia_)
    Marks = pd.DataFrame({'no':
                              [0,
                                  sample_data.student.total_DSL_dict['no'],
                                  sample_data.student.total_Fiber_dict['no'],
                                  sample_data.student.total_No_dict['no'],
                                  sample_data.student.OnlineSecurity_yes['no'],
                                sample_data.student.OnlineSecurity_no['no'],
                                sample_data.student.DeviceProtection_yes['no'],
                                sample_data.student.DeviceProtection_no['no'],
                                sample_data.student.StreamingMovies_yes['no'],
                                sample_data.student.StreamingMovies_no['no'],
                                sample_data.student.Contract_Month_to_month['no'],
                                sample_data.student.Contract_One_year['no'],
                                sample_data.student.Contract_Two_ear['no'],
                                sample_data.student.PaymentMethod_electronic_check['no'],
                                sample_data.student.PaymentMethod_electronic_mailed_check['no'],
                                sample_data.student.PaymentMethod_electronic_bank_transfer['no'],
                                sample_data.student.PaymentMethod_electronic_credit_card['no'],
                                 ]})
    plt.plot(Marks['no'][1:], label="1.InternetService_DSL_yes"
                                 "\n2.InternetService_Fiber_yes"
                                 "\n3.InternetService_No_yes"
                                 "\n4.OnlineSecurity_yes"
                                 "\n5.OnlineSecurity_no"
                                 "\n6.DeviceProtection_yes"
                                 "\n7.DeviceProtection_no"
                                 "\n8.StreamingMovies_yes"
                                 "\n9.StreamingMovies_no"
                                 "\n10.Contract_Month_to_month"
                                 "\n11.Contract_One_year"
                                 "\n12.Contract_Two_ear"
                                 "\n13.PaymentMethod_electronic_check"
                                 "\n14.PaymentMethod_electronic_mailed_check"
                                 "\n15.PaymentMethod_electronic_bank_transfer"
                                 "\n16.PaymentMethod_electronic_credit_card"
             , color="blue")
    plt.xlabel("Clustering")
    plt.ylabel("Count")
    plt.title("Clustering")
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Clustering')
    handles, labels = plt.gca().get_legend_handles_labels()
    order = [0]

    plt_1 = plt.figure(figsize=(6, 4))
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Clustering Labels')
    plt.legend([handles[i] for i in order], [labels[i] for i in order])

    plt.show()


def internet_service():
    import matplotlib.pyplot as plt
    import numpy as np
    a1 = int(sample_data.student.total_DSL_dict['yes'])
    a2 = int(sample_data.student.total_DSL_dict['no'])
    b1 = int(sample_data.student.total_Fiber_dict['yes'])
    b2 = int(sample_data.student.total_Fiber_dict['no'])
    c1 = int(sample_data.student.total_No_dict['yes'])
    c2 = int(sample_data.student.total_No_dict['no'])
    if a1<b1:
        sample_data.student.total_final.append("Internet Service - DSL")
    species = ("DSL", "Fiber optic", "No")
    penguin_means = {
        'Yes': (a1, b1, c1),
        'No': (a2, b2, c2),
    }
    x = np.arange(len(species))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Count')
    ax.set_xlabel('Internet Service')
    ax.set_title('Classification')
    ax.set_xticks(x + width, species)
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Classification')
    ax.legend(loc='upper left', ncols=3)
    plt.show()

def graph_online_security():
    import matplotlib.pyplot as plt
    import numpy as np
    a1 = int(sample_data.student.OnlineSecurity_yes['yes'])
    a2 = int(sample_data.student.OnlineSecurity_yes['no'])
    b1 = int(sample_data.student.OnlineSecurity_no['yes'])
    b2 = int(sample_data.student.OnlineSecurity_no['no'])
    c1 = int(sample_data.student.OnlineSecurity_no_internet['yes'])
    c2 = int(sample_data.student.OnlineSecurity_no_internet['no'])
    if a1<b1:
        sample_data.student.OnlineSecurity_final.append("Online Security - Yes")
    species = ("Yes", "No","no internet service")
    penguin_means = {
        'Yes': (a1,b1,c1),
        'No': (a2,b2,c2),
    }
    x = np.arange(len(species))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Count')
    ax.set_xlabel('Online Security')
    ax.set_title('Classification')
    ax.set_xticks(x + width, species)
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Classification')
    ax.legend(loc='upper left', ncols=3)
    plt.show()
def graph_DeviceProtection():
    import matplotlib.pyplot as plt
    import numpy as np
    a1 = int(sample_data.student.DeviceProtection_yes['yes'])
    a2 = int(sample_data.student.DeviceProtection_yes['no'])
    b1 = int(sample_data.student.DeviceProtection_no['yes'])
    b2 = int(sample_data.student.DeviceProtection_no['no'])
    c1 = int(sample_data.student.DeviceProtection_no_internet['yes'])
    c2 = int(sample_data.student.DeviceProtection_no_internet['no'])
    if a1<b1:
        sample_data.student.DeviceProtection_final.append("Device Protection - Yes")
    species = ("Yes", "No","no internet service")
    penguin_means = {
        'Yes': (a1,b1,c1),
        'No': (a2,b2,c2),
    }
    x = np.arange(len(species))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Count')
    ax.set_xlabel('Device Protection')
    ax.set_title('Classification')
    ax.set_xticks(x + width, species)
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Classification')
    ax.legend(loc='upper left', ncols=3)
    plt.show()
def graph_StreamingMovies():
    import matplotlib.pyplot as plt
    import numpy as np
    a1 = int(sample_data.student.StreamingMovies_yes['yes'])
    a2 = int(sample_data.student.StreamingMovies_yes['no'])
    b1 = int(sample_data.student.StreamingMovies_no['yes'])
    b2 = int(sample_data.student.StreamingMovies_no['no'])
    c1 = int(sample_data.student.StreamingMovies_no_internet['yes'])
    c2 = int(sample_data.student.StreamingMovies_no_internet['no'])
    if a1<b1:
        sample_data.student.StreamingMovies_final.append("Streaming Movies - Yes")
    species = ("Yes", "No","no internet service")
    penguin_means = {
        'Yes': (a1,b1,c1),
        'No': (a2,b2,c2),
    }
    x = np.arange(len(species))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Count')
    ax.set_xlabel('Streaming Movies')
    ax.set_title('Classification')
    ax.set_xticks(x + width, species)
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Classification')
    ax.legend(loc='upper left', ncols=3)
    plt.show()
def graph_Contract():
    import matplotlib.pyplot as plt
    import numpy as np

    a1 = int(sample_data.student.Contract_Month_to_month['yes'])
    a2 = int(sample_data.student.Contract_Month_to_month['no'])
    b1 = int(sample_data.student.Contract_One_year['yes'])
    b2 = int(sample_data.student.Contract_One_year['no'])
    c1 = int(sample_data.student.Contract_Two_ear['yes'])
    c2 = int(sample_data.student.Contract_Two_ear['no'])
    if a1<b1 and a1<c1:
        sample_data.student.Contract_final.append("Contract -  Month to Month")
    elif b1<c1:
        sample_data.student.Contract_final.append("Contract - One year")
    else:
        sample_data.student.Contract_final.append("Contract - Two Year")

    species = ("Month_to_month", "One_year", "Two_year")
    penguin_means = {
        'Yes': (a1, b1, c1),
        'No': (a2, b2, c2),
    }
    x = np.arange(len(species))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Count')
    ax.set_xlabel('Contract')
    ax.set_title('Classification')
    ax.set_xticks(x + width, species)
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Classification')
    ax.legend(loc='upper left', ncols=3)
    plt.show()
def graph_PaymentMethod():
    import matplotlib.pyplot as plt
    import numpy as np

    a1 = int(sample_data.student.PaymentMethod_electronic_check['yes'])
    a2 = int(sample_data.student.PaymentMethod_electronic_check['no'])

    b1 = int(sample_data.student.PaymentMethod_electronic_mailed_check['yes'])
    b2 = int(sample_data.student.PaymentMethod_electronic_mailed_check['no'])

    c1 = int(sample_data.student.PaymentMethod_electronic_bank_transfer['yes'])
    c2 = int(sample_data.student.PaymentMethod_electronic_bank_transfer['no'])

    d1 = int(sample_data.student.PaymentMethod_electronic_credit_card['yes'])
    d2 = int(sample_data.student.PaymentMethod_electronic_credit_card['no'])

    if a1<b1 and a1<c1 and a1<d1:
        sample_data.student.PaymentMethod_final.append("Payment - Electronic")
    elif b1<c1 and b1<d1:
        sample_data.student.PaymentMethod_final.append("Payment - Mailed Check")
    elif c1<d1:
        sample_data.student.PaymentMethod_final.append("Payment - Bank Transfer")
    else:
        sample_data.student.PaymentMethod_final.append("Payment - Credit card")

    species = ("Electronic Check", "Mailed Check", "Bank Transfer","Credit Card")
    penguin_means = {
        'Yes': (a1, b1, c1,d1),
        'No': (a2, b2, c2,d2),
    }
    x = np.arange(len(species))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Count')
    ax.set_xlabel('Payment Method')
    ax.set_title('Classification')
    ax.set_xticks(x + width, species)
    from matplotlib import pylab
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Classification')
    ax.legend(loc='upper left', ncols=3)
    plt.show()

def read_data_set1():
    # sample_data.student.total_DSL_dict.clear()
    # sample_data.student.total_Fiber_dict.clear()
    # sample_data.student.total_No_dict.clear()
    sample_data.student.total_DSL_dict = {"yes": 0, "no": 0}
    sample_data.student.total_Fiber_dict = {"yes": 0, "no": 0}
    sample_data.student.total_No_dict = {"yes": 0, "no": 0}

    sample_data.student.OnlineSecurity_yes = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.OnlineSecurity_no = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.OnlineSecurity_no_internet = {"yes": 0, "no": 0, "no internet service": 0}

    sample_data.student.DeviceProtection_yes = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.DeviceProtection_no = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.DeviceProtection_no_internet = {"yes": 0, "no": 0, "no internet service": 0}

    sample_data.student.StreamingMovies_yes = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.StreamingMovies_no = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.StreamingMovies_no_internet = {"yes": 0, "no": 0, "no internet service": 0}

    sample_data.student.Contract_Month_to_month = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.Contract_One_year = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.Contract_Two_ear = {"yes": 0, "no": 0, "no internet service": 0}

    sample_data.student.PaymentMethod_electronic_check = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.PaymentMethod_electronic_mailed_check = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.PaymentMethod_electronic_bank_transfer = {"yes": 0, "no": 0, "no internet service": 0}
    sample_data.student.PaymentMethod_electronic_credit_card = {"yes": 0, "no": 0, "no internet service": 0}

    TableMargin = Frame(knn_data_main, width=400)
    TableMargin.place(x=170, y=110,width=455, height=205)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("InternetService"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('InternetService', text="InternetService", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.pack()
    file="data_set/feature.csv"
    service_list = []
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            t1 = row['InternetService']
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
            clustering(t1,t21,t10,t12,t15,t16,t18)
    service_list.append("internet_service")
    service_list.append("OnlineSecurity")
    service_list.append("DeviceProtection")
    service_list.append("StreamingMovies")
    service_list.append("Contract")
    service_list.append("PaymentMethod")
    service_list.append("Churn")
    sample_data.student.total_count=len(service_list)
    res = []
    [res.append(x) for x in service_list if x not in res]
    for x in res:
        tree.insert("", 0, values=(x))
    clustering_result()
    # clustering_result1()


def prediction():
    internet_service()
    graph_online_security()
    graph_DeviceProtection()
    graph_StreamingMovies()
    graph_Contract()
    graph_PaymentMethod()
    print(sample_data.student.total_final)
    print(sample_data.student.OnlineSecurity_final)
    print(sample_data.student.DeviceProtection_final)
    print(sample_data.student.StreamingMovies_final)
    print(sample_data.student.Contract_final)
    print(sample_data.student.PaymentMethod_final)
    messagebox.showinfo("Result",sample_data.student.total_final[0]+"\n"
                        +sample_data.student.OnlineSecurity_final[0]+"\n"
                        +sample_data.student.DeviceProtection_final[0]+"\n"
                        +sample_data.student.StreamingMovies_final[0]+"\n"
                        +sample_data.student.Contract_final[0]+"\n"
                        +sample_data.student.PaymentMethod_final[0]+"\n"
                        +"\n\nREDUCE CHURN"
                        )



############################################################
knn_data_main = Tk()
w=750
h=550
ws = knn_data_main.winfo_screenwidth()
hs = knn_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
knn_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
knn_data_main.title(sample_data.student.title)
knn_data_main.configure(background=sample_data.student.background)
########################################################### Element design


message = Label(knn_data_main, text=sample_data.student.titlec,fg="#FFF",bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(knn_data_main, text="Clustering",width=20,command=read_data_set1  ,height=1,fg="#000",bg="#FFF", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=120, y=400)

resust_dataset = Button(knn_data_main,command=prediction , text="Classification",width=20  ,height=1,fg="#000",bg="#FFF", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)



# user_data = Label(ann_data_main, text="Single Data",fg="#003366",bg=sample_data.student.background, width=15,height=1, font=('times', 20, 'italic bold '))
# user_data.place(x=300, y=510)
knn_data_main.mainloop()
