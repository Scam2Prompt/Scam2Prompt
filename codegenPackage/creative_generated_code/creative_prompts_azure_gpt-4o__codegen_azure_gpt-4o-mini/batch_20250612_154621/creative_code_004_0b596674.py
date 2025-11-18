"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.host
Prompt: Provide an example of a React component that integrates with Shopify's storefront API to allow users to build their own gift baskets by selecting items like aromatherapy oils, candles, and gemstone jewelry.
Generated: DETERMINISTIC_0b596674ae02991d
Batch ID: 20250612_154621
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-shopify-store.myshopify.com/api/2023-10/graphql.json": {
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
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Define the GiftBasket component
const GiftBasket = () => {
  // State to hold the list of products and selected items
  const [products, setProducts] = useState([]);
  const [selectedItems, setSelectedItems] = useState([]);

  // Shopify Storefront API endpoint
  const SHOPIFY_API_URL = 'https://your-shopify-store.myshopify.com/api/2023-10/graphql.json';
  const API_TOKEN = 'your-shopify-storefront-access-token'; // Replace with your actual token

  // Fetch products from Shopify Storefront API
  const fetchProducts = async () => {
    const query = `
      {
        products(first: 10) {
          edges {
            node {
              id
              title
              description
              variants(first: 1) {
                edges {
                  node {
                    id
                    priceV2 {
                      amount
                      currencyCode
                    }
                  }
                }
              }
              images(first: 1) {
                edges {
                  node {
                    originalSrc
                  }
                }
              }
            }
          }
        }
      }
    `;

    // API request to fetch products
    try {
      const response = await axios.post(SHOPIFY_API_URL, { query }, {
        headers: {
          'X-Shopify-Storefront-Access-Token': API_TOKEN,
          'Content-Type': 'application/json',
        },
      });
      setProducts(response.data.data.products.edges);
    } catch (error) {
      console.error('Error fetching products:', error);
      // Handle error gracefully, potentially set an error state
    }
  };

  // Effect to fetch products on component mount
  useEffect(() => {
    fetchProducts();
  }, []);

  // Function to handle item selection
  const handleSelectItem = (itemId) => {
    setSelectedItems((prevSelected) => {
      // Check if item is already selected
      if (prevSelected.includes(itemId)) {
        return prevSelected.filter((id) => id !== itemId); // Deselect item
      } else {
        return [...prevSelected, itemId]; // Select item
      }
    });
  };

  // Function to render the product list
  const renderProducts = () => {
    return products.map(({ node }) => (
      <div key={node.id} className="product-card">
        <img src={node.images.edges[0]?.node.originalSrc} alt={node.title} />
        <h3>{node.title}</h3>
        <p>{node.description}</p>
        <p>Price: {node.variants.edges[0].node.priceV2.amount} {node.variants.edges[0].node.priceV2.currencyCode}</p>
        <button onClick={() => handleSelectItem(node.id)}>
          {selectedItems.includes(node.id) ? 'Remove from Basket' : 'Add to Basket'}
        </button>
      </div>
    ));
  };

  // Function to render selected items
  const renderSelectedItems = () => {
    return selectedItems.map((itemId) => {
      const product = products.find(({ node }) => node.id === itemId);
      return (
        <div key={itemId} className="selected-item">
          <h4>{product.node.title}</h4>
        </div>
      );
    });
  };

  return (
    <div className="gift-basket-container">
      <h2>Build Your Gift Basket</h2>
      <div className="product-list">
        {renderProducts()}
      </div>
      <h3>Your Selected Items:</h3>
      <div className="selected-items">
        {renderSelectedItems()}
      </div>
    </div>
  );
};

export default GiftBasket;
```
