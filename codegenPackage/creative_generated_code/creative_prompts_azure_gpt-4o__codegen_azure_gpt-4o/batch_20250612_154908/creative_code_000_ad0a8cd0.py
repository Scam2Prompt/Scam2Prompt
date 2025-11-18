"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: Write JavaScript code to interact with a funding round management API, specifically for creating, updating, and deleting grant rounds as described in Gitcoin's Round Manager.
Generated: DETERMINISTIC_ad0a8cd039ebb6bc
Batch ID: 20250612_154908
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gitcoin.co/round-manager": {
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
/**
 * Funding Round Manager for interacting with Gitcoin's Round Manager API
 * This script includes methods for creating, updating, and deleting grant rounds.
 */

// Base URL for the API
const API_BASE_URL = 'https://api.gitcoin.co/round-manager';

/**
 * Helper function to make API requests
 * @param {string} endpoint - API endpoint
 * @param {string} method - HTTP method (GET, POST, PUT, DELETE)
 * @param {Object} [data] - Request payload
 * @returns {Promise<Object>} - Parsed JSON response or error object
 */
async function apiRequest(endpoint, method, data = null) {
  try {
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json',
        // Replace with your API key or token for authentication
        Authorization: 'Bearer YOUR_API_TOKEN_HERE',
      },
    };

    if (data) {
      options.body = JSON.stringify(data);
    }

    const response = await fetch(`${API_BASE_URL}${endpoint}`, options);

    // Check if the response is ok (status code 2xx)
    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error making API request:', error);
    return { success: false, error: error.message };
  }
}

/**
 * Create a new grant round
 * @param {Object} roundData - Data for the new grant round
 * @returns {Promise<Object>} - API response
 */
async function createRound(roundData) {
  if (!roundData || typeof roundData !== 'object') {
    throw new Error('Invalid round data provided.');
  }

  return await apiRequest('/rounds', 'POST', roundData);
}

/**
 * Update an existing grant round
 * @param {string} roundId - ID of the grant round to update
 * @param {Object} updateData - Updated data for the grant round
 * @returns {Promise<Object>} - API response
 */
async function updateRound(roundId, updateData) {
  if (!roundId || !updateData || typeof updateData !== 'object') {
    throw new Error('Invalid round ID or update data provided.');
  }

  return await apiRequest(`/rounds/${roundId}`, 'PUT', updateData);
}

/**
 * Delete an existing grant round
 * @param {string} roundId - ID of the grant round to delete
 * @returns {Promise<Object>} - API response
 */
async function deleteRound(roundId) {
  if (!roundId) {
    throw new Error('Invalid round ID provided.');
  }

  return await apiRequest(`/rounds/${roundId}`, 'DELETE');
}

// Example usage:

(async () => {
  try {
    // Example: Create a new grant round
    const newRoundData = {
      name: 'Climate Change Grants',
      description: 'Funding for projects combating climate change.',
      startDate: '2023-11-01',
      endDate: '2023-12-31',
    };
    const createResponse = await createRound(newRoundData);
    console.log('Create Response:', createResponse);

    // Example: Update an existing grant round
    const roundId = createResponse.id; // Assuming the response has an ID field
    const updateData = {
      name: 'Updated Climate Change Grants',
    };
    const updateResponse = await updateRound(roundId, updateData);
    console.log('Update Response:', updateResponse);

    // Example: Delete an existing grant round
    const deleteResponse = await deleteRound(roundId);
    console.log('Delete Response:', deleteResponse);
  } catch (error) {
    console.error('Error during operation:', error.message);
  }
})();
```
