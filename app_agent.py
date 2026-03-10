import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Credit Risk Agent", layout="wide")

st.title("Credit Risk Monitoring Agent")

st.markdown("Ask questions about customer risk, drift, or portfolio health.")

query = st.text_area("Enter your query")

if st.button("Run Agent"):
    if query.strip():
        with st.spinner("Analyzing risk..."):
            response = run_agent(query)
        st.success("Analysis Complete")
        st.write(response)
    else:
        st.warning("Please enter a query.")