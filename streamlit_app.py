import streamlit as st

st.set_page_config(layout="wide"
                  
                  )

#hide_menu_style = """
#        <style>
#        #MainMenu {visibility: hidden;}
#        </style>
#        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

c1, c2 = st.columns((1, 1))

c1.text_input('Enter your website url', 'http://www.gmail.com',48)

c2.text_input('Enter your website url', 'http://www.hotmail.com',48)

