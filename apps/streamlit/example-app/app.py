import streamlit as st

st.set_page_config(
    page_title="Example App",
    page_icon="📊",
    layout="wide",
)

st.title("Example App")
st.write("Welcome to your Streamlit app. Edit this file to get started.")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Metric A", value="123", delta="4.5%")
with col2:
    st.metric(label="Metric B", value="456", delta="-2.1%")
with col3:
    st.metric(label="Metric C", value="789", delta="1.0%")
