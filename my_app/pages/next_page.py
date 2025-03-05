import pickle
import streamlit as st
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
st.title("Next Page")
res=""

import os

model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "model.pkl"))
with open(model_path, "rb") as f:
    model = pickle.load(f)


# Retrieve stored data
user_name = st.session_state.get("user_name", "Guest")
age = st.session_state.get("age", "Age not set")
gender = st.session_state.get("gender", "Not set")
job = st.session_state.get("selected_image", "Not selected")
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



#standardization
prediction = model.predict(scaled_list)
res = "Survived 🟢" if prediction[0] == 1 else "Did Not Survive 🔴"

titanic_powers = [
    "Being able to drown humorously : No matter how dire, your drowning is always comedic.",  # 
    "Being able to swim like a toad : Your swimming style is awkward yet oddly effective.",  # 
    "Dramatic Sinker : You go down like a Shakespearean tragedy, slow and over-the-top.",  # 
    "Bubble Trail Artist : Your drowning leaves behind artistic bubble patterns.",  # 
    "Fish Whisperer : You can command fish to help (but they mostly just laugh).",  #
    "Elegant Floater : No matter what, you float with grace and poise.",
     "Synchronized Screamer : Your screams perfectly match others like a choir.",  
    "The Plank Magnet : Any floating debris actively drifts toward you.    ",  # Any floating debris actively drifts toward you.
    "Jack’s Revenge : Ghost Jack ensures you never find a floating door.",  #
]
power=random.choice(titanic_powers)

if "age" not in st.session_state or "gender" not in st.session_state or "selected_image" not in st.session_state:
    st.error("You haven't filled all details! Please go back and complete them.")
    if st.button("Go Back"):
        st.switch_page("app.py")  # Replace with your main file name


if gender == "male":
    img_src = "https://static.vecteezy.com/system/resources/previews/027/191/041/original/pixel-art-male-techer-character-2-png.png"
else:
    img_src = "https://static.vecteezy.com/system/resources/previews/027/190/801/original/pixel-art-female-teacher-character-3-png.png"

# Display the correct image
st.markdown(
    f"""
    <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
       
        .box-container {{
            display: flex;
            height: 500px;
            border: 2px solid #ccc;
        }}
        .stAppHeader{{
            display:none
        }}
        .left-box {{
            flex: 1;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .right-box {{
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        .right-box .top, .right-box .bottom {{
            flex: 1;
            border-top: 2px solid #ccc;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction:column;
            
        }}
        .pi{{
            border:2px solid white;
            padding:10px;
            border-radius:8px;
            margin:20px;
            width:80%;
    
           
        }}
         .st{{
                 font-family: 'Press Start 2P', cursive; 
    
                display:flex;
                allign-items:center;
                justify-content:center;
                height:100px
                width:80%;
                font-size:30px;
                margin:30px;
                border:4px solid white;
                
            }}
    </style>
    
    <div class="st">You {res}!!!</div>
    <div class="box-container">
        <div class="left-box">
           <img src="{img_src}" width="200">
        </div>
        <div class="right-box">
            <div class="top">
                <p class ="pi">Gender : {gender}</p>
                <p class="pi">Job :{job}
            </div>
            <div class="bottom">
              <p class ="pi">Salary : {salary}</p>
              <p class="pi">Your Superpower : {power}</p>
            </div>
        </div>
    </div>
    
   
    """,
    unsafe_allow_html=True
)
