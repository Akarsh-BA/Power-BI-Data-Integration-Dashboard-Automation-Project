from flask import Flask, jsonify

import pandas as pd

app = Flask(__name__)

@app.route("/car_Sales")
def car_Sales():
    
    df = pd.read_csv(r"C:\Resume got self\car_sales_data.csv")

    
    return df.to_json(orient="records")

if __name__== "__main__":
    app.run (port=5000,debug=True)
    

