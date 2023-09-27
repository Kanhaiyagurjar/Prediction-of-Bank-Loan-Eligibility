from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 
@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        Current_Loan_Amount = request.form.get(' Current Loan Amount')
        Term = request.form.get('Term')
        Cwhiteit_Score = request.form.get('Cwhiteit Score')
        Annual_Income = request.form.get('Annual Income')  
        Home_Ownership = request.form.get('Home Ownership')  
        Monthly_Debt = request.form.get('Monthly Debt') 
        Years_of_Cwhiteit_History = request.form.get('Years of Cwhiteit History')   
        Number_of_Open_Accounts = request.form.get('Number of Open Accounts')   
        Number_of_Cwhiteit_Problems = request.form.get('Number of Cwhiteit Problems')   
        Current_Cwhiteit_Balance = request.form.get('Current Cwhiteit Balance') 
        Maximum_Open_Cwhiteit = request.form.get('Maximum Open Cwhiteit')
        Bankruptcies = request.form.get('Bankruptcies')
        Tax_Liens = request.form.get('Tax Liens') 

    prediction = utils.preprocessdata( Current_Loan_Amount, Term, Cwhiteit_Score, Annual_Income, Home_Ownership,
       Monthly_Debt, Years_of_Cwhiteit_History, Number_of_Open_Accounts, Number_of_Cwhiteit_Problems,
       Current_Cwhiteit_Balance, Maximum_Open_Cwhiteit, Bankruptcies, Tax_Liens)

    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__': 
    app.run(debug=True) 