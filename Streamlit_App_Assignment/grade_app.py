
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# Grade Calculation Function
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

# Title
st.title("🎓 Student Grade Calculator")
st.write("### Enter a mark between 0 and 100 to calculate the grade.")

# Input
mark = st.number_input(
    "Enter your mark:",
    min_value=0,
    max_value=100,
    value=85,
    step=1
)

grade = calculate_grade(mark)

# Dynamic Colors and Messages
if grade == "A":
    card_color = "#28a745"
    message = "Excellent Performance! 🏆"
    emoji = "🌟"

elif grade == "B":
    card_color = "#007bff"
    message = "Very Good Work! 👏"
    emoji = "🎉"

elif grade == "C":
    card_color = "#fd7e14"
    message = "Good Job! Keep Improving 👍"
    emoji = "😊"

elif grade == "D":
    card_color = "#ffc107"
    message = "Needs More Practice 📚"
    emoji = "✍️"

else:
    card_color = "#dc3545"
    message = "Don't Give Up! Keep Learning 💪"
    emoji = "🚀"

# Result Card
col1, col2, col3 = st.columns([0.3, 3.4, 0.3])

with col2:
    st.markdown(f"""
    <div style="
        background:{card_color};
        padding:30px;
        border-radius:20px;
        text-align:center;
        color:white;
        margin-top:20px;
        box-shadow:0px 5px 20px rgba(0,0,0,0.3);
    ">
        <h1 style="margin:0; color:white;">Result</h1>
        <h3 style="color:white;">Mark Entered: {mark}</h3>
        <h3 style="color:white;">Grade</h3>
        <div style="
            font-size:80px;
            font-weight:bold;
            margin:20px 0;
            color:white;
        ">{grade}</div>
        <h3 style="color:white;">{emoji} {message}</h3>
    </div>
    """, unsafe_allow_html=True)

# Grading Scale
st.subheader("📌 Grading Scale")

st.markdown("""
| Mark Range | Grade |
|------------|-------|
| 🟢 90 - 100 | A |
| 🔵 80 - 89 | B |
| 🟠 70 - 79 | C |
| 🟡 60 - 69 | D |
| 🔴 Below 60 | E |
""")

st.info(
    "Enter a value from 0 to 100. "
    "The grade is calculated based on the grading scale above."
)

st.markdown(
    "<center>Made with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)