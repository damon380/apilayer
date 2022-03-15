import streamlit as st


st.set_page_config(layout="wide", 
#                   menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!",
#         'View app source':"# This is a header. This is an *extremely* cool app!"
#        }
# menu_items={'View App Source' : None}                 
                  )

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)



@st.cache(suppress_st_warning=True)
def main():
    st.header('Text and Audio Extractor with Streamlit')
    st.sidebar.title("Text and Audio Extractor")
    st.sidebar.header("Extract from PDF")
    page = st.sidebar.selectbox("Tool", ["Text Extractor", "Audio Extractor"])

    if  page == 'Text Extractor':
        st.title('Text Extractor')
        c1, c2 = st.columns((1, 1))
        c1.text_input('Enter your website url', 'http://www.gmail.com',48)
        c2.text_input('Enter your website url', 'http://www.hotmail.com',48)


        

    elif page == 'Audio Extractor':
        st.title('Audio Extractor')
        
                    
    else:
        st.write( 'Error404')
    
if __name__ == '__main__':
    main()
