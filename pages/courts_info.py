import streamlit as st
import sys
sys.path.append("simpledata")
from courtdata import high_courts
from courtdata import district_courts
from colors import color_bb


def render_title():
    st.markdown("""<button class="button">
  <span class="button-text" style='font-weight:bold'>&nbsp;Courts Information&nbsp</span>
  <span class="hover-text" aria-hidden="true" style='font-weight:bold'>&nbsp;Courts Information&nbsp</span>
</button>
""",
        unsafe_allow_html=True,
    )

def show_supreme_court_details():
    title_text=f"<p style='font-family:Monospace ;font-size:38px; color:#ff0d5e; text-align:top;'>Supreme Court of India</p>"
    st.markdown(title_text, unsafe_allow_html=True)
    supreme_court = {
    "establishment_date": "January 28, 1950",
    "place": "New Delhi, India",
    "description": "The Supreme Court of India is the highest judicial authority in the country and is located in New Delhi. It was established on January 28, 1950, and serves as the final court of appeal and the highest constitutional court in India. The Supreme Court exercises original, appellate, and advisory jurisdiction. As an apex court, it hears appeals against the judgments of high courts and ensures the uniform interpretation and application of laws across the country.The Supreme Court comprises the Chief Justice of India and a fixed number of judges, as determined by Parliament. It has the power of judicial review, allowing it to examine the constitutionality of laws and executive actions. The decisions of the Supreme Court set legal precedents that guide lower courts and various authorities. It plays a crucial role in upholding the fundamental rights and liberties of citizens, ensuring justice"}
    st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top; font-weight:bold'>Establishment Date:</span> {supreme_court['establishment_date']}</span>",unsafe_allow_html=True)
    st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top; font-weight:bold'>Place:</span> {supreme_court['place']}</span>",unsafe_allow_html=True)
    st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top; font-weight:bold'>Description:</span> {supreme_court['description']}</span>",unsafe_allow_html=True)



def show_high_courts_list():
    title_text=f"<p style='font-family:Monospace ;font-size:38px; color:#fc53fc; text-align:top;'>High Courts in India</p>"
    st.markdown(title_text, unsafe_allow_html=True)
    st.write("India has High Courts in each state and union territory. The High Courts "
             "exercise jurisdiction over their respective state or union territory and "
             "serve as the highest judicial authority at the state level. Click on any "
             "High Court below to learn more about it.")
    
    # Display buttons for each High Court
    selected_high_court = st.selectbox("Select a High Court", list(high_courts.keys()))
    def show_high_court_details(selected_high_court):
       st.markdown(f"<p style='font-family:Monospace ;font-size:25px; color:#fc53fc; text-align:top;'>{selected_high_court} Court Details</p>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>High Court Name:</span> {high_courts[selected_high_court]['name']}</span>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>Establishment Date:</span> {high_courts[selected_high_court]['establishment_date']}</span>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>Place:</span> {high_courts[selected_high_court]['place']}</span>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>Description:</span> {high_courts[selected_high_court]['description']}</span>",unsafe_allow_html=True)

# Show Details button for High Courts
    if st.button("Show Details"):
       show_high_court_details(selected_high_court)



def show_district_courts_list():
    title_text=f"<p style='font-family:Monospace ;font-size:38px; color:#f34c20; text-align:top;'>District Courts in India</p>"
    st.markdown(title_text, unsafe_allow_html=True)
    st.write("Each district in India typically has its own district court, also known as the "
             "Principal Civil Court of Original Jurisdiction. District courts handle civil and "
             "criminal cases within their territorial jurisdiction. Click on any district court "
             "below to learn more about it.")

    # Display buttons for each District Court
    selected_district_court = st.selectbox("Select a District Court", list(district_courts.keys()))
    def show_district_court_details(selected_district_court):
       st.markdown(f"<p style='font-family:Monospace ;font-size:25px; color:#fc53fc; text-align:top;'>{selected_district_court} Court Details</p>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>High Court Name:</span> {district_courts[selected_district_court]['name']}</span>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>Establishment Date:</span> {district_courts[selected_district_court]['establishment_date']}</span>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>Place:</span> {district_courts[selected_district_court]['place']}</span>",unsafe_allow_html=True)
       st.markdown(f"<span style='font-size:20px;'><span style='font-family:Monospace ;font-size:20px; color:{color_bb}; text-align:top;'>Description:</span> {district_courts[selected_district_court]['description']}</span>",unsafe_allow_html=True)
    # Show Details button for District Courts
    if st.button("Show Details"):
        show_district_court_details(selected_district_court)

