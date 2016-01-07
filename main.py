from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """
    Serves a hello world message to our curious user. It looks like this:

    >>> response = app.test_client().get('/')
    >>> response.data.decode()
    'Hello World!'

    :return:
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run()
