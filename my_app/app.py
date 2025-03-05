import streamlit as st
if "gender" not in st.session_state:
    st.session_state["gender"] = "None"
selected = st.session_state.get("gender", "None")
if "male_click_count" not in st.session_state:
    st.session_state["male_click_count"] = 0
if "female_click_count" not in st.session_state:
    st.session_state["female_click_count"] = 0

if selected == "None":
    css_style = """
    <style>
    .box {
        width: 45%;
        height: 250px;
        background-color: #333333;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 10;
        margin-top: 100px;
        border-radius: 50px;
        cursor: pointer;
        opacity: 0.6;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
        .left-box, .right-box {
            z-index: 14;
            cursor: pointer;
        }
    </style>
    """
elif selected =="male":
    css_style = """
    <style>
    .left-box {
        width: 45%;
        height: 250px;
        background-color: #333333;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 10;
        margin-top: 100px;
        border-radius: 50px;
        cursor: pointer;
        opacity: 1;
        transform: scale(1.1);
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .right-box{display:none}
    </style>
    """
elif selected == "female":
    css_style = """
    <style>
    .right-box {
        position:absolute
        width: 60%;
        height: 250px;
        background-color: #333333;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 10;
        margin-top: 100px;
        border-radius: 50px;
        cursor: pointer;
        opacity: 1;
        transform: scale(1.1);
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .left-box{display:none;}
    </style>
    """
    
st.markdown(css_style, unsafe_allow_html=True)



st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

        .stAppHeader { display: none; }        
        .pixel-font { font-family: 'Press Start 2P', cursive; }

        .title-start {
            font-size: 30px;
            text-align: center;
            margin-bottom: 40px;
            color: white;
            z-index: 2;
            margin-top: 150px;
        }

        .title {
            font-size: 35px;
            text-align: center;
            color: white;
            z-index: 2;
            margin-top: 20px;
        }

        .stApp {
            position: relative;
            min-height: 100vh;
            background-size: 95%;
            opacity:0.8;
            background-position: center;
            background-image: url('https://pixelartusa.com/cdn/shop/files/4BP57titanic2_2048x.jpg?v=1696262400');
        }

        /* Ensure overlays are behind the content */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background-image: inherit;
            background-size: inherit;
            background-position: inherit;
            background-repeat: inherit;
            filter: blur(3px);
            pointer-events: none;
            z-index: -2; /* Send behind all content */
        }

        .stApp::after {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: rgba(0, 0, 0, 0.3); /* Lighter overlay */
            pointer-events: none;
            z-index: -1; /* Behind content but above the background */
        }

        .stApp > .streamlit-expanderHeader, .stApp > .stMarkdown {
            position: relative;
        }

        /* Custom image styling */
        .custom-image {
            border-radius: 12px;
            
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            margin: 100px auto 0;
            z-index: 10;
        }

        /* Box styling */
        
        .box:hover {
            opacity: 1;
            transform: scale(1.1);
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }


        .titl {
            font-size: 27px;
            margin-bottom: 40px;
            margin-left: 20px;
            color: white;
            z-index: 2;
            margin-top: 40px;
            position:relative;
            top:100px;
        }

        .bg {
            border-radius: 50px;
            width: 100%;
            padding-left: 40px;
            padding-right: 40px;
            height: 500px;
            background-color: #4d4d4d;
            margin-top: 100px;
            z-index: 1;
        }
    </style>
""", unsafe_allow_html=True)

# Title with pixel font
st.markdown('<div class="pixel-font title">Can You Survive Titanic?</div>', unsafe_allow_html=True)

# Display image with custom styling
st.markdown("""
    <img class="custom-image" src="https://art.pixilart.com/2bedf2c0551da67.gif" width="500" />
""", unsafe_allow_html=True)

# Title and horizontal line for distinction
st.markdown('<div class="pixel-font title-start">Lets Start !!</div>', unsafe_allow_html=True)
st.markdown("""
    <hr style="border: 3px solid #444444; width: 100%; margin: 30px 0;" />
