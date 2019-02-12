from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitch) > 0)

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitch) > 0)

photos = UploadSet('photos',IMAGES)
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitch) > 0)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    login_manager.init_app(app)

    #configure UploadSet
    configure_uploads(app,photos)
    mail.init_app(app)

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #registering our blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app
