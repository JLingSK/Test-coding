import streamlit as st

st.set_page_config(page_title="TB PathQuest", layout="centered")

st.title("🧭 TB PathQuest: Your Journey with Tuberculosis")
st.markdown("You are experiencing symptoms that might be tuberculosis. Your decisions will determine your fate—and others’ too.")

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "outcome" not in st.session_state:
    st.session_state.outcome = None
if "decision_path" not in st.session_state:
    st.session_state.decision_path = []

def reset_game():
    st.session_state.stage = "start"
    st.session_state.outcome = None
    st.session_state.decision_path = []

# Game stages
def stage_start():
    st.subheader("Stage 1: Persistent Cough and Fatigue")
    st.markdown("You’ve been coughing for over 2 weeks and feel increasingly tired. Your family urges you to see a doctor.")
    choice = st.radio("What do you do?", ["Go to the clinic", "Wait and try herbs/self-medication"], key="q1")
    if st.button("Next", key="b1"):
        st.session_state.decision_path.append(choice)
        if choice == "Go to the clinic":
            st.session_state.stage = "clinic_visit"
        else:
            st.session_state.stage = "delay_seek_care"

def stage_clinic_visit():
    st.subheader("Stage 2A: Clinic Consultation")
    st.markdown("The doctor suspects TB and recommends a sputum test.")
    choice = st.radio("Do you agree to the sputum test?", ["Yes, take the test", "No, I don't trust it"], key="q2a")
    if st.button("Next", key="b2a"):
        st.session_state.decision_path.append(choice)
        if choice == "Yes, take the test":
            st.session_state.stage = "test_positive"
        else:
            st.session_state.stage = "refused_test"

def stage_delay_seek_care():
    st.subheader("Stage 2B: Delay in Seeking Care")
    st.markdown("Your symptoms worsen after two more weeks. You now have night sweats and weight loss.")
    choice = st.radio("What do you do now?", ["Go to hospital", "Visit traditional healer"], key="q2b")
    if st.button("Next", key="b2b"):
        st.session_state.decision_path.append(choice)
        if choice == "Go to hospital":
            st.session_state.stage = "test_positive"
        else:
            st.session_state.stage = "misdiagnosed"

def stage_test_positive():
    st.subheader("Stage 3A: Confirmed TB Diagnosis")
    st.markdown("Your TB test is positive. The clinic starts Directly Observed Treatment, Short-course (DOTS).")
    choice = st.radio("Do you follow the full treatment?", ["Yes, complete it", "Stop after 2 months"], key="q3a")
    if st.button("Next", key="b3a"):
        st.session_state.decision_path.append(choice)
        if choice == "Yes, complete it":
            st.session_state.outcome = "cured"
        else:
            st.session_state.outcome = "transmitted"
        st.session_state.stage = "outcome"

def stage_refused_test():
    st.subheader("Stage 3B: No Diagnosis Made")
    st.markdown("Without the test, the cause of your illness remains unclear. You get worse and cough up blood.")
    choice = st.radio("Do you now return to the clinic?", ["Yes, return", "No, stay home"], key="q3b")
    if st.button("Next", key="b3b"):
        st.session_state.decision_path.append(choice)
        if choice == "Yes, return":
            st.session_state.stage = "test_positive"
        else:
            st.session_state.outcome = "death"
            st.session_state.stage = "outcome"

def stage_misdiagnosed():
    st.subheader("Stage 3C: Traditional Treatment Fails")
    st.markdown("The herbal treatment does not work. You continue to deteriorate.")
    choice = st.radio("Do you now go to the hospital?", ["Yes", "No, I’ll continue herbs"], key="q3c")
    if st.button("Next", key="b3c"):
        st.session_state.decision_path.append(choice)
        if choice == "Yes":
            st.session_state.stage = "test_positive"
        else:
            st.session_state.outcome = "death"
            st.session_state.stage = "outcome"

def show_outcome():
    st.subheader("🏁 Final Outcome")

    if st.session_state.outcome == "cured":
        st.success("🎉 You completed the full treatment and are cured of TB. You also protected others from infection.")
    elif st.session_state.outcome == "transmitted":
        st.warning("😷 You stopped treatment early. Your TB may return, and you risked infecting others.")
    elif st.session_state.outcome == "death":
        st.error("💀 You did not seek timely or effective treatment. TB progressed and was fatal.")

    st.markdown("### 🧾 Your Decision Path:")
    for i, decision in enumerate(st.session_state.decision_path, 1):
        st.markdown(f"**{i}.** {decision}")

    st.button("🔁 Restart Game", on_click=reset_game)

# Routing
if st.session_state.stage == "start":
    stage_start()
elif st.session_state.stage == "clinic_visit":
    stage_clinic_visit()
elif st.session_state.stage == "delay_seek_care":
    stage_delay_seek_care()
elif st.session_state.stage == "test_positive":
    stage_test_positive()
elif st.session_state.stage == "refused_test":
    stage_refused_test()
elif st.session_state.stage == "misdiagnosed":
    stage_misdiagnosed()
elif st.session_state.stage == "outcome":
    show_outcome()
