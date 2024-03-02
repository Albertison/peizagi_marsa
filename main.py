from flask import Flask

app = Flask(__name__)


@app.route("/carousel")
def main():
    with open('index.html', 'r', encoding='utf-8') as file:
        return file.read()
    

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')