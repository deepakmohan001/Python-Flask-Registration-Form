from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    phone=request.form['phone']
    email=request.form['email']
    return render_template('register.html',name=name,phone=phone,email=email)



app.add_url_rule('/home','home',home)
if __name__=='__main__':
    app.run(debug=True)
