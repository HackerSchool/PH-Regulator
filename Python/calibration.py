
import os
import sys
import numbers
import time
import Adafruit_ADS1x15
import numpy as np
import pandas as pd

buffer_solution_PH = []
values = []
values_1 = []
voltage = []

def calibration():

    # Create an ADS1115 ADC (16-bit) instance
    adc = Adafruit_ADS1x15.ADS1115()
    
    GAIN = 2/3

   
    float_nums = np.arange(0, 14.01, 0.01)
    #print(float_nums)
    

    print('---- Calibration ----')
    

    while True:
        try:
            number_of_points = int(input('How many points will be used to calibrate the sensor ? '))
            break
        except ValueError:
            os.system('cls')
            print("Enter a number, please.")
            
    

    for i in range(number_of_points):
            
                while True:
                    try:
                        buffer_solution_PH.insert(i,float(input('Enter buffer solution PH : ')))
                        print('')
                        print('----------------------------------------------------')
                        print("Put the probe in the solution and wait for 1 minute.")
                        print('----------------------------------------------------')
                        print('')

                                                
                        for remaining in range(60, 0, -1):
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                            sys.stdout.flush()
                            time.sleep(1)

                            

                        for i in range(10):
                            values.insert(i, adc.read_adc(0, gain=GAIN))
                            time.sleep(1)

                        values_1.insert(i, round(sum(values)/len(values)))
                        print('')
                        sys.stdout.write("\rComplete!            \n")
                        
                        break
                    except:
                        print("Enter a number between 0 and 14 please.")
                        pass

                

                voltage =[element * ((5/65536)*1000) for element in values_1] # mV
            

                
    #print(buffer_solution_PH)
    #print(values_1)
    print('Success !!!')
    print('Saving data to ph_calibration.txt')

    #Displaying the array

    col1 = "Buffer PH"
    col2 = "Values"
    col3 = "Avg. Values"
    col4 = "Voltage"
    data = pd.DataFrame({col1:buffer_solution_PH,col2:values_1,col3:values_1,col4:voltage})
    data.to_excel('calibration.xlsx', sheet_name='sheet1', index=False)
   
    #Displaying the contents of the xlsx file
    
    data1 = pd.read_excel (r'/home/pi/PH_Dosemeter/calibration.xlsx') 
    PH =  data1['Buffer PH'].tolist()
    Values_1 =  data1['Values'].tolist()
    AvgValues = data1['Avg. Values'].tolist()
    Voltage = data1['Voltage'].tolist()

    print("Contents in calibration.xlsx: ")
    print ("PH list : " + str(PH))
    print ("Values list : " + str(values))
    print ("Avg. Values : " + str(AvgValues))
    print ("Voltage list : " + str(Voltage))
     


