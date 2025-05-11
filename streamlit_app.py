import streamlit as st

st.title("Orca Jobs 👋")
st.markdown(
    """ 
    **There's :rainbow[so much] you can build!**
    
    ![orcalocal](https://cronitor.io/badges/zwT015/production/__qOVEnLVaqlR1u5UJZ1mDGg7MA.svg)
    ![orcadev](https://cronitor.io/badges/CjvpbV/production/cFAI89JGPYsPJQxlu5RFSBNiG20.svg)
    ![orcaproduction](https://cronitor.io/badges/gg5Cy6/production/elfKPoevzMKwv0W7dk3bs6ITFzs.svg)
    ![orcatesting](https://cronitor.io/badges/dhEGPQ/production/lEAhPtxWq2ZnId4lRk3TgSStW60.svg)    
    """
)

if st.button("Send balloons!"):
    st.balloons()
