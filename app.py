import streamlit as st
from game import Game   # replace with your filename

st.title("Monopoly Game")

# ---- Setup Phase ----
if "game" not in st.session_state:
    st.subheader("Setup Game")

    num_players = st.number_input("Number of players", min_value=2, max_value=4, step=1)

    player_names = []
    for i in range(num_players):
        name = st.text_input(f"Player {i+1} name", key=f"name_{i}")
        player_names.append(name)

    if st.button("Start Game"):
        if all(player_names):
            st.session_state.game = Game(num_players, player_names)
        else:
            st.warning("Enter all player names")

# ---- Game Phase ----
if "game" in st.session_state:
    game = st.session_state.game

    st.subheader("Game State")

    state = game.get_state()
    for p in state:
        st.write(p)

    st.subheader("Turn")

    if st.button("Roll Dice"):
        result = game.turn()

        st.write("### Result")
        st.write(result["result"])

        st.write("### Updated State")
        st.write(result["state"])