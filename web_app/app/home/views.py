from flask import render_template, jsonify
from . import home
from pycoingecko import CoinGeckoAPI


@home.route("/refreshprices")
def refreshprices():
    cg = CoinGeckoAPI()

    return jsonify(cg.get_price(ids='bitcoin,binance-coin,pancakeswap', vs_currencies='usd'))

@home.route("/")
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template("page/home/index.html", title="Welcome")


@home.route("/dashboard")
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template("page/home/dashboard.html", title="Dashboard")
