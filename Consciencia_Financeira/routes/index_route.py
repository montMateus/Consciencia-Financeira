from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')

