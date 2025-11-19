"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: "Design a simple web application using HTML, CSS, and JavaScript to provide an interface for clients to access and manage their factoring services, including uploading invoices and tracking liquidity."
Generated: DETERMINISTIC_2382b37a793944ff
Batch ID: 20250622_211508
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
  <title>Factoring Services Management</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Factoring Services Management</h1>
  </header>

  <main>
    <!-- Section for uploading invoices -->
    <section id="upload-section">
      <h2>Upload Invoice</h2>
      <form id="upload-form">
        <label for="invoice-file">Select Invoice File:</label>
        <input type="file" id="invoice-file" name="invoice-file" accept=".pdf,.doc,.docx,.jpg,.png" required>
        <button type="submit">Upload</button>
      </form>
      <p id="upload-status"></p>
    </section>

    <!-- Section for tracking liquidity -->
    <section id="liquidity-section">
      <h2>Liquidity Tracker</h2>
      <table id="liquidity-table">
        <thead>
          <tr>
            <th>Invoice ID</th>
            <th>Status</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          <!-- Rows will be dynamically populated -->
        </tbody>
      </table>
    </section>
  </main>

  <footer>
    <p>&copy; 2023 Factoring Services Inc.</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

header {
  background-color: #4CAF50;
  color: white;
  padding: 1rem;
  text-align: center;
}

main {
  padding: 2rem;
}

footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem;
  position: fixed;
  bottom: 0;
  width: 100%;
}

/* Upload section styles */
#upload-section {
  margin-bottom: 2rem;
}

#upload-form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
}

#upload-form label {
  margin-bottom: 0.5rem;
}

#upload-form input {
  margin-bottom: 1rem;
}

#upload-form button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 0.5rem;
  cursor: pointer;
}

#upload-form button:hover {
  background-color: #45a049;
}

#upload-status {
  margin-top: 1rem;
  color: #333;
}

/* Liquidity tracker styles */
#liquidity-section {
  margin-top: 2rem;
}

#liquidity-table {
  width: 100%;
  border-collapse: collapse;
}

#liquidity-table th, #liquidity-table td {
  border: 1px solid #ddd;
  padding: 0.5rem;
  text-align: left;
}

#liquidity-table th {
  background-color: #4CAF50;
  color: white;
}
```

```javascript
// script.js

// Handle invoice upload
document.getElementById('upload-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  const fileInput = document.getElementById('invoice-file');
  const file = fileInput.files[0];

  if (!file) {
    document.getElementById('upload-status').textContent = 'Please select a file to upload.';
    return;
  }

  // Simulate file upload (replace with actual server-side logic)
  document.getElementById('upload-status').textContent = `Uploading ${file.name}...`;

  setTimeout(() => {
    document.getElementById('upload-status').textContent = `File ${file.name} uploaded successfully!`;
  }, 2000);
});

// Simulate liquidity data (replace with actual server-side data fetching)
const liquidityData = [
  { invoiceId: 'INV001', status: 'Paid', amount: '$1,000' },
  { invoiceId: 'INV002', status: 'Pending', amount: '$500' },
  { invoiceId: 'INV003', status: 'Overdue', amount: '$300' },
];

// Populate liquidity table
const liquidityTableBody = document.querySelector('#liquidity-table tbody');
liquidityData.forEach((entry) => {
  const row = document.createElement('tr');
  row.innerHTML = `
    <td>${entry.invoiceId}</td>
    <td>${entry.status}</td>
    <td>${entry.amount}</td>
  `;
  liquidityTableBody.appendChild(row);
});
```
