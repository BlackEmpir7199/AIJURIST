import streamlit as st
import time
from deta import Deta
import datetime
import case_info 
from colors import color_bb
import os
from dotenv import load_dotenv



load_dotenv()
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
cases_db = deta.Base("aijurist")

def scrollDown():
   scroll= '''
    <script>
    window.scroll({
  bottom: 100,
  left: 100,
  behavior: "smooth",
})
</script>
'''
   st.markdown(scroll, unsafe_allow_html=True)

def render_title():
    st.markdown(
        f"""<button data-text="Awesome" class="button">
    <span class="actual-text" style='font-weight:bold'>&nbsp;PREDICTOR&nbsp;</span>
    <span class="hover-text" aria-hidden="true" style='font-weight:bold'>&nbsp;PREDICTOR&nbsp;</span>
</button>""",
        unsafe_allow_html=True,
    )


def get_color_for_percentage(percentage):
    if percentage < 30:
        return "#FF0000"
    elif 30 <= percentage < 50:
        return "#FF8C00"
    elif 50 <= percentage < 75:
        return "#FFD700"
    else:
        return "#32CD32"
    
def predict_case(case_scenario,petitioner_name,respondent_name,legal_evidence,email):
    # Replace this with your actual machine learning model prediction logic
    prediction = 0.95
    prediction_datetime = datetime.datetime.now()
    prediction_datetime_str = prediction_datetime.strftime("%Y-%m-%d %H:%M:%S") 
    case_data = {
        "case_scenario": case_scenario,
        "petitioner_name": petitioner_name,
        "respondent_name": respondent_name,
        "legal_evidence": legal_evidence,
        "prediction": prediction,
        "prediction_datetime": prediction_datetime_str,
        "email":email
    }
    cases_db.put(case_data)
    progress_bar = st.progress(0)
    text_placeholder = st.empty()   
    for i in range(101):
        progress_bar.progress(i)
        time.sleep(0.05)
        text_placeholder.write(f"Progress: {i}%")
    return prediction

def render_predictor_page(email):
    render_title()
    title_text ="""<style>
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
    st.markdown(title_text, unsafe_allow_html=True)
    st.write("Welcome to the AI Jurist Predictor! Please enter your case scenario below, and our advanced machine learning model will predict the chances of winning the case.")
    col1,col2=st.columns([1,1])
    with col2:
        case_scenario= st.text_area("Case Description:",height=287)
        
    with col1:
        first_party = st.text_input(label="Petitioner's Name:")
        second_party = st.text_input(label="Respondent's Name:")
        #vert_space = '<div style="padding: 10px 5px;"></div>'
        evidence = st.text_area("Legal Evidence:",height=1)  
        
    col4,coln,col5=st.columns([1,0.25,1])   
    with coln:
        st.empty()    
    with col4:
            predict_btn=st.button("Predict",on_click=scrollDown())
            if predict_btn:
                if first_party.strip() == "":
                    st.error(body="Please enter a Petitioner Name")
                elif second_party.strip()=="":
                    st.error(body="Please enter a Respondent Name")
                elif case_scenario.strip() == "":
                    st.error(body="Please enter a Case Description")
                else:
                    prediction = predict_case(case_scenario,first_party,second_party,evidence,email)
            # Display the prediction outcome
                    prediction_percentage = f"{prediction * 100:.2f}%"
                    color = get_color_for_percentage(prediction * 100)
                    highlighted_text = f"<p style='font-size: 24px;'>Based on the provided case description, our AI Jurist predicts that you have a <p style='font-size: 24px; color: {color};'>{prediction_percentage}</p><p style='font-size: 24px;'> chance of winning the case.</p></p>"
                    st.markdown(highlighted_text, unsafe_allow_html=True)

            # Disclaimer
                    vert_space = '<div style="padding: 45px 5px;"></div>'
                    st.markdown(vert_space, unsafe_allow_html=True)
                    st.write("Disclaimer: The prediction provided by our AI Jurist is based on statistical patterns in legal data and should be considered as an informed opinion rather than professional legal advice. Legal outcomes can be influenced by various factors, and we recommend consulting with a qualified legal professional for personalized advice and representation.")    

    
    with  col5:
        vert_space = '<div style="padding: 12px 5px;"></div>'
        st.markdown(vert_space, unsafe_allow_html=True)
        st.image("assets/_Craft an image 1.png",width=375)
 
