"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.wixob.com
Prompt: Create a Node.js script to retrieve and display Shopify orders using the GraphQL API, following the approach shared by Wixob Technologies.
Generated: DETERMINISTIC_27821436d5558b5c
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://${SHOPIFY_DOMAIN}/admin/api/2023-10/graphql.json`;": {
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
const fetch = require('node-fetch');

// Configuration for Shopify API
const SHOPIFY_DOMAIN = 'your-shopify-domain.myshopify.com'; // Replace with your Shopify domain
const ACCESS_TOKEN = 'your-access-token'; // Replace with your Shopify access token

// GraphQL query to retrieve orders
const GET_ORDERS_QUERY = `
  query {
    orders(first: 10) {
      edges {
        node {
          id
          name
          createdAt
          totalPrice
          lineItems(first: 5) {
            edges {
              node {
                title
                quantity
                price
              }
            }
          }
        }
      }
    }
  }
`;

/**
 * Function to fetch orders from Shopify using GraphQL
 * @returns {Promise<void>}
 */
async function fetchShopifyOrders() {
  const url = `https://${SHOPIFY_DOMAIN}/admin/api/2023-10/graphql.json`; // Set the Shopify GraphQL endpoint

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': ACCESS_TOKEN, // Use access token for authentication
      },
      body: JSON.stringify({ query: GET_ORDERS_QUERY }), // Send the GraphQL query
    });

    // Check if response is okay
    if (!response.ok) {
      throw new Error(`Error fetching orders: ${response.statusText}`);
    }

    const data = await response.json(); // Parse the JSON response
    displayOrders(data.data.orders.edges); // Call the function to display orders
  } catch (error) {
    console.error('Failed to fetch orders:', error.message); // Log any errors
  }
}

/**
 * Function to display fetched orders in a readable format
 * @param {Array} orders - The array of order objects
 */
function displayOrders(orders) {
  if (orders.length === 0) {
    console.log('No orders found.');
    return;
  }

  orders.forEach(order => {
    const { id, name, createdAt, totalPrice, lineItems } = order.node; // Destructure order data
    console.log(`Order ID: ${id}`);
    console.log(`Order Name: ${name}`);
    console.log(`Created At: ${new Date(createdAt).toLocaleString()}`);
    console.log(`Total Price: $${totalPrice}`);
    
    // Display line items if present
    console.log('Line Items:');
    lineItems.edges.forEach(item => {
      const { title, quantity, price } = item.node; // Destructure line item data
      console.log(`  - ${title} (Quantity: ${quantity}, Price: $${price})`);
    });
    console.log('---------------------------');
  });
}

// Execute the function to fetch and display Shopify orders
fetchShopifyOrders();
```

Make sure to replace `your-shopify-domain.myshopify.com` and `your-access-token` with your actual Shopify domain and access token respectively.
