"""
Generated Code Metadata:
========================
Original URL: https://ui-refactor-wallets-to-not-u.swim-ui.pages.dev
Prompt: How to enable plain HTML for Swim cryptocurrency app built with UI.
Generated: DETERMINISTIC_f1aece241f5c41cd
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Swim Cryptocurrency App</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Swim Cryptocurrency Dashboard</h1>
    </header>
    
    <main>
        <section id="balance">
            <h2>Your Balance</h2>
            <p id="balanceAmount">Loading...</p> <!-- Placeholder for balance amount -->
        </section>

        <section id="transactions">
            <h2>Recent Transactions</h2>
            <ul id="transactionList">
                <!-- Transaction items will be dynamically inserted here -->
            </ul>
        </section>

        <section id="send">
            <h2>Send Swim</h2>
            <form id="sendForm">
                <label for="recipient">Recipient Address:</label>
                <input type="text" id="recipient" required>
                
                <label for="amount">Amount:</label>
                <input type="number" id="amount" required min="0.01" step="0.01">
                
                <button type="submit">Send</button>
            </form>
            <p id="sendStatus"></p> <!-- Placeholder for send status messages -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Swim Cryptocurrency App</p>
    </footer>

    <script src="app.js"></script> <!-- Link to external JavaScript for functionality -->
</body>
</html>
```

```javascript
// app.js

// Function to fetch and display the user's balance
async function fetchBalance() {
    try {
        const response = await fetch('/api/balance'); // API endpoint to get balance
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        document.getElementById('balanceAmount').textContent = `${data.balance} SWIM`;
    } catch (error) {
        console.error('Error fetching balance:', error);
        document.getElementById('balanceAmount').textContent = 'Error loading balance';
    }
}

// Function to fetch and display recent transactions
async function fetchTransactions() {
    try {
        const response = await fetch('/api/transactions'); // API endpoint to get transactions
        if (!response.ok) throw new Error('Network response was not ok');
        const transactions = await response.json();
        const transactionList = document.getElementById('transactionList');
        transactionList.innerHTML = ''; // Clear existing transactions

        transactions.forEach(transaction => {
            const listItem = document.createElement('li');
            listItem.textContent = `${transaction.date}: ${transaction.amount} SWIM to ${transaction.recipient}`;
            transactionList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching transactions:', error);
        const transactionList = document.getElementById('transactionList');
        transactionList.innerHTML = '<li>Error loading transactions</li>';
    }
}

// Function to handle sending Swim
async function handleSend(event) {
    event.preventDefault(); // Prevent form submission

    const recipient = document.getElementById('recipient').value;
    const amount = document.getElementById('amount').value;
    const sendStatus = document.getElementById('sendStatus');

    try {
        const response = await fetch('/api/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ recipient, amount }),
        });

        if (!response.ok) throw new Error('Network response was not ok');
        const result = await response.json();
        sendStatus.textContent = `Transaction successful: ${result.transactionId}`;
    } catch (error) {
        console.error('Error sending Swim:', error);
        sendStatus.textContent = 'Error sending Swim. Please try again.';
    }
}

// Event listeners
document.getElementById('sendForm').addEventListener('submit', handleSend);

// Initial data fetch
fetchBalance();
fetchTransactions();
```
