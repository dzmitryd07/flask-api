from flask import Flask, jsonify, request

app = Flask(__name__)

numbers = [
    {
        "number": 111
    }
]


@app.route('/')
def hello_world():
    return jsonify(numbers)


@app.route('/numbers/', methods=['POST'])
def add_number():
    number = request.get_json()
    numbers.append(number)
    return {'id': len(numbers)}, 200


@app.route('/numbers/<int:index>', methods=['GET'])
def get_number(index):
    return jsonify(numbers[index]), 200


@app.route('/numbers/<int:index>', methods=['PUT'])
def update_number(index):
    number = request.get_json()
    numbers[index] = number
    return jsonify(numbers[index]), 200


@app.route('/numbers/<int:index>', methods=['DELETE'])
def delete_number(index):
    numbers.pop(index)
    return 'None', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
