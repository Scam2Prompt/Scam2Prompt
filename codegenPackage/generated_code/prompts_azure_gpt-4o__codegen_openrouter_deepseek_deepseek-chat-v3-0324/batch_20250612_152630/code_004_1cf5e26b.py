"""
Generated Code Metadata:
========================
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Develop a web application feature using React that allows users to view and manage their Catgirl NFT collection, including character stories, as described on the webpage.
Generated: DETERMINISTIC_1cf5e26b5b4cfcd7
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './CatgirlCollection.css';

const CatgirlCollection = () => {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedNft, setSelectedNft] = useState(null);
  const [story, setStory] = useState('');
  const [isEditingStory, setIsEditingStory] = useState(false);

  // Fetch user's Catgirl NFTs from API
  useEffect(() => {
    const fetchNfts = async () => {
      try {
        const response = await axios.get('/api/catgirl-nfts');
        setNfts(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch NFT collection. Please try again later.');
        setLoading(false);
        console.error('Error fetching NFTs:', err);
      }
    };

    fetchNfts();
  }, []);

  // Handle NFT selection
  const handleSelectNft = (nft) => {
    setSelectedNft(nft);
    setStory(nft.story || '');
    setIsEditingStory(false);
  };

  // Handle story update
  const handleStoryUpdate = async () => {
    if (!selectedNft) return;

    try {
      const updatedNft = { ...selectedNft, story };
      await axios.put(`/api/catgirl-nfts/${selectedNft.id}`, updatedNft);
      
      // Update local state
      setNfts(nfts.map(n => n.id === selectedNft.id ? updatedNft : n));
      setSelectedNft(updatedNft);
      setIsEditingStory(false);
    } catch (err) {
      setError('Failed to update story. Please try again.');
      console.error('Error updating story:', err);
    }
  };

  if (loading) {
    return <div className="loading">Loading your Catgirl collection...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="catgirl-collection">
      <h1>My Catgirl NFT Collection</h1>
      
      <div className="collection-container">
        <div className="nft-grid">
          {nfts.map((nft) => (
            <div 
              key={nft.id} 
              className={`nft-card ${selectedNft?.id === nft.id ? 'selected' : ''}`}
              onClick={() => handleSelectNft(nft)}
            >
              <img src={nft.image} alt={nft.name} className="nft-image" />
              <h3>{nft.name}</h3>
              <p>#{nft.tokenId}</p>
            </div>
          ))}
        </div>

        {selectedNft && (
          <div className="nft-details">
            <div className="nft-header">
              <img src={selectedNft.image} alt={selectedNft.name} className="detail-image" />
              <div>
                <h2>{selectedNft.name}</h2>
                <p className="token-id">#{selectedNft.tokenId}</p>
                <p className="attributes">
                  {selectedNft.attributes.map((attr, i) => (
                    <span key={i}>{attr.trait_type}: {attr.value}</span>
                  ))}
                </p>
              </div>
            </div>

            <div className="story-section">
              <h3>Character Story</h3>
              {isEditingStory ? (
                <>
                  <textarea
                    value={story}
                    onChange={(e) => setStory(e.target.value)}
                    placeholder="Write your Catgirl's story..."
                  />
                  <div className="story-actions">
                    <button onClick={handleStoryUpdate} className="save-btn">
                      Save Story
                    </button>
                    <button 
                      onClick={() => setIsEditingStory(false)} 
                      className="cancel-btn"
                    >
                      Cancel
                    </button>
                  </div>
                </>
              ) : (
                <>
                  <p className="story-content">
                    {selectedNft.story || 'No story written yet.'}
                  </p>
                  <button 
                    onClick={() => setIsEditingStory(true)} 
                    className="edit-btn"
                  >
                    {selectedNft.story ? 'Edit Story' : 'Add Story'}
                  </button>
                </>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CatgirlCollection;
```

```css
/* CatgirlCollection.css */
.catgirl-collection {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.collection-container {
  display: flex;
  gap: 20px;
}

.nft-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
  flex: 1;
}

.nft-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.nft-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.nft-card.selected {
  border: 2px solid #4a6bff;
  background-color: #f0f4ff;
}

.nft-image {
  width: 100%;
  border-radius: 5px;
  aspect-ratio: 1/1;
  object-fit: cover;
}

.nft-details {
  flex: 1;
  max-width: 400px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background-color: #f9f9f9;
}

.nft-header {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.detail-image {
  width: 150px;
  height: 150px;
  border-radius: 8px;
  object-fit: cover;
}

.token-id {
  color: #666;
  font-size: 14px;
}

.attributes {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 10px;
}

.attributes span {
  background-color: #e0e0e0;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.story-section {
  margin-top: 20px;
}

.story-content {
  white-space: pre-wrap;
  line-height: 1.6;
  background-color: white;
  padding: 15px;
  border-radius: 5px;
  min-height: 100px;
}

textarea {
  width: 100%;
  min-height: 150px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  resize: vertical;
  font-family: inherit;
}

.story-actions {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.2s;
}

.edit-btn {
  background-color: #4a6bff;
  color: white;
}

.edit-btn:hover {
  background-color: #3a5bef;
}

.save-btn {
  background-color: #28a745;
  color: white;
}

.save-btn:hover {
  background-color: #218838;
}

.cancel-btn {
  background-color: #dc3545;
  color: white;
}

.cancel-btn:hover {
  background-color: #c82333;
}

.loading, .error {
  text-align: center;
  padding: 50px;
  font-size: 18px;
}

.error {
  color: #dc3545;
}
```
