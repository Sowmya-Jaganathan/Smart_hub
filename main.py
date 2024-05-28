from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="abc123"
app.config["MYSQL_DB"]="flask"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql= MySQL(app)

@app.route('/')
def index():
  return render_template("main.html")

#@app.route('/')
#def pay(): 
 #  if request.method=='POST':
  #    return render_template('payment.html')

@app.route('/lo',methods=['GET','POST'])
def lo():
    if request.method=='POST':
        Username=request.form['Username']
        password=request.form['password']
        con=mysql.connection.cursor()
        sql="select username,password from signup WHERE username=%s and password=%s"
        con.execute(sql,[Username,password])
        mysql.connection.commit()
        con.close()
        return redirect (url_for("index"))
    return render_template("login.html")



@app.route('/signup',methods=['GET','POST'])
def sign():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        con=mysql.connection.cursor()
        sql="insert into signup(username,email,password) value (%s,%s,%s)"
        con.execute(sql,[username,email,password])
        mysql.connection.commit()
        con.close()
        return redirect (url_for("lo"))
    return render_template("signup.html")

@app.route('/forgot password',methods=['GET','POST'])
def forgot():
     if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']
        
        con=mysql.connection.cursor()
        sql="insert into forgot_password(email,password) value(%s,%s)"
        con.execute(sql,[email,password])
        mysql.connection.commit()
        con.close()
        return redirect (url_for("lo"))
     return render_template("forgot password.html")



if __name__ == '__main__':
    app.run(debug=True)