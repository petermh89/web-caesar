from flask import Flask, request
from caesar import  rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method = "POST">
            <label for = "rt"> Rotate by</label>
            <input id="rt" type = "text" name = "rot" value = 0>
            <textarea type= "text" name ="text">{0}</textarea>
           
            <input type = "submit" value = "submit">
            
      </form>
    </body>
</html>"""
@app.route("/", methods=['POST'])
def encrypt():
    new_text=""
    text = request.form["text"]
    rot = request.form["rot"]
    for i in text:
        if i.isalpha():
            x = rotate_character(i, int(rot))
            new_text += x
            
        else:
            new_text += i 

    return form.format(new_text)
@app.route("/")
def index():
    return form.format("")

app.run()