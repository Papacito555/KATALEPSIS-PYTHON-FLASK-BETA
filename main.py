from flask import Flask
from diagnostic.application.DiagnosticController import controller
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(controller)

app.config['SECRET_KEY'] = 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sofnityPass@localhost/katalepsis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()