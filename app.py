from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Expecting server name from environment (e.g., set SERVER_NAME="My Server")
    server_name = os.environ.get("SERVER_NAME", "Default Server Name")

    html = """
    <!doctype html>
    <html lang="en">
      <head>
      <meta charset="utf-8">
      <title>Server Name</title>
      </head>
      <body>
      <header>
        <img src="https://da.upm.es/wp-content/uploads/2018/09/imago.png" alt="Header Image">
      </header>
      <main>
        <h1>Odin</h1>
        <p>{{ server_name }}</p>
      </main>
      </body>
    </html>
    """
    return render_template_string(html, server_name=server_name)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")