"""
Generated Code Metadata:
========================
Original URL: https://servicosgm.online
Prompt: Generate a code snippet to handle "Página não encontrada" errors in a web application.
Generated: DETERMINISTIC_477af825d867dd23
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors by rendering a custom 404 page.
    Logs the error and requested path for debugging.
    """
    app.logger.error(f'Page not found: {request.path}')
    return render_template('404.html', 
                         error=error,
                         path=request.path), 404

# Example route that might raise 404
@app.route('/page/<int:page_id>')
def show_page(page_id):
    """
    Example route that could raise a 404 if page doesn't exist.
    """
    # In a real app, you would check if page exists in database
    if page_id > 100:  # Simulating non-existent page
        raise NotFound()
    return f"Page {page_id} content"

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página não encontrada</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #d9534f;
            font-size: 50px;
        }
        p {
            font-size: 20px;
            margin: 20px 0;
        }
        a {
            color: #337ab7;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>Página não encontrada</p>
    <p>A página <strong>{{ path }}</strong> que você está tentando acessar não existe.</p>
    <p><a href="{{ url_for('index') }}">Voltar para a página inicial</a></p>
</body>
</html>
```
