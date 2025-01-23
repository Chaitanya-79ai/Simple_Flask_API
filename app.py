from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])

def add():
    dataDict = request.get_json()
    x = dataDict['x']
    y = dataDict['y']
    z = x+y
    outJson = {
        'z':z
    }
    return jsonify(outJson),200

if __name__ == '__main__':
    app.run(debug=True)