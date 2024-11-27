import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure Google Gemini API
api_key = 'AIzaSyA3SOhkZnM_M01ew8HM3ZeJdG6rhbf8DOg'
genai.configure(api_key=api_key)


# Function to get advice from Gemini AI
#def get_baby_advice(problem_description, age, gender, image=None):
#    try:
#        # Check if the problem is related to babies or children using expanded keywords
#        baby_related_keywords = [
#            "baby", "infant", "child", "newborn", "toddler", "daughter", "son", "crying", "diaper", "feeding", "sleeping"
#        ]
#        if not any(keyword in problem_description.lower() for keyword in baby_related_keywords):
#            return "The input doesn't seem to be related to babies or children. Please provide a relevant description."
#
#        model = genai.GenerativeModel('gemini-1.5-flash')
#        inputs = [
#            f"The baby is {age} months old.",
#            f"The baby's gender is {gender}.",
#            problem_description
#        ]
#        if image:
#            inputs.append(image)
#        response = model.generate_content(inputs)
#        return response.text
#    except Exception as e:
#        return f"Error generating advice: {str(e)}"


def get_baby_advice(problem_description, age, gender, image=None):
    try:
        # Check if the problem is related to babies or children using expanded keywords
        baby_related_keywords = [
            "baby", "infant", "child", "newborn", "toddler", "daughter", "son", "crying", "diaper", "feeding", "sleeping"
        ]
        if not any(keyword in problem_description.lower() for keyword in baby_related_keywords):
            return "The input doesn't seem to be related to babies or children. Please provide a relevant description."

        model = genai.GenerativeModel('gemini-1.5-flash')
        inputs = [
            f"The baby is {age} months old.",
            f"The baby's gender is {gender}.",
            problem_description
        ]
        if image:
            inputs.append(image)
        response = model.generate_content(inputs)

        # Split the response into sentences or sections
        response_text = response.text
        sentences = response_text.split('. ')  # Split by sentences (basic)

        # Assume the first sentence is the most probable reason
        if sentences:
            main_reason = sentences[0].strip() + '.'  # Most probable reason
            additional_info = '. '.join(sentences[1:]).strip()  # More detailed options

            return f"{main_reason}\n\n{additional_info}"
        else:
            return "No advice could be generated. Please try again with more details."

    except Exception as e:
        return f"Error generating advice: {str(e)}"



#Functions for Baby Profile
# Function to retrieve session state to store baby profile
if "baby_profile" not in st.session_state:
    st.session_state.baby_profile = {}

# Function to display the baby profile form
def create_baby_profile():
    st.subheader("Create Your Baby's Profile")

    name = st.text_input("Baby's Name")
    birth_date = st.date_input("Baby's Birth Date")
    gender = st.radio("Baby's Gender", ["Male", "Female", "Other"])
    picture = st.file_uploader("Upload Baby's Picture", type=["jpg", "png", "jpeg"])
    weight = st.number_input("Baby's Weight (kg)", min_value=0.0, step=0.1)
    length = st.number_input("Baby's Length (cm)", min_value=0.0, step=0.1)

    if st.button("Save Profile"):
        st.session_state.baby_profile = {
            "name": name,
            "birth_date": birth_date,
            "gender": gender,
            "picture": picture,
            "weight": weight,
            "length": length
        }
        st.success("Baby's profile saved successfully!")




# Set page configuration
st.set_page_config(
    page_title="BabyConnect",
    page_icon="🍼",
    layout="wide"
)

