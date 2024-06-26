from flask import Flask, render_template
import whois

app = Flask(__name__)


def domainCheck(domain):
    try:
        return whois.whois(domain)
    except:
        return None


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/check/<domain>")
def check(domain):
    if "." not in domain:
        domain += ".com"
    result = domainCheck(domain)
    if result:
        return render_template("check.html", result=result, domain=domain)
    else:
        return render_template("domainNotFound.html", domain=domain)


@app.route("/raw/<domain>")
def raw(domain):
    result = domainCheck(domain)
    if result:
        return result
    else:
        return {"error": "Domain not found"}

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
