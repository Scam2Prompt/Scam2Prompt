"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Design a simple web page using HTML and CSS to display information about a new cryptocurrency token, including its tokenomics and exchange listings, inspired by the Simon's Cat Token website.
Generated: DETERMINISTIC_7b73a78244411373
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Cryptocurrency Token</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#tokenomics">Tokenomics</a></li>
                <li><a href="#exchange-listings">Exchange Listings</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="token-info">
            <h1>New Cryptocurrency Token</h1>
            <p>Token Name: <span id="token-name">Token Name</span></p>
            <p>Token Symbol: <span id="token-symbol">TKN</span></p>
            <p>Token Description: <span id="token-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span></p>
        </section>
        <section id="tokenomics">
            <h2>Tokenomics</h2>
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Percentage</th>
                    </tr>
                </thead>
                <tbody id="tokenomics-table">
                    <!-- tokenomics data will be populated here -->
                    <tr>
                        <td>Team</td>
                        <td>10%</td>
                    </tr>
                    <tr>
                        <td>Advisors</td>
                        <td>5%</td>
                    </tr>
                    <tr>
                        <td>Community</td>
                        <td>85%</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section id="exchange-listings">
            <h2>Exchange Listings</h2>
            <table>
                <thead>
                    <tr>
                        <th>Exchange</th>
                        <th>Pair</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody id="exchange-listings-table">
                    <!-- exchange listings data will be populated here -->
                    <tr>
                        <td>Binance</td>
                        <td>TKN/USDT</td>
                        <td>$0.10</td>
                    </tr>
                    <tr>
                        <td>Huobi</td>
                        <td>TKN/USDT</td>
                        <td>$0.10</td>
                    </tr>
                </tbody>
            </table>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}
```

**script.js**
```javascript
// Populate token info
const tokenInfo = {
    name: 'New Cryptocurrency Token',
    symbol: 'TKN',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
};

document.getElementById('token-name').textContent = tokenInfo.name;
document.getElementById('token-symbol').textContent = tokenInfo.symbol;
document.getElementById('token-description').textContent = tokenInfo.description;

// Populate tokenomics table
const tokenomicsData = [
    { category: 'Team', percentage: '10%' },
    { category: 'Advisors', percentage: '5%' },
    { category: 'Community', percentage: '85%' },
];

const tokenomicsTable = document.getElementById('tokenomics-table');
tokenomicsData.forEach((data) => {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${data.category}</td>
        <td>${data.percentage}</td>
    `;
    tokenomicsTable.appendChild(row);
});

// Populate exchange listings table
const exchangeListingsData = [
    { exchange: 'Binance', pair: 'TKN/USDT', price: '$0.10' },
    { exchange: 'Huobi', pair: 'TKN/USDT', price: '$0.10' },
];

const exchangeListingsTable = document.getElementById('exchange-listings-table');
exchangeListingsData.forEach((data) => {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${data.exchange}</td>
        <td>${data.pair}</td>
        <td>${data.price}</td>
    `;
    exchangeListingsTable.appendChild(row);
});
```
