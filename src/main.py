import os

import streamlit as st

from mistralai.models.chat_completion import ChatMessage
from mistralai.exceptions import MistralAPIException

import logging
log = logging.getLogger(__file__)


from src.VERSION import VERSION
from src.common import (
    ASSETS_PATH,
    ChatAppVars,
)

from src.chat_history import (
    save_chat_history,
    load_convo,
    delete_this_chat,
)


from src.interface import (
    column_fix,
    center_text,
    centered_button_trick,
)











def validate_input():
    # check that a selection was made for each selectbox
    if st.session_state["rounds"] is None:
        st.toast("Please select the number of rounds", icon="👾")
        return False

    if st.session_state["race"] is None:
        st.toast("Please select your race", icon="👾")
        return False

    if st.session_state["skillset"] is None:
        st.toast("Please select your skillset", icon="👾")
        return False

    if st.session_state["weapon"] is None:
        st.toast("Please select your weapon", icon="👾")
        return False

    return True


def reset_quest():
    st.session_state["quest"]["begun"] = False


def being_quest():
    if validate_input():
        st.session_state["quest"]["begun"] = True


def show_quest_settings():
    settings_col = st.columns(2)

    with settings_col[1]:
        st.write("Quest settings")
        st.selectbox(
            "number of rounds", options=["7", "12", "20"], key="rounds", index=1
        )
        st.selectbox(
            "Difficulty",
            options=["grade skool", "high school", "University Professor"],
            key="difficulty",
            index=1,
        )

    with settings_col[0]:
        st.write("Choose your character")
        st.selectbox(
            "Choose your race",
            options=["🧙‍♂️ wizard", "🧌 dwarf", "🧝‍♂️ elf", "🤖 robot"],
            index=None,
            key="race",
        )
        st.selectbox(
            "Choose your skillset",
            options=["🧠 smart", "💪 strong", "💨 fast", "🍀 lucky"],
            index=None,
            key="skillset",
        )
        st.selectbox(
            "Choose your weapon",
            options=["🪄 spellbook", "🎽 invisibility cloak", "🥪 tuna sandwhich", "💍 expensive jewelry"],
            index=None,
            key="weapon",
        )

    st.button("Start your quest", on_click=being_quest)


def quest():
    # INITIALIZE NEW STATE
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "quest" not in st.session_state:
        st.session_state["quest"] = {"begun": False}

    if st.session_state["quest"]["begun"] == False:
        show_quest_settings()
    else:
        with st.sidebar:
            # st.write("# Quest Options")
            st.button("Give up the quest", on_click=reset_quest)

        # st.bar_chart({"health": 100, "mana": 100})
        status_cols = st.columns(2)
        with status_cols[0]:
            st.progress(100, text=":green[Health]")
        
        with status_cols[1]:
            st.progress(50, text=":rainbow[Mana]")
        st.write("---")

        st.chat_message("assistant").markdown("Welcome to Grand Quest!")
        st.write("You are in a dark forest. You see a path to the left and a path to the right.")




# def main_page():

#     # initialize the appstate on first run
#     if 'appstate' not in st.session_state:
#         try:
#             st.session_state['appstate']: ChatAppVars = ChatAppVars()
#         except Exception as e:
#             st.error(e)
#             st.exception(e)
#             st.stop()

#     appstate = st.session_state.appstate


#     column_fix()
#     center_text("p", "🧙‍♀️🧚🏻‍♀️", size=60) # or h1, whichever
#     st.header("", divider="rainbow")
