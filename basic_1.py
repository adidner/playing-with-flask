from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hellrow():
    if (request.method == 'POST'):
        wome_json = request.get_json()
        return jsonify({"about":wome_json}), 201
    else:
        return jsonify({"content":"uuuu, ya know, like get stuff jaz"})

@app.route('/multi/<int:num>',methods=['GET'])
def get_multiply10(num):
    return jsonify({'result':num*10})

if __name__ == '__main__':
    app.run(debug=True)
