from flask import Flask,render_template, flash,redirect,url_for,request,jsonify
from forms import RegistrationForm, LoginForm
from tele import send_message
from db_manage import get_by_id
import json
app = Flask(__name__)


# user defined python functions
from db_manage import get_event_data


app.config['SECRET_KEY'] = 'd5127eb2837a46bbe8f019e561efd53b'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/student",methods =['GET','POST'])
def student():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged In!")
        return redirect(url_for('student_panel'))
    return render_template('studentlogin.html',subject ="Student Login!",form = form)

@app.route("/staff",methods =['GET','POST'])
def staff():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged In!")
        return redirect(url_for('staff_panel'))
    return render_template('staff.html',subject = "Staff Login!", form = form)
@app.route("/hod",methods =['GET','POST'])
def hod():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged In!")
        return redirect(url_for('hod_panel'))
    return render_template('hod.html',subject='Hod Login!',form = form)



@app.route("/student_panel")
def student_panel():
    data = get_event_data()
    # post_data = ''
    # for i in data:
        # post_data+=str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3])+" "+str(i[4])+" "+"\n"
        
    
    return render_template('student_panel.html',post_data = data)


@app.route("/staff_panel")
def staff_panel():
    return render_template('staff_panel.html')

@app.route("/hod_panel")
def hod_panel():
    return render_template('hod_panel.html')


@app.route('/forward',methods=['POST','GET'])
def forward():
    name = "siddu"
    data = request.form
    s = []
    msg = f'{name} wants to join '
    for x  in request.form:
        s.append(request.form.get(x))
    
    with open('snip.txt','w') as f:
        for x in s:
            f.write(x+'-')
    with open('snip.txt','r') as f:
        val = f.readline().split('-')[0]
        a= get_by_id((val)[0])
    for i in a[0]:
        msg+=i
    msg+=" and has requested for attendance!"
    send_message(str(msg))
    return "Request Made!"
        

    


if __name__=='__main__':
    app.run(debug=True)


