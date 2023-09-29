import streamlit as st #all streamlit commands will be available through the "st" alias
import writer_lib as glib #reference to local lib script

#
st.set_page_config(page_title="Prompt to create marketing content") #HTML title
st.title("Personal Write") #page title

col1, col2, col3 = st.columns(3) #create 2 columns



with col1: #everything in this with block will be placed in column 1
    st.subheader("Content generation prompt") #subhead for this column
    input_text = st.text_area("Input text", label_visibility="collapsed") #display a multiline text box with no label
    go_button = st.button("Go", type="primary") #display a primary button


if go_button: #code in this if block will be run when the button is clicked
    with st.spinner("Creating..."): #show a spinner while the code in this with block runs
        response_content = glib.get_text_response(input_content=input_text) #call the model through the supporting library
        prompt_template = f"""Create images based on the description below
        ```
        {response_content}
        ```
        """
        generated_image = glib.get_image_response(prompt_content=prompt_template) #call the model through the supporting library

with col2: #everything in this with block will be placed in column 2
    st.subheader("Text result") #subhead for this column        
    if go_button:
        st.write(response_content)
 
with col3: #everything in this with block will be placed in column 2
    st.subheader("Image result") #subhead for this column        
    if go_button:
        st.image(generated_image) #display the generated image
       
