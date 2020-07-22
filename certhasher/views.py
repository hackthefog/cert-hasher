from certhasher import app
from flask import render_template, make_response, url_for, send_file, abort, flash, request, redirect
import numpy as np

def keyHash(params):
    params = ['name', str(params[0]), 'role', str(params[1]), 'type', str(params[2])]

    if len(params) % 2 != 0:

        import random

        return ("ERROR: odd number of arguments (" +
        len(params) +
        ") [" +
        random.random() +
        "]")

    def hashParam(inp):
        inp = str(inp)
        
        output = 0

        if len(inp) != 0:
            for i in range(len(inp)):
                char = ord(inp[i])
                
                output = np.int32(output << 5) - output + char
                # print(output)
                output = (output & output)
                # print(output)
        return output

    correctHash = 0
    for i in range(0, len(params), 2):

        correctHash += int(hashParam(params[i] + "|" + params[i + 1])) / len(params)

    correctHash = hashParam(correctHash)
    return correctHash

@app.route('/hash/verify', methods=['GET'])
def hash():
    '''
    Hash here
    '''
    name = request.args['name']
    role = request.args['role']
    typ = request.args['type']

    return str(keyHash([name, role, typ]))

@app.route('/hash/encode', methods=['GET'])
def encode():
    '''
    Hash here
    '''
    name = request.args['name']
    role = request.args['role']
    typ = request.args['type']

    return str(keyHash([name, role, typ]))

@app.route('/generate', methods=['GET'])
def generate():
    '''
    Generate link
    '''
    name = request.args['name']
    role = request.args['role']
    typ = request.args['type']

    key = keyHash([name, role, typ])

    url = f"https://certificate.hackthefog.com?name={name}&role={role}&type={typ}&key={key}"

    return url
