from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_key', methods=['POST'])
def receive_key():
    key = request.form.get('key')
    if key:
        with open('received_key.txt', 'w') as file:
            file.write(key)
        return jsonify({"message": "Key received and stored"}), 200
    else:
        return jsonify({"message": "No key provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
