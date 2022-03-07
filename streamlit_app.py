import streamlit as st
menu_items = {
	'Get help': YOUR_HELP_URL_STRING,
	'Report a bug': YOUR_BUG_PAGE_URL_STRING,
	'About': '''
	 ## My Custom App

	 Some markdown to show in the About dialog.
	'''
}

st.set_page_config(menu_items=menu_items)
st.write("Apilayer")
