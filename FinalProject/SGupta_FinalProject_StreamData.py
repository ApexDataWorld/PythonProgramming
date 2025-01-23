#Read in some data to sample from
import pandas as pd
data = pd.read_csv("data/power_streaming_data.csv")
# Cast the "Hour" column to DoubleType
data["hour_double"] = data["Hour"].astype(float)

#Now a for loop to sample a few rows and output them to a data set
#Put a pause in as well
import numpy as np
import time

for i in range(0,50):
    #randomly sample a few rows
    temp = data.loc[np.random.randint(data.shape[0], size = 5)]
    #temp["timestamp"] = [time.strftime("%H:%M:%S", time.localtime())]*5
    temp.to_csv("csv_files/power_streaming_data_" + str(i) + ".csv", index = False, header = True)
    time.sleep(10)