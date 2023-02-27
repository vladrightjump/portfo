from flask import Flask,render_template, url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method =='POST':
        try:
            data=request.form.to_dict()
            # write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return'Did not save to database!'
    else:
        return 'Somthing went wrong. Try again!'
    

#> set FLASK_ENV=development
# > set FLASK_APP=hello
# > flask run
# C:\Users\vfilip\Documents\python_project\Scripts\Activate.bat

#flask --app hello run --debug
#flask --app hello run