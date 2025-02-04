import streamlit as st
import time

# Initialize session state variables
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.time_left = 40  # Default work time
if 'cooldown_running' not in st.session_state:
    st.session_state.cooldown_running = False
    st.session_state.cooldown_time_left = 20  # Default cooldown time
if 'set_count' not in st.session_state:
    st.session_state.set_count = 0  # Track number of sets completed

# Function to start the workout timer
def start_timer():
    st.session_state.timer_running = True
    st.session_state.cooldown_running = False  # Stop cooldown when workout starts
    st.session_state.cooldown_time_left = 20  # Reset cooldown time

# Function to stop the workout timer and start cooldown
def stop_timer():
    st.session_state.timer_running = False
    st.session_state.cooldown_running = True
    st.session_state.set_count += 1  # Increase set count after each stop

# Function to reset everything
def reset_timer():
    st.session_state.timer_running = False
    st.session_state.cooldown_running = False
    st.session_state.time_left = 40
    st.session_state.cooldown_time_left = 20
    st.session_state.set_count = 0  # Reset set count

# Define workout routines
workouts = {
    "Day 1 - Upper Body HIIT & Strength": {
        "HIIT": [
            "Jump Rope",
            "Push-Ups",
            "Dumbbell Thrusters",
            "Battle Ropes or Kettlebell Swings",
            "Burpees",
            "Mountain Climbers",
            "Plank-to-Push-Up"
        ],
        "Strength": [
            "Bench Press",
            "Overhead Shoulder Press",
            "Incline Dumbbell Press",
            "Dips",
            "Triceps Rope Pushdowns",
            "Hanging Leg Raises"
        ]
    },
    "Day 2 - Lower Body HIIT & Strength": {
        "HIIT": [
            "Jump Squats",
            "Lunges",
            "Step-Ups",
            "Kettlebell Swings",
            "Sprint Intervals",
            "Sumo Deadlifts",
            "Plank with Leg Lifts"
        ],
        "Strength": [
            "Squats (Back or Front)",
            "Romanian Deadlifts",
            "Bulgarian Split Squats",
            "Glute Bridges or Hip Thrusts",
            "Calf Raises",
            "Ab Rollouts"
        ]
    },
    "Day 3 - Full Body HIIT & Strength": {
        "HIIT": [
            "Rowing Machine or Assault Bike",
            "Kettlebell Snatch",
            "Burpee Pull-Ups",
            "Jump Lunges",
            "Dumbbell Clean & Press",
            "Box Jumps",
            "Russian Twists"
        ],
        "Strength": [
            "Deadlifts",
            "Pull-Ups",
            "Barbell Rows",
            "Dumbbell Snatch",
            "Hammer Curls",
            "Plank (Hold 60 sec)"
        ]
    }
}

# Streamlit UI
st.title("HIIT + Weightlifting Workout App")

# Select workout day
day = st.selectbox("Select your workout day:", list(workouts.keys()))

# Display workout routine
st.subheader("HIIT Workout:")
for exercise in workouts[day]["HIIT"]:
    st.write(f"- {exercise}")

st.subheader("Weightlifting Routine:")
for exercise in workouts[day]["Strength"]:
    st.write(f"- {exercise}")

# Display set count
st.subheader(f"✅ Sets Completed: {st.session_state.set_count}")

# HIIT Timer Controls
st.subheader("HIIT Timer")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Start"):
        start_timer()
with col2:
    if st.button("Stop"):
        stop_timer()
with col3:
    if st.button("Reset"):
        reset_timer()

# Live Countdown Timer Display
timer_display = st.empty()

if st.session_state.timer_running:
    for i in range(st.session_state.time_left, -1, -1):
        st.session_state.time_left = i
        timer_display.write(f"⏳ **Workout Time Left: {i} sec**")  # Update the countdown
        progress = max(0, min((i / 40) * 100, 100))  # Ensure value stays between 0-100
        st.progress(progress)  # Show shrinking green bar
        time.sleep(1)
    stop_timer()

# Cooldown Timer Display and Red Alert
cooldown_display = st.empty()

if st.session_state.cooldown_running:
    for i in range(st.session_state.cooldown_time_left, -1, -1):
        st.session_state.cooldown_time_left = i
        
        # Show red alert if cooldown time exceeds 20 sec
        if i == 0:
            cooldown_display.markdown(
                '<p style="font-size:40px; color:red; font-weight:bold;">🚨 REST TIME OVER! GET BACK TO WORK! 🚨</p>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<audio autoplay><source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav"></audio>',
                unsafe_allow_html=True,
            )  # Play sound alert when cooldown ends

        cooldown_display.write(f"🛑 **Cooldown Time Left: {i} sec**")
        time.sleep(1)

    st.session_state.cooldown_running = False  # Stop the cooldown timer

# Display Final Countdown Values (if timer is stopped)
if not st.session_state.timer_running:
    timer_display.write(f"⏳ **Workout Time Left: {st.session_state.time_left} sec**")

if not st.session_state.cooldown_running:
    cooldown_display.write(f"🛑 **Cooldown Time Left: {st.session_state.cooldown_time_left} sec**")

# Progress Tracking
st.subheader("Workout Completion")
for exercise in workouts[day]["Strength"]:
    st.checkbox(f"Completed: {exercise}")

st.success("🔥 Workout Tracker Updated! Enjoy your training! 💪")
