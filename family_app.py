import streamlit as st
import pandas as pd
import datetime
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Family Website", layout="wide")

st.title("👨‍👩‍👧‍👦 Welcome to Our Family Website")

# Simulated storage (in production, use a database or persistent backend)
if "birthdays" not in st.session_state:
    st.session_state.birthdays = []

if "recipes" not in st.session_state:
    st.session_state.recipes = []

if "blog_posts" not in st.session_state:
    st.session_state.blog_posts = []

if "achievements" not in st.session_state:
    st.session_state.achievements = []

if "locations" not in st.session_state:
    st.session_state.locations = []

# Sidebar Navigation
page = st.sidebar.selectbox("Go to", [
    "📜 About the Family",
    "👨‍👩‍👧‍👦 Add Yourself to Family Tree",
    "🗓️ Add Birthday/Anniversary",
    "📷 Photo Gallery Upload",
    "📝 Write a Blog Update",
    "🧾 Share a Recipe",
    "🏆 Share Achievement",
    "📍 Share Your Location",
    "🎥 Upload a Video"
])

# Sections
if page == "📜 About the Family":
    st.header("📜 About the Family")
    st.write("Welcome! Submit your details to help us build this digital home together.")

elif page == "👨‍👩‍👧‍👦 Add Yourself to Family Tree":
    st.header("👨‍👩‍👧‍👦 Add Yourself")
    name = st.text_input("Your Full Name")
    relation = st.text_input("Your relation (e.g., Son, Uncle, Cousin)")
    bio = st.text_area("Short bio or fun fact")
    if st.button("Submit to Tree"):
        st.success(f"Thanks {name}, your info has been added!")

elif page == "🗓️ Add Birthday/Anniversary":
    st.header("🗓️ Add Birthday or Anniversary")
    name = st.text_input("Name")
    event_type = st.selectbox("Event Type", ["Birthday", "Anniversary"])
    date = st.date_input("Date")
    if st.button("Submit Event"):
        st.session_state.birthdays.append({"Name": name, "Event": event_type, "Date": date})
        st.success("Event added successfully!")
    if st.session_state.birthdays:
        st.subheader("Submitted Events")
        st.dataframe(pd.DataFrame(st.session_state.birthdays))

elif page == "📷 Photo Gallery Upload":
    st.header("📷 Upload Family Photos")
    photos = st.file_uploader("Upload photos", type=["jpg", "png"], accept_multiple_files=True)
    if photos:
        for photo in photos:
            st.image(photo, width=300)

elif page == "📝 Write a Blog Update":
    st.header("📝 Family Blog")
    author = st.text_input("Your Name")
    content = st.text_area("What's the update?")
    if st.button("Post Blog"):
        st.session_state.blog_posts.append({"Author": author, "Content": content})
        st.success("Blog posted!")
    if st.session_state.blog_posts:
        st.subheader("Recent Posts")
        for post in st.session_state.blog_posts:
            st.write(f"**{post['Author']}**: {post['Content']}")

elif page == "🧾 Share a Recipe":
    st.header("🧾 Submit a Family Recipe")
    recipe_name = st.text_input("Recipe Name")
    recipe_desc = st.text_area("How to make it?")
    if st.button("Add Recipe"):
        st.session_state.recipes.append({"Recipe": recipe_name, "Instructions": recipe_desc})
        st.success("Recipe submitted!")
    if st.session_state.recipes:
        st.subheader("Family Recipes")
        for recipe in st.session_state.recipes:
            st.markdown(f"**{recipe['Recipe']}**")
            st.markdown(f"{recipe['Instructions']}")

elif page == "🏆 Share Achievement":
    st.header("🏆 Share a Milestone")
    name = st.text_input("Name")
    description = st.text_area("Describe the achievement")
    if st.button("Add Achievement"):
        st.session_state.achievements.append({"Name": name, "Achievement": description})
        st.success("Achievement added!")
    if st.session_state.achievements:
        st.subheader("Family Achievements")
        for item in st.session_state.achievements:
            st.markdown(f"**{item['Name']}** - {item['Achievement']}")

elif page == "📍 Share Your Location":
    st.header("📍 Where Do You Live?")
    name = st.text_input("Your Name")
    city = st.text_input("City")
    lat = st.number_input("Latitude", format="%.6f")
    lon = st.number_input("Longitude", format="%.6f")
    if st.button("Submit Location"):
        st.session_state.locations.append({"Name": name, "City": city, "Lat": lat, "Lon": lon})
        st.success("Location submitted!")

    if st.session_state.locations:
        st.subheader("Family Map")
        map = folium.Map(location=[20.0, 80.0], zoom_start=2)
        for loc in st.session_state.locations:
            folium.Marker(location=[loc["Lat"], loc["Lon"]], popup=f"{loc['Name']} - {loc['City']}").add_to(map)
        st_folium(map, width=700)

elif page == "🎥 Upload a Video":
    st.header("🎥 Upload Family Videos")
    videos = st.file_uploader("Upload videos", type=["mp4", "mov"], accept_multiple_files=True)
    for vid in videos:
        st.video(vid)
