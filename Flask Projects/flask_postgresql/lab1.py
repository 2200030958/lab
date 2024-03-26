from flask import Flask, render_template, request, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "123"

conn = psycopg2.connect(
    database="new", user='postgres',
    password='Sai@2004',
    host='127.0.0.1', port='5435'
)

# Creating a cursor object using the cursor() method
with conn:
    with conn.cursor() as cur:
        # Creating table as per requirement
        sql = """CREATE TABLE STUDENTD(
                 REGNUM INT NOT NULL,
                 NAME CHAR(20) NOT NULL,
                 SUBJECT1 CHAR(20),
                 SUBJECT2 CHAR(20)
              );"""
        # cur.execute(sql)
        # conn.commit()

print("Table created successfully........")


@app.route('/')
def welcome():
    return render_template('try1.html')


@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        regnum = request.form.get('regnum', type=int, default=0)
        name = request.form['name']
        subject1 = request.form['subject1']
        subject2 = request.form['subject2']

        with conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO STUDENTD (REGNUM,NAME,SUBJECT1,SUBJECT2) VALUES (%s,%s,%s,%s)",
                            (regnum, name, subject1, subject2))
                flash('Student Added successfully')

        return render_template('Success.html')


@app.route('/view_student', methods=['POST'])
def view_student(regnum):
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM STUDENTD WHERE REGNUM = %s", (regnum,))
            student = cur.fetchone()

    return render_template('view_student.html', student=student)


@app.route('/next')
def next():
    return render_template('try1.html')


if __name__ == "__main__":
    app.run(debug=True)
