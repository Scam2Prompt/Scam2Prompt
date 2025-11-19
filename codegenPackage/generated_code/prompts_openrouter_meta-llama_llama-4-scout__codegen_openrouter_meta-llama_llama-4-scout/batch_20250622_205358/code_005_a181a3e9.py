"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Develop a Node.js application to generate a PDF document for a customized Egypt tour package, including details such as itinerary, prices, and customer information, inspired by the services offered by Magic Egypt Tours."
Generated: DETERMINISTIC_a181a3e97280d51f
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const pdfkit = require('pdfkit');
const fs = require('fs');

// Define a class for the Egypt tour package
class EgyptTourPackage {
  /**
   * Constructor for EgyptTourPackage
   * @param {string} customerName - Customer name
   * @param {string} customerEmail - Customer email
   * @param {string} tourName - Tour name
   * @param {string} itinerary - Tour itinerary
   * @param {number} price - Tour price
   * @param {number} duration - Tour duration
   */
  constructor(customerName, customerEmail, tourName, itinerary, price, duration) {
    this.customerName = customerName;
    this.customerEmail = customerEmail;
    this.tourName = tourName;
    this.itinerary = itinerary;
    this.price = price;
    this.duration = duration;
  }
}

// Define a function to generate PDF
function generatePdf(tourPackage) {
  // Create a new PDF document
  const doc = new pdfkit();

  // Set PDF metadata
  doc.fontSize(24).text(`Egypt Tour Package: ${tourPackage.tourName}`, 100, 100);
  doc.moveDown(0.5);

  // Add customer information
  doc.fontSize(18).text('Customer Information:', 100, 150);
  doc.fontSize(14).text(`Name: ${tourPackage.customerName}`, 100, 170);
  doc.fontSize(14).text(`Email: ${tourPackage.customerEmail}`, 100, 190);

  // Add tour details
  doc.moveDown(1);
  doc.fontSize(18).text('Tour Details:', 100, 220);
  doc.fontSize(14).text(`Itinerary: ${tourPackage.itinerary}`, 100, 240);
  doc.fontSize(14).text(`Price: $${tourPackage.price}`, 100, 260);
  doc.fontSize(14).text(`Duration: ${tourPackage.duration} days`, 100, 280);

  // Save PDF to a file
  const pdfFile = `tour_package_${tourPackage.customerName}.pdf`;
  doc.pipe(fs.createWriteStream(pdfFile));
  doc.end();

  return pdfFile;
}

// Create an Express application
const app = express();
app.use(express.json());

// API endpoint to generate PDF
app.post('/generate-pdf', (req, res) => {
  try {
    const { customerName, customerEmail, tourName, itinerary, price, duration } = req.body;
    const tourPackage = new EgyptTourPackage(customerName, customerEmail, tourName, itinerary, price, duration);
    const pdfFile = generatePdf(tourPackage);
    res.status(201).json({ message: 'PDF generated successfully', pdfFile });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error generating PDF' });
  }
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
