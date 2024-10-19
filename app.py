from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"
    system_username = os.getlogin()
    ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput('top -b -n 1')
    
    return f"""
    <h1>Server Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {system_username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=8080)