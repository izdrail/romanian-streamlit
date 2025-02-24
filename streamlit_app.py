import spacy_streamlit
import streamlit as st
models = ["ro_core_news_lg"]
default_text = "Ghinionul pare să urmărească trenurile care circulă pe ruta Roșiori-Radomirești din sudul țării, unde trei incidente au avut loc, în doar câteva zile. Primul, la începutul săptămânii, când un tren cu 89 de pasageri a fost cuprins de flăcări și evacuat de urgență. Două zile mai târziu, un om a murit după ce două garnituri private de marfă s-au ciocnit. Și, tot pe aceeași rută, ieri dimineață s-a stricat o locomotivă, iar oamenii au fost nevoiți să aștepte zeci de minute în ger."
spacy_streamlit.visualize(models, default_text)

