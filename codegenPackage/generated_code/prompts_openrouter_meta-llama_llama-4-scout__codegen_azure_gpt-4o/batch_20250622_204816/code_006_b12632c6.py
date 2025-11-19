"""
Generated Code Metadata:
========================
Original URL: https://nftseahub.com
Prompt: Design a basic user interface for an NFT marketplace like NFTSeaHub, including features for buying, selling, and discovering digital assets.
Generated: DETERMINISTIC_b12632c685d70007
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Database setup
DATABASE = 'nft_marketplace.db'

def init_db():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            owner TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Routes
@app.route('/')
def home():
    """
    Home page route.
    Displays all available NFTs for discovery.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets')
    assets = cursor.fetchall()
    conn.close()
    return render_template('home.html', assets=assets)

@app.route('/buy/<int:asset_id>', methods=['POST'])
def buy(asset_id):
    """
    Route for buying an NFT.
    Updates the owner of the NFT in the database.
    """
    new_owner = request.form.get('new_owner')
    if not new_owner:
        flash('Owner name is required to complete the purchase.', 'error')
        return redirect(url_for('home'))
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('UPDATE assets SET owner = ? WHERE id = ?', (new_owner, asset_id))
    conn.commit()
    conn.close()
    flash('NFT purchased successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    """
    Route for selling an NFT.
    Allows users to list a new NFT for sale.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        owner = request.form.get('owner')

        if not name or not price or not owner:
            flash('Name, price, and owner are required fields.', 'error')
            return redirect(url_for('sell'))

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO assets (name, description, price, owner) VALUES (?, ?, ?, ?)',
                       (name, description, float(price), owner))
        conn.commit()
        conn.close()
        flash('NFT listed for sale successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('sell.html')

@app.route('/discover/<int:asset_id>')
def discover(asset_id):
    """
    Route for discovering details of a specific NFT.
    Displays detailed information about the selected NFT.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets WHERE id = ?', (asset_id,))
    asset = cursor.fetchone()
    conn.close()
    if not asset:
        flash('NFT not found.', 'error')
        return redirect(url_for('home'))
    return render_template('discover.html', asset=asset)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page."""
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates
Below are the basic HTML templates required for the application:

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>NFT Marketplace</title>
</head>
<body>
    <h1>Welcome to NFT Marketplace</h1>
    <a href="/sell">Sell an NFT</a>
    <h2>Available NFTs</h2>
    <ul>
        {% for asset in assets %}
        <li>
            <strong>{{ asset[1] }}</strong> - ${{ asset[3] }} <br>
            Owner: {{ asset[4] }} <br>
            <a href="/discover/{{ asset[0] }}">Discover</a>
            <form action="/buy/{{ asset[0] }}" method="POST">
                <input type="text" name="new_owner" placeholder="Your Name">
                <button type="submit">Buy</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/sell.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Sell NFT</title>
</head>
<body>
    <h1>Sell an NFT</h1>
    <form action="/sell" method="POST">
        <input type="text" name="name" placeholder="NFT Name" required><br>
        <textarea name="description" placeholder="Description"></textarea><br>
        <input type="number" name="price" placeholder="Price" required><br>
        <input type="text" name="owner" placeholder="Your Name" required><br>
        <button type="submit">List NFT</button>
    </form>
</body>
</html>
```

#### `templates/discover.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Discover NFT</title>
</head>
<body>
    <h1>{{ asset[1] }}</h1>
    <p>{{ asset[2] }}</p>
    <p>Price: ${{ asset[3] }}</p>
    <p>Owner: {{ asset[4] }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```

#### `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```
