"""
Generated Code Metadata:
========================
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Generate a code snippet to redirect users to a webpage with instructions on enabling JavaScript, if JavaScript is disabled in their browser.
Generated: DETERMINISTIC_eb8d341bf0d4174a
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Disabled</title>
    <noscript>
        <meta http-equiv="refresh" content="0;url=/enable-javascript">
    </noscript>
</head>
<body>
    <noscript>
        You are being redirected to a page with instructions on enabling JavaScript...
    </noscript>
</body>
</html>
```

```python
# For a Python/Flask solution

from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enable-javascript')
def enable_javascript():
    return render_template('enable-javascript.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- enable-javascript.html template -->

<!DOCTYPE html>
<html>
<head>
    <title>Enable JavaScript</title>
</head>
<body>
    <h1>JavaScript is Disabled</h1>
    <p>Please enable JavaScript in your browser to continue.</p>
    <ol>
        <li>For Chrome: Settings > Advanced > Site Settings > JavaScript</li>
        <li>For Firefox: Options > Content > Enable JavaScript</li>
        <li>For Safari: Preferences > Security > Enable JavaScript</li>
    </ol>
</body>
</html>
```

```javascript
// Alternatively, using JavaScript to detect and redirect

function detectJavascript() {
    try {
        return window.self !== window.top;
    } catch (e) {
        return true; // assume JS is enabled if an error occurs
    }
}

function redirectToEnableJavascript() {
    window.location.href = '/enable-javascript';
}

if (!detectJavascript()) {
    redirectToEnableJavascript();
}
```
