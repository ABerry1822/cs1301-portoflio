import streamlit as st
import os
def get_image_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_app_dir = os.path.dirname(current_dir)
    return os.path.join(main_app_dir, "Images", filename)
st.title("My Plants!")
st.image(get_image_path("group.jpeg))
st.write(f'This is my collection of plants! Most of them have been with me the whole semester, but some are new')
left, right = st.columns(2)
with left:
    st.header(f'New Plants!')
    st.image(get_image_path("antherium.jpg))
    st.write(f"This antherium plant has been back in my hometown, but now it is in Atlanta! This plant has liked a lot of light, so it enjoys my windowsill.")
    st.image("(get_image_path("pony palm.jpg)")
    st.write(f'This is a new plant that my mom bought and brought to me. It is a pony palm! It is very low maintenance and only needs to be watered once a month.')
with right:
    st.header(f'Original Plants!')
    st.image(get_image_path("propogations.jpeg"))
    st.write(f"These two bottles are propogations of my philodendron that I brought with me! My floormates and I are going to trade propogations. Propogating philodendrons is very easy")
    st.image("https://imgur.com/undefined")
    st.write(f"Not only did this plant come with me to college, it also is my oldest plant! I am unsure what it is, but it has grown a lot with me, so I think it's cool")
    st.image("https://imgur.com/cNLtir5")
    st.write(f'This is a part of my group of succulents! It is not looking healthy right now, so I did not take a picture of it. When a chain of hearts blooms, it sprouts little bulbs!')

