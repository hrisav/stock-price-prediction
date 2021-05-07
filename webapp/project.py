import flask
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method=='GET':
        return "Error : Use Homepage to enter values"
    algorithm=['Simple Average','Moving Average','Simple Exponential Smoothing','Holt Winter Exponential Smoothing','ARIMA','ARCH','GARCH','Random Forest','Gradient Boosting','XG Boost','K Nearest Neighbors','Linear Regression','MARS','Simple RNN','GRU','LSTM','NLP']
    score=[4.188,1.333,1.35,1.1577,0.0153,5.311,3.964,0.4518,0.4509,4.087,4.09,0.046,0.0647,0.1763,0.1982,0.1713]
    model_value=int(request.form['algo'])
    model_name=algorithm[model_value-1]
    if model_value<17:
        score_value="RMSE : "+str(score[model_value-1])
    else:
        score_value=''
    img_path=model_name+'.png'
    return render_template("predict.html",**locals())


if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0")
