from flask import Flask, render_template, request 

app = Flask(__name__)  
 
@app.route('/')  
def index():
    return render_template('index.html')  

@app.route('/stage_B2')
def stage_B2():
    return render_template('stage_B2.html')

@app.route('/cahier_des_charges')
def cahier_des_charges():
    return render_template('cahier_des_charges.html')

@app.route('/a_propos')
def a_propos():
    return render_template('a_propos.html')



if __name__ == "__main__":  
    app.run(debug=True)
