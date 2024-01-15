from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import json
import html2text

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=true)

def isTrue(value):
    lowerValue = value.lower()
    return lowerValue == 'true' or lowerValue == '1'

@app.route('/', methods=['POST', 'GET'])
def index():
    h2Text = html2text.HTML2Text()

    url = request.args.get('url')
    print(url)
    selector = request.args.get('selector')
    parse = request.args.get('parse', default=0, type=isTrue)
    ignoreLinks = request.args.get('ignoreLinks', default=0, type=isTrue)

    h2Text.ignore_links = ignoreLinks

    page = requests.get(url)
    html = page.text

    soup = BeautifulSoup(html, "html.parser")
    elements = soup.css.select(selector)
    
    # #Add option to remove tags

    elementsList = []
    parsedElement = ""
    
    for element in elements:
        htmlElement = str(element)

        if (parse):
            parsedElement = h2Text.handle(htmlElement)
        else:
            parsedElement = htmlElement

    elementsList.append(parsedElement)

    return jsonify({
        'elements': elementsList
    })