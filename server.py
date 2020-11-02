from flask import Flask, url_for, request, jsonify
from markupsafe import escape
from datetime import datetime

app = Flask(__name__)



files = {}

def log(filename, request, code):
    ip = request.remote_addr
    header = request.method
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("var/log/log.lg", "a") as f:
        f.write(f"{ip}  {dt_string}  \"{header} {filename}\" {code}\n")
    
@app.route('/storage/<filename>', methods=['GET'])
def get(filename):
    global files
    if filename in files:
        log(f"/storage/{filename}", request, 200)
        return files[filename], 200

    log(f"/storage/{filename}", request, 404)
    return "", 404

@app.route('/storage/<filename>', methods=['PUT'])
def put(filename):
    global files
    data = request.json
    files[filename] = data
    log(f"/storage/{filename}", request, 201)
    return "", 201

@app.route('/storage/<filename>', methods=['DELETE'])
def profile(filename):
    global files
    if filename in files:
        del files[filename]
    log(f"/storage/{filename}", request, 204)
    return "", 204

@app.route('/<something>', methods=['GET', 'DELETE', 'PUT'])
def smth(something):
    log(something, request, 400)
    return "", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
