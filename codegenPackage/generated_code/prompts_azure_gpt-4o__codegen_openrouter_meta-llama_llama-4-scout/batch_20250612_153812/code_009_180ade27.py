"""
Generated Code Metadata:
========================
Original URL: https://berachain.crabdance.com
Prompt: Create a user interface design in HTML/CSS for displaying Berachain token eligibility results and NFT holder rules.
Generated: DETERMINISTIC_180ade278db5f65d
Batch ID: 20250612_153812
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
    <title>Berachain Token Eligibility Results</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Berachain Token Eligibility Results</h1>
    </header>
    <main>
        <section id="eligibility-results">
            <h2>Eligibility Results</h2>
            <table id="eligibility-table">
                <thead>
                    <tr>
                        <th>Wallet Address</th>
                        <th>Eligible</th>
                        <th>Token Balance</th>
                    </tr>
                </thead>
                <tbody id="eligibility-table-body">
                    <!-- Eligibility results will be populated here -->
                </tbody>
            </table>
        </section>
        <section id="nft-holder-rules">
            <h2>NFT Holder Rules</h2>
            <ul id="nft-holder-rules-list">
                <li>Must hold a minimum of 1 Berachain NFT</li>
                <li>NFT must be held in the user's wallet for at least 30 days</li>
                <li>NFT must be a valid Berachain NFT (not a duplicate or invalid)</li>
            </ul>
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    margin-top: 0;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}

#nft-holder-rules-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#nft-holder-rules-list li {
    margin-bottom: 0.5em;
}
```

**script.js**
```javascript
// Sample eligibility results data
const eligibilityResults = [
    {
        walletAddress: '0x1234567890abcdef',
        eligible: true,
        tokenBalance: 100
    },
    {
        walletAddress: '0x9876543210fedcba',
        eligible: false,
        tokenBalance: 50
    }
];

// Function to populate eligibility results table
function populateEligibilityTable(results) {
    const tableBody = document.getElementById('eligibility-table-body');
    tableBody.innerHTML = '';

    results.forEach(result => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${result.walletAddress}</td>
            <td>${result.eligible ? 'Yes' : 'No'}</td>
            <td>${result.tokenBalance}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to handle errors
function handleError(error) {
    console.error(error);
    alert('An error occurred: ' + error.message);
}

// Populate eligibility results table on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        populateEligibilityTable(eligibilityResults);
    } catch (error) {
        handleError(error);
    }
});
```
