from flask import Blueprint, current_app, send_from_directory

logo_bp = Blueprint('logo', __name__)

@logo_bp.route('/logo.png')
def serve_logo():
    return send_from_directory(current_app.static_folder, 'img/logo.png')
