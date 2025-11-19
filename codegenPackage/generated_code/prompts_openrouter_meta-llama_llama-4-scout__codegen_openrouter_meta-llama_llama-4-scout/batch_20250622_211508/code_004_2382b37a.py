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

**index.html**
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
        <section id="invoice-upload">
            <h2>Upload Invoice</h2>
            <form id="invoice-form">
                <label for="invoice-file">Select Invoice File:</label>
                <input type="file" id="invoice-file" accept=".pdf,.docx,.doc">
                <button id="upload-btn">Upload</button>
                <div id="upload-status"></div>
            </form>
        </section>
        <section id="liquidity-tracking">
            <h2>Track Liquidity</h2>
            <table id="liquidity-table">
                <thead>
                    <tr>
                        <th>Invoice ID</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="liquidity-table-body"></tbody>
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

h2 {
    margin-top: 0;
}

#invoice-form {
    display: flex;
    flex-direction: column;
}

#invoice-file {
    padding: 0.5em;
}

#upload-btn {
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#upload-btn:hover {
    background-color: #3e8e41;
}

#upload-status {
    margin-top: 0.5em;
}

#liquidity-table {
    border-collapse: collapse;
    width: 100%;
}

#liquidity-table th, #liquidity-table td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

#liquidity-table th {
    background-color: #f0f0f0;
}
```

**script.js**
```javascript
// Get elements
const invoiceForm = document.getElementById('invoice-form');
const invoiceFileInput = document.getElementById('invoice-file');
const uploadBtn = document.getElementById('upload-btn');
const uploadStatus = document.getElementById('upload-status');
const liquidityTableBody = document.getElementById('liquidity-table-body');

// Set up event listeners
invoiceForm.addEventListener('submit', handleInvoiceUpload);

// Function to handle invoice upload
function handleInvoiceUpload(event) {
    event.preventDefault();

    // Get selected file
    const file = invoiceFileInput.files[0];

    // Check if file is selected
    if (!file) {
        uploadStatus.textContent = 'Please select a file';
        return;
    }

    // Create a new FormData object
    const formData = new FormData();
    formData.append('invoice', file);

    // Send AJAX request to server to upload file
    fetch('/api/upload-invoice', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            uploadStatus.textContent = 'Invoice uploaded successfully';
            invoiceFileInput.value = ''; // Reset file input
            // Fetch and update liquidity table
            fetchLiquidity();
        } else {
            uploadStatus.textContent = 'Error uploading invoice: ' + data.message;
        }
    })
    .catch(error => {
        console.error('Error uploading invoice:', error);
        uploadStatus.textContent = 'Error uploading invoice';
    });
}

// Function to fetch and update liquidity table
function fetchLiquidity() {
    fetch('/api/liquidity')
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const rows = data.liquidity.map(item => {
                return `
                    <tr>
                        <td>${item.invoiceId}</td>
                        <td>${item.amount}</td>
                        <td>${item.status}</td>
                    </tr>
                `;
            }).join('');
            liquidityTableBody.innerHTML = rows;
        } else {
            console.error('Error fetching liquidity:', data.message);
        }
    })
    .catch(error => {
        console.error('Error fetching liquidity:', error);
    });
}

// Initial fetch of liquidity data
fetchLiquidity();
```

**server.js (using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const multer = require('multer');
const upload = multer({ dest: './uploads/' });

// Middleware
app.use(express.json());
app.use(express.static('public'));

// API endpoint to upload invoice
app.post('/api/upload-invoice', upload.single('invoice'), (req, res) => {
    try {
        // Process uploaded invoice
        const invoice = req.file;
        // TO DO: implement invoice processing logic
        res.json({ success: true, message: 'Invoice uploaded successfully' });
    } catch (error) {
        console.error('Error uploading invoice:', error);
        res.json({ success: false, message: 'Error uploading invoice' });
    }
});

// API endpoint to fetch liquidity data
app.get('/api/liquidity', (req, res) => {
    try {
        // TO DO: implement logic to fetch liquidity data
        const liquidity = [
            { invoiceId: 'INV001', amount: 1000, status: 'Pending' },
            { invoiceId: 'INV002', amount: 500, status: 'Approved' },
        ];
        res.json({ success: true, liquidity });
    } catch (error) {
        console.error('Error fetching liquidity:', error);
        res.json({ success: false, message: 'Error fetching liquidity' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