""", unsafe_allow_html=True)

# Background container with interactive boxes
st.markdown('''
    <div class="bg">
        <div class="pixel-font titl">1. Choose Gender: </div>
        <div class="box left-box">
            <img width="150px" style="border-radius:30px;" src="https://media.tenor.com/Np69ChcpefYAAAAC/pixel-art.gif">
            <p class="pixel-font" style="margin-top: 20px;">Male</p>
        </div>
        <div class="box right-box">
            <img width="150px" style="border-radius:30px;" src="https://img2.reactor.cc/pics/post/downvote-Pixel-Gif-Pixel-Art-Anime-7876807.gif">
            <p class="pixel-font" style="margin-top:20px;">Female</p>
        </div>
    </div>
''', unsafe_allow_html=True)



st.markdown("""
    <style>
        /* Style the Streamlit button using its CSS structure */
        .stButton > button {
            background-color: #696969;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            font-family: 'Press Start 2P', cursive;
            font-size: 16px;
            cursor: pointer;
            position:relative;
            left:130px;
        }
        .stButton > button:hover {
            background-color: #353839;
            color:white;
        }
    </style>
""", unsafe_allow_html=True)

# Define custom CSS for the container
st.markdown(
    """
    <style>
        .my-container {
            background-color: #333333;  /* light grey background */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container and inject an opening <div> tag
with st.container():
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    
    # Set up session state for gender


    # Create two columns for horizontal alignment of buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Male"):
            st.session_state.gender = "male"
            st.session_state["male_click_count"] += 2
         
    with col2:
        if st.button("Female"):
            st.session_state.gender = "female"
            st.session_state["female_click_count"] += 2
            

    
    # Close the container div
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown(
    f'<div style="text-align: center; color: white; font-size: 18px; background-color:#333333;margin:35px;font-family: \'Press Start 2P\', cursive; border-radius:30px; padding:20px">'
    f'Selected gender: {st.session_state.gender}'
    '</div>',
    unsafe_allow_html=True
)



st.markdown("""
    <hr style="border: 3px solid #444444; width: 100%; margin: 30px 0;" />
""", unsafe_allow_html=True)



# Create a container that visually looks like the left-box
st.markdown("""
    <style>
     .boxi {
        width: 50%;
        height: 200px;
        background-color: #333333;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 10;
        margin-top: 100px;
        border-radius: 20px;
        cursor: pointer;
        opacity: 0.85;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        font-size:27px;
    }
  .pixel-fonti { font-family: 'Press Start 2P', cursive; }
    
    </style>
    
    <div class="boxi pixel-fonti "> Select Your Age</div>
    
    
    
    
    """, unsafe_allow_html=True)



st.markdown("""
    <style>
        /* Example: target the slider container using one of the auto-generated classes */
        .st-an {
            /* Adjust these values as needed */
            height: 80px !important;
        }
        /* Example: target the slider thumb */
        .st-au {
            height: 40px !important;
            width: 1000px !important;
            background-color: #696969 !important;
            border: 2px solid #353839 !important;
            border-radius: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

age = st.slider("", min_value=0, max_value=100, value=25, step=1)
st.markdown(
    f"""
    <p style="color: white; background: #333333; font-family: 'Press Start 2P', cursive; font-size: 20px; padding: 20px; border-radius: 30px;text-align:center;">
        Your age is: {age}
    </p>
    """,
    unsafe_allow_html=True
)
if age<19:
    st.write("u a kid!! ahahhahah ")

st.markdown("""
    <hr style="border: 3px solid #444444; width: 100%; margin: 30px 0; " />
""", unsafe_allow_html=True)





# Create a container that visually looks like the left-box
st.markdown("""
    <style>
     .boxi {
        width: 100%;
        height: 250px;
        background-color: #333333;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 10;
        margin-top: 100px;
        border-radius: 50px;
        cursor: pointer;
        opacity: 0.85;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        font-size:27px;
    }
  .pixel-fonti { font-family: 'Press Start 2P', cursive; }
    
    </style>
    
    <div class="boxi pixel-fonti "> Job Occupation!</div>
    
    
    
    
    
    """, unsafe_allow_html=True)

import streamlit as st

# Initialize the selected image in session state
if "selected_image" not in st.session_state:
    st.session_state["selected_image"] = None

#import streamlit as st

# Initialize selected image if not already set
if "selected_image" not in st.session_state:
    st.session_state["selected_image"] = None

# Create a big container with custom styling
st.markdown("""
    <style>
        .big-container {
            background-color: #333333;
            padding: 20px;
            border-radius: 20px;
            margin-bottom: 20px;
        }
        .container-title {
            text-align: center;
            color: white;
            font-family: 'Press Start 2P', cursive;
        }
    </style>
   
       
    """, unsafe_allow_html=True)

# Row 1: Two images
col1, col2 = st.columns(2)
with col1:
    st.image("https://static.vecteezy.com/system/resources/previews/027/190/969/original/pixel-art-mechanic-show-his-muscle-png.png",width=200)
    if st.button("Engineer", key="img1"):
         st.session_state.selected_image = "Engineer"
with col2:
    st.image("https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/f07feb7ba77b872.png",width=200)
    if st.button("Farmer", key="img2"):
         st.session_state.selected_image = "Farmer"

# Row 2: Two images
col3, col4 = st.columns(2)
with col3:
    st.image("https://static.vecteezy.com/system/resources/previews/027/191/041/original/pixel-art-male-techer-character-2-png.png", width=200)
    if st.button("Job Worker", key="img3"):
         st.session_state.selected_image = "Job Worker"
with col4:
    st.image("https://cdn.pixabay.com/photo/2021/03/02/17/26/pixel-6063246_960_720.png", width=200)
    if st.button("Gamer", key="img4"):
         st.session_state.selected_image = "Gamer"

# Close the container div
st.markdown("</div>", unsafe_allow_html=True)

# Display the selected image text below the container
if st.session_state.selected_image:
    st.markdown(
        f"""
        <div style="text-align: center; color: white; font-family: 'Press Start 2P', cursive; font-size: 24px; border-radius:20px;margin-top:20px;background-color:#333333",padding:30px;margin:40px;>
            You selected: {st.session_state.selected_image}
        </div>
        """,
        unsafe_allow_html=True
    )




st.markdown("""
    <hr style="border: 3px solid #444444; width: 100%; margin: 30px 0;" />
""", unsafe_allow_html=True)
st.markdown("""
    <style>
     .boxi {
        width: 100%;
        height: 150px;
        background-color: #1E90FF;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 10;
        margin-top: 100px;
        border-radius: 20px;
        cursor: pointer;
        opacity: 0.85;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        font-size:27px;
    }.aa{
        margin-bottom:30px;
        border-radius:5px
        height
    }
  .pixel-fonti { font-family: 'Press Start 2P', cursive; }
    
    </style>
    
    <div class="boxi pixel-fonti  aa"> Choose Your IQ!</div>
    
    
    
    
    
    """, unsafe_allow_html=True)

col9, col8 = st.columns(2)
a=0
with col9:
    if st.button("🔴 40(Below Average)"):
        a=1
    if st.button("🔵 80(Average)"):
        a=1
# Create main layout

with col8:
    if st.button("🟢 120(genius)"):
        a=1
    if st.button("🟡 150(Genius)"):
        a=1
        
if a==1:
    st.markdown(
        f"""
        <div style="text-align: center; color: white; font-family: 'Press Start 2P', cursive; font-size: 24px; border-radius:20px;margin-top:20px;background-color:#333333",padding:30px;margin:40px;>
            Your IQ: 0
        </div>
        """,
        unsafe_allow_html=True
    )
# Example data to pass
if "user_name" not in st.session_state:
    st.session_state.user_name = "unknown"
    st.session_state.age = age


# Inject CSS targeting st.page_link's underlying button (which may share classes with st.button)
st.markdown("""
    <hr style="border: 5px solid #444444; width: 100%; margin: 30px 0;" />
""", unsafe_allow_html=True)

# This creates a new row with five columns.
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
with col3:
    st.page_link("pages/next_page.py", label="Check Results!!", icon="➡️")

st.markdown("""
    <hr style="border: 5px solid #444444; width: 100%; margin: 30px 0;" />
""", unsafe_allow_html=True)
