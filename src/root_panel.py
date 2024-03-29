# Streamlit-Authenticator, Part 2: Adding advanced features to your authentication component
# https://blog.streamlit.io/streamlit-authenticator-part-2-adding-advanced-features-to-your-authentication-component/

import os
import json
import yaml
import streamlit as st


def root_panel():
    st.write("# 🤴🏻 ROOT PANEL")
    st.session_state.authenticator.logout(f"Logout `{st.session_state.username}`", "main")
    st.header("", divider="rainbow")

    if 'toast_message' in st.session_state:
        # st.toast(st.session_state.toast_message)
        st.toast(st.session_state.toast_message)

    with open("./auth.yaml") as file:
        config = yaml.safe_load(file)

    list_of_usernames = config['credentials']['usernames']
    st.write("""## Authorized users""")
    with st.container(border=True, height=400):
        st.write(list_of_usernames)



    ### CREATE USER
    with st.form("new_user_form", clear_on_submit=True, border=True):
        st.write("## Create user")

        st.text_input("Username", key="new_username")
        st.text_input("Password", key="new_password")

        if st.form_submit_button("🐣 CREATE USER"):
            create_new_user(list_of_usernames=list_of_usernames,
                            username=st.session_state.new_username,
                            password=st.session_state.new_password)

    ### CHANGE PASSWORD
    with st.form("change_password", clear_on_submit=True, border=True):
        st.write("## Change a password")

        st.selectbox("Username", options=list_of_usernames, key="user_to_change", index=None)
        # user a password type so that autocorrect doesn't kick in.. lame I know...
        st.text_input("Password", key="chpass_password", type="password")

        if st.form_submit_button("🔐 CHANGE PASSWORD"):
            create_new_user(list_of_usernames=list_of_usernames,
                            username=st.session_state.user_to_change,
                            password=st.session_state.chpass_password,
                            force_for_password_change=True)

    del list_of_usernames['root'] # DO NOT show the root user in the following selectboxes

    ### DELETE USER
    with st.form("delete_user", clear_on_submit=True, border=True):
        st.write("## Delete user")
        st.selectbox("Username", options=list_of_usernames, key="user_to_delete", index=None)

        if st.form_submit_button(f"💥 DELETE USER"):
                if st.session_state.user_to_delete is None:
                    st.error("Select a user to delete from the dropdown.")
                else:
                    delete_user(st.session_state.user_to_delete)


    ### READ USER CHATS
    # Note: we create the form in this manner to prevent errors that occur when we "nest" elements
    read_user_chats_form = st.form("read_user_chats", clear_on_submit=True, border=True)
    read_user_chats_form.write("## Read user's chat history")
    read_user_chats_form.selectbox("Username", options=list_of_usernames, key="user_to_snoop", index=None)



def create_new_user(list_of_usernames, username: str, password: str, force_for_password_change=False):
    if force_for_password_change is False:
        if st.session_state.new_username == 'root':
            st.error("Can't create a `root` user, dummy!")
            return

        if username in [None, ""] or st.session_state.new_password in [None, ""]:
            st.error("Enter a username and password")
            return

        # check if username is unique
        if username in list_of_usernames:
            st.error(f"User: `{username}` already exists")
            return
    else:
        # we are forcing a password change on an existing user
        if username not in list_of_usernames:
            st.error(f"User: `{username}` does not exist")
            return

    import streamlit_authenticator as stauth
    password_hash = stauth.Hasher([password]).generate()[0]

    with open("./auth.yaml") as file:
        config = yaml.safe_load(file)

    # add user to list and save to file
    config['credentials']['usernames'][username] = {'password': password_hash}
    config['credentials']['usernames'][username]['email'] = f"{username}@plebby.me"
    config['credentials']['usernames'][username]['name'] = f"{username}"

    with open("./auth.yaml", 'w') as file:
        yaml.dump(config, file)

    if force_for_password_change:
        st.session_state.toast_message = f"changed password for: `{username}`"
    else:
        st.session_state.toast_message = f"created user: `{username}`"
    st.rerun()



def delete_user(username: str):

    with open("./auth.yaml") as file:
        config = yaml.safe_load(file)

    # remove 'username' from config
    del config['credentials']['usernames'][username]

    with open("./auth.yaml", 'w') as file:
        yaml.dump(config, file)

    st.session_state.toast_message = f"deleting user: `{username}`"
    st.rerun()
