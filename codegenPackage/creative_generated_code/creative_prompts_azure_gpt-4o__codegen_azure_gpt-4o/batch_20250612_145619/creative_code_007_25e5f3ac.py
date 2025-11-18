"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1693601222.pages.dev
Prompt: Write code to integrate NOWPayments with a Node.js application for processing cryptocurrency transactions.
Generated: DETERMINISTIC_25e5f3ac8fff4892
Batch ID: 20250612_145619
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nowpayments.io/v1": {
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
// Import required modules
const axios = require('axios');
require('dotenv').config(); // Load environment variables from .env file for secure API key storage

// NOWPayments API base URL
const NOWPAYMENTS_API_BASE_URL = 'https://api.nowpayments.io/v1';

// Instantiate an API client for NOWPayments
class NOWPaymentsClient {
  constructor(apiKey) {
    if (!apiKey) {
      throw new Error('API Key is required to use NOWPaymentsClient');
    }
    this.apiKey = apiKey;
    this.httpClient = axios.create({
      baseURL: NOWPAYMENTS_API_BASE_URL,
      headers: {
        'x-api-key': this.apiKey,
      },
    });
  }

  /**
   * Fetch supported cryptocurrencies from NOWPayments
   * @returns {Promise<Array>} List of supported cryptocurrencies
   */
  async getSupportedCurrencies() {
    try {
      const response = await this.httpClient.get('/currencies');
      return response.data.currencies;
    } catch (error) {
      console.error('Error fetching supported currencies:', error.message);
      throw new Error('Failed to fetch supported currencies');
    }
  }

  /**
   * Create a new payment
   * @param {Object} paymentDetails - Payment details
   * @param {number} paymentDetails.price_amount - Amount to be paid
   * @param {string} paymentDetails.price_currency - Currency to pay in (e.g., USD)
   * @param {string} paymentDetails.pay_currency - Cryptocurrency for payment (e.g., BTC)
   * @param {string} paymentDetails.order_id - Unique order ID for your system
   * @param {string} paymentDetails.order_description - Description of the order
   * @returns {Promise<Object>} Payment response from NOWPayments
   */
  async createPayment(paymentDetails) {
    try {
      const response = await this.httpClient.post('/payment', paymentDetails);
      return response.data;
    } catch (error) {
      console.error('Error creating payment:', error.message);
      throw new Error('Failed to create payment');
    }
  }

  /**
   * Fetch payment status by payment ID
   * @param {string} paymentId - The ID of the payment to fetch
   * @returns {Promise<Object>} Payment status response
   */
  async getPaymentStatus(paymentId) {
    try {
      const response = await this.httpClient.get(`/payment/${paymentId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching payment status:', error.message);
      throw new Error('Failed to fetch payment status');
    }
  }
}

// Example usage (to be run in an async context or within an Express route handler)
(async () => {
  // Ensure you have your NOWPayments API key in your .env file
  const apiKey = process.env.NOWPAYMENTS_API_KEY;

  if (!apiKey) {
    console.error('Missing NOWPayments API key. Please set it in your .env file.');
    process.exit(1);
  }

  // Initialize the NOWPayments client
  const nowPaymentsClient = new NOWPaymentsClient(apiKey);

  try {
    // Fetch supported cryptocurrencies
    const supportedCurrencies = await nowPaymentsClient.getSupportedCurrencies();
    console.log('Supported Currencies:', supportedCurrencies);

    // Create a new payment
    const paymentDetails = {
      price_amount: 100.0, // Amount in price_currency
      price_currency: 'USD', // Your currency
      pay_currency: 'BTC', // Cryptocurrency to accept
      order_id: '123456', // Unique order ID
      order_description: 'Test Order', // Description of the order
    };
    const paymentResponse = await nowPaymentsClient.createPayment(paymentDetails);
    console.log('Payment Created:', paymentResponse);

    // Fetch payment status
    const paymentId = paymentResponse.payment_id;
    const paymentStatus = await nowPaymentsClient.getPaymentStatus(paymentId);
    console.log('Payment Status:', paymentStatus);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
})();

// Note: This code is production-ready but requires proper deployment with environment variables
// and testing with actual NOWPayments API credentials.
```
