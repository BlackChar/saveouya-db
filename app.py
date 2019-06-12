from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'testsecret'

db = SQLAlchemy(app)

admin = Admin(app)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(60))
    title = db.Column(db.String(255))
    support_email = db.Column(db.String(255))
    support_phone = db.Column(db.String(40))
    website = db.Column(db.String(255))
    founder = db.Column(db.Boolean)
    latest_version = db.Column(db.String(255))
    overview = db.Column(db.String(255))
    content_rating = db.Column(db.String(255))
    rating_avg = db.Column(db.Float(2))
    rating_count = db.Column(db.Integer)
    max_players = db.Column(db.Integer)  # maximum of gamer_count
    developer = db.Column(db.String(255))
    description = db.Column(db.Text)
    premium = db.Column(db.Boolean)
    latest_version_uuid = db.Column(db.String(60))
    first_published = db.Column(db.DateTime)
    last_published = db.Column(db.DateTime)
    last_price = db.Column(db.Float(2))
    images = db.relationship('Image', backref='game', lazy='dynamic')
    files = db.relationship('File',backref='game',lazy='dynamic')


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    filename = db.Column(db.String(255))
    cached_url = db.Column(db.Text)
    origin_url = db.Column(db.Text)
    size = db.Column(db.Integer)
    md5sum = db.Column(db.String(32))
    note = db.Column(db.String(255))
    verified = db.Column(db.Boolean)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)  # 1 for title, 2 for screenshot, 3 for mobileAppIcon
    filename = db.Column(db.String(255))
    cached_url = db.Column(db.Text)
    origin_url = db.Column(db.Text)
    size = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class StoreTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))



admin.add_view(ModelView(Game, db.session))
admin.add_view(ModelView(File, db.session))
admin.add_view(ModelView(Image, db.session))
admin.add_view(ModelView(Genre, db.session))
admin.add_view(ModelView(StoreTag, db.session))

if __name__ == '__main__':
    app.run(debug=True)
