import streamlit as st
import time
import arxiv

st.title("📚 Simple Research Agent")

# Step 3a: User enters a research topic
query = st.text_input("Enter your research topic:")

# Step 3b: User selects number of papers to fetch
num_results = st.slider("Number of papers to fetch:", 1, 5, 3)

# Step 3c: When the user clicks search
if st.button("Search"):
    #st.info("Searching for papers...")

    #st.info("Searching for papers...")  # Show message in placeholder
    # Placeholder for info message
    placeholder = st.empty()
    placeholder.info("Searching for papers...")
    
    # Search papers on arXiv
    search = arxiv.Search(
        query=query,
        max_results=num_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    # Automatically remove the message after 3 seconds
    time.sleep(3)
    placeholder.empty()
    
    # Display results
    for paper in search.results():
        st.subheader(paper.title)
        st.write(paper.summary[:500] + "...")  # Show first 500 characters
        st.markdown(f"[Read Full Paper]({paper.entry_id})")
