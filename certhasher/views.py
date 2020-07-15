from certhasher import app
from flask import render_template, make_response, url_for, send_file, abort, flash, request, redirect


@app.route('/hash/verify/<name>', methods=['GET'])
def index(name):
    '''
    Hash here
    '''
    return True