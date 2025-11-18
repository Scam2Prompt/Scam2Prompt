"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Develop a Dapp interface that enables users to explore verified guilds and manage roles, based on the Guild Connect functionality described on the ICO Protocol page.
Generated: DETERMINISTIC_9aa76eb9aec8f8c6
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries for Ethereum and React
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Contract } from 'ethers';
import guildContractABI from './guildContractABI.json'; // Assuming the ABI is stored in this JSON file

// Define the GuildDapp component
const GuildDapp = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [guilds, setGuilds] = useState([]);
  const [selectedGuild, setSelectedGuild] = useState(null);
  const [roles, setRoles] = useState([]);
  const [loading, setLoading] = useState(true);

  // Contract address for the Guild Connect functionality
  const GUILD_CONTRACT_ADDRESS = '0xYourGuildContractAddress';

  // Initialize Web3 and fetch user accounts
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);
        fetchGuilds(web3Instance);
      } else {
        console.error('Ethereum object not found. Install MetaMask.');
        alert('Please install MetaMask to use this app!');
      }
    };

    initWeb3();
  }, []);

  // Fetch guilds from the smart contract
  const fetchGuilds = async (web3Instance) => {
    try {
      const contract = new Contract(GUILD_CONTRACT_ADDRESS, guildContractABI, web3Instance);
      const guildList = await contract.getVerifiedGuilds(); // Assuming this is a contract function
      setGuilds(guildList);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching guilds:', error);
      alert('Failed to fetch guilds. Please try again later.');
      setLoading(false);
    }
  };

  // Fetch roles for the selected guild
  const fetchRoles = async (guildId) => {
    try {
      const contract = new Contract(GUILD_CONTRACT_ADDRESS, guildContractABI, web3);
      const roleList = await contract.getRoles(guildId); // Assuming this is a contract function
      setRoles(roleList);
    } catch (error) {
      console.error('Error fetching roles:', error);
      alert('Failed to fetch roles. Please try again later.');
    }
  };

  // Handle guild selection
  const handleGuildSelect = (guild) => {
    setSelectedGuild(guild);
    fetchRoles(guild.id);
  };

  // Render loading state and guild list
  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Guild Explorer</h1>
      <h2>Connected Account: {account}</h2>
      <div>
        <h3>Verified Guilds</h3>
        <ul>
          {guilds.map((guild, index) => (
            <li key={index} onClick={() => handleGuildSelect(guild)}>
              {guild.name}
            </li>
          ))}
        </ul>
      </div>
      {selectedGuild && (
        <div>
          <h3>Roles in {selectedGuild.name}</h3>
          <ul>
            {roles.map((role, index) => (
              <li key={index}>{role}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

// Export the GuildDapp component as the default export
export default GuildDapp;
```