# Add custom CSS for background styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #CBEEC4; /* Light green background */
        }
        h1 {
            color: #B359F7; /* Purple title color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

################################ SIDEBAR #########################################################################
page = st.sidebar.radio("Select a page", options=["Home", "My Baby", "Facts & Figures", "Get Advice", "FAQ"])



################################ HOME #########################################################################
if page == "Home":
    st.title("🍼 BabyConnect – Your Trusted Guide to Baby Care")

    # Create two columns, with the left column being larger
    col1, col2 = st.columns([3, 1])

    # Display content in the left column
    with col1:
        st.write(
        """
        As a parent or caregiver, you're constantly learning and adapting to the needs of your little one. Baby Connect is here to make that journey a little easier. Whether you're looking for expert advice, discovering important milestones, or simply seeking reassurance, our app provides personalized guidance to help you navigate the early years of your baby’s life.

        <b><span style="color:#B359F7;">What we offer:</span></b>

        👶 <b><span style="color:#B359F7;">PERSONAL BABY PROFILE</span></b>: Keep track of your baby’s development, history of searches, and more.

        📈 <b><span style="color:#B359F7;">LEARN ABOUT BABY DEVELOPMENT</span></b>: Understand the stages of your baby’s growth and development with helpful insights.

        🤖 <b><span style="color:#B359F7;">AI-POWERED BABY ADVICE</span></b>: Get answers to your baby-related questions based on AI-generated insights.

        ❓ <b><span style="color:#B359F7;">FAQ SECTION</span></b>: Find answers to common baby-related questions in our comprehensive FAQ section.

        📄 <b><span style="color:#B359F7;">PDF REPORT</span></b>: Generate a detailed PDF report summarizing your baby’s development and health, perfect for sharing with doctors.

        <b><span style="color:#B359F7;">Join thousands of parents who trust Baby Connect for expert advice and peace of mind.</span></b>
        """,
        unsafe_allow_html=True
    )

    # Display the GIF in the right column
    with col2:
        st.image("bottle.gif", use_column_width=True)


#################################### FACTS & FIGURES #######################################################################

# Add a page for Facts & Figures
elif page == "Facts & Figures":
    st.title(" Facts & Figures About Babies")

    # First row of facts (2 columns)
    col1, col2 = st.columns(2)

    with col1:
        st.image("baby_3.jpg", width=150)
        st.write(
            """**1. Babies have around 100 bones at birth.**
            A baby's skeleton is made of **cartilage** that will gradually turn into bone as they grow. By the time a child reaches adulthood, they will have about 206 bones.
            """
        )

    with col2:
        st.image("baby_4.jpg", width=150)
        st.write(
            """**2. Newborns spend about 16-18 hours sleeping daily.**
            Sleep is essential for babies' **growth** and development. It helps in the creation of **connections** in the brain and supports the body's **healing** processes.
            """
        )

    # Add extra space between rows
    st.write("\n\n")  # Adds two line breaks for separation

    # Second row of facts (2 columns)
    col3, col4 = st.columns(2)

    with col3:
        st.image("baby_5.jpg", width=150)
        st.write(
            """**3. Babies can recognize their mother’s voice at birth.**
            From the moment they are born, babies are able to **hear** sounds, and by the time they’re a few days old, they can recognize the **voice** of their mother.
            """
        )

    with col4:
        st.image("baby_6.jpg", width=150)
        st.write(
            """**4. Babies' vision improves significantly in the first 6 months.**
            At birth, babies can see only **blurry** shapes, but within the first few months, their vision improves, allowing them to see **faces** clearly and follow moving objects.
            """
        )


#################################### MY BABY #######################################################################

# Add a section for baby profile creation
elif page == "My Baby":
    st.title("My Baby's Profile")

    # Show the profile creation form
    create_baby_profile()

    # Display the saved baby profile if available
    if st.session_state.baby_profile:
        st.subheader("Saved Baby Profile")
        st.write(f"**Name**: {st.session_state.baby_profile['name']}")
        st.write(f"**Birth Date**: {st.session_state.baby_profile['birth_date']}")
        st.write(f"**Gender**: {st.session_state.baby_profile['gender']}")
        if st.session_state.baby_profile["picture"]:
            st.image(st.session_state.baby_profile["picture"], use_column_width=True)
        st.write(f"**Weight**: {st.session_state.baby_profile['weight']} kg")
        st.write(f"**Length**: {st.session_state.baby_profile['length']} cm")

#################################### GET ADVICE #######################################################################

elif page == "Get Advice":
    st.title("Get AI-Powered Baby Advice")
    st.write(
        """Welcome to the application page! You can upload an image of your baby's condition or describe the problem,
        and our AI will provide you with possible solutions or advice. Please remember that this app is not a substitute for professional medical advice."""
    )

    # Input: Age of the baby
    age = st.slider("Select the age of your baby (in months):", min_value=0, max_value=24, value=6, step=1)

    # Input: Gender of the baby
    gender = st.radio("Select the gender of your baby:", options=["Male", "Female"], index=0)

    # Input: Text description of the problem
    problem_description = st.text_input("Describe the problem your baby is experiencing:", key="problem_input")

    # Input: Upload an image
    uploaded_file = st.file_uploader("Upload an image of the issue (optional):", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Button to get advice
    if st.button("Get Advice"):
        if not problem_description and not image:
            st.warning("Please provide a description or upload an image to get advice.")
        else:
            st.info("Analyzing... please wait.")
            advice = get_baby_advice(problem_description, age, gender, image)
            st.subheader("Here is the advice:")
            st.write(advice)

    st.write(
        """
        **Disclaimer:** The advice provided by this app is based on AI-generated insights and should not replace consulting a licensed pediatrician or healthcare professional.
        """
    )


    #################################### FAQ #######################################################################

elif page == "FAQ":
    st.title("Baby FAQ")
    st.image("baby1.jpg", use_column_width=True)
    st.write("Here are answers to some commonly asked questions about babies:")

    # FAQ Section
    st.subheader("1. How often should I feed my newborn?")
    st.write("Newborns typically need to be fed every 2-3 hours. Watch for hunger cues such as sucking on hands or fussiness.")

    st.subheader("2. How much sleep does a newborn need?")
    st.write("Newborns usually sleep up to 16-17 hours a day in short intervals, typically lasting 2-4 hours at a time.")

    st.subheader("3. What is tummy time, and why is it important?")
    st.write("Tummy time is supervised playtime on the baby's stomach. It helps strengthen neck and shoulder muscles and prevents flat spots on the head.")

    st.subheader("4. How do I know if my baby is getting enough milk?")
    st.write("Signs include regular wet and dirty diapers, consistent weight gain, and a satisfied demeanor after feeding.")

    st.subheader("5. When should I start introducing solid foods?")
    st.write("Solid foods can be introduced around 6 months old, but consult your pediatrician to ensure your baby is ready.")

