from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from .assistant import AssistantManager
import markdown

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
  
    description: str = request.form.get('description')
    field: str = request.form.get('field')
    
    print(description)
    content = {
        "field": field,
        "description": description,
    }
    content = str(content)
    meta_data = 'Recommend only one material and please leave your answer in the following json format.  { title: string (e.g Optimal material for fingerprint replacement), material: string (e.g. Acrylic), reason: string (e.g acrylic is highly biocamptible and as tough as fingerprints), key_properties: array of string(not more than 5) }'
    
    api_prompt = content + '\n' + meta_data
    
    print(api_prompt)
    
    manager = AssistantManager()
    manager.create_assistant()
    manager.create_thread()
    manager.add_message_to_thread(role='user', content=api_prompt)
    manager.run_assistant()
    response = manager.wait_for_completion()
    
    return response # render_template('response.html', response=description)