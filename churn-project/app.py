
#from crypt import methods
import joblib
from flask import Flask , render_template , request
import preprocess

app = Flask(__name__)

scaler= joblib.load('Models/scaler.h5')
model = joblib.load('Models/model.h5')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods= ['POST'])
def get_prediction():
    if request.method == 'POST' :
        gender = request.form['gender']
        SeniorCitizen = request.form['SeniorCitizen']
        Partner = request.form['Partner']
        Dependents = request.form['Dependents']
        tenure = request.form['tenure']
        PhoneService = request.form['PhoneService']
        PaperlessBilling = request.form['PaperlessBilling']
        MonthlyCharges = request.form['MonthlyCharges']
        TotalCharges = request.form['TotalCharges']
        Contract = request.form['Contract']
        PaymentMethod = request.form['PaymentMethod']
        MultipleLines = request.form['MultipleLines']
        InternetService = request.form['InternetService']
        OnlineSecurity = request.form['OnlineSecurity']
        OnlineBackup = request.form['OnlineBackup']
        DeviceProtection = request.form['DeviceProtection']
        TechSupport = request.form['TechSupport']
        StreamingTV = request.form['StreamingTV']
        StreamingMovies = request.form['StreamingMovies']
    data ={'gender': gender , 'SeniorCitizen' : SeniorCitizen ,'Partner': Partner,  'Dependents': Dependents, 'tenure': tenure , 'PhoneService': PhoneService , 'PaperlessBilling': PaperlessBilling, 'MonthlyCharges': MonthlyCharges , 'TotalCharges': TotalCharges , 'Contract':Contract , 'PaymentMethod': PaymentMethod, 'MultipleLines':MultipleLines ,'InternetService': InternetService, 'OnlineSecurity':OnlineSecurity, 'OnlineBackup': OnlineBackup, 'DeviceProtection':DeviceProtection, 'TechSupport': TechSupport, 'StreamingTV': StreamingTV, 'StreamingMovies':StreamingMovies}
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    prediction = model.predict(scaled_data)[0]
    prediction = int(prediction)

    #return str(prediction)

    if prediction == 0:
        
        return  render_template('prediction.html' , x= 'the customer will not leave you' )
    elif prediction ==1:
        
        return  render_template('prediction.html' , x = 'the customer will leave you soon')





if __name__ =='__main__' :
    app.run(debug = True)