from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Expecting authors to be comma-separated (e.g., "Alice, Bob, Charlie")
    authors_env = os.environ.get("AUTHORS", "")
    authors = [name.strip() for name in authors_env.split(",") if name.strip()]

    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Creators</title>
      </head>
      <body>
        <header>
          <img src="https://da.upm.es/wp-content/uploads/2018/09/imago.png" alt="Header Image">
        </header>
        <main>
          <h1>Creators</h1>
          <ul>
            {% for creator in authors %}
              <li>{{ creator }}</li>
            {% endfor %}
          </ul>
        </main>
      </body>
    </html>
    """
    return render_template_string(html, authors=authors)

if __name__ == '__main__':
    app.run(debug=True)