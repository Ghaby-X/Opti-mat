from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from .assistant import AssistantManager

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return '<p>Blueprint baby</p>'

@bp.route('/form', methods=('GET', 'POST'))
def form():
    return render_template('form.html')

@bp.route('/response', methods =('GET', 'POST'))
def response():
    if request.method == 'GET':
        return 'method not allowed'
    
    description = request.form.get('description')
    
    manager = AssistantManager()
    manager.create_assistant()
    manager.create_thread()
    manager.add_message_to_thread(role='user', content=description)
    manager.run_assistant()
    response = manager.wait_for_completion()

    return render_template('response.html', response=response)