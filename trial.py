import pandas as pd
import random
data1 = pd.read_csv(r'C:\Users\HP\Downloads\Medicine-Recommendation-System-Personalized-Medical-Recommendation-System-with-Machine-Learning-main\doctorReviews (2).csv')
#print(data1.head())
data2 = pd.read_csv(r'C:\Users\HP\Downloads\Medicine-Recommendation-System-Personalized-Medical-Recommendation-System-with-Machine-Learning-main\docsche.csv')
data2=data2.drop('speciality', axis=1)
#print(data2.head())

data1['key'] = range(len(data1)) 
data2['key'] = range(len(data2))
output = pd.merge(data1, data2, on='key', how='left') 

print(output.head(1).to_string())
#print(output.shape)
filtered_rows = []
a=random.randint(1,10) #to select a random no to decide how many doctors to display
for i in range(1, a+1):
    p=random.randint(1, 143)
    filtered_row = output[output['key'] == p]
    #print(filtered_row)
    filtered_rows.append(filtered_row.to_string(index=False))
    #print(filtered_row.to_string(index=False)) 

#print(filtered_rows)

