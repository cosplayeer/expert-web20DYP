from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)


@main.route("/admin")
def index():
    u = current_user()
    # boards = Board.all()
    # print(boards)
    if u.username == 'admin':
        return render_template('board/admin_index.html')
    else:
        abort(403)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Board.new(form)
    return redirect(url_for('topic.index'))

