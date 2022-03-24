import requests 

base_url = "https://hsfs7sfy86.execute-api.us-west-1.amazonaws.com/default/cc-default-pred"

# Example of input parameters to use for model 
parameters = {
    "LIMIT_BAL" : 70000, 
    "AGE"       : 30, 
    "PAY_0"     : 1, 
    "PAY_2"     : 1, 
    "PAY_3"     : 1, 
    "PAY_4"     : 1, 
    "PAY_5"     : 1, 
    "PAY_6"     : 1, 
    "BILL_AMT1" : 65802, 
    "BILL_AMT2" : 67369, 
    "BILL_AMT3" : 65701, 
    "BILL_AMT4" : 66782, 
    "BILL_AMT5" : 36137, 
    "BILL_AMT6" : 36894, 
    "PAY_AMT1"  : 3200, 
    "PAY_AMT2"  : 0, 
    "PAY_AMT3"  : 3000, 
    "PAY_AMT4"  : 3000, 
    "PAY_AMT5"  : 1500, 
    "PAY_AMT6"  : 0, 
    "FEMALE"    : 0, 
    "GRAD"      : 0, 
    "UNI"       : 1, 
    "HIGH"      : 0, 
    "EDUC_NA"   : 0, 
    "MARRIED"   : 0
}

locals().update(parameters)

# Endpoints 
p1 = f"?AGE={AGE}&BILL_AMT1={BILL_AMT1}&BILL_AMT2={BILL_AMT2}&"
p2 = f"BILL_AMT3={BILL_AMT3}&BILL_AMT4={BILL_AMT4}&"
p3 = f"BILL_AMT5={BILL_AMT5}&BILL_AMT6={BILL_AMT6}&"
p4 = f"EDUC_NA={EDUC_NA}&FEMALE={FEMALE}&GRAD={GRAD}&"
p5 = f"HIGH={HIGH}&LIMIT_BAL={LIMIT_BAL}&MARRIED={MARRIED}&"
p6 = f"PAY_0={PAY_0}&PAY_2={PAY_2}&PAY_3={PAY_3}&PAY_4={PAY_4}&"
p7 = f"PAY_5={PAY_5}&PAY_6={PAY_6}&PAY_AMT1={PAY_AMT1}&"
p8 = f"PAY_AMT2={PAY_AMT2}&PAY_AMT3={PAY_AMT3}&PAY_AMT4={PAY_AMT4}&"
p9 = f"PAY_AMT5={PAY_AMT5}&PAY_AMT6={PAY_AMT6}&UNI={UNI}"

pars = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9

r = requests.get(base_url + pars).json()

print(r)