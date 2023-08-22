"""
Currency Convertor App
By: Abhishek Kumar 
"""
#imports
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import requests

#methods
common_currency_codes = (
    'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD',
    'MXN', 'SGD', 'HKD', 'NOK', 'KRW', 'TRY', 'RUB', 'INR', 'BRL', 'ZAR',
    'SAR', 'AED', 'THB', 'PLN', 'DKK', 'MYR', 'IDR', 'TWD', 'QAR', 'COP',
    'ARS', 'CLP', 'PHP', 'CZK', 'EGP', 'ILS', 'KWD', 'HUF', 'NGN', 'RON'
)

def main():
    #main method
    if "name" not in st.session_state:
        user=""
    else:
        user= st.session_state.name
    
    colored_header(
        label="CURRENCY CONVERTOR 💱",
        description=f"Hey {user}!😀 This app will help you check how much amount you will get on converting a currency into other.",
        color_name="violet-70"
    )
    with st.sidebar:
        st.subheader("**Enter the values:**")
        with st.form("currency convertor"):
            current_currency=st.selectbox("select current currency: ", common_currency_codes,placeholder="select the currency")
            convert_currency=st.selectbox("convert to currency: ", common_currency_codes,placeholder="select the currency")
            amount=st.number_input("Amount: ")
            submitted = st.form_submit_button("Submit")
    if submitted:
        api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={convert_currency}&have={current_currency}&amount={amount}'
        response = requests.get(api_url, headers={'X-Api-Key': ''})
        data = response.json()
        if response.status_code == requests.codes.ok:
            add_vertical_space(5)  #creates vertical space
            col1,col2=st.columns(2)
            with col1:
                st.metric(data.get("old_currency"),data.get("old_amount"))
            with col2:
                st.metric(data.get("new_currency"),data.get("new_amount"))
        else:
            #print("Error:", response.status_code, response.text)
            st.error("Error: Unable to process.⌛")

if __name__ == "__main__":
    main()