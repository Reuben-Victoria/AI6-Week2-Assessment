import streamlit as st
from quotes import scrape_quotes  

st.title("Quotes Scraper with Generator")

st.write("Streaming quotes from **quotes.toscrape.com**...")

# Stream and display quotes
for q in scrape_quotes():
    st.write(f"**{q['quote']}** — {q['author']}")
