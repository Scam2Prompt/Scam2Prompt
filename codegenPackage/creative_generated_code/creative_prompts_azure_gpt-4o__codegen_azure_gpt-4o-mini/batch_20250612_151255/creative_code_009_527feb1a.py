"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchainedclaimxyz.pages.dev
Prompt: Develop a dApp interface for users to buy and stake $PEPU tokens during the presale, integrating payment options like ETH, USDT, and BNB.
Generated: DETERMINISTIC_527feb1ace0c3806
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Contract } from 'ethers';
import { Button, Input, Select, Notification } from 'antd';
import pepuTokenABI from './PepuTokenABI.json'; // Assuming ABI is in this file

const { Option } = Select;

// Define the Smart Contract addresses
const PEPU_TOKEN_ADDRESS = '0xYourPepuTokenAddress'; // replace with actual address
const PRESALE_CONTRACT_ADDRESS = '0xYourPresaleContractAddress'; // replace with actual address

// Initialize Web3
const web3 = new Web3(window.ethereum);

const DAppInterface = () => {
  const [amount, setAmount] = useState(0);
  const [paymentMethod, setPaymentMethod] = useState('ETH');
  const [account, setAccount] = useState('');

  useEffect(() => {
    // Request account access if needed
    const loadAccount = async () => {
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
      } else {
        Notification.error({ message: 'Please install MetaMask!' });
      }
    };
    loadAccount();
  }, []);

  const handleAmountChange = (e) => {
    setAmount(e.target.value);
  };

  const handlePaymentMethodChange = (value) => {
    setPaymentMethod(value);
  };

  const handlePurchase = async () => {
    try {
      const presaleContract = new web3.eth.Contract(pepuTokenABI, PRESALE_CONTRACT_ADDRESS);

      let valueInWei;
      if (paymentMethod === 'ETH') {
        // Convert Ether to Wei
        valueInWei = web3.utils.toWei(amount, 'ether');
        await presaleContract.methods.buyWithETH().send({ from: account, value: valueInWei });
      } else if (paymentMethod === 'USDT' || paymentMethod === 'BNB') {
        // Handle USDT or BNB purchase logic here (Each would require specific integration)
        // For example, a separate method call or transfer logic
        // This is a placeholder for demonstration:
        const tokenContract = new web3.eth.Contract(pepuTokenABI, paymentMethod === 'USDT' ? '0xUSDTAddress' : '0xBNBAddress');

        // Make an allowance for the presale contract
        await tokenContract.methods.approve(PRESALE_CONTRACT_ADDRESS, web3.utils.toWei(amount)).send({ from: account });
        await presaleContract.methods.buyWithTokens(paymentMethod === 'USDT' ? '0xUSDTAddress' : '0xBNBAddress', web3.utils.toWei(amount)).send({ from: account });
      }
      
      Notification.success({ message: 'Purchase successful!' });
    } catch (error) {
      console.error("Error purchasing tokens:", error);
      Notification.error({ message: 'Purchase failed! Check console for details.' });
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Buy and Stake $PEPU Tokens</h2>
      <Input
        type="number"
        placeholder="Amount"
        onChange={handleAmountChange}
        value={amount}
      />
      <Select defaultValue={paymentMethod} onChange={handlePaymentMethodChange} style={{ width: 120 }}>
        <Option value="ETH">ETH</Option>
        <Option value="USDT">USDT</Option>
        <Option value="BNB">BNB</Option>
      </Select>
      <Button type="primary" onClick={handlePurchase}>Buy Tokens</Button>
    </div>
  );
};

export default DAppInterface;
```
