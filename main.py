#selenium - allows us to automate web browser so we can actually navigate to a webpage 
#         - we can grab all the content thats on that page then we could do filtering on it
#         - and pass it to llm (chatgpt)

import streamlit as st

from scrape import scrape_website

st.title("AI Web Scrapper")
url = st.text_input("Enter a Webste URL: ")

if st.button("Scrape Site"):
    st.write("Scrapping the website")
    result = scrape_website(url)
    print(result)