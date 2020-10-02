from flask import Flask, render_template,request,redirect,url_for , flash , make_response
import json
import requests
from module import get_spoti_info
import sys


app = Flask(__name__)


### PAGINA PRINCIPAL ##
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "POST":
        artist = request.form.get("artist")
        print(artist)
        csv = get_spoti_info("2f6b44cdc0b543ec8a54aed0b588070c","0edbbe90fb3248e98987290336e63c70",artist)
        resp = make_response(csv)
        resp.headers["Content-Disposition"] = "attachment; filename=export_artist.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=5001)

