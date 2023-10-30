import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

#load save model

model_sentiment = pickle.load(open('model_sentiment.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf_idf.sav","rb"))))

#title

st.title ('Prediksi Sentiment Komentar')

clean_teks = st.text_input("Masukkan Komentar")

sentiment_detection = ''

if st.button('Hasil Deteksi'):
    predict_sentiment = model_sentiment.predict(loaded_vec.fit_transform([clean_teks]))
    
    if (predict_sentiment == 1):
        sentiment_detection = 'Sentiment Positif'
    elif (predict_sentiment == 0):
        sentiment_detection = 'Sentiment Negatif'
    else :
        sentiment_detection = 'Sentiment Netral'
st.success(sentiment_detection)