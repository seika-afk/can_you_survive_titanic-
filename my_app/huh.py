import pickle


import streamlit as st
import numpy as np
import random
from sklearn.preprocessing import StandardScaler

with open("model.pkl", "rb") as f:  
    model = pickle.load(f)  


scaler=StandardScaler()



# Retrieve stored data

age = 18
gender ="male"
job = "Engineer"
# Determine the correct image based on gender





#job worker 150-200
#engineer: 50-200
#farmer: 40-250
#game: 10-50

salary=0
match job:
    case 'Engineer':
        salary = random.randint(50,200)
    case 'Farmer':
        salary= random.randint(40,250)
    case 'Job_Worker':
        salary= random.randint(150,200)
    case 'Gamer':
        salary= random.randint(10,100)


# sex,pclass,age,fare,salary,embarked
#PREPROCESSING
gen=0
pclass=0
if(gender== "male"):
    gen=1

if(salary>180):
    pclass=1
    parch=1
    embark=1
elif (salary>100 and salary<180):
    pclass=2
    parch=1
    embark=2
else:
    pclass=3
    parch=0
    embark=3
    
    
lisi = np.array([pclass, gen, age, parch, salary, embark]).reshape(1, -1)  
scaled_list=scaler.fit_transform(lisi)

#standardization
prediction = model.predict(scaled_list)
result = "Survived 🟢" if prediction[0] == 1 else "Did Not Survive 🔴"
print(result)