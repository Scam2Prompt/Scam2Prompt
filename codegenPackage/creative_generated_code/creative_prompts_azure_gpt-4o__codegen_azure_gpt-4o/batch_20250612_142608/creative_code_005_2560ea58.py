"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Provide code examples for integrating external APIs into GitBook documentation using the Polymarket GitBook template's OpenAPI integration features.
Generated: DETERMINISTIC_2560ea58a6b487ac
Batch ID: 20250612_142608
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```yaml
# This is the OpenAPI Specification (YAML format) to integrate with the Polymarket GitBook template.
# It defines an external API endpoint for documentation purposes.
# Ensure this file is included in your GitBook's configuration.

openapi: 3.0.3
info:
  title: Polymarket API
  description: >
    This is the API documentation for Polymarket, generated using the 
    Polymarket GitBook template's OpenAPI integration features.
  version: 1.0.0

servers:
  - url: https://api.polymarket.com/v1
    description: Production Server

paths:
  /markets:
    get:
      summary: Retrieve all active markets
      description: >
        Fetches a list of all active markets available on Polymarket.
      operationId: getMarkets
      parameters:
        - name: limit
          in: query
          description: The maximum number of results to return.
          required: false
          schema:
            type: integer
            default: 10
        - name: offset
          in: query
          description: The offset for pagination.
          required: false
          schema:
            type: integer
            default: 0
      responses:
        '200':
          description: A list of active markets.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: Unique identifier for the market.
                    title:
                      type: string
                      description: Title of the market.
                    status:
                      type: string
                      description: Current status of the market.
        '400':
          description: Bad Request - Invalid query parameters.
        '500':
          description: Internal Server Error.

  /markets/{id}:
    get:
      summary: Retrieve specific market details
      description: >
        Fetches details of a specific market by its unique identifier.
      operationId: getMarketById
      parameters:
        - name: id
          in: path
          description: Unique identifier for the market.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Details of the market.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: Unique identifier for the market.
                  title:
                    type: string
                    description: Title of the market.
                  description:
                    type: string
                    description: Detailed description of the market.
                  status:
                    type: string
                    description: Current status of the market.
        '404':
          description: Market not found.
        '500':
          description: Internal Server Error.

components:
  schemas:
    Market:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the market.
        title:
          type: string
          description: Title of the market.
        description:
          type: string
          description: Detailed description of the market.
        status:
          type: string
          description: Current status of the market.
```

```json
// Sample `book.json` configuration for GitBook to include the OpenAPI integration.
{
  "plugins": [
    "openapi"
  ],
  "pluginsConfig": {
    "openapi": {
      "specs": [
        {
          "url": "./openapi.yaml", // Path to the OpenAPI spec file
          "basePath": "/api",
          "title": "Polymarket API"
        }
      ]
    }
  }
}
```

```javascript
// Example of using the Polymarket API with JavaScript (Node.js).

const axios = require('axios'); // Use axios for simplified HTTP requests

const BASE_URL = 'https://api.polymarket.com/v1';

// Function to fetch all active markets
async function fetchActiveMarkets(limit = 10, offset = 0) {
  try {
    const response = await axios.get(`${BASE_URL}/markets`, {
      params: { limit, offset },
    });
    console.log('Active Markets:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching active markets:', error.response?.data || error.message);
    throw error;
  }
}

// Function to fetch details of a specific market
async function fetchMarketDetails(marketId) {
  try {
    const response = await axios.get(`${BASE_URL}/markets/${marketId}`);
    console.log('Market Details:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching market details:', error.response?.data || error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Fetch active markets
    const markets = await fetchActiveMarkets();
    console.log('Markets Retrieved:', markets);

    // Fetch details of the first market (if available)
    if (markets.length > 0) {
      const marketDetails = await fetchMarketDetails(markets[0].id);
      console.log('First Market Details:', marketDetails);
    }
  } catch (err) {
    console.error('An error occurred:', err.message);
  }
})();
```
