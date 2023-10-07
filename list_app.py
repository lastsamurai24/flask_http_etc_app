from flask import Flask, render_template

app = Flask(__name__)


@app.route("/members")
def members():
    # リストの作成
    members = ["Bob", "Tom", "Ken"]
    # 変数membersを渡してあげる
    return render_template("members.html", members=members)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
