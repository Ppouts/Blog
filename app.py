import os  
import pyzipper 
import pikepdf  
from flask import Flask, render_template, request 

app = Flask(__name__)  
 
@app.route('/')  
def index():
    return render_template('index.html')  

@app.route('/Stage B3')
def Stage_B3():
    return render_template('Stage B3.html')



if __name__ == "__main__":  
    app.run(debug=True)
