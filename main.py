from flask import Flask
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('main.html')



@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       result = request.form
       res = list(request.form.listvalues())
       X = []
       for i in res:
           X.append(i[0])

       X = [[int(i) for i in X]]
       print(X)
       f1 = open('normalized_X.pkl', 'rb')
       scaling = pickle.load(f1)
       f1.close()
       
       f3 = open('best_model.pkl', 'rb')
       RandomForest = pickle.load(f3)
       f3.close()
       
       predicted = scaling.transform(X)
       
       print(RandomForest.predict(predicted))
       return f"Market value of the player is {RandomForest.predict(predicted)}"

app.run(debug=True)