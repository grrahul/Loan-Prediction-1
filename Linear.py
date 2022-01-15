import streamlit as st 
import pickle
import numpy as np  


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data 

data = load_model()

linear_reg_load = data["model"]
le_gender = data["le_gender"]
le_married = data["le_married"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Loan Predicition")

    st.write("""### We need some information to predict the loan predicition""")

    st.write(""" ### Model - Linear Regression""")



    gender_1 = {
    "Male",
    "Female",
    }

    marital_status = {
    "Yes",
    "No",
    }

    education = {
    "Graduate",
    "Not Graduate",
    }

    credit_history = {
    "1",
    "0",
    }


    gender = st.selectbox("Gender",gender_1)
    marital_status = st.selectbox("Marital Status",marital_status)
    education = st.selectbox("Education",education)
    credit = st.selectbox("Credit Score",credit_history)
    income = st.slider("Income (in $)", 0, 100000, 1000,100)
    loan_amount = st.slider("Loan Amount (in $)", 0, 1000, 100,10)
    loan_amount_term = st.slider("Loan Amount Term (in months)", 0, 480, 40,20)


    ok = st.button("Calculate Loan Status")
    if ok:
        x = np.array([[gender, marital_status,  education, income, loan_amount, loan_amount_term, credit]])
        x[:, 0] = le_gender.transform(x[:, 0])
        x[:, 1] = le_married.transform(x[:, 1])
        x[:, 2] = le_education.transform(x[:, 2])
        x = x.astype(float)

        loan = linear_reg_load.predict(x)
        if(loan >= 0.5):
            ans = 'Yes'
        else:
            ans = 'No'
        #st.subheader(f"The Loan Approval Status is {loan[0]:.2f}")
        st.subheader(f"The Loan Approval Status  - " + " " + ans)


    
    
