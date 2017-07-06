from tumbler import Tumbler
app = Tumbler(__name__)


@app.route("/")
def hello():
    return "Hello"
