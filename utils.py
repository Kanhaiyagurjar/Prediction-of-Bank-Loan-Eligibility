import numpy as np 
import joblib 


def preprocessdata( Current_Loan_Amount, Term, Cwhiteit_Score, Annual_Income, Home_Ownership,
       Monthly_Debt, Years_of_Cwhiteit_History, Number_of_Open_Accounts, Number_of_Cwhiteit_Problems,
       Current_Cwhiteit_Balance, Maximum_Open_Cwhiteit, Bankruptcies, Tax_Liens):
    test_data = [[ Current_Loan_Amount, Term, Cwhiteit_Score, Annual_Income, Home_Ownership,
       Monthly_Debt, Years_of_Cwhiteit_History, Number_of_Open_Accounts, Number_of_Cwhiteit_Problems,
       Current_Cwhiteit_Balance, Maximum_Open_Cwhiteit, Bankruptcies, Tax_Liens] ]  
    trained_model = joblib.load("model.pkl") 
    prediction = trained_model.predict(test_data) 

    return prediction 