def render_courts_info():
    render_title()
    vert_space = '<div style="padding: 8px 2px;"></div>'
    st.markdown(vert_space, unsafe_allow_html=True)
    court_text ="""<style>
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
  --animation-color:#37c4ff;
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
    st.markdown(court_text, unsafe_allow_html=True)
    st.write("Discover valuable information about various courts, including jurisdiction, historical background, and notable cases, on our Courts Information page.")
    # Show three label buttons
    col1,col2,col3=st.columns([1,1,1])
    if "supreme_court_button_state" not in st.session_state:
        st.session_state.supreme_court_button_state = False

    if "high_court_button_state" not in st.session_state:
        st.session_state.high_court_button_state = False

    if "district_court_button_state" not in st.session_state:
        st.session_state.district_court_button_state = False
    supreme_court_button_state = st.session_state.get("supreme_court_button_state", False)
    high_court_button_state = st.session_state.get("high_court_button_state", False)
    district_court_button_state = st.session_state.get("district_court_button_state", False)

    # Handle button clicks and show details accordingly
    with col1:
        if st.button("Supreme Court"):
            st.session_state.supreme_court_button_state = not supreme_court_button_state
            if supreme_court_button_state:
                st.session_state.high_court_button_state = False
                st.session_state.district_court_button_state = False
    with col2:
        if st.button("High Courts"):
            st.session_state.high_court_button_state = not high_court_button_state
            if high_court_button_state:
                st.session_state.supreme_court_button_state = False
                st.session_state.district_court_button_state = False
    with col3:
        if st.button("District Courts"):
            st.session_state.district_court_button_state = not district_court_button_state
            if district_court_button_state:
                st.session_state.supreme_court_button_state = False
                st.session_state.high_court_button_state = False
    
    col4,col5=st.columns([2,1])
    # Show court details based on the selected button
    def show_court_image(court_image):
        with col5:
           vert_space = '<div style="padding: 40px 5px;"></div>'
           st.markdown(vert_space,unsafe_allow_html=True)
           st.image(court_image,width=435)

    with col4:
       if st.session_state.supreme_court_button_state:
           show_court_image("assets/_Visualize a di 2.png")
           show_supreme_court_details()
           vert_space = '<div style="padding: 30px 5px;"></div>'
           st.markdown(vert_space,unsafe_allow_html=True)
           st.write("Disclaimer: The information provided about the Supreme Courts is intended for general informational purposes only. It does not constitute legal advice or representation. For specific legal matters, always consult with qualified legal professionals.")
       elif st.session_state.high_court_button_state:
           show_court_image("assets/_Visualize a di 1.png")
           show_high_courts_list()
           vert_space = '<div style="padding: 30px 5px;"></div>'
           st.markdown(vert_space,unsafe_allow_html=True)
           st.write("Disclaimer: The information presented regarding High Courts is intended to be informative and educational in nature. It should not be construed as legal advice or a substitute for professional legal counsel. Seek advice from qualified legal experts for individualized legal concerns.")
       elif st.session_state.district_court_button_state:
           show_court_image("assets/small judicial  1.png")
           show_district_courts_list()
           vert_space = '<div style="padding: 30px 5px;"></div>'
           st.markdown(vert_space,unsafe_allow_html=True)
           st.write("Disclaimer: The information pertaining to District Courts is for general knowledge and reference only. It is not meant to be a substitute for legal advice or guidance. Please be aware that there are 672 district courts, and this information highlights only significant courts. For specific legal issues, consult with a qualified lawyer or legal professional.")





