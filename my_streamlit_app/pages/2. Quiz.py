import streamlit as st
import random

st.title("What Plant Are You?")
st.write("Discover your plant personality")

environment = st.radio(
    "1. What's your ideal environment?",
    ["Breezy beach", "Quiet castle", "Bustling city", "Fairy Garden"]
)
energy_level = st.selectbox(
    "2. How energetic are you?",
    ["Very - always moving", "Average - depends on my mood", "Low - chilled out"]
)
favcolors = st.multiselect(
    "3. Pick your favorite colors",
    ["Green", "Yellow","Pink", "Purple", "Blue"]
)
socialnum = st.slider(
    "4. How social are you? (1=lone wolf, 10=life of the party)",
        1,5,3
    )
patiencelevel= st.number_input(
    "5. On a scale of 1-10, how patient are you?",
    min_value =1, max_value=10, value=5
)
if st.button("Get My Results!"):
    CactusScore = 0
    PothosScore = 0
    SunflowerScore = 0
    SnakePlantScore = 0

    
    if environment == "Breezy beach":
        SunflowerScore += 1
        CactusScore += 2
    elif environment == "Quiet castle":
        PothosScore += 1
        SnakePlantScore += 1
    elif environment == "Fairy Garden":
        PothosScore += 2
    if energy_level == "Very - always moving":
        SunflowerScore += 2
        PothosScore += 1
    elif energy_level == "Average - depends on my mood":
        SnakePlantScore += 1
    elif energy_level == "Low - chilled out":
        CactusScore += 2
    
    if "Green" in favcolors:
        CactusScore += 3
        PothosScore += 2
        SnakePlantScore += 1
    if "Pink" in favcolors:
        SunflowerScore +=1
        CactusScore += 1
    if "Purple" in favcolors:
        SnakePlantScore += 3
        PothosScore += 1
    if "Yellow" in favcolors:
        SunflowerScore += 3
    if "Blue" in favcolors:
        CactusScore += 1
    if socialnum <= 3:
        CactusScore += 4
    if socialnum > 3 and socialnum <= 5:
        SnakePlantScore += 4
    if socialnum >5 and socialnum <=7:
        PothosScore += 4
    if socialnum >7:
        SunflowerScore += 4
    if patiencelevel <=3:
        SunflowerScore +=1
    if patiencelevel > 3 and patiencelevel <= 5:
        PothosScore += 2
    if patiencelevel >5 and patiencelevel <= 7:
        SnakePlantScore += 3
    if patiencelevel >7:
        CactusScore += 4
    if CactusScore > SunflowerScore and CactusScore > SnakePlantScore and CactusScore > PothosScore:
        st.success(f'**You are a Cactus!**')
        st.write("Dependable, resilient, and detetermined")
        st.image("images/cactus.jpeg")
    elif SunflowerScore > CactusScore and SunflowerScore > SnakePlantScore and SunflowerScore > PothosScore:
        st.success(f'**You are a Sunflower!**')
        st.write(f'Outgoing, optimistic, and cheery')
        st.image(f'images/sunflower.jpeg"')
    elif SnakePlantScore > SunflowerScore and SnakePlantScore > CactusScore and SnakePlantScore > PothosScore:
        st.success(f'**You are a Snake Plant!**')
        st.write(f'Mysterious, adaptable, and sophisticated')
        st.image("images/snake_plant.jpeg")
    elif PothosScore > SunflowerScore and PothosScore > CactusScore and PothosScore > SnakePlantScore:
        st.success(f'**You are a Pothos!**')
        st.write(f'Cool, lighthearted, and peacekeeping')
        st.image("images/pothos.jpeg")
    else:
        st.success("**It's a tie!**'")
        st.write('You have a balanced plant personality!')
        st.image("images/neutral.jpeg")
                   
        
        
