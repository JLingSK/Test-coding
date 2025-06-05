import streamlit as st

st.set_page_config(page_title="TB Truth Quest", layout="centered")

st.title("🦠 TB Truth Quest")
st.markdown("**Can you break the myths and uncover the truth about Tuberculosis?**")

# Initialise session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "ready" not in st.session_state:
    st.session_state.ready = False

def restart_game():
    st.session_state.score = 0
    st.session_state.stage = 0
    st.session_state.ready = False

# READY SECTION
if not st.session_state.ready:
    st.subheader("Are you ready for the challenge?")
    if st.button("I'm Ready!"):
        st.session_state.ready = True
else:
    # SCENARIO LOGIC
    def scenario_1():
        st.subheader("Scenario 1: A Rumour at the Market")
        st.markdown("> Your friend says: 'TB only affects poor people!'")
        answer = st.radio("Do you agree?", ["Yes", "No"], key="q1")
        if st.button("Next", key="b1"):
            if answer == "No":
                st.session_state.score += 1
                st.info("✅ Correct! TB can affect anyone, regardless of income, age, or background.")
            else:
                st.warning("❌ Incorrect. TB can affect anyone, not just poor people.")
            st.session_state.stage += 1

    def scenario_2():
        if st.session_state.score == 0:
            st.subheader("Scenario 2A: Misinformed Uncle")
            st.markdown("> Your uncle says: 'You can treat TB with herbs only.'")
            answer = st.radio("Do you agree with him?", ["Yes", "No"], key="q2a")
            if st.button("Next", key="b2"):
                if answer == "No":
                    st.session_state.score += 1
                    st.info("✅ Correct! TB cannot be cured with herbs alone. Effective treatment requires specific antibiotics for several months.")
                else:
                    st.warning("❌ Incorrect. TB needs proper antibiotics, not just herbs.")
                st.session_state.stage += 1
        else:
            st.subheader("Scenario 2B: Social Media Post")
            st.markdown("> A post online says: 'TB spreads by sharing food.'")
            answer = st.radio("Do you believe this?", ["Yes", "No"], key="q2b")
            if st.button("Next", key="b2"):
                if answer == "No":
                    st.session_state.score += 1
                    st.info("✅ Correct! TB does not spread by sharing food. It spreads through the air when a person with active TB coughs or sneezes.")
                else:
                    st.warning("❌ Incorrect. TB spreads through the air, not by sharing food.")
                st.session_state.stage += 1

    def scenario_3():
        st.subheader("Scenario 3: Someone at Work Has TB")
        st.markdown("> A colleague has TB. Some think he should be isolated for months.")
        answer = st.radio("Is long isolation always needed?", ["Yes", "No"], key="q3")
        if st.button("Next", key="b3"):
            if answer == "No":
                st.session_state.score += 1
                st.info("✅ Correct! Not all TB patients need long isolation. With proper treatment, most people with TB quickly become non-infectious.")
            else:
                st.warning("❌ Incorrect. Most TB patients are not infectious after starting treatment.")
            st.session_state.stage += 1

    def scenario_4():
        st.subheader("Scenario 4: Stopping Treatment Early")
        st.markdown("> Your neighbour stopped TB medication after 2 months as he felt better.")
        answer = st.radio("Is that okay?", ["Yes", "No"], key="q4")
        if st.button("Next", key="b4"):
            if answer == "No":
                st.session_state.score += 1
                st.info("✅ Correct! Stopping TB medication early is dangerous. The full course must be completed to cure TB and prevent resistance.")
            else:
                st.warning("❌ Incorrect. Stopping early can cause TB to come back and become resistant.")
            st.session_state.stage += 1

    def scenario_5():
        st.subheader("Scenario 5: BCG Vaccine Debate")
        st.markdown("> A friend says: 'We don’t need BCG vaccine anymore.'")
        answer = st.radio("Do you agree?", ["Yes", "No"], key="q5")
        if st.button("See Result", key="b5"):
            if answer == "No":
                st.session_state.score += 1
                st.info("✅ Correct! The BCG vaccine is still important in many countries to protect against severe forms of TB, especially in children.")
            else:
                st.warning("❌ Incorrect. BCG vaccine is still needed in many places to protect children.")
            st.session_state.stage += 1

    def show_result():
        st.subheader("🏁 Your Outcome")

        score = st.session_state.score
        st.markdown(f"**Your total score: {score}/5**")

        if score == 5:
            st.success("🏆 TB Awareness Champion! You busted the myths and protected your community.")
        elif 3 <= score < 5:
            st.info("🥈 Rising Advocate. Good job! A bit more learning and you'll be a TB ambassador.")
        else:
            st.warning("🥉 Misinformed but Motivated. Don't worry – try again to learn more!")

        st.button("🔄 Play Again", on_click=restart_game)

    # RENDER GAME STAGES
    if st.session_state.stage == 0:
        scenario_1()
    elif st.session_state.stage == 1:
        scenario_2()
    elif st.session_state.stage == 2:
        scenario_3()
    elif st.session_state.stage == 3:
        scenario_4()
    elif st.session_state.stage == 4:
        scenario_5()
    else:
        show_result()
