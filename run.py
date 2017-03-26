import os
from flask import Flask, render_template, url_for
from lyrics import word_frequencies
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wordcloud/<artist>/<title>')
def lyrical(artist, title):
    wf = word_frequencies(artist, title)
    return render_template('wordcloud.html', words=wf)

@app.route('/demo1')
def demo1():
    wf = word_frequencies("daft punk","harderbetterfasterstronger")
    return render_template('demo1.html', words=wf, song="mp3/daft.mp3")

@app.route('/demo2')
def demo2():
    wf = word_frequencies("rachel platten","fightsong")
    return render_template('demo2.html', words=wf, song="mp3/fight.mp3")

@app.route('/demo3')
def demo3():
    wf = word_frequencies("the beatles","yellow submarine")
    return render_template('demo3.html', words=wf, song="mp3/yellow.mp3")

"""@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)"""

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
