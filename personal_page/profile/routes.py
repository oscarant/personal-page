from flask import render_template, redirect, url_for, request, Blueprint, current_app as app
from . import models
import git

profile_bp = Blueprint('profile', __name__, static_url_path="",
                       static_folder="static",
                       template_folder="templates"
                       )


@profile_bp.route("/")
def profile():
    return 'Hello World!'


@profile_bp.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/Oscaran02/personal_page')
        origin = repo.remotes.origin
        origin.pull()
        return 'Update successful', 200
    else:
        return 'Wrong event type', 400