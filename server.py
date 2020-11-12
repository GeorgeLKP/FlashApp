from flask import Flask, request, render_template, jsonify, redirect
import json
import requests

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return(render_template('index.html'))

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    API_KEY = '502205cbb8d32fcf3ae32345096641f2'
    city = request.args.get('q')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    #data = response.content
    #temperature = response.content('main')
    temperature = response.json()
    weather = temperature["weather"][0]["description"]
    return 'weather: ' + weather


@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    return redirect("https://www.qoo10.sg/s/SIMILAC-4?keyword=similac+4&keyword_auto_change=", code=302)

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                    <h1>The framework value is: {}</h1>'''.format(language, framework)
                    
    return '''<form method="POST">
                Language: <input type="text" name="language"><br>
                Framework: <input type="test" name+"framework"><br>
                <input type="submit" value="submit"><br>
            </form>'''

if __name__ == '__main__':
    app.run(debug=True)
