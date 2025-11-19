"""
Generated Code Metadata:
========================
Original URL: https://vsisithashai.pages.dev
Prompt: Create a Node.js code example to interact with a cryptocurrency mining facility's API, such as Hash AI's, to retrieve mining efficiency metrics and optimize mining operations.
Generated: DETERMINISTIC_9576796df8d1b19a
Batch ID: 20250622_210443
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hashai.example.com/v1": {
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
const axios = require('axios');
const { performance } = require('perf_hooks');

// Configuration for the mining API
const MINING_API_CONFIG = {
  baseURL: 'https://api.hashai.example.com/v1',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.MINING_API_KEY}`
  }
};

// Initialize API client
const miningApiClient = axios.create(MINING_API_CONFIG);

/**
 * Retrieves mining efficiency metrics from the API
 * @param {string} minerId - ID of the mining rig
 * @returns {Promise<Object>} Mining efficiency metrics
 */
async function getMiningEfficiencyMetrics(minerId) {
  try {
    const response = await miningApiClient.get(`/miners/${minerId}/efficiency`);
    return response.data;
  } catch (error) {
    throw new Error(`Failed to fetch efficiency metrics: ${error.message}`);
  }
}

/**
 * Optimizes mining operations based on current metrics
 * @param {string} minerId - ID of the mining rig
 * @param {Object} optimizationParams - Parameters for optimization
 * @returns {Promise<Object>} Optimization result
 */
async function optimizeMiningOperations(minerId, optimizationParams) {
  try {
    const startTime = performance.now();
    const response = await miningApiClient.post(
      `/miners/${minerId}/optimize`,
      optimizationParams
    );
    const endTime = performance.now();
    
    return {
      ...response.data,
      optimizationDuration: endTime - startTime
    };
  } catch (error) {
    throw new Error(`Optimization failed: ${error.message}`);
  }
}

/**
 * Main function to demonstrate mining optimization workflow
 */
async function main() {
  try {
    const minerId = 'rig-12345';
    
    // Get current efficiency metrics
    const metrics = await getMiningEfficiencyMetrics(minerId);
    console.log('Current Mining Metrics:', metrics);
    
    // Optimize based on metrics
    const optimizationParams = {
      algorithm: metrics.recommendedAlgorithm,
      powerMode: 'balanced',
      threshold: metrics.currentEfficiency * 1.1 // Aim for 10% improvement
    };
    
    const result = await optimizeMiningOperations(minerId, optimizationParams);
    console.log('Optimization Result:', result);
    
  } catch (error) {
    console.error('Mining operation error:', error.message);
    process.exit(1);
  }
}

// Execute main function if this is the main module
if (require.main === module) {
  if (!process.env.MINING_API_KEY) {
    console.error('Error: MINING_API_KEY environment variable is required');
    process.exit(1);
  }
  
  main();
}

module.exports = {
  getMiningEfficiencyMetrics,
  optimizeMiningOperations
};
```
