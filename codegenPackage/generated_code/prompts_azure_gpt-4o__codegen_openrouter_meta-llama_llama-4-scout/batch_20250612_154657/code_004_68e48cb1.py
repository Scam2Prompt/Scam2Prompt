"""
Generated Code Metadata:
========================
Original URL: https://claim.manatoken.net
Prompt: Write JavaScript code to create a front-end interface for a personalized web discovery platform, incorporating features like a rating system and user collections as described in Stumble! ®.
Generated: DETERMINISTIC_68e48cb1c2f655dd
Batch ID: 20250612_154657
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

// Define a single discovery item component
function DiscoveryItem({ item, onRate, onAddToCollection }) {
  // Render a single discovery item
  return (
    <div className="discovery-item">
      <h2>{item.title}</h2>
      <p>{item.description}</p>
      <img src={item.imageUrl} alt={item.title} />
      <div className="actions">
        <button onClick={() => onRate(item.id, 1)}>Like (1)</button>
        <button onClick={() => onRate(item.id, 0)}>Dislike (0)</button>
        <button onClick={() => onAddToCollection(item.id)}>Add to Collection</button>
      </div>
    </div>
  );
}

// Define the main discovery platform component
function DiscoveryPlatform() {
  // Initialize state for discovery items, user ratings, and collections
  const [discoveryItems, setDiscoveryItems] = useState([]);
  const [userRatings, setUserRatings] = useState({});
  const [userCollections, setUserCollections] = useState([]);

  // Fetch discovery items from API on mount
  useEffect(() => {
    fetch('/api/discovery-items')
      .then(response => response.json())
      .then(data => setDiscoveryItems(data));
  }, []);

  // Handle rating changes
  const handleRate = (itemId, rating) => {
    // Update user ratings state
    setUserRatings(prevRatings => ({ ...prevRatings, [itemId]: rating }));

    // Persist rating to API
    fetch(`/api/discovery-items/${itemId}/rate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ rating }),
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  };

  // Handle adding items to user collections
  const handleAddToCollection = itemId => {
    // Update user collections state
    setUserCollections(prevCollections => [...prevCollections, itemId]);

    // Persist collection change to API
    fetch(`/api/users/collections`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ itemId }),
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  };

  // Render discovery platform
  return (
    <div className="discovery-platform">
      <h1>Discovery Platform</h1>
      {discoveryItems.map(item => (
        <DiscoveryItem
          key={item.id}
          item={item}
          onRate={handleRate}
          onAddToCollection={handleAddToCollection}
        />
      ))}
      <div className="user-collections">
        <h2>User Collections</h2>
        <ul>
          {userCollections.map(itemId => (
            <li key={itemId}>{itemId}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

// Render the discovery platform to the DOM
ReactDOM.render(
  <React.StrictMode>
    <DiscoveryPlatform />
  </React.StrictMode>,
  document.getElementById('root')
);

// Example API responses for demonstration purposes
const apiResponses = {
  '/api/discovery-items': [
    { id: 1, title: 'Item 1', description: 'Description 1', imageUrl: 'https://example.com/image1.jpg' },
    { id: 2, title: 'Item 2', description: 'Description 2', imageUrl: 'https://example.com/image2.jpg' },
  ],
  '/api/discovery-items/1/rate': { message: 'Rating updated successfully' },
  '/api/users/collections': { message: 'Item added to collection successfully' },
};

// Mock API implementation for demonstration purposes
function mockApi(request, response) {
  const url = request.url;
  if (url === '/api/discovery-items') {
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify(apiResponses[url]));
  } else if (url.startsWith('/api/discovery-items/')) {
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify(apiResponses[`${url}/rate`]));
  } else if (url === '/api/users/collections') {
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify(apiResponses[url]));
  } else {
    response.writeHead(404, { 'Content-Type': 'text/plain' });
    response.end('Not Found');
  }
}

// Run the mock API server for demonstration purposes
import http from 'http';
http.createServer(mockApi).listen(3001, () => {
  console.log('Mock API server listening on port 3001');
});
```
