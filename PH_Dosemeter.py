import os
import sys
import time
from calibration import calibration
from read_values import read_calibration_file, read_values
from reset import reset
1
# Menu

print('------ Menu ------')
print('| 1. Calibration |')
print('| 2. Read values |')
print('| 3. Reset       |')
print('| 4. Quit        |')

option = input('Select one of the options above: ')

while option not in ['1','2','3','4']:
    os.system('cls')
    print('------ Menu ------')
    print('| 1. Calibration |')
    print('| 2. Read values |')
    print('| 3. Reset       |')
    print('| 4. Quit        |')

    option = input('Select one of the options above: ')
    

if option =='1':
    calibration()
elif option == '2':
    read_calibration_file()
    read_values()
elif option == '3':
    reset()
elif option == '4':
    sys.exit()
