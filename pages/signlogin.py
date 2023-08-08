import streamlit as st
import os
from streamlit_option_menu import option_menu
from deta import Deta
from password_strength import PasswordPolicy
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Initialize Deta with your Deta Project Key
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
users_db = deta.Base("users")

# Password policy for password strength check
password_policy = PasswordPolicy.from_names(
    length=8,  # Minimum length: 8 characters
    uppercase=1,  # At least 1 uppercase letter
    numbers=1,  # At least 1 digit
    special=1,  # At least 1 special character
)


def writer():
    text = """<h1 class="changing-text">
        You can
        <div class="texts-container">
            <span style="color: #205fff;">Predict<br/>
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
    font-size: 24px;
}

.texts-container{
    display: inline-block;
    height: 24px;
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

    st.markdown(text, unsafe_allow_html=True)
    st.markdown(css_custom, unsafe_allow_html=True)


def render_title(n):
    if(n==1):
        st.markdown(
        f"""<button data-text="Awesome" class="button">
    <span class="actual-text" style='font-weight:bold'>&nbsp;User Signup&nbsp;</span>
    <span class="hover-text" aria-hidden="true" style='font-weight:bold'>&nbsp;User Signup&nbsp;</span>
</button>""",
        unsafe_allow_html=True,
    )
    elif(n==2):
        st.markdown(
        f"""<button data-text="Awesome" class="button">
    <span class="actual-text" style='font-weight:bold'>&nbsp;User Login&nbsp;</span>
    <span class="hover-text" aria-hidden="true" style='font-weight:bold'>&nbsp;User Login&nbsp;</span>
</button>""",
        unsafe_allow_html=True,
    )    

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


def is_valid_email(email):
    # Check if the email is valid using email_validator library
    try:
        valid = validate_email(email)
        email = valid.email
        return True
    except EmailNotValidError as e:
        return False


def send_welcome_email(email):
    # Sender's email details
    sender_email = os.getenv("sender_email")  # Replace with your email address
    sender_password = os.getenv("sender_password") # Replace with your email password

    # Subject and body of the email
    subject = "Welcome to AIJurist!"
    body = f"""Dear User,

Thank you for registering with AIJurist! We are thrilled to have you as part of our community.

AIJurist is a powerful tool that allows you to predict, search, analyze, and learn with ease. We are constantly adding new features and improvements to enhance your experience.

👉 Experience accurate legal case predictions powered by cutting-edge AI technology.
👉 Make informed decisions based on data-backed insights for your legal matters.
👉 Accessible interface for both legal professionals and newcomers.
👉 Remember, AIJurist's predictions complement, not replace, professional legal advice.

If you have any questions, suggestions, or feedback, feel free to reach out to our support team at Aijuristofficial@outlook.com.

Once again, welcome to AIJurist, and we hope you have a fantastic experience!

Best regards,
The AIJurist Team
"""

    # Send the email
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False


def check_password_strength(password):
    # Check if the password meets the defined criteria
    errors = []

    if len(password) < 8:
        errors.append("Password should be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        errors.append("Password should contain at least 1 uppercase letter.")
    if not any(char.isdigit() for char in password):
        errors.append("Password should contain at least 1 digit.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in password):
        errors.append("Password should contain at least 1 special character.")

    return "\n".join(errors)

def check_email_availability(email):
    # Check if the email is already registered in the database
    existing_users = users_db.fetch({"email": email})
    return not existing_users.items

def register_user(username, email, password):
    # Save user data to the database
    user_data = {"username": username, "email": email, "password": password}
    users_db.put(user_data)

def render_login_page():
    col1,col2,col3 = st.columns([0.1,0.3,0.5])
    with col2:
        st.markdown(
            """<p style='font-size: 29px; font-weight: 700;'>
            <span style='color: #250fff;'>AI J</span>urist
            </p>""",
            unsafe_allow_html=True)
    with col3:
        writer()

    # Options for the menu
    options = ["Sign up", "Login"]
    
    # Icons for the menu options
    icons = ["person-add", "person-fill"]
    col4,col5,col6 = st.columns([0.38,3.4,0.4])
    with col5:
        selected = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        orientation="horizontal",
        default_index=0,
        styles={
            "nav-link": {"--hover-color": "#205fff"},
            "nav-link-selected": {"background-color": "#205fff"}
        }
    )

        if selected == "Sign up":
            vert_space = '<div style="padding: 12px 5px;"></div>'
            st.markdown(vert_space, unsafe_allow_html=True)
            render_title(1)
            vert_space = '<div style="padding: 12px 5px;"></div>'
            st.markdown(vert_space, unsafe_allow_html=True)
        
        # Use st.form() for a cleaner look
            with st.form(key="register_form"):
                username = st.text_input("Username:")
                email = st.text_input("Gmail ID:")
                password = st.text_input("Password:", type="password")
                confirm_password = st.text_input("Confirm Password:", type="password")

                if st.form_submit_button("Register"):
                    if not email.strip():
                        st.error("Please enter a Gmail ID.")
                    elif not is_valid_email(email):
                        st.error("Invalid Gmail ID.")
                    elif not password.strip():
                        st.error("Please enter a password.")
                    else:
                    # Check password strength
                        error_messages = check_password_strength(password)
                        if error_messages:
                            st.warning(error_messages)
                        elif password != confirm_password:
                            st.error("Passwords do not match.")
                        elif not check_email_availability(email):
                            st.error("Gmail ID is already registered. Please use a different Gmail ID.")
                        else:   
                        # Register the user and save data to the database
                            with st.spinner("Sending welcome email..  This may take few seconds"):
                                if send_welcome_email(email):
                                    register_user(username, email, password)
                                    st.success("Successfully Signed up and Welcome email is sent!😊")
                                else:
                                    st.info("Error while sending welcome email, Please provide an authenticated email.🥹")

        elif selected == "Login":
            vert_space = '<div style="padding: 12px 5px;"></div>'
            st.markdown(vert_space, unsafe_allow_html=True)
            render_title(2)
            vert_space = '<div style="padding: 12px 5px;"></div>'
            st.markdown(vert_space, unsafe_allow_html=True)

        # Use st.form() for a cleaner look
            with st.form(key="signin_form"):
                email = st.text_input("Gmail ID:")
                password = st.text_input("Password:", type="password")

                if st.form_submit_button("Sign In"):
                    if not email.strip():
                      st.error("Please enter your Gmail ID.")
                    elif not password.strip():
                        st.error("Please enter your password.")
                    else:
                    # Check if the email exists in the database
                        existing_users = users_db.fetch({"email": email})
                        if not existing_users.items:
                            st.error("User not found. Please check your Gmail ID or register.")
                        else:
                        # Verify the password
                            existing_user = existing_users.items[0]
                            if existing_user["password"] == password or st.session_state.email:
                                st.success("Successfully signed in!")
                                st.write("You can now surf with our Navigtor🏄‍♂️")
                                st.session_state.email=email
                            else:
                                st.error("Incorrect password. Please try again.")
        return email
    # Use the option_menu from the streamlit_option_menu library


