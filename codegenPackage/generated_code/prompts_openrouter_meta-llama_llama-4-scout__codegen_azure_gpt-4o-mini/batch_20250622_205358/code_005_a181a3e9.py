"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Develop a Node.js application to generate a PDF document for a customized Egypt tour package, including details such as itinerary, prices, and customer information, inspired by the services offered by Magic Egypt Tours."
Generated: DETERMINISTIC_a181a3e97280d51f
Batch ID: 20250622_205358
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000/generate-pdf`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const pdf = require('html-pdf');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Serve static files (like CSS) from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to generate PDF for the Egypt tour package
app.post('/generate-pdf', (req, res) => {
    const { customerName, itinerary, price } = req.body;

    // Validate input data
    if (!customerName || !itinerary || !price) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    // Create HTML content for the PDF
    const htmlContent = `
        <html>
            <head>
                <title>Egypt Tour Package</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    h1 { color: #2c3e50; }
                    .itinerary { margin: 20px 0; }
                    .price { font-weight: bold; color: #e74c3c; }
                </style>
            </head>
            <body>
                <h1>Customized Egypt Tour Package</h1>
                <p>Customer Name: ${customerName}</p>
                <div class="itinerary">
                    <h2>Itinerary</h2>
                    <p>${itinerary}</p>
                </div>
                <div class="price">
                    <h2>Price</h2>
                    <p>${price}</p>
                </div>
            </body>
        </html>
    `;

    // Options for PDF generation
    const options = {
        format: 'A4',
        orientation: 'portrait',
        border: {
            top: '1in',
            right: '1in',
            bottom: '1in',
            left: '1in'
        }
    };

    // Generate PDF
    pdf.create(htmlContent, options).toFile('tour-package.pdf', (err, result) => {
        if (err) {
            return res.status(500).json({ error: 'Error generating PDF.' });
        }
        // Send the generated PDF file as a response
        res.download(result.filename, 'Egypt_Tour_Package.pdf', (err) => {
            if (err) {
                return res.status(500).json({ error: 'Error downloading PDF.' });
            }
            // Optionally, delete the file after sending
            fs.unlink(result.filename, (err) => {
                if (err) console.error('Error deleting file:', err);
            });
        });
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Instructions to Run the Application
1. Ensure you have Node.js installed on your machine.
2. Create a new directory for the project and navigate into it.
3. Run `npm init -y` to create a `package.json` file.
4. Install the required packages by running:
   ```bash
   npm install express html-pdf body-parser
   ```
5. Save the above code in a file named `app.js`.
6. Start the application by running:
   ```bash
   node app.js
   ```
7. Use a tool like Postman to send a POST request to `http://localhost:3000/generate-pdf` with a JSON body containing `customerName`, `itinerary`, and `price`.
