from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")

def hello():
    cmd = ["echo", "<html><head><title>Test</title><table border = 1><tr><td><h1>Hello World.</h1></td></tr></table></html>"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out
if __name__ == "__main__" :
    app.run()
