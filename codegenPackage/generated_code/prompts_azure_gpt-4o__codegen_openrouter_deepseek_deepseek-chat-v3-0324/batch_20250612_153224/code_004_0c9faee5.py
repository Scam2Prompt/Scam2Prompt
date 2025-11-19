"""
Generated Code Metadata:
========================
Original URL: https://corelabs.pe
Prompt: Write JavaScript code for connecting multiple platforms using APIs, inspired by CoreLabs' focus on improving process automation and system interoperability.
Generated: DETERMINISTIC_0c9faee5e29a9b1c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Multi-Platform API Connector
 * Inspired by CoreLabs' focus on process automation and system interoperability
 * 
 * Features:
 * - Connects to multiple platforms via their APIs
 * - Handles authentication, rate limiting, and error handling
 * - Provides unified interface for cross-platform operations
 */

class APIConnector {
  /**
   * Initialize the API Connector with configuration
   * @param {Object} config - Configuration object for APIs
   */
  constructor(config) {
    this.config = config;
    this.platforms = {};
    this.initializePlatforms();
  }

  /**
   * Initialize all configured platforms
   */
  initializePlatforms() {
    for (const [platformName, platformConfig] of Object.entries(this.config.platforms)) {
      try {
        const PlatformClass = require(`./platforms/${platformName}`);
        this.platforms[platformName] = new PlatformClass(platformConfig);
        console.log(`Successfully initialized ${platformName} platform`);
      } catch (error) {
        console.error(`Failed to initialize ${platformName}:`, error.message);
      }
    }
  }

  /**
   * Execute an operation across multiple platforms
   * @param {string} operation - Operation to perform
   * @param {Object} data - Data for the operation
   * @param {Array} targetPlatforms - Platforms to target (empty for all)
   * @returns {Promise<Object>} - Results from all platforms
   */
  async executeOperation(operation, data, targetPlatforms = []) {
    const results = {};
    const platformsToUse = targetPlatforms.length > 0 
      ? targetPlatforms.filter(p => this.platforms[p])
      : Object.keys(this.platforms);

    for (const platform of platformsToUse) {
      try {
        if (!this.platforms[platform][operation]) {
          throw new Error(`Operation ${operation} not supported by ${platform}`);
        }

        results[platform] = await this.platforms[platform][operation](data);
      } catch (error) {
        results[platform] = {
          error: true,
          message: error.message,
          stack: process.env.NODE_ENV === 'development' ? error.stack : undefined
        };
        console.error(`Error executing ${operation} on ${platform}:`, error.message);
      }
    }

    return results;
  }

  /**
   * Get status of all connected platforms
   * @returns {Object} - Status of each platform
   */
  getStatus() {
    const status = {};
    for (const [platform, instance] of Object.entries(this.platforms)) {
      status[platform] = {
        connected: !!instance,
        lastSync: instance?.lastSync || null,
        rateLimit: instance?.rateLimit || null
      };
    }
    return status;
  }
}

// Example platform implementation (Salesforce)
class SalesforcePlatform {
  constructor(config) {
    this.config = config;
    this.authenticated = false;
    this.lastSync = null;
    this.rateLimit = { remaining: 100, limit: 100 };
    this.authenticate();
  }

  async authenticate() {
    // Simulate authentication
    await new Promise(resolve => setTimeout(resolve, 500));
    this.authenticated = true;
    console.log('Salesforce authenticated successfully');
  }

  async createRecord(data) {
    if (!this.authenticated) throw new Error('Not authenticated');
    
    // Simulate API call with rate limiting
    if (this.rateLimit.remaining <= 0) {
      throw new Error('Rate limit exceeded');
    }
    
    this.rateLimit.remaining--;
    this.lastSync = new Date();
    
    // Simulate successful record creation
    return { success: true, id: `salesforce-${Date.now()}`, data };
  }

  async queryRecords(query) {
    if (!this.authenticated) throw new Error('Not authenticated');
    
    // Simulate API call with rate limiting
    if (this.rateLimit.remaining <= 0) {
      throw new Error('Rate limit exceeded');
    }
    
    this.rateLimit.remaining--;
    this.lastSync = new Date();
    
    // Simulate query results
    return {
      success: true,
      records: [
        { id: 'salesforce-1', name: 'Sample Record 1' },
        { id: 'salesforce-2', name: 'Sample Record 2' }
      ]
    };
  }
}

// Example usage
const config = {
  platforms: {
    salesforce: {
      clientId: 'your-client-id',
      clientSecret: 'your-client-secret',
      apiVersion: 'v50.0'
    }
    // Add other platform configurations here
  }
};

// Create connector instance
const apiConnector = new APIConnector(config);

// Example operation
async function exampleUsage() {
  try {
    // Create record across all platforms
    const createResults = await apiConnector.executeOperation(
      'createRecord',
      { name: 'Test Record', type: 'Account' }
    );
    console.log('Create Results:', createResults);

    // Query records from Salesforce only
    const queryResults = await apiConnector.executeOperation(
      'queryRecords',
      { query: 'SELECT Id, Name FROM Account LIMIT 2' },
      ['salesforce']
    );
    console.log('Query Results:', queryResults);

    // Get system status
    console.log('System Status:', apiConnector.getStatus());
  } catch (error) {
    console.error('Error in example usage:', error);
  }
}

// Run example
exampleUsage();
```
