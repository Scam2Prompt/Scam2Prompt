"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.ebookzone.club
Prompt: Write a Python function to check if a user is logged in to a website before allowing access to downloadable book formats like RTF and FB2.
Generated: DETERMINISTIC_1c593a55043b8d34
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from functools import wraps
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

def login_required(f):
    """
    Decorator to check if a user is logged in.
    
    Args:
        f: The function to wrap.
        
    Returns:
        The wrapped function or a redirect to the login page.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # User is not logged in; redirect to login page
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login page for users.
    Handles both displaying the login form and processing login requests.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Authentication placeholder (replace with actual authentication logic)
        if username == 'admin' and password == 'password':  # Example credentials
            session['user_id'] = username
            return redirect(url_for('download_books'))
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/download_books')
@login_required
def download_books():
    """
    Page for downloading book formats (RTF and FB2).
    Accessible only to logged-in users.
    """
    return '''
        <h1>Download Books</h1>
        <ul>
            <li><a href="/download/book1.rtf">Download Book 1 (RTF)</a></li>
            <li><a href="/download/book2.fb2">Download Book 2 (FB2)</a></li>
        </ul>
    '''

@app.route('/download/<file_format>')
@login_required
def download(file_format):
    """
    Endpoint to handle the actual file download.
    
    Args:
        file_format: The format of the book to download (e.g., 'book1.rtf').
        
    Returns:
        A file response to download the specified book format.
    """
    try:
        # Placeholder for actual file path
        file_path = f'books/{file_format}'  # Ensure the file exists on the server
        return app.send_static_file(file_path)  # Use Flask's static file serving
    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f"Error downloading file {file_format}: {e}")
        return "The requested file could not be downloaded.", 404

@app.route('/logout')
def logout():
    """
    Logout the user and clear the session.
    """
    session.pop('user_id', None)  # Clear user session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
