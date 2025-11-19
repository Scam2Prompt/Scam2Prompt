"""
Generated Code Metadata:
========================
Original URL: https://magiccraft-migrate.pages.dev
Prompt: "Develop a basic marketplace dapp using Web3 and React, similar to MagicCraft's marketplace for buying and selling in-game items."
Generated: DETERMINISTIC_c02634245e5dba21
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready React and Web3.js implementation for a basic marketplace DApp:

```jsx
// File: src/components/Marketplace.jsx
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import MarketplaceContractABI from '../contracts/Marketplace.json';

const Marketplace = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Contract address (replace with your deployed contract address)
  const contractAddress = '0x123...abc';

  // Initialize Web3 and contract
  useEffect(() => {
    const init = async () => {
      try {
        // Check if Web3 is injected by the browser (MetaMask)
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          // Listen for account changes
          window.ethereum.on('accountsChanged', (newAccounts) => {
            setAccount(newAccounts[0]);
          });

          // Initialize contract
          const contractInstance = new web3Instance.eth.Contract(
            MarketplaceContractABI,
            contractAddress
          );
          setContract(contractInstance);

          // Load marketplace items
          await loadItems(contractInstance);
        } else {
          setError('Please install MetaMask to use this DApp');
        }
      } catch (err) {
        console.error('Initialization error:', err);
        setError('Failed to initialize Web3 and contract');
      } finally {
        setLoading(false);
      }
    };

    init();

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', () => {});
      }
    };
  }, []);

  // Load items from the contract
  const loadItems = async (contractInstance) => {
    try {
      const itemCount = await contractInstance.methods.itemCount().call();
      const items = [];

      for (let i = 1; i <= itemCount; i++) {
        const item = await contractInstance.methods.items(i).call();
        if (item.id !== '0') { // Skip empty items
          items.push({
            id: item.id,
            name: item.name,
            price: web3.utils.fromWei(item.price, 'ether'),
            seller: item.seller,
            owner: item.owner,
            forSale: item.forSale
          });
        }
      }

      setItems(items);
    } catch (err) {
      console.error('Error loading items:', err);
      setError('Failed to load marketplace items');
    }
  };

  // Buy an item
  const buyItem = async (itemId, price) => {
    try {
      setLoading(true);
      const priceInWei = web3.utils.toWei(price, 'ether');
      await contract.methods.purchaseItem(itemId).send({
        from: account,
        value: priceInWei
      });
      await loadItems(contract);
    } catch (err) {
      console.error('Error purchasing item:', err);
      setError('Failed to purchase item');
    } finally {
      setLoading(false);
    }
  };

  // List a new item for sale
  const listItem = async (name, price) => {
    try {
      setLoading(true);
      const priceInWei = web3.utils.toWei(price, 'ether');
      await contract.methods.listItem(name, priceInWei).send({ from: account });
      await loadItems(contract);
    } catch (err) {
      console.error('Error listing item:', err);
      setError('Failed to list item');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="marketplace">
      <h1>Game Item Marketplace</h1>
      <p>Connected account: {account}</p>

      <div className="item-list">
        <h2>Items for Sale</h2>
        {items.length === 0 ? (
          <p>No items available</p>
        ) : (
          <ul>
            {items
              .filter(item => item.forSale)
              .map(item => (
                <li key={item.id}>
                  <h3>{item.name}</h3>
                  <p>Price: {item.price} ETH</p>
                  <p>Seller: {item.seller}</p>
                  <button onClick={() => buyItem(item.id, item.price)}>
                    Buy
                  </button>
                </li>
              ))}
          </ul>
        )}
      </div>

      <div className="list-item">
        <h2>List New Item</h2>
        <form onSubmit={(e) => {
          e.preventDefault();
          const name = e.target.name.value;
          const price = e.target.price.value;
          listItem(name, price);
        }}>
          <input type="text" name="name" placeholder="Item name" required />
          <input type="number" name="price" placeholder="Price in ETH" step="0.01" min="0" required />
          <button type="submit">List Item</button>
        </form>
      </div>
    </div>
  );
};

export default Marketplace;
```

```json
// File: src/contracts/Marketplace.json
{
  "abi": [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "seller",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "bool",
          "name": "forSale",
          "type": "bool"
        }
      ],
      "name": "ItemListed",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "buyer",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "seller",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "ItemPurchased",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_name",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "_price",
          "type": "uint256"
        }
      ],
      "name": "listItem",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_id",
          "type": "uint256"
        }
      ],
      "name": "purchaseItem",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "itemCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256
