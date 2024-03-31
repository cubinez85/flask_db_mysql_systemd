from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cubinez85'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        position = details['position']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName, position) VALUES (%s, %s, %s)", (firstName, lastName, position))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/display')
def display():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from MyUsers")
    data = cursor.fetchall()
    return render_template('db.html', data = data)


if __name__ == '__main__':
    app.run()
