import streamlit as st
from deta import Deta
from predictor import render_predictor_page
from previous_predictions import render_previous_predictions
from case_info import render_case_info
from courts_info import render_courts_info
from signlogin import render_login_page
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os 

load_dotenv()
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
users_db = deta.Base("users")

email = ""


if "email" not in st.session_state:
    st.session_state.email = ""
    
def get_username_by_email(email):
    existing_users = users_db.fetch({"email": email})
    return existing_users.items[0]['username'] if existing_users.items else None



def status_shower(email,username,status):
    text = f"""<button id="btn-message" class="button-message">
	<div class="content-avatar">
		<div class="status-user"></div>
		<div class="avatar">
			<svg class="user-img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12,12.5c-3.04,0-5.5,1.73-5.5,3.5s2.46,3.5,5.5,3.5,5.5-1.73,5.5-3.5-2.46-3.5-5.5-3.5Zm0-.5c1.66,0,3-1.34,3-3s-1.34-3-3-3-3,1.34-3,3,1.34,3,3,3Z"></path></svg>
		</div>
	</div>
	<div class="notice-content">
		<div class="username">{username}</div>
		<div class="lable-message">{status}<span class="number-message"></span></div>
		<div class="user-id">{email}</div>
	</div>
</button>"""
    if status=="Logged in":
        online_status="#00da00"
    else:
        online_status="#880808"

    css = """<style>
    #btn-message {
  --text-color: rgb(255, 255, 255);
  --bg-color-sup: #5e5e5e;
  --bg-color: #2b2b2b;
  --bg-hover-color: #161616;
  --online-status: {online_status};
  --font-size: 16px;
  --btn-transition: all 0.2s ease-out;
}

.button-message {
  display: flex;
  justify-content: center;
  align-items: center;
  font: 400 var(--font-size) Helvetica Neue, sans-serif;
  box-shadow: 0 0 2.17382px rgba(0,0,0,.049),0 1.75px 6.01034px rgba(0,0,0,.07),0 3.63px 14.4706px rgba(0,0,0,.091),0 22px 48px rgba(0,0,0,.14);
  background-color: var(--bg-color);
  border-radius: 68px;
  cursor: pointer;
  padding: 6px 10px 6px 6px;
  width: fit-content;
  height: 40px;
  border: 0;
  margin: 10px 10px 10px 60px;
  overflow: hidden;
  position: relative;
  transition: var(--btn-transition);
}

.button-message:hover {
  height: 48px;
  padding: 8px 20px 8px 8px;
  background-color: var(--bg-hover-color);
  transition: var(--btn-transition);
}

.button-message:active {
  transform: scale(0.99);
}

.content-avatar {
  width: 30px;
  height: 30px;
  margin: 0;
  transition: var(--btn-transition);
  position: relative;
}

.button-message:hover .content-avatar {
  width: 40px;
  height: 40px;
}

.avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  background-color: var(--bg-color-sup);
}

.user-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.status-user {
  position: absolute;
  width: 6px;
  height: 6px;
  right: 1px;
  bottom: 1px;
  border-radius: 50%;
  outline: solid 2px var(--bg-color);
  background-color: var({online_status});
  transition: var(--btn-transition);
  animation: active-status 2s ease-in-out infinite;
}

.button-message:hover .status-user {
  width: 10px;
  height: 10px;
  right: 1px;
  bottom: 1px;
  outline: solid 3px var(--bg-hover-color);
}

.notice-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  padding-left: 8px;
  text-align: initial;
  color: var(--text-color);
}

.username {
  letter-spacing: -6px;
  height: 0;
  opacity: 0;
  transform: translateY(-20px);
  transition: var(--btn-transition);
}

.user-id {
  font-size: 12px;
  letter-spacing: -6px;
  height: 0;
  opacity: 0;
  transform: translateY(10px);
  transition: var(--btn-transition);
}

.lable-message {
  display: flex;
  align-items: center;
  opacity: 1;
  transform: scaleY(1);
  transition: var(--btn-transition);
}

.button-message:hover .username {
  height: auto;
  letter-spacing: normal;
  opacity: 1;
  transform: translateY(0);
  transition: var(--btn-transition);
}

.button-message:hover .user-id {
  height: auto;
  letter-spacing: normal;
  opacity: 1;
  transform: translateY(0);
  transition: var(--btn-transition);
}

.button-message:hover .lable-message {
  height: 0;
  transform: scaleY(0);
  transition: var(--btn-transition);
}

.lable-message, .username {
  font-weight: 600;
}

.number-message {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin-left: 8px;
  font-size: 12px;
  width: 16px;
  height: 16px;
  background-color: var(--bg-color-sup);
  border-radius: 20px;
}

/*==============================================*/
@keyframes active-status {
  0% {
    background-color: var({online_Status});
  }

  33.33% {
    background-color: #93e200;
  }

  66.33% {
    background-color: #93e200;
  }

  100% {
    background-color: var({online_status});
  }
}</style>"""
    st.sidebar.markdown(text,unsafe_allow_html=True)
    st.sidebar.markdown(css,unsafe_allow_html=True)

def writer():
    text = """<h1 class="changing-text">
        You can
        <div class="texts-container">
            <span style="color: #37c4ff;">Predict<br/>
                                      Search<br/>
                                     Analyse<br/>
                                     Learn</span>
        </div>
    </h1>"""
    css_custom = """<style>
.changing-text{
    text-transform: uppercase;
    color: #fff;    
    font-family: verdana;
    font-size: 16px;
}

.texts-container{
    display: inline-block;
    height: 23px;
    overflow: hidden;
    color: #ff7a00;
}

.texts-container span{
    display: block;
    animation: moveUp 8s infinite;
}

@keyframes moveUp{
    0%{
        transform: translateY(0);
    }

    25%{
        transform: translateY(-26%);
    }

    50%{
        transform: translateY(-51%);
    }

    75%{
        transform: translateY(-76%);
    }

    100%{
        transform: translateY(0);
    }
}
</style>"""

    st.sidebar.markdown(text, unsafe_allow_html=True)
    st.sidebar.markdown(css_custom, unsafe_allow_html=True)


    
