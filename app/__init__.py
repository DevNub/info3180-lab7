from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'


app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
filefolder = app.config['UPLOAD_FOLDER']

from app import views
