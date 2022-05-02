import flask_sqlalchemy
db = flask_sqlalchemy.SQLAlchemy()

class Friends(db.Model):
    __tablename__= 'friends'
    id1 = db.Column(db.Integer, primary_key=True)
    id2 = db.Column(db.Integer, primary_key=True)