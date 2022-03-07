import streamlit as st
menu_items = {
	'Get help': 'http://techmeme.com',
	'Report a bug': 'http://woolwich.xyz,
	'About': '''
	 ## My Custom App

	 Some markdown to show in the About dialog.
	'''
}

st.set_page_config(menu_items=menu_items)
st.write("Apilayer")
