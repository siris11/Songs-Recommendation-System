import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit.components.v1 as components
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "3def5f6debbc4c109d2b78dd3e882151"
CLIENT_SECRET = "a6c505b412164288849082ab6b277d8e"



# Initalize the spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret= CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager= client_credentials_manager)


def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


def recommend(song):
    index = music[music['song']== song].index[0]
    dist = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in dist[1:10]:
        #fetching the movie poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names,recommended_music_posters



# --- LINKS FOR REQUIRED ANIMATION AND IMAGES ---

# animation html scripts
spotify_animation_html = """
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="https://assets10.lottiefiles.com/packages/lf20_a6hjf7nd.json"  background="transparent"  speed="1"  style="width: 105px; height: 105px;"  loop  autoplay></lottie-player> """
astro_animation_html = """
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="https://assets4.lottiefiles.com/packages/lf20_euaveaxu.json"  background="transparent"  speed="1"  style="width: 170px; height: 160px;"  loop  autoplay></lottie-player> """

# Title and intro Heading
heading_animation = "<p style = 'font-size: 40px;'><b>Spotify Music Recommendation System</b></p>"

# --- HEADING SECTION ---

with st.container():
    left_col, right_col = st.columns([1, 8])
    with left_col:
        components.html(spotify_animation_html)
    with right_col:
        st.markdown(heading_animation, unsafe_allow_html=True)
music = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

song_list = music['song'].values
selected_song = st.selectbox("Pick your favourite songs🎵",
                             song_list)


if st.button('Confirm Selection'):
    recommended_music_names,recommended_music_posters = recommend(selected_song)
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col1:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
    with col2:
        st.text(recommended_music_names[5])
        st.image(recommended_music_posters[5])
    with col3:
        st.text(recommended_music_names[6])
        st.image(recommended_music_posters[6])
    with col4:
        st.text(recommended_music_names[7])
        st.image(recommended_music_posters[7])

    
# ---------------------------------------------------------------------------------------------- #
# --- CONTACT FORM & SOCIAL LINKS ---
# static images
spotify_logo = "https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png"
casette = 'https://www.scdn.co/i/500/cassette.svg'

st.markdown("""---""")

contact_form = """
<form action="https://formsubmit.co/sirisure10@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea><br>
     <button type="submit">Send</button>
</form>"""

with st.container():
    left_col, right_col = st.columns([6, 4])
    with left_col:
        st.header(":mailbox: Get In Touch With Me!")
        st.markdown("""<p style = 'font-size: 20px;'>Social Links : <a href='https://www.instagram.com/illogical.apple/', target='_blank'><img width="48" height="48" src="https://img.icons8.com/fluency/48/instagram-new.png" alt="instagram-new"/></a>
        <a href='https://www.linkedin.com/in/sirisure2004/' target='_blank'><img width="48" height="48" src="https://img.icons8.com/color/48/linkedin.png" alt="linkedin"/></a>
        <a target='_blank' href='https://github.com/siris11/'><img width="48" height="48" src="https://img.icons8.com/sf-regular-filled/48/FFFFFF/github.png" alt="github"/></a>
        <a target='_blank' href='mailto:sirisure10@gmail.com'><img width="48" height="48" src="https://img.icons8.com/fluency/48/gmail.png" alt="gmail"/></a>
        """, unsafe_allow_html=True)
        st.markdown(contact_form, unsafe_allow_html=True)
        
    with right_col:
        st.image(casette, use_column_width = True)
        st.markdown("""<p align='right' style = 'font-size: 20px;'>Thanks For Visiting ! </p>""", unsafe_allow_html=True)

st.markdown("""
<style>
input[type=text],
input[type=email],
textarea {
    width: 80%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical 
	}

button[type=submit] {
    background-color: #1DDA63;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
	}
button[type=submit]:hover {
    background-color: #ffffff
    color: black;
	}
</style>""", unsafe_allow_html=True)
#-----------------------------------------------------------------------------------------------------
# ----- Footer -----
footer = """<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #000000;
    color: black;
    text-align: center;
	}
</style>
<div class="footer">
<font color = 'white'>Developed with ❤ by Siri</font>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
