import streamlit as st
import requests

st.set_page_config(page_title="Ethical Consumer Chatbot", page_icon="💎")

st.title("💎 Ethical Consumer Chatbot")
st.subheader("Discover the values behind your favorite luxury brands")

brand_name = st.text_input("Enter a luxury brand name:")

BASE_URL = "http://127.0.0.1:5000"  # Local Flask server

if st.button("Get Brand Origin"):
    if brand_name:
        response = requests.get(f"{BASE_URL}/brand_origin", params={"brand": brand_name})
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Origin Story of {brand_name}:**")
            st.info(data.get("origin_story", "No origin story available."))
        else:
            st.error("Failed to retrieve origin story. Please try again.")
    else:
        st.warning("Please enter a brand name.")

if st.button("Get Full Brand Info"):
    if brand_name:
        response = requests.get(f"{BASE_URL}/brand_info", params={"brand": brand_name})
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Origin Story:**")
            st.info(data.get("origin_story", "No origin story available."))
            
            st.write(f"**Ethical Practices:**")
            st.success(data.get("ethical_practices", "No ethical information available."))
            
            if "sustainability_rating" in data:
                st.write(f"**Sustainability Rating:**")
                st.success(data.get("sustainability_rating", "No sustainability rating available."))
        else:
            st.error("Failed to retrieve brand info. Please try again.")
    else:
        st.warning("Please enter a brand name.")

st.markdown("---")
st.caption("Powered by Flask, OpenAI, and Streamlit")