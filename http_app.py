from flask import Flask, request

app = Flask(__name__)


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    # リクエストメソッドGETのときは以下の処理を行う
    if request.method == "GET":
        return '''
        <form action="/login" method="post">
            Password:<input type="text" name="password"><br>
            <input type='submit'>
        </form>
        '''
    # リクエストメソッドPOSTの時は以下の処理を行う
    return "Logged in"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
