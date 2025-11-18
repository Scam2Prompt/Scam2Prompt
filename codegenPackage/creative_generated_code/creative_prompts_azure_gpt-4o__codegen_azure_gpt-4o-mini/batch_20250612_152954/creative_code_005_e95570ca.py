"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-catecoin-club.pages.dev
Prompt: Develop a React component to connect a wallet and display active and completed Catecoin stakes, including the ability to withdraw tokens.
Generated: DETERMINISTIC_e95570cac60dc11c
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import styled from 'styled-components';

// Styled components for the UI
const Container = styled.div`
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 600px;
  margin: auto;
`;

const Button = styled.button`
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

const StakeList = styled.ul`
  list-style-type: none;
  padding: 0;
`;

const StakeItem = styled.li`
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
`;

const WalletConnect = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [activeStakes, setActiveStakes] = useState([]);
  const [completedStakes, setCompletedStakes] = useState([]);

  // Connect to the user's wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await provider.listAccounts();
        setProvider(provider);
        setAccount(accounts[0]);
        fetchStakes(accounts[0]); // Fetch stakes after connecting
      } catch (error) {
        console.error('Error connecting wallet:', error);
      }
    } else {
      alert('MetaMask is not installed. Please install it to use this feature.');
    }
  };

  // Fetch active and completed stakes for the connected account
  const fetchStakes = async (account) => {
    try {
      // Simulated fetch calls for stakes, replace with actual calls to your smart contract
      const active = await getActiveStakes(account); // Replace with actual implementation
      const completed = await getCompletedStakes(account); // Replace with actual implementation
      setActiveStakes(active);
      setCompletedStakes(completed);
    } catch (error) {
      console.error('Error fetching stakes:', error);
    }
  };

  // Placeholder function to simulate fetching active stakes
  const getActiveStakes = async (account) => {
    // Replace with actual logic to fetch active stakes from your smart contract
    return [{ id: 1, amount: 50 }, { id: 2, amount: 100 }];
  };

  // Placeholder function to simulate fetching completed stakes
  const getCompletedStakes = async (account) => {
    // Replace with actual logic to fetch completed stakes from your smart contract
    return [{ id: 3, amount: 30 }, { id: 4, amount: 70 }];
  };

  // Withdraw tokens from a specific stake
  const withdrawTokens = async (stakeId) => {
    try {
      // Implement withdrawal logic here
      console.log(`Withdrawing tokens for stake ID: ${stakeId}`);
      // Example: await contract.withdraw(stakeId);
      // Update stakes after withdrawal
      fetchStakes(account);
    } catch (error) {
      console.error('Error withdrawing tokens:', error);
    }
  };

  useEffect(() => {
    // Check if wallet is already connected on component mount
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.listAccounts();
        if (accounts.length > 0) {
          setProvider(provider);
          setAccount(accounts[0]);
          fetchStakes(accounts[0]);
        }
      }
    };
    checkWalletConnection();
  }, []);

  return (
    <Container>
      <h1>Catecoin Wallet Connection</h1>
      {!account ? (
        <Button onClick={connectWallet}>Connect Wallet</Button>
      ) : (
        <div>
          <h2>Connected Account: {account}</h2>
          <h3>Active Stakes</h3>
          <StakeList>
            {activeStakes.map((stake) => (
              <StakeItem key={stake.id}>
                <span>Stake ID: {stake.id}</span> - <span>Amount: {stake.amount} Catecoin</span>
                <Button onClick={() => withdrawTokens(stake.id)}>Withdraw</Button>
              </StakeItem>
            ))}
          </StakeList>
          <h3>Completed Stakes</h3>
          <StakeList>
            {completedStakes.map((stake) => (
              <StakeItem key={stake.id}>
                <span>Stake ID: {stake.id}</span> - <span>Amount: {stake.amount} Catecoin</span>
              </StakeItem>
            ))}
          </StakeList>
        </div>
      )}
    </Container>
  );
};

export default WalletConnect;
```
