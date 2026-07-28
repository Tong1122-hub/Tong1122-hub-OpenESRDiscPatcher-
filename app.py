from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(message='Hello from Flask scaffold!')


def _self_test():
    # Call the view function directly under an application context to avoid
    # compatibility issues with the test client and Werkzeug metadata.
    with app.app_context():
        resp = hello()
        # `hello()` returns a Flask Response; get_json() works on it
        try:
            body = resp.get_json()
        except Exception:
            body = resp.get_data(as_text=True)
        status = getattr(resp, 'status_code', 200)
        print('Flask self-test status:', status)
        print('Flask self-test body:', body)


if __name__ == '__main__':
    _self_test()
