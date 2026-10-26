
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<center><h2>Student Attendance Tracker</h2><a href="/attendance">Mark Attendance</a></center>'

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/success', methods=['POST'])
def success():
    student_id = request.form['student_id']
    student_name = request.form['student_name']
    attendance_date = request.form['attendance_date']
    status = request.form['status']
    subject_name = request.form.get('subject_name', '')    
    return render_template(
        'success.html',
        student_id=student_id,
        student_name=student_name,
        attendance_date=attendance_date,
        subject_name=subject_name,
        status=status
    )

if __name__ == '__main__':
    app.run(debug=True)
