from flask import Flask, request, redirect

app = Flask(__name__)

url_mapping = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_id = str(len(url_mapping) + 1)
        url_mapping[short_id] = original_url

        return f"""
        <h2>Short URL Created!</h2>
        <a href='/{short_id}'>
        http://127.0.0.1:5000/{short_id}
        </a>
        """

    return '''
    <h1>Simple URL Shortener</h1>

    <form method="POST">
        <input type="text"
               name="url"
               placeholder="Enter URL">

        <button type="submit">
        Shorten
        </button>
    </form>
    '''

@app.route('/<short_id>')
def redirect_url(short_id):

    if short_id in url_mapping:
        return redirect(url_mapping[short_id])

    return "URL not found"

if __name__ == '__main__':
    app.run(debug=True)