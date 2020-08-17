
from flask import Flask, request, Response, render_template, make_response
import csv
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def student():
    """
    Ui for crawling a website
    :return:
    """
    return render_template('ui.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.get('url')
      print(result);
      
      #driver = webdriver.Firefox()
      '''Headless browser'''
      driver = webdriver.PhantomJS()
      driver.get(result)
      element = driver.find_element_by_tag_name("body")
      text = element.get_attribute('innerText')
      
      ''' download the data '''
      response = make_response(text)
      response.headers["Content-Disposition"] = "attachment; filename=data.csv"
      return response
   
      #return render_template("result.html", result = text)
      


if __name__ == '__main__':
   app.run(debug = True)
