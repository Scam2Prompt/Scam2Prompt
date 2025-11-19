"""
Generated Code Metadata:
========================
Original URL: https://projectvox.pages.dev
Prompt: Create a decentralized application (dApp) that allows users to sign in, connect their wallet, and explore verified guilds, inspired by the Guildhall platform's functionality.
Generated: DETERMINISTIC_50fd4230912c52e2
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Frontend (React + Ethers.js)
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// Guildhall smart contract ABI (simplified for example)
const GUILDHALL_ABI = [
  {
    "inputs": [],
    "name": "getVerifiedGuilds",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "guildAddress",
        "type": "address"
      }
    ],
    "name": "getGuildDetails",
    "outputs": [
      {
        "components": [
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "description",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "logoUrl",
            "type": "string"
          },
          {
            "internalType": "bool",
            "name": "isVerified",
            "type": "bool"
          }
        ],
        "internalType": "struct Guildhall.Guild",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

const GUILDHALL_ADDRESS = "0x123..."; // Replace with actual contract address

function App() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState(null);
  const [guilds, setGuilds] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("Please install MetaMask!");
      }

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(provider);

      const accounts = await provider.send("eth_requestAccounts", []);
      setAccount(accounts[0]);

      const signer = provider.getSigner();
      setSigner(signer);

      await fetchVerifiedGuilds(provider);
    } catch (err) {
      setError(err.message);
      console.error(err);
    }
  };

  // Fetch verified guilds
  const fetchVerifiedGuilds = async (provider) => {
    try {
      setLoading(true);
      const contract = new ethers.Contract(GUILDHALL_ADDRESS, GUILDHALL_ABI, provider);
      const guildAddresses = await contract.getVerifiedGuilds();

      const guildsWithDetails = await Promise.all(
        guildAddresses.map(async (address) => {
          const details = await contract.getGuildDetails(address);
          return {
            address,
            ...details
          };
        })
      );

      setGuilds(guildsWithDetails);
      setLoading(false);
    } catch (err) {
      setError("Failed to fetch guilds");
      console.error(err);
      setLoading(false);
    }
  };

  // Check if wallet is connected on page load
  useEffect(() => {
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.listAccounts();
        
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          setProvider(provider);
          setSigner(provider.getSigner());
          await fetchVerifiedGuilds(provider);
        }
      }
    };

    checkWalletConnection();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Guildhall Explorer</h1>
        {!account ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {account.substring(0, 6)}...{account.substring(38)}</p>
          </div>
        )}
      </header>

      <main>
        {error && <div className="error">{error}</div>}

        {loading ? (
          <div className="loading">Loading guilds...</div>
        ) : (
          <div className="guilds-container">
            <h2>Verified Guilds</h2>
            {guilds.length > 0 ? (
              <ul className="guilds-list">
                {guilds.map((guild, index) => (
                  <li key={index} className="guild-card">
                    <img src={guild.logoUrl} alt={guild.name} className="guild-logo" />
                    <h3>{guild.name}</h3>
                    <p>{guild.description}</p>
                    <div className="guild-address">{guild.address}</div>
                  </li>
                ))}
              </ul>
            ) : (
              <p>No verified guilds found</p>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
```

```solidity
// Smart Contract (Solidity)
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Guildhall {
    struct Guild {
        string name;
        string description;
        string logoUrl;
        bool isVerified;
    }

    address public admin;
    mapping(address => Guild) public guilds;
    address[] public verifiedGuilds;

    event GuildRegistered(address indexed guildAddress, string name);
    event GuildVerified(address indexed guildAddress);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function registerGuild(
        string memory _name,
        string memory _description,
        string memory _logoUrl
    ) external {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(guilds[msg.sender].name).length == 0, "Guild already registered");

        guilds[msg.sender] = Guild({
            name: _name,
            description: _description,
            logoUrl: _logoUrl,
            isVerified: false
        });

        emit GuildRegistered(msg.sender, _name);
    }

    function verifyGuild(address _guildAddress) external onlyAdmin {
        require(bytes(guilds[_guildAddress].name).length > 0, "Guild not registered");
        require(!guilds[_guildAddress].isVerified, "Guild already verified");

        guilds[_guildAddress].isVerified = true;
        verifiedGuilds.push(_guildAddress);

        emit GuildVerified(_guildAddress);
    }

    function getVerifiedGuilds() external view returns (address[] memory) {
        return verifiedGuilds;
    }

    function getGuildDetails(address _guildAddress) external view returns (Guild memory) {
        return guilds[_guildAddress];
    }

    function transferAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "Invalid address");
        admin = _newAdmin;
    }
}
```

```css
/* App.css */
.App {
  text-align: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.App-header {
  margin-bottom: 40px;
}

button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 12px 24px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 10px 2px;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #45a049;
}

.wallet-info {
  margin: 20px 0;
  padding: 10px;
  background-color: #f8f8f8;
  border-radius: 4px;
}

.error {
  color: #ff0000;
  margin: 20px 0;
  padding: 10px;
  background-color: #ffeeee;
  border-radius: 4px;
}

.loading {
  margin: 40px 0;
  font-style: italic;
}

.guilds-container {
  margin-top: 30px;
}

.guilds-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  list-style: none;
  padding: 0;
}

.guild-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  text-align:
