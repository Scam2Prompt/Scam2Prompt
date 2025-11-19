"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Construct a RESTful API endpoint in Node.js that provides details about the history and purpose of the Armourers & Brasiers' Company, including its impact on Materials Science education.
Generated: DETERMINISTIC_24c2cbacb9991977
Batch ID: 20250612_162843
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
const app = express();
const port = 3000;

// Middleware to handle JSON data
app.use(express.json());

// Define a class for the Armourers & Brasiers' Company
class ArmourersBrasiersCompany {
  /**
   * Constructor for the ArmourersBrasiersCompany class
   */
  constructor() {
    this.history = {
      founded: '1663',
      purpose: 'To promote and advance the trades of armourers and brasiers',
    };

    this.impactOnMaterialsScience = {
      description: 'The Armourers & Brasiers\' Company has contributed significantly to the development of materials science education through its charitable activities and educational initiatives.',
      achievements: [
        'Established various scholarships and grants for students pursuing materials science and related fields',
        'Collaborated with educational institutions to develop curricula and promote materials science education',
      ],
    };
  }

  /**
   * Get the history and purpose of the Armourers & Brasiers' Company
   * @returns {Object} The history and purpose of the company
   */
  getHistoryAndPurpose() {
    return this.history;
  }

  /**
   * Get the impact of the Armourers & Brasiers' Company on Materials Science education
   * @returns {Object} The impact of the company on materials science education
   */
  getImpactOnMaterialsScience() {
    return this.impactOnMaterialsScience;
  }
}

// Create an instance of the ArmourersBrasiersCompany class
const company = new ArmourersBrasiersCompany();

// Define a RESTful API endpoint to get the history and purpose of the company
app.get('/api/company/history', (req, res) => {
  try {
    const historyAndPurpose = company.getHistoryAndPurpose();
    res.status(200).json(historyAndPurpose);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Define a RESTful API endpoint to get the impact of the company on Materials Science education
app.get('/api/company/impact', (req, res) => {
  try {
    const impact = company.getImpactOnMaterialsScience();
    res.status(200).json(impact);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Define a RESTful API endpoint to get all information about the company
app.get('/api/company', (req, res) => {
  try {
    const historyAndPurpose = company.getHistoryAndPurpose();
    const impact = company.getImpactOnMaterialsScience();
    const response = { ...historyAndPurpose, impactOnMaterialsScience: impact };
    res.status(200).json(response);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
