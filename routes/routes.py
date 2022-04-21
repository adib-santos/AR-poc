"""
import time
from flask import render_template
from flask import Blueprint, render_template

blueprint = Blueprint('templates', __name__)

@blueprint.route('/')
def index(): 
    return render_template('templates/index.html')
"""