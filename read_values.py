from itertools import count
import os
import sys
import numbers
import time
import Adafruit_ADS1x15
import matplotlib.pyplot as plt
from scipy import stats
import ast
from datetime import datetime
import pandas as pd


def read_calibration_file():

    global slope 
    global intercept

    try:
            #Displaying the contents of the xlsx file
    
            data1 = pd.read_excel (r'/home/pi/PH_Dosemeter/calibration.xlsx') 
            PH =  data1['Buffer PH'].tolist()
            #Values_1 =  data1['Values'].tolist()
            #AvgValues = data1['Avg. Values'].tolist()
            Voltage = data1['Voltage'].tolist()


            slope, intercept, r, p, std_err = stats.linregress(PH, Voltage)

            

            print('Calibration results loaded!')

            print('')

            print('Slope: ' + str(slope))
            print('Intercept: ' + str(intercept))

            
    except:
            print("calibration.xlsx ERROR ! Please run calibration !")
            sys.exit(1)

        

def read_values():

    values = []

    while True:

        timeout = time.time() + 60*5   # 5 minutes from now

        try:

                # Create an ADS1115 ADC (16-bit) instance
                adc = Adafruit_ADS1x15.ADS1115()
                
                GAIN = 2/3

                for i in range(10):
                    values.insert(i, adc.read_adc(0, gain=GAIN))
                    time.sleep(1)

                values_1 = round(sum(values)/len(values))
                voltage = values_1 * ((5.00/65536)*1000)  # mV

                current_ph = (voltage- intercept)/slope 

                # datetime object containing current date and time
                now = datetime.now()
                
                # dd/mm/YY H:M:S
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                print(dt_string)	
                print('')
                print('PH: '+ str(current_ph) + '  V: ' + str(voltage))
                print('Temp:')
                print('')


        except KeyboardInterrupt or time.time() > timeout:
            pass