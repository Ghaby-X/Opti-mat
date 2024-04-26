from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from .assistant import AssistantManager
import json

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return '<p>Blueprint baby</p>'

@bp.route('/form', methods=('GET', 'POST'))
def form():
    return render_template('form.html')

@bp.route('/response', methods =('GET', 'POST'))
def process():
    if request.method == 'GET':
        print('not allowed')
        return 'method not allowed'
    about: str = request.form.get('about')
    function: str = request.form.get('function')
    cost_constraint: str = request.form.get('cost_constraint')
    
    content = {
        "about": about,
        "function": function,
        "cost_constraint": cost_constraint,
    }

    content = str(content)
    meta_data = 'Recommend only one material and please leave your answer in the following json format.  { title: string (e.g Optimal material for fingerprint replacement), material: string (e.g. Acrylic), reason: string (e.g acrylic is highly biocamptible and as tough as fingerprints), key_properties: array of string(not more than 5) }'
    
    api_prompt = content + '\n' + meta_data
    
    manager = AssistantManager()
    manager.create_assistant()
    manager.create_thread()
    manager.add_message_to_thread(role='user', content=api_prompt)
    manager.run_assistant()
    response = manager.wait_for_completion()
    response = json.loads(response)
    
    keys = list(response.keys())
    isPresent = (('material' in keys) and ('title' in keys) and ('reason' in keys) and ('key_properties' in keys))
    print(isPresent)
    
    if len(keys) == 1:
        response = response[keys[0]]
    
    if isPresent:
        print('in here')
        return render_template('response.html', title = response['title'], material=response['material'], reason=response['reason'], key_properties = response['key_properties'])
        

    return render_template('response.html', title='hello', material='helloo', reason='hellooo', key_properties=['helloooooo']) # render_template('error.html')

