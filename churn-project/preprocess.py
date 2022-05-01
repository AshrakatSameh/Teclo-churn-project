def pre_gender(gender):
    if gender == 'Female':
        return 0
    elif gender == 'Male':
        return 1
    

def pre_SeniorCitizen(SeniorCitizen):
    if SeniorCitizen == 'Yes':
        return 1
    elif SeniorCitizen =='No':
        return 0
    
    
def pre_Partner(Partner):
    if Partner== 'Yes':
        return 1
    elif Partner=="No":
        return 0
    

def pre_Dependents(Dependents):
    if Dependents== 'Yes':
        return 1
    elif Dependents == 'No':
        return 0
    
    

    
    
    
def pre_PhoneService(PhoneService):
    if PhoneService =="Yes":
        return 1
    elif PhoneService == 'No':
        return 0
    
    
def pre_PaperlessBilling (PaperlessBilling):
    if PaperlessBilling  == 'Yes':
        return 1
    elif PaperlessBilling == 'No':
        return 0
    
    
def pre_MultipleLines(MultipleLines):
    if MultipleLines == 'Yes':
        return [0, 0, 1]
    elif MultipleLines =='No':
        return [1, 0, 0]
    elif MultipleLines == 'No phone service':
        return [0, 1 , 0]
    
    
def pre_InternetService(InternetService):
    if InternetService == 'DSL':
        return [1, 0 ,0]
    elif InternetService == 'Fiber optic':
        return [0, 1 ,0]
    
    elif InternetService == 'No':
        return [0, 0, 1]
    
    
def pre_OnlineSecurity(OnlineSecurity):
    if OnlineSecurity == 'Yes':
        return [0, 0, 1]
    elif OnlineSecurity == 'No':
        return [1, 0, 0]
    elif OnlineSecurity== 'No internet service':
        return [0, 1,0]
    
def pre_OnlineBackup(OnlineBackup):
    if OnlineBackup == 'Yes':
        return [0,0, 1]
    elif OnlineBackup == 'No':
        return [1, 0, 0]
    elif OnlineBackup== 'No internet service':
        return [0, 1, 0]
    
def pre_DeviceProtection(DeviceProtection):
    if DeviceProtection == 'Yes':
        return [0,0,1]
    elif DeviceProtection == 'No':
        return [1,0,0]
    elif DeviceProtection == 'No internet service':
        return [0,1,0]
    
def pre_TechSupport(TechSupport):
    if TechSupport == 'Yes':
        return [0,0,1]
    elif TechSupport == 'No':
        return [1,0,0]
    elif TechSupport == 'No internet service':
        return [0,1,0]
    
    
def pre_StreamingTV(StreamingTV):
    if StreamingTV == 'Yes':
        return [0,0,1]
    elif StreamingTV == 'No':
        return [1,0,0]
    elif StreamingTV == 'No internet service':
        return [0,1,0]
    
    
def pre_StreamingMovies(StreamingMovies):
    if StreamingMovies =='Yes':
        return [0,0,1]
    elif StreamingMovies =='No':
        return [1,0,0]
    elif StreamingMovies =='No internet service':
        return [0,1,0]
    

def pre_Contract(Contract):
    if Contract =='Month-to-month':
        return [1,0,0]
    elif Contract =='One year':
        return [0,1,0]
    elif Contract == 'Two year':
        return [0,0,1]
    
    
def pre_PaperlessBilling(PaperlessBilling):
    if PaperlessBilling =="Yes":
        return 1
    elif PaperlessBilling =="No":
        return 0
    
def pre_PaymentMethod(PaymentMethod):
    if PaymentMethod == 'Mailed check':
        return [0,0,0,1]
    elif PaymentMethod == 'Bank transfer (automatic)':
        return [1,0,0,0]
    elif PaymentMethod == 'Credit card (automatic)':
        return [0,1,0,0]
    elif PaymentMethod =='Electronic check':
        return [0,0,1,0]


def preprocess_data(data):
    gender =  pre_gender(data['gender'])
    SeniorCitizen = pre_SeniorCitizen(data['SeniorCitizen'])
    Partner = pre_Partner(data['Partner'])
    Dependents = pre_Dependents(data['Dependents'])
    tenure = data['tenure']
    PhoneService = pre_PhoneService(data['PhoneService'])
    PaperlessBilling = pre_PaperlessBilling (data['PaperlessBilling'])
    MonthlyCharges = data['MonthlyCharges']
    TotalCharges = data['TotalCharges']
    Contract = pre_Contract(data['Contract'])
    PaymentMethod = pre_PaymentMethod(data['PaymentMethod'])
    MultipleLines = pre_MultipleLines(data['MultipleLines'])
    InternetService = pre_InternetService(data['InternetService'])
    OnlineSecurity = pre_OnlineSecurity(data['OnlineSecurity'])
    OnlineBackup = pre_OnlineBackup(data['OnlineBackup'])
    DeviceProtection= pre_DeviceProtection(data['DeviceProtection'])
    TechSupport = pre_TechSupport(data['TechSupport'])
    StreamingTV = pre_StreamingTV(data['StreamingTV'])
    StreamingMovies = pre_StreamingMovies(data['StreamingMovies'])
    
    final_data = [gender] + [SeniorCitizen] + [Partner] + [Dependents] +  [tenure] + [PhoneService]+ [PaperlessBilling]+ [MonthlyCharges ,TotalCharges]+ Contract + PaymentMethod + MultipleLines+ InternetService+ OnlineSecurity+ OnlineBackup+ DeviceProtection+TechSupport+ StreamingTV+ StreamingMovies
    
    return final_data