import streamlit as st
from deta import Deta
import datetime
import os
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
cases_db = deta.Base("aijurist")


def delete_case(case_id):
    # Function to delete a specific case based on its ID
    cases_db.delete(case_id)

def render_title():
    st.markdown("""<button class="button">
  <span class="button-text" style='font-weight:bold'>&nbsp;PREDICTED CASES&nbsp</span>
  <span class="hover-text" aria-hidden="true" style='font-weight:bold'>&nbsp;PREDICTED CASES&nbsp</span>
</button>
""",
        unsafe_allow_html=True,
    )

def render_previous_predictions(email):
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
.expander-title {
            font-size: 18px;
            font-weight: bold;
        }
      
/* button styling */
.button {
  --border-right: 6px;
  --text-stroke-color: rgba(255,255,255,0.6);
  --animation-color:#205fff;
  --fs-size: 2em;
  letter-spacing: 2px;
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
    st.write("The Predicted Cases page showcases users' past predictions and their respective case details. Stay informed about your previous assessments for reference and analysis.")
    previous_cases_response = cases_db.fetch({"email": email})
    
    # Check if there are any cases in the response
    if not previous_cases_response.items:
        st.info("No previous predictions available.")
    else:
        sorted_cases = sorted(previous_cases_response.items, key=lambda x: x.get("prediction_datetime"), reverse=True)
        for idx, case in enumerate(sorted_cases):
            prediction_datetime_str = case.get("prediction_datetime")
            prediction_datetime = datetime.datetime.strptime(prediction_datetime_str, "%Y-%m-%d %H:%M:%S")
            prediction_date_time = prediction_datetime.strftime("%d/%m/%Y %I:%M %p")
            with st.expander(f"Case {idx+1} - {case['petitioner_name']} vs {case['respondent_name']} [{prediction_date_time}]"):
                st.write(f"**Case Description:** {case['case_scenario']}")
                st.write(f"**Legal Evidence:** {case['legal_evidence']}")
                st.write(f"**Prediction:** {case['prediction']*100:.2f}%")
                if st.button(f"Delete Case  {idx+1}"):
                    delete_case(case["key"])
                    st.success("Case successfully deleted.")
    # Add content for the previous predictions page here
    if (st.button("Delete All") and (not previous_cases_response.items)):
        with st.spinner("Deleting..."):
            for case in previous_cases_response.items: 
                delete_case(case["key"])
            st.success("All cases successfully deleted.")
    else:
            st.info("No cases to be deleted.")
