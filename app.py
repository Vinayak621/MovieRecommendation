import streamlit as st
import pickle
import pandas as pd
import requests

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
    rm=[]
    rm_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        rm.append(movies.iloc[i[0]].title)
        rm_poster.append((fetch_poster(movie_id)))
    return rm,rm_poster

def fetch_poster(movie_id):
        response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e3cb933a85ccf2a04f49aec9efc0d167&language=en-US'.format(movie_id))
        data=response.json()
        print(data)
        return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
st.title("movie recommendation system")
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
selected_movie_name=st.selectbox('how would you like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])    
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])        
            