import streamlit as st
from Adress.Adress import *
import base64



street_name = st.text_input("Give street name:") 

house_nr = st.text_input("give house number:")
postcode = st.text_input("give postcode: ")

if postcode:
    try:
        adress1 = Adress(street_name,house_nr,postcode)

        adress1.open_adress_tiff_url()

        adress1.read_adress_tiff()
        markdown_text = f'<span style="font-family:Courier; color:black; font-size: 20px;">x_coordinate: {adress1.get_x_coordinate()} y_coordinate: {adress1.get_y_coordinate()}</span>'
        st.markdown(markdown_text, unsafe_allow_html=True)
        file_ = open("Assets/cat-typing.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        placeholder = st.empty()
        placeholder2 = st.empty()
        placeholder.text("Calculating chm, It may take about 6 minutes in the meantime enjoy this cat gif")
        cat_html =  f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">'
        placeholder2.markdown(cat_html,unsafe_allow_html=True)
        
        adress1.calculate_chm()
        
        placeholder2.empty()
        placeholder.empty()
        st.write("\n")
        st.write(adress1.get_chm())

        st.pyplot(adress1.plot_3d())
        st.plotly_chart(adress1.go_plot())
    except:
        markdown_text = f'<span style="font-family:Courier; color:black; font-size: 20px;">could not locate the adress please give a an another adress  </span>'
        st.markdown(markdown_text, unsafe_allow_html=True)
    