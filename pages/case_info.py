import streamlit as st
import pandas as pd

def render_title():
    st.markdown("""<button class="button">
  <span class="button-text" style='font-weight:bold'>&nbsp;Case Overview&nbsp</span>
  <span class="hover-text" aria-hidden="true" style='font-weight:bold'>&nbsp;Case&nbsp;Overview&nbsp</span>
</button>
""",
        unsafe_allow_html=True,
    )

# Function to find similar cases (replace this with your AI model or database query)
def find_similar_cases(case_name):
    # Replace this with your actual logic to find similar cases
    # For demonstration, we are using a sample dataframe
    cases_data = {
        'Case Name': ['Case 1', 'Case 2', 'Case 3'],
        'Date': ['2022-01-15', '2022-03-10', '2022-05-20'],
        'Court': ['Supreme Court', 'District Court', 'High Court'],
        'Keywords': [['crime', 'robbery'], ['contract', 'breach'], ['employment', 'discrimination']],
    }
    cases_df = pd.DataFrame(cases_data)
    return cases_df

# Function to display individual case cards as expanders
def display_case_card(case):
    with st.expander(f"Case ID: {case['Case Name']}"):
        st.write("Date:", case['Date'])
        st.write("Court:", case['Court'])
        st.write("Keywords:", ", ".join(case['Keywords']))

def render_case_info():
    render_title()
    case_text ="""<style>
/* === removing default button style ===*/
/* === removing default button style ===*/
.button {
  margin: 0;
  height: auto;
  background: transparent;
  padding: 0;
  border: none;
}

/* button styling */
.button {
  --border-right: 6px;
  --text-stroke-color: rgba(255,255,255,0.6);
  --animation-color:#205fff;
  --fs-size: 2em;
  letter-spacing: 3px;
  text-decoration: none;
  font-size: var(--fs-size);
  font-family: "Arial";
  position: relative;
  text-transform: uppercase;
  color: transparent;
  -webkit-text-stroke: 1px var(--text-stroke-color);
}
/* this is the text, when you hover on button */
.hover-text {
  position: absolute;
  box-sizing: border-box;
  content: attr(data-text);
  color: var(--animation-color);
  width: 0%;
  inset: 0;
  border-right: var(--border-right) solid var(--animation-color);
  overflow: hidden;
  transition: 1.5s;
  -webkit-text-stroke: 1px var(--animation-color);
}
/* hover */
.button:hover .hover-text {
  width: 100%;
  filter: drop-shadow(0 0 23px var(--animation-color))
}

</style>
"""   
    st.markdown(case_text, unsafe_allow_html=True)
    st.write("Welcome to the AI Jurist Predictor! Utilizing historical data from similar cases, our advanced machine learning model provides precise predictions for your legal proceedings.")
    col1, coln, col2 = st.columns([2, 0.2, 1])   
    with coln:
        st.empty()
    with col1:
        case_name = st.text_area("Enter Case Description:", height=280)
        search_button = st.button("Find Similar Cases")
    with col2:
        st.image("assets/_Create a neon  1.png", width=370)  
    if search_button:
        # Call your AI model or database to find similar cases
        similar_cases = find_similar_cases(case_name)
        st.info("Data-driven enhancements being integrated: This is just an example of how this page will work")
        # Display search results
        st.header("Similar Cases:")
        if similar_cases.empty:
            st.warning("No similar cases found.")
        else:
            for idx, case in similar_cases.iterrows():
                display_case_card(case)
        vert_space = '<div style="padding: 45px 5px;"></div>'
        st.markdown(vert_space, unsafe_allow_html=True)
        st.write("The Cases Overview page serves as an informative platform to input case details and explore similar cases that have taken place in the past. However, it does not offer legal advice or representation. The presented results are based on statistical patterns in legal data and may not accurately predict specific legal outcomes. For tailored legal advice and representation, it is advisable to seek counsel from qualified legal professionals.")
