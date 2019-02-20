from flask import render_template, Blueprint

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.html')