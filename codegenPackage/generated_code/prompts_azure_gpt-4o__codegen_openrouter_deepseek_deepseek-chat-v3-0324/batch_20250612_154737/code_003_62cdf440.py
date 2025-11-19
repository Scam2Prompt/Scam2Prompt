"""
Generated Code Metadata:
========================
Original URL: https://graph-networks-app.vercel.app
Prompt: Write a function to integrate The Graph Networks Registry v0.0.0 into a web application for real-time graph data visualization.
Generated: DETERMINISTIC_62cdf44011ba5c1c
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// graph-registry-integration.js

const axios = require('axios');
const { createClient } = require('graphql-ws');
const { WebSocket } = require('ws');

/**
 * Integrates The Graph Networks Registry for real-time graph data visualization.
 */
class GraphRegistryIntegration {
  /**
   * Initializes the GraphRegistryIntegration with configuration.
   * @param {Object} config - Configuration object
   * @param {string} config.httpEndpoint - HTTP endpoint for GraphQL queries
   * @param {string} config.wsEndpoint - WebSocket endpoint for subscriptions
   * @param {string} [config.apiKey] - Optional API key for authentication
   */
  constructor(config) {
    if (!config.httpEndpoint || !config.wsEndpoint) {
      throw new Error('HTTP and WebSocket endpoints are required');
    }

    this.httpEndpoint = config.httpEndpoint;
    this.wsEndpoint = config.wsEndpoint;
    this.apiKey = config.apiKey || null;
    this.wsClient = null;
  }

  /**
   * Makes a GraphQL query to the registry.
   * @param {string} query - GraphQL query string
   * @param {Object} [variables] - Query variables
   * @returns {Promise<Object>} - Query result
   */
  async query(query, variables = {}) {
    try {
      const headers = {};
      if (this.apiKey) {
        headers['Authorization'] = `Bearer ${this.apiKey}`;
      }

      const response = await axios.post(
        this.httpEndpoint,
        { query, variables },
        { headers }
      );

      if (response.data.errors) {
        throw new Error(response.data.errors[0].message);
      }

      return response.data.data;
    } catch (error) {
      console.error('Query error:', error.message);
      throw error;
    }
  }

  /**
   * Subscribes to GraphQL subscription for real-time updates.
   * @param {string} subscription - GraphQL subscription string
   * @param {Object} [variables] - Subscription variables
   * @param {Function} callback - Callback for received data
   * @returns {Function} - Function to unsubscribe
   */
  subscribe(subscription, variables = {}, callback) {
    if (!this.wsClient) {
      this.wsClient = createClient({
        url: this.wsEndpoint,
        webSocketImpl: WebSocket,
        connectionParams: this.apiKey ? { Authorization: `Bearer ${this.apiKey}` } : {},
      });
    }

    const unsubscribe = this.wsClient.subscribe(
      { query: subscription, variables },
      {
        next: (data) => callback(null, data),
        error: (err) => callback(err),
        complete: () => console.log('Subscription completed'),
      }
    );

    return unsubscribe;
  }

  /**
   * Disconnects the WebSocket client.
   */
  disconnect() {
    if (this.wsClient) {
      this.wsClient.dispose();
      this.wsClient = null;
    }
  }

  /**
   * Example query to get subgraphs.
   * @returns {Promise<Array>} - List of subgraphs
   */
  async getSubgraphs() {
    const query = `
      query {
        subgraphs {
          id
          displayName
          currentVersion {
            subgraphDeployment {
              ipfsHash
            }
          }
        }
      }
    `;
    return this.query(query);
  }

  /**
   * Example subscription for subgraph updates.
   * @param {Function} callback - Callback for updates
   * @returns {Function} - Function to unsubscribe
   */
  subscribeToSubgraphUpdates(callback) {
    const subscription = `
      subscription {
        subgraphUpdated {
          id
          displayName
          currentVersion {
            subgraphDeployment {
              ipfsHash
            }
          }
        }
      }
    `;
    return this.subscribe(subscription, {}, callback);
  }
}

module.exports = GraphRegistryIntegration;
```
