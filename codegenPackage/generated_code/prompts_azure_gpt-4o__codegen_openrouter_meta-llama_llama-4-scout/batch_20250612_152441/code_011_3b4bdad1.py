"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Create a Node.js script to fetch and display information about Artyfact's virtual events, such as NFT exhibitions and eSport tournaments, using a hypothetical API.
Generated: DETERMINISTIC_3b4bdad1f82634ac
Batch ID: 20250612_152441
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

/**
 * Artyfact API client
 */
class ArtyfactApiClient {
  /**
   * Constructor
   * @param {string} apiUrl - Base URL of the Artyfact API
   * @param {string} apiKey - API key for authentication
   */
  constructor(apiUrl, apiKey) {
    this.apiUrl = apiUrl;
    this.apiKey = apiKey;
  }

  /**
   * Fetch virtual events
   * @returns {Promise<object>} Promise resolving to an object with virtual events
   */
  async fetchVirtualEvents() {
    try {
      const response = await axios.get(`${this.apiUrl}/events`, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 200) {
        throw new Error(`Failed to fetch virtual events: ${response.statusText}`);
      }

      return response.data;
    } catch (error) {
      console.error('Error fetching virtual events:', error.message);
      throw error;
    }
  }

  /**
   * Fetch event details
   * @param {string} eventId - ID of the event
   * @returns {Promise<object>} Promise resolving to an object with event details
   */
  async fetchEventDetails(eventId) {
    try {
      const response = await axios.get(`${this.apiUrl}/events/${eventId}`, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 200) {
        throw new Error(`Failed to fetch event details: ${response.statusText}`);
      }

      return response.data;
    } catch (error) {
      console.error(`Error fetching event details: ${error.message}`);
      throw error;
    }
  }
}

/**
 * Display virtual events
 * @param {object} events - Object with virtual events
 */
function displayVirtualEvents(events) {
  console.log('Virtual Events:');
  events.forEach((event) => {
    console.log(`- ${event.name} (ID: ${event.id})`);
  });
}

/**
 * Display event details
 * @param {object} eventDetails - Object with event details
 */
function displayEventDetails(eventDetails) {
  console.log(`Event Details (ID: ${eventDetails.id}):`);
  console.log(`- Name: ${eventDetails.name}`);
  console.log(`- Description: ${eventDetails.description}`);
  console.log(`- Type: ${eventDetails.type}`);
}

/**
 * Main function
 */
async function main() {
  try {
    // Load API URL and key from environment variables
    const apiUrl = process.env.ARTYFACT_API_URL;
    const apiKey = process.env.ARTYFACT_API_KEY;

    if (!apiUrl || !apiKey) {
      throw new Error('API URL or key is missing');
    }

    // Create API client
    const client = new ArtyfactApiClient(apiUrl, apiKey);

    // Fetch virtual events
    const events = await client.fetchVirtualEvents();
    displayVirtualEvents(events);

    // Fetch and display event details for the first event
    if (events.length > 0) {
      const eventId = events[0].id;
      const eventDetails = await client.fetchEventDetails(eventId);
      displayEventDetails(eventDetails);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Run main function
main();
```
