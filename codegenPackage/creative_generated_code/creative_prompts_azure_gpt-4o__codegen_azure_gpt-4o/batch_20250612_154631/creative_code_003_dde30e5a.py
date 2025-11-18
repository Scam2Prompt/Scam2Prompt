"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vue-coinbase.vercel.app
Prompt: Write a Vue.js application that requires JavaScript to fetch and display cryptocurrency exchange rates using Coinbase's API, inspired by https://vue-coinbase.vercel.app.
Generated: DETERMINISTIC_dde30e5a56a3daeb
Batch ID: 20250612_154631
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coinbase.com/v2/exchange-rates": {
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
// Vue.js application to fetch and display cryptocurrency exchange rates from Coinbase API

// Import Vue and axios
import { createApp } from 'vue';
import axios from 'axios';

// Define the main component
const App = {
  data() {
    return {
      exchangeRates: {}, // Object to store fetched exchange rates
      loading: true, // Loading state
      error: null, // Error message
    };
  },
  methods: {
    // Fetch exchange rates from Coinbase API
    async fetchExchangeRates() {
      const API_URL = 'https://api.coinbase.com/v2/exchange-rates';
      try {
        // Make GET request to Coinbase API
        const response = await axios.get(API_URL);
        // Extract relevant data
        this.exchangeRates = response.data.data.rates;
      } catch (err) {
        // Handle errors and update error message
        this.error = 'Failed to fetch exchange rates. Please try again later.';
      } finally {
        // Update loading state
        this.loading = false;
      }
    },
  },
  // Lifecycle hook to fetch data on component mount
  mounted() {
    this.fetchExchangeRates();
  },
  template: `
    <div id="app">
      <!-- Display loading message -->
      <div v-if="loading">Loading exchange rates...</div>

      <!-- Display error message -->
      <div v-if="error" class="error">{{ error }}</div>

      <!-- Display exchange rates -->
      <table v-if="!loading && !error">
        <thead>
          <tr>
            <th>Currency</th>
            <th>Rate (USD)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(rate, currency) in exchangeRates" :key="currency">
            <td>{{ currency }}</td>
            <td>{{ rate }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  `,
};

// Create Vue app and mount it to the DOM
createApp(App).mount('#app');
```

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cryptocurrency Exchange Rates</title>
  <script type="module" src="main.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #f4f4f4;
    }
    .error {
      color: red;
    }
  </style>
</head>
<body>
  <div id="app"></div>
</body>
</html>
```

### Notes:
- Run `npm install axios` to install the required dependency (`axios`).
- Ensure the `main.js` file contains the Vue.js app code shown above.
- This code adheres to Vue.js best practices, includes error handling, and is production-ready.
