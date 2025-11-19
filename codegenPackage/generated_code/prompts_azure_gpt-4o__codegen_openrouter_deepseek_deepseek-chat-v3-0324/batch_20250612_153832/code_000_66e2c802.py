"""
Generated Code Metadata:
========================
Original URL: https://opensea-clone-ten.vercel.app
Prompt: Write code to create an OpenSea-like NFT marketplace interface that includes features such as "Collections," "Stats," and "Resources," using React and Tailwind CSS.
Generated: DETERMINISTIC_66e2c8029b5e6023
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';

const NFTMarketplace = () => {
  const [activeTab, setActiveTab] = useState('collections');
  const [collections, setCollections] = useState([
    { id: 1, name: 'Bored Ape Yacht Club', volume: '120K ETH', floor: '12.5 ETH' },
    { id: 2, name: 'CryptoPunks', volume: '95K ETH', floor: '65 ETH' },
    { id: 3, name: 'Doodles', volume: '45K ETH', floor: '5.2 ETH' },
  ]);
  const [stats, setStats] = useState({
    totalVolume: '1.2M ETH',
    totalSales: '450K',
    totalUsers: '1.5M'
  });
  const [resources] = useState([
    { id: 1, title: 'How to create an NFT', url: '#' },
    { id: 2, title: 'NFT Security Guide', url: '#' },
    { id: 3, title: 'Marketplace FAQ', url: '#' }
  ]);

  const renderTabContent = () => {
    switch (activeTab) {
      case 'collections':
        return (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {collections.map(collection => (
              <div key={collection.id} className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow">
                <h3 className="text-xl font-semibold mb-2">{collection.name}</h3>
                <div className="flex justify-between text-gray-600">
                  <span>Volume: {collection.volume}</span>
                  <span>Floor: {collection.floor}</span>
                </div>
              </div>
            ))}
          </div>
        );
      case 'stats':
        return (
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold mb-6">Marketplace Statistics</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-gray-100 p-4 rounded-lg">
                <h3 className="text-lg font-semibold mb-2">Total Volume</h3>
                <p className="text-2xl font-bold">{stats.totalVolume}</p>
              </div>
              <div className="bg-gray-100 p-4 rounded-lg">
                <h3 className="text-lg font-semibold mb-2">Total Sales</h3>
                <p className="text-2xl font-bold">{stats.totalSales}</p>
              </div>
              <div className="bg-gray-100 p-4 rounded-lg">
                <h3 className="text-lg font-semibold mb-2">Total Users</h3>
                <p className="text-2xl font-bold">{stats.totalUsers}</p>
              </div>
            </div>
          </div>
        );
      case 'resources':
        return (
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold mb-6">Resources</h2>
            <ul className="space-y-4">
              {resources.map(resource => (
                <li key={resource.id}>
                  <a href={resource.url} className="text-blue-600 hover:underline">
                    {resource.title}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">NFT Marketplace</h1>
        <p className="text-gray-600">Discover, collect, and sell extraordinary NFTs</p>
      </header>

      <nav className="mb-8">
        <ul className="flex space-x-4 border-b border-gray-200">
          {['collections', 'stats', 'resources'].map(tab => (
            <li key={tab}>
              <button
                onClick={() => setActiveTab(tab)}
                className={`px-4 py-2 font-medium ${activeTab === tab ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-500 hover:text-gray-700'}`}
              >
                {tab.charAt(0).toUpperCase() + tab.slice(1)}
              </button>
            </li>
          ))}
        </ul>
      </nav>

      <main>
        {renderTabContent()}
      </main>

      <footer className="mt-12 pt-6 border-t border-gray-200 text-center text-gray-500">
        <p>© 2023 NFT Marketplace. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default NFTMarketplace;
```
