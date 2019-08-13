from flask import Flask, request, render_template

app = Flask(__name__)

class Item():
    def __init__(self, name, amounts):
        self.name = name
        self.amounts = amounts


@app.route("/")
def hello():

    # Items = [
    #     Item("Apples", 5),
    #     Item("Computer", 1),
    #     Item("Pear", 4)
    # ]

    Items = [
        {"name": "Apples", "amounts": 5},
        {"name": "Computer", "amounts": 1},
        {"name": "Pear", "amounts": 4}
    ]

    for item in Items:
        item["amounts"] = item["amounts"] * 2

    person = ("Chikamso", "Kanu")

    output = render_template("start.html", person=person , Items=Items)
    return output

@app.route("/test")
def test():
    args =  request.args
    age = args.get("age")
    name = args.get("name")

    return render_template("test.html", name = name, age = age)