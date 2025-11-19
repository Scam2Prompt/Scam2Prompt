"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Generate a JavaScript code snippet to create a simple webpage for displaying available medical specialties and their corresponding prices, similar to Asbeviclin's services page.
Generated: DETERMINISTIC_a5dca02f32964116
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// medical-specialties.js

class MedicalSpecialty {
  /**
   * Represents a medical specialty with a name and price.
   * @param {string} name - The name of the medical specialty.
   * @param {number} price - The price of the medical specialty.
   */
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

class MedicalSpecialtiesPage {
  /**
   * Represents a webpage for displaying medical specialties and their prices.
   */
  constructor() {
    this.specialties = [];
  }

  /**
   * Adds a medical specialty to the page.
   * @param {MedicalSpecialty} specialty - The medical specialty to add.
   */
  addSpecialty(specialty) {
    this.specialties.push(specialty);
  }

  /**
   * Renders the medical specialties page.
   */
  render() {
    const html = `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Medical Specialties</title>
        <style>
          body {
            font-family: Arial, sans-serif;
          }
          table {
            border-collapse: collapse;
          }
          th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
          }
        </style>
      </head>
      <body>
        <h1>Medical Specialties</h1>
        <table>
          <thead>
            <tr>
              <th>Specialty</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody id="specialties-table-body">
          </tbody>
        </table>

        <script>
          // Render specialties data
          const specialtiesData = ${JSON.stringify(this.specialties.map(s => ({ name: s.name, price: s.price })))};

          const specialtiesTableBody = document.getElementById('specialties-table-body');

          specialtiesData.forEach(specialty => {
            const row = document.createElement('tr');
            row.innerHTML = `
              <td>${specialty.name}</td>
              <td>$${specialty.price.toFixed(2)}</td>
            `;
            specialtiesTableBody.appendChild(row);
          });
        </script>
      </body>
      </html>
    `;

    return html;
  }
}

// Example usage
function main() {
  try {
    const page = new MedicalSpecialtiesPage();

    // Add medical specialties
    page.addSpecialty(new MedicalSpecialty('Cardiology', 100));
    page.addSpecialty(new MedicalSpecialty('Neurology', 200));
    page.addSpecialty(new MedicalSpecialty('Oncology', 300));

    // Render the page
    const html = page.render();
    console.log(html);

    // Save to file or serve
    // For demonstration purposes, we'll just save to a file
    const fs = require('fs');
    fs.writeFileSync('medical-specialties.html', html);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
