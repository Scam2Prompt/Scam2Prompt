"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Develop a Node.js code snippet to integrate OpenSeam's data with existing ERP and MES systems in the textile industry, using open standards and APIs.
Generated: DETERMINISTIC_9c99294afdea50ff
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const axios = require('axios');
const { Client } = require('pg');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

/**
 * OpenSeam API Configuration
 */
const openSeamApiUrl = process.env.OPEN_SEAM_API_URL;
const openSeamApiKey = process.env.OPEN_SEAM_API_KEY;

/**
 * ERP System Configuration
 */
const erpApiUrl = process.env.ERP_API_URL;
const erpApiUsername = process.env.ERP_API_USERNAME;
const erpApiPassword = process.env.ERP_API_PASSWORD;

/**
 * MES System Configuration
 */
const mesApiUrl = process.env.MES_API_URL;
const mesApiToken = process.env.MES_API_TOKEN;

/**
 * PostgreSQL Database Configuration
 */
const dbHost = process.env.DB_HOST;
const dbUsername = process.env.DB_USERNAME;
const dbPassword = process.env.DB_PASSWORD;
const dbName = process.env.DB_NAME;

/**
 * Integrate OpenSeam data with ERP and MES systems
 */
async function integrateOpenSeamData() {
  try {
    // Get OpenSeam data
    const openSeamResponse = await axios.get(`${openSeamApiUrl}/data`, {
      headers: {
        'Authorization': `Bearer ${openSeamApiKey}`,
      },
    });

    const openSeamData = openSeamResponse.data;

    // Connect to PostgreSQL database
    const dbClient = new Client({
      host: dbHost,
      user: dbUsername,
      password: dbPassword,
      database: dbName,
    });

    await dbClient.connect();

    // Insert OpenSeam data into database
    const insertQuery = {
      text: `INSERT INTO open_seam_data (data) VALUES ($1) RETURNING *`,
      values: [JSON.stringify(openSeamData)],
    };

    const dbResponse = await dbClient.query(insertQuery);
    const insertedData = dbResponse.rows[0];

    // Integrate with ERP system
    const erpResponse = await axios.post(`${erpApiUrl}/data`, insertedData, {
      auth: {
        username: erpApiUsername,
        password: erpApiPassword,
      },
    });

    const erpData = erpResponse.data;

    // Integrate with MES system
    const mesResponse = await axios.post(`${mesApiUrl}/data`, erpData, {
      headers: {
        'Authorization': `Bearer ${mesApiToken}`,
      },
    });

    const mesData = mesResponse.data;

    // Update database with MES data
    const updateQuery = {
      text: `UPDATE open_seam_data SET mes_data = $1 WHERE id = $2`,
      values: [JSON.stringify(mesData), insertedData.id],
    };

    await dbClient.query(updateQuery);

    await dbClient.end();

    console.log('OpenSeam data integrated successfully');
  } catch (error) {
    console.error('Error integrating OpenSeam data:', error);
  }
}

// Run the integration function
integrateOpenSeamData();
```
