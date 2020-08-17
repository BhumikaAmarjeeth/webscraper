import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from flask import Flask, request, Response, render_template, send_file
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    
    
@app.route("/get_site_scrape", methods=["POST", "GET"])
def site_scraper():
    driver = webdriver.Firefox()
    start_url = request.args.get("start_url")
    print (start_url)
    driver.get(start_url)
    element = driver.find_element_by_tag_name("body")
    text = element.get_attribute('innerText')
    print("Sending main file={}", text)
    resp = Response(send_file(text, as_attachment=True), mimetype='application/plain')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)



