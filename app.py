import streamlit as st
import random
import time

# Initialize session state for scores and level
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'equation' not in st.session_state:
    st.session_state.equation = None
if 'hidden_value' not in st.session_state:
    st.session_state.hidden_value = None
if 'choices' not in st.session_state:
    st.session_state.choices = []

# Function to generate equation
def generate_equation(level):
    """Generate an addition or subtraction equation with one missing number."""
    num1 = random.randint(1, 10 + level * 2)  # Increase difficulty with level
    num2 = random.randint(1, 10 + level * 2)
    if random.choice([True, False]):
        # Addition equation
        answer = num1 + num2
        if random.choice([True, False]):
            equation = f"⬜ + {num2} = {answer}"
            hidden_value = num1
        else:
            equation = f"{num1} + ⬜ = {answer}"
            hidden_value = num2
    else:
        # Subtraction equation
        answer = num1 - num2 if num1 > num2 else num2 - num1
        if random.choice([True, False]):
            equation = f"⬜ - {num2} = {answer}" if num1 > num2 else f"⬜ - {num1} = {answer}"
            hidden_value = num1 if num1 > num2 else num2
        else:
            equation = f"{num1} - ⬜ = {answer}" if num1 > num2 else f"{num2} - ⬜ = {answer}"
            hidden_value = num2 if num1 > num2 else num1
    
    # Generate answer choices
    choices = [hidden_value, hidden_value + random.randint(1, 3), hidden_value - random.randint(1, 3)]
    random.shuffle(choices)

    return equation, hidden_value, choices

# Generate new equation when needed
if st.session_state.equation is None:
    st.session_state.equation, st.session_state.hidden_value, st.session_state.choices = generate_equation(st.session_state.level)

# UI Design
st.title("🔢 Math Drop Game")
st.markdown(f"**Level:** {st.session_state.level} | **Score:** {st.session_state.score}/10")

st.write("Find the missing number:")

# Show equation
st.markdown(f"### {st.session_state.equation}")

# Simulate falling numbers
st.write("### Pick the correct number:")
selected_number = st.radio("", st.session_state.choices, index=None, key="selected_number")

# Check answer
if selected_number is not None:
    if selected_number == st.session_state.hidden_value:
        st.success("✅ Correct!")
        st.session_state.score += 1

        # Level up every 10 points
        if st.session_state.score % 10 == 0:
            st.session_state.level += 1
            st.session_state.score = 0  # Reset score for new level
            st.success(f"🎉 Level Up! You are now on Level {st.session_state.level}")

        # Generate new equation
        st.session_state.equation, st.session_state.hidden_value, st.session_state.choices = generate_equation(st.session_state.level)
    else:
        st.error("❌ Wrong! Try Again.")

# Restart button
if st.button("Restart Game"):
    st.session_state.score = 0
    st.session_state.level = 1
    st.session_state.equation, st.session_state.hidden_value, st.session_state.choices = generate_equation(st.session_state.level)
    st.experimental_rerun()