def render_quote_card():
    st.sidebar.markdown(
        f"""<div class="card">
  <p class="heading">
    Injustice anywhere is a threat to justice everywhere.
  </p>
  <p>Martin Luther King
</p></div>""",
        unsafe_allow_html=True,
    )

def render_run_hello():
    st.sidebar.markdown(f"""<div class="animation">Hello There..</div>""",unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="AI Jurist Dashboard",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="🏛️",  # Replace with an appropriate icon representing your app
    )
    custom_css = """
<style>
body {
    background-color: #1A1A1A;
    color: #FFFFFF;
    font-family: monospace;
    layout:wide;
}
[data-testid="stToolbar"] {visibility: 
            hidden !important;}
footer {visibility: 
            hidden !important;}
.stButton {
    color: #FFFFFF !important;
}
.stProgress > div > div > div > div {
 background-image: linear-gradient(to right, #205fff, #0094ff, #00bcff, #00deff, #5ffbf1);

        }
.card {
  position: relative;
  width: 250px;
  height: 150px;
  background-color: #000;
  display: flex;
  flex-direction: column;
  justify-content: end;
  padding: 12px;
  gap: 12px;
  margin:30px;
  border-radius: 8px;
  cursor: pointer;
}

.card::before {
  content: '';
  position: absolute;
  inset: 0;
  left: -5px;
  margin: auto;
  width: 250px;
  height: 150px;
  border-radius: 10px;
  background: linear-gradient(-45deg, #205fff 0%, #37a9ff 100% );
  z-index: -10;
  pointer-events: none;
  transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card::after {
  content: "";
  z-index: -1;
  position: absolute;
  inset: 0;
  background: linear-gradient(-45deg, #37a9ff 0%, #205fff 100% );
  transform: translate3d(0, 0, 0) scale(0.94);
  filter: blur(20px);
}

.heading {
  font-size: 14px;
  text-transform: capitalize;
  font-weight: 700;
}

.card p:not(.heading) {
  font-size: 13px;
}

.card p:last-child {
  color: #37c4ff;
  font-weight: 900;
}

.card:hover::after {
  filter: blur(30px);
}

.card:hover::before {
  transform: rotate(-180deg) scaleX(0.80) scaleY(1.1);
}

@keyframes typing {
  from {
    width: 0;
  }
}

@keyframes blink-caret {
  50% {
    border-color: transparent;
  }
}
.animation {
  font: bold 200% Consolas, Monaco, monospace;
  border-right: .1em solid black;
  width: 30.20ch;
  white-space: nowrap;
  overflow: hidden;
  -webkit-animation: typing 5s steps(13, end),
	           blink-caret .5s step-end infinite alternate;
}
 
     
/* Add other custom styles for different components here */
</style>
"""
    #st.sidebar.image("assets/ai-juris-low-resolution-logo-color-on-transparent-background.png",width=130)
    st.markdown(custom_css, unsafe_allow_html=True) 
        

    # Custom CSS to style the sidebar
    #side_text=f"<p style='font-family: \"Exo2\", sans-serif;font-size:30px; color:#FF00FF'>AI Jurist Dashboard</p>"
    #st.sidebar.markdown(side_text,unsafe_allow_html= True)
    
    with st.sidebar:
        selected_page=option_menu(
        menu_title="Navigator",
        menu_icon="cast",
        options=["Sign Up/Login","Predictor","Case Overview","Predicted Cases","Courts Info"],
        icons=["person","boxes","journal","database","info-square-fill"],
        default_index=0,
        styles={
            
            "nav-link": {"--hover-color": "#37c4ff"},
            "nav-link-selected": {"background-color": "#37c4ff"}}
    )

    # Create a dictionary of page names and corresponding functions
    pages = {
        "Sign Up/Login":render_login_page,
        "Predictor": render_predictor_page,
        "Predicted Cases": render_previous_predictions,
        "Case Overview": render_case_info,
        "Courts Info": render_courts_info,
    }
    email = ""
    if selected_page == "Sign Up/Login":
            if st.session_state.email:  
                    if st.button("Logout"):
                        st.session_state.email = False
                        email = render_login_page()   
            else:
                email = render_login_page()
            
    else:
        email = st.session_state.email  # Retrieve the user's email from the session

    # ...

    if selected_page == "Case Overview":
        if email:
            render_case_info()
        else:
            st.info("PLEASE LOGIN TO ACCESS CASE OVERVIEW")
    elif selected_page == "Predictor":
        if email:
            render_predictor_page(email)
        else:
            st.info("PLEASE LOGIN TO ACCESS PREDICTOR")
    elif selected_page == "Predicted Cases":
        if email:
            render_previous_predictions(email)
        else:
            st.info("PLEASE LOGIN TO ACCESS PREDICTED CASES")
    elif selected_page == "Courts Info":
        if email:
          render_courts_info()
        else:
          st.info("PLEASE LOGIN TO ACCESS COURTS INFO")  
       
    render_quote_card()
    if st.session_state.email:
      if selected_page =="Sign Up/Login":
          status_shower("You are already logged in","","Logged in")
      else:   
          status_shower(email,get_username_by_email(email),"Logged in")
    else:
      status_shower("You are logged out","","Logged out") 
      
      
if __name__=="__main__":
    main()
