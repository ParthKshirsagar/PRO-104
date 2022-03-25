import csv
from collections import Counter

file = 'height_weight_data.csv'

with open(file, newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

weight_data = []
file_data.pop(0)

for i in range(len(file_data)):
    n_numb = file_data[i][2]
    weight_data.append(float(n_numb))

n = len(weight_data)

def mean():
    total = 0
    for i in weight_data:
        total += i
    mean = total/n
    print("Mean (Average): " + str(mean))

def median():
    weight_data.sort()
    if(n % 2 == 0):
        numb1 = float(weight_data[n//2])
        numb2 = float(weight_data[(n//2) - 1])
        median = (numb1 + numb2)/2
    else:
        median = weight_data[n//2]
    print("Median: " + str(median))

def mode():
    data = Counter(weight_data)
    range_of_data = {
        '75-85': 0,
        '85-95': 0,
        '95-105': 0,
        '105-115': 0,
        '115-125': 0,
        '125-135': 0,
        '135-145': 0,
        '145-155': 0,
        '155-165': 0,
        '165-175': 0
    }
    for weight, occurance in data.items():
        if(75 < float(weight) < 85):
            range_of_data['75-85'] += occurance
        elif(85 < float(weight) < 95):
            range_of_data['85-95'] += occurance
        elif(95 < float(weight) < 105):
            range_of_data['95-105'] += occurance
        elif(105 < float(weight) < 115):
            range_of_data['105-115'] += occurance
        elif(115 < float(weight) < 125):
            range_of_data['115-125'] += occurance
        elif(125 < float(weight) < 135):
            range_of_data['125-135'] += occurance
        elif(135 < float(weight) < 145):
            range_of_data['135-145'] += occurance
        elif(145 < float(weight) < 155):
            range_of_data['145-155'] += occurance
        elif(155 < float(weight) < 165):
            range_of_data['155-165'] += occurance
        elif(165 < float(weight) < 175):
            range_of_data['165-175'] += occurance

    mode_range, mode_occurance = 0,0
    for range, occurance in range_of_data.items():
        if(occurance > mode_occurance):
            mode_range, mode_occurance = [int(range.split('-')[0]), int(range.split('-')[1])], occurance
    
    mode = float((mode_range[0] + mode_range[1])/2)
    print("Mode: " + str(mode))

def main():
    mean()
    median()
    mode()

main()