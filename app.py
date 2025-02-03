import streamlit as st
import time

# Initialize session state for timer
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.time_left = 40  # Default work time

# Function to start timer
def start_timer():
    st.session_state.timer_running = True

# Function to stop timer
def stop_timer():
    st.session_state.timer_running = False

# Function to reset timer
def reset_timer():
    st.session_state.timer_running = False
    st.session_state.time_left = 40

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

# HIIT Timer
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

# Countdown Timer Logic with Live Display
if st.session_state.timer_running:
    while st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

    stop_timer()

# Show the countdown timer on the app screen
st.write(f"⏳ **Time Left:** {st.session_state.time_left} sec")

# Progress Tracking
st.subheader("Workout Completion")
for exercise in workouts[day]["Strength"]:
    st.checkbox(f"Completed: {exercise}")

st.success("Workout Tracker Ready! Try it out.")
