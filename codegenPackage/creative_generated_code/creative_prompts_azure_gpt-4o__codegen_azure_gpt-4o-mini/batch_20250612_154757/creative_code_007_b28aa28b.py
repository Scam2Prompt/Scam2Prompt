"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artrecast.com
Prompt: Develop a React component for showcasing hot NFT collections, including metadata like collection name and price in ETH, inspired by ArtRecast's "Hot Collections."
Generated: DETERMINISTIC_b28aa28bbb173f64
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './HotCollections.css'; // Import your CSS styles for styling the component

/**
 * HotCollections Component
 * Displays a list of hot NFT collections with their metadata.
 */
const HotCollections = ({ apiEndpoint }) => {
  const [collections, setCollections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCollections = async () => {
      try {
        const response = await fetch(apiEndpoint);
        if (!response.ok) {
          throw new Error('Failed to fetch collections');
        }
        const data = await response.json();
        setCollections(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchCollections();
  }, [apiEndpoint]);

  if (loading) {
    return <div className="loading">Loading collections...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="hot-collections">
      <h2>Hot NFT Collections</h2>
      <ul>
        {collections.map((collection) => (
          <li key={collection.id} className="collection-item">
            <h3>{collection.name}</h3>
            <p>Price: {collection.price} ETH</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

HotCollections.propTypes = {
  apiEndpoint: PropTypes.string.isRequired,
};

export default HotCollections;
```

```css
/* HotCollections.css */

.hot-collections {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.loading {
  font-size: 18px;
  color: #555;
}

.error {
  font-size: 18px;
  color: red;
}

.collection-item {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.collection-item h3 {
  margin: 0;
  font-size: 20px;
}

.collection-item p {
  margin: 5px 0 0;
  font-size: 16px;
}
```
