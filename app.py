import streamlit as st
import pandas as pd
import base64
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import get_movie_data

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="ISMAGIMOVIES", layout="wide")

# --- CUSTOM CSS (Styles) ---

# --- CUSTOM CSS (Styles) ---
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@300;400;700&display=swap');

    /* Global Text Styles */
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Bebas Neue', cursive;
        letter-spacing: 2px;
    }

    /* Movie Card Styling */
    div[data-testid="column"] img {
        border-radius: 12px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    /* Hover Effect - The "Pop" */
    div[data-testid="column"] img:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(229, 9, 20, 0.6); /* Red Glow */
        cursor: pointer;
    }

    /* Button Styling to match the theme */
    div.stButton > button {
        background-color: #E50914; /* Netflix Red */
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: bold;
        transition: background-color 0.3s;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #b20710; /* Darker Red on hover */
    }

    /* Footer Styling */
    .footer {
        font-size: 0.8em;
        color: #888888;
        margin-top: 50px;
        text-align: center;
        border-top: 1px solid #333;
        padding-top: 20px;
    }
</style>
""", unsafe_allow_html=True)


# --- LOAD DATA ---
df = get_movie_data()

# --- RECOMMENDATION LOGIC ---
def recommend(movie_title):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(df['tags']).toarray()
    similarity = cosine_similarity(vectors)
    movie_index = df[df['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]
    
    recs = []
    for i in movies_list:
        movie_id = i[0]
        recs.append(df.iloc[movie_id])
    return recs

# --- APP NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_movie' not in st.session_state:
    st.session_state.selected_movie = None

def go_home():
    st.session_state.page = 'home'
    st.session_state.selected_movie = None

def show_details(movie_title):
    st.session_state.page = 'details'
    st.session_state.selected_movie = movie_title

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 🍿 ISMAGIMOVIES")
    if st.button("🏠 Home"):
        go_home()
    
    st.markdown("---")
    st.markdown("### Search")
    search_query = st.selectbox("Find a movie", [""] + list(df['title'].values))
    if search_query:
        show_details(search_query)

    # --- GROUP FOOTER ---
    st.markdown("<br><br><br>", unsafe_allow_html=True) # Adds some space
    st.markdown("---")
    st.markdown("""
    <div class='footer'>
    © All rights reserved by:<br>
    Haitam Louastri<br>
    Ibrahima Bamba<br>
    Othman Drif
    </div>
    """, unsafe_allow_html=True)

# --- MAIN CONTENT ---

# >>> VIEW 1: HOME PAGE <<<
# >>> VIEW 1: HOME PAGE <<<
if st.session_state.page == 'home':
    
    # --- IMAGE FUNCTION ---
    def get_base64_image(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except FileNotFoundError:
            return ""

    # --- SLIDESHOW LOGIC ---
    if 'slide_index' not in st.session_state:
        st.session_state.slide_index = 0

    slider_movies = df.head(5)
    current_index = st.session_state.slide_index % len(slider_movies)
    featured_movie = slider_movies.iloc[current_index]

    # IMAGE PROCESSING
    img_path = featured_movie['image']
    if "http" not in img_path:
        b64_img = get_base64_image(img_path)
        img_url = f"data:image/jpeg;base64,{b64_img}"
    else:
        img_url = img_path

    # --- DISPLAY SLIDE (HTML FLUSHED LEFT) ---
    
    st.markdown(f"""
<div style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url('{img_url}'); background-size: cover; background-position: center; padding: 60px; border-radius: 15px; margin-bottom: 20px; text-align: center; border: 1px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5); color: white;">
<h1 style="font-size: 4em; font-weight: bold; text-shadow: 2px 2px 10px #000; margin-bottom: 10px;">{featured_movie['title']}</h1>
<p style="font-size: 1.3em; max-width: 800px; margin: 0 auto; line-height: 1.5; text-shadow: 1px 1px 5px #000;">{featured_movie['description']}</p>
<div style="margin-top: 30px;">
<span style="background-color: #E50914; color: white; padding: 8px 15px; border-radius: 5px; font-weight: bold; margin-right: 10px;">{featured_movie['genre']}</span>
<span style="background-color: rgba(255,255,255,0.2); color: #fff; padding: 8px 15px; border-radius: 5px; font-weight: bold; backdrop-filter: blur(5px);">⭐ {featured_movie['rating']}</span>
</div>
</div>
""", unsafe_allow_html=True)

    # --- NAVIGATION BUTTONS ---
    col_prev, col_spacer, col_next = st.columns([1, 6, 1])

    with col_prev:
        if st.button("◀", use_container_width=True):
            st.session_state.slide_index -= 1
            st.rerun()

    with col_next:
        if st.button("▶", use_container_width=True):
            st.session_state.slide_index += 1
            st.rerun()

    # --- MOVIE GRID ---
    st.markdown("---")
    st.markdown('<p class="big-title">Trending Now</p>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    for index, row in df.iterrows():
        col = cols[index % 4]
        with col:
            st.image(row['image'], use_container_width=True)
            st.markdown(f"**{row['rating']}**")
            if st.button(f"Watch {row['title']}", key=row['id']):
                show_details(row['title'])
                st.rerun()

# >>> VIEW 2: DETAILS PAGE <<<
elif st.session_state.page == 'details':
    movie = df[df['title'] == st.session_state.selected_movie].iloc[0]
    
    if st.button("← Back to Home"):
        go_home()
        st.rerun()
    
    st.markdown(f'<h1 style="font-size:3em;">{movie["title"]}</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(movie['image'], use_container_width=True)
    with col2:
        st.subheader("Overview")
        st.write(movie['description'])
        st.markdown(f"**Genre:** {movie['genre']}")
        st.markdown(f"**Tags:** {movie['tags']}")
        st.button("▶ Play Movie")
    
    st.markdown("---")
    st.subheader("You might also like:")
    
    recommendations = recommend(movie['title'])
    
    r_cols = st.columns(3)
    for idx, rec in enumerate(recommendations):
        with r_cols[idx]:
            st.image(rec['image']
            
            
            
            , use_container_width=True)
            st.markdown(f"**{rec['title']}**")
            if st.button(f"View {rec['title']}", key=f"rec_{idx}"):
                show_details(rec['title'])
                st.rerun()