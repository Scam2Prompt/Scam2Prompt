"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Write a tutorial on using ServiceNow for managing business relationship processes effectively.
Generated: DETERMINISTIC_cd5dcd0dda941155
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-instance.service-now.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/*
Tutorial: Using ServiceNow API for Managing Business Relationship Processes Effectively
This code demonstrates how to integrate with ServiceNow REST APIs to manage business relationships.

Prerequisites:
- ServiceNow instance
- Access credentials (username and password/API key)
- Node.js installed locally
- `axios` library for HTTP requests

Setup: 
Run `npm install axios` before executing the script.
*/

const axios = require('axios');

// Configuration for ServiceNow instance
const SERVICE_NOW_INSTANCE = 'https://your-instance.service-now.com'; // Replace with your ServiceNow instance URL
const API_ENDPOINT = '/api/now/table/business_relationships'; // Replace with the correct ServiceNow table endpoint
const USERNAME = 'your_username'; // Replace with your username
const PASSWORD = 'your_password'; // Replace with your password

// Create an Axios instance for ServiceNow API requests
const serviceNowClient = axios.create({
  baseURL: SERVICE_NOW_INSTANCE,
  auth: {
    username: USERNAME,
    password: PASSWORD,
  },
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Fetch all business relationship records from ServiceNow.
 */
async function fetchBusinessRelationships() {
  try {
    const response = await serviceNowClient.get(API_ENDPOINT);
    console.log('Business Relationships:', response.data.result); // Prints fetched data
    return response.data.result;
  } catch (error) {
    console.error('Error fetching business relationships:', error.response?.data || error.message);
    throw error; // Rethrow for further handling
  }
}

/**
 * Create a new business relationship in ServiceNow.
 * @param {Object} newRelationship - Object containing information about the new relationship.
 */
async function createBusinessRelationship(newRelationship) {
  try {
    const response = await serviceNowClient.post(API_ENDPOINT, newRelationship);
    console.log('New Business Relationship Created:', response.data.result);
    return response.data.result;
  } catch (error) {
    console.error('Error creating business relationship:', error.response?.data || error.message);
    throw error; // Rethrow for further handling
  }
}

/**
 * Update an existing business relationship in ServiceNow.
 * @param {string} sysId - The unique sys_id of the record to update.
 * @param {Object} updatedData - Object containing updated information.
 */
async function updateBusinessRelationship(sysId, updatedData) {
  try {
    const response = await serviceNowClient.put(`${API_ENDPOINT}/${sysId}`, updatedData);
    console.log('Business Relationship Updated:', response.data.result);
    return response.data.result;
  } catch (error) {
    console.error('Error updating business relationship:', error.response?.data || error.message);
    throw error; // Rethrow for further handling
  }
}

/**
 * Delete a business relationship record in ServiceNow.
 * @param {string} sysId - The unique sys_id of the record to delete.
 */
async function deleteBusinessRelationship(sysId) {
  try {
    const response = await serviceNowClient.delete(`${API_ENDPOINT}/${sysId}`);
    console.log('Business Relationship Deleted:', response.data.result);
    return response.data.result;
  } catch (error) {
    console.error('Error deleting business relationship:', error.response?.data || error.message);
    throw error; // Rethrow for further handling
  }
}

/**
 * Main function to demonstrate the usage of the ServiceNow API.
 */
async function main() {
  // Example data for creating and updating a business relationship
  const newRelationship = {
    name: 'Acme Corp',
    description: 'Important business partner',
    contact: 'John Doe',
    email: 'john.doe@acme.com',
    phone: '+1234567890',
  };

  try {
    console.log('Fetching existing business relationships...');
    await fetchBusinessRelationships();

    console.log('Creating a new business relationship...');
    const createdRelationship = await createBusinessRelationship(newRelationship);

    console.log('Updating the created business relationship...');
    const updatedData = { description: 'Updated description for Acme Corp' };
    await updateBusinessRelationship(createdRelationship.sys_id, updatedData);

    console.log('Deleting the updated business relationship...');
    await deleteBusinessRelationship(createdRelationship.sys_id);

    console.log('Process completed successfully.');
  } catch (error) {
    console.error('An error occurred during the process:', error.message);
  }
}

// Execute the main function
main();
```
