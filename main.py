import streamlit as st
import pandas


st.set_page_config(layout="wide")


st.title("Best Company Name")
content_first ="""
A scelerisque purus semper eget duis at tellus at urna. Praesent semper feugiat nibh sed pulvinar proin gravida hendrerit. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit. 
At ultrices mi tempus imperdiet nulla malesuada pellentesque elit. Sed sed risus pretium quam vulputate dignissim suspendisse in. Quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus.
Aliquam id diam maecenas ultricies mi eget. Facilisis gravida neque convallis a cras semper auctor neque. Vitae auctor eu augue ut lectus arcu bibendum at varius. Fringilla est ullamcorper eget nulla facilisi etiam dignissim. 
Consequat id porta nibh venenatis cras sed. Ultrices neque ornare aenean euismod elementum nisi quis eleifend. Volutpat blandit aliquam etiam erat velit scelerisque.
"""
st.write(content_first)

col1, col2, col3 = st.columns(3)

workers_content = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in workers_content[0::3].iterrows():
        st.header(f"""{row["first name"]} {row["last name"]}""")
        st.subheader(row["role"])
        st.image("images/" + row["image"])
        
with col2:
    for index, row in workers_content[1::3].iterrows():
        st.header(f'{row["first name"]} {row["last name"]}')
        st.subheader(row["role"])
        st.image("images/" + row["image"])
        
with col3:
    for index, row in workers_content[2::3].iterrows():
        st.header(f'{row["first name"]} {row["last name"]}')
        st.subheader(row["role"])
        st.image("images/" + row["image"])