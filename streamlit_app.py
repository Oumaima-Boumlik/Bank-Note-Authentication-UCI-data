import pickle
import streamlit as st 


pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;"> Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type variance Here")
    skewness = st.text_input("Skewness", "Type skewness Here")
    curtosis = st.text_input("Curtosis", "Type curtosis Here")
    entropy = st.text_input("Entropy", "Type entropy Here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
    st.success('The predicted value is {}'.format(result))


if __name__ == '__main__':
    main()
