import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.dates
#import meta as mt
import numpy as np
from datetime import timedelta


def plc(dataframe, name, retailer = 0, product = 0, ignore_returns = 1):

        #Bliver ordnet før denne metode, lige nu er det her til at lave test data
        if retailer != 0:
                dataframe = dataframe[dataframe.retailerID == retailer]
        if product != 0:
                dataframe = dataframe[dataframe.productID == product]
        #Parametre til metadata, pt. udkommenteret fordi meget af det bliver gjort i navnet
        # firstdate = str(dataframe['date'].iloc[0])
        # lastdate = str(dataframe['date'].iloc[-1])
        # retailer = str(dataframe['retailerID'].iloc[0])
        # product = str(dataframe['productID'].iloc[0])
        #Sortering og plot
        if ignore_returns:
                dataframe = dataframe[dataframe.quantity >= 0]

        dataframe_quantity = dataframe.groupby(by='date').sum()
        #Den brokker sig pt over denne linje, når der er fundet ud af hvorfor og der er fixet slet denne kommentar :D
        dataframe['discountP'] = (- dataframe['discount'] ) / (dataframe['turnover'] - dataframe['discount']) * 100
        dataframe_discount = dataframe.groupby(by='date').mean()
        dataframe_turnover = dataframe.groupby(by='date').sum()

        #Sammensætter en ny dataframe kun med dem vi er interesserede i
        dataframe_plot = pd.concat([dataframe_quantity['quantity'], dataframe_discount['discountP'], dataframe_turnover['turnover']],
                                   axis = 1, keys = ['quantity', 'discount', 'turnover'])
        #Fungere ligesom groupby, men med en bestemt frekvens 4D = 4 dage, W = week

        dataframe_weekly = dataframe_plot.resample('W').agg({'quantity' : 'sum', 'turnover' : 'sum'})
        dataframe_weekly.plot()
        #Udkommenteret mulighed for at lave 2 y akser, jeg syntes det virkede mere uoverskueligt
        plt.figure()
        ax = dataframe_weekly.plot(secondary_y=['turnover'])
        ax.set_ylabel('quantity')
        ax.right_ax.set_ylabel('turnover')
        #Sætter max-værdier for akserne
        #ax.set_ylim(ymax=22000, ymin=-50)
        #ax.right_ax.set_ylim(ymax=850000, ymin=-50)

        datemin = pd.datetime(2016, 6, 1)
        datemax = pd.datetime(2017,9, 10)
        ax.set_xlim(datemin, datemax)

        #Tjekker for mappen, hvis den ikke findes oprettes den
        directory = os.path.dirname(name)
        if not os.path.exists(directory):
                os.makedirs(directory)
        plt.tight_layout()
        plt.savefig('%s.png' % name)
        # mt.addMetaData('%s.png' %name, {'from':firstdate, 'to':lastdate,
        #                                  'retailer':retailer, 'product':product})
        plt.close()

