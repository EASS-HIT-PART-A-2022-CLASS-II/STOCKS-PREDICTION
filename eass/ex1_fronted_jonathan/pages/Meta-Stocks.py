from main import *

st.set_page_config(page_title="Data Science In Finance Stocks",
                #page_icon=":bar_chart:",
                layout="wide"
                )
st.title("Meta's Stocks:")

start = st.date_input('Start', value=pd.to_datetime('2018-01-01'))
end = st.date_input('End', pd.datetime.now())
#df = yfinance.download("META",start,end)['Adj Close']

#r = httpx.get("http://backend-service:8080/selector/5")
r1 = httpx.get("http://backend-service:8080/Meta")
print(type(r1.json()))
df2 = pd.read_json(r1.json())
st.line_chart(df2["Adj Close"])
st.dataframe(data=df2)

#------------------
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#------------------
#Button to send the data to ML for prediction:
if st.button('Make A Prediction'):
    st.write('Please Wait Making A Prediction . . .') #displayed when the button is clicked
