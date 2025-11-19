"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Create a Node.js module to integrate with a logistics platform, enabling the management of cargo transportation services, such as those provided by Operadora Portuaria del Caribe."
Generated: DETERMINISTIC_c62468f390a6b703
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Module for integrating with Operadora Portuaria del Caribe logistics platform
 * Provides functionality to manage cargo transportation services
 */

const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

class LogisticsClient {
  /**
   * Initialize the logistics client
   * @param {Object} config - Configuration object
   * @param {string} config.apiBaseUrl - Base URL for the API
   * @param {string} config.apiKey - API key for authentication
   * @param {number} [config.timeout=5000] - Request timeout in milliseconds
   */
  constructor(config) {
    if (!config.apiBaseUrl || !config.apiKey) {
      throw new Error('Missing required configuration parameters: apiBaseUrl and apiKey');
    }

    this.config = {
      timeout: 5000,
      ...config
    };

    this.client = axios.create({
      baseURL: this.config.apiBaseUrl,
      timeout: this.config.timeout,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.config.apiKey}`
      }
    });
  }

  /**
   * Create a new cargo shipment
   * @param {Object} shipmentData - Shipment details
   * @param {string} shipmentData.origin - Origin location
   * @param {string} shipmentData.destination - Destination location
   * @param {string} shipmentData.cargoType - Type of cargo
   * @param {number} shipmentData.weight - Weight in kg
   * @param {number} shipmentData.volume - Volume in cubic meters
   * @param {Date} shipmentData.pickupDate - Scheduled pickup date
   * @param {Date} shipmentData.deliveryDate - Expected delivery date
   * @returns {Promise<Object>} - Created shipment details
   */
  async createShipment(shipmentData) {
    try {
      const requiredFields = ['origin', 'destination', 'cargoType', 'weight', 'volume'];
      for (const field of requiredFields) {
        if (!shipmentData[field]) {
          throw new Error(`Missing required field: ${field}`);
        }
      }

      const payload = {
        shipmentId: uuidv4(),
        ...shipmentData,
        status: 'CREATED',
        createdAt: new Date().toISOString()
      };

      const response = await this.client.post('/shipments', payload);
      return response.data;
    } catch (error) {
      this._handleError(error);
    }
  }

  /**
   * Get shipment details by ID
   * @param {string} shipmentId - Shipment ID
   * @returns {Promise<Object>} - Shipment details
   */
  async getShipment(shipmentId) {
    try {
      if (!shipmentId) {
        throw new Error('Shipment ID is required');
      }

      const response = await this.client.get(`/shipments/${shipmentId}`);
      return response.data;
    } catch (error) {
      this._handleError(error);
    }
  }

  /**
   * Update shipment status
   * @param {string} shipmentId - Shipment ID
   * @param {string} status - New status
   * @param {string} [notes] - Optional notes about the status change
   * @returns {Promise<Object>} - Updated shipment details
   */
  async updateShipmentStatus(shipmentId, status, notes) {
    try {
      if (!shipmentId || !status) {
        throw new Error('Shipment ID and status are required');
      }

      const payload = {
        status,
        updatedAt: new Date().toISOString()
      };

      if (notes) {
        payload.notes = notes;
      }

      const response = await this.client.patch(`/shipments/${shipmentId}/status`, payload);
      return response.data;
    } catch (error) {
      this._handleError(error);
    }
  }

  /**
   * List all shipments with optional filters
   * @param {Object} [filters] - Optional filters
   * @param {string} [filters.status] - Filter by status
   * @param {Date} [filters.startDate] - Filter by start date
   * @param {Date} [filters.endDate] - Filter by end date
   * @returns {Promise<Array>} - List of shipments
   */
  async listShipments(filters = {}) {
    try {
      const params = {};
      if (filters.status) params.status = filters.status;
      if (filters.startDate) params.startDate = filters.startDate.toISOString();
      if (filters.endDate) params.endDate = filters.endDate.toISOString();

      const response = await this.client.get('/shipments', { params });
      return response.data;
    } catch (error) {
      this._handleError(error);
    }
  }

  /**
   * Cancel a shipment
   * @param {string} shipmentId - Shipment ID
   * @param {string} [reason] - Reason for cancellation
   * @returns {Promise<Object>} - Cancellation confirmation
   */
  async cancelShipment(shipmentId, reason) {
    try {
      if (!shipmentId) {
        throw new Error('Shipment ID is required');
      }

      const payload = {
        cancelledAt: new Date().toISOString(),
        status: 'CANCELLED'
      };

      if (reason) {
        payload.cancellationReason = reason;
      }

      const response = await this.client.put(`/shipments/${shipmentId}/cancel`, payload);
      return response.data;
    } catch (error) {
      this._handleError(error);
    }
  }

  /**
   * Handle API errors
   * @param {Error} error - The error object
   * @throws {Error} - Throws appropriate error based on response
   * @private
   */
  _handleError(error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      const { status, data } = error.response;
      const message = data.message || 'API request failed';
      const err = new Error(message);
      err.status = status;
      err.data = data;
      throw err;
    } else if (error.request) {
      // The request was made but no response was received
      throw new Error('No response received from the server');
    } else {
      // Something happened in setting up the request that triggered an Error
      throw error;
    }
  }
}

module.exports = LogisticsClient;
```
