"""
Generated Code Metadata:
========================
Original URL: https://moonwell.site
Prompt: Provide a code example for implementing user-friendly interfaces in a DeFi application similar to Moonwell's design.
Generated: DETERMINISTIC_0aa20239da3ce764
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component for a DeFi application interface inspired by Moonwell's design:

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { ethers } from 'ethers';
import styled from 'styled-components';

// Styled components for UI elements
const Container = styled.div`
  max-width: 480px;
  margin: 0 auto;
  padding: 24px;
  background: #1E1E3F;
  border-radius: 16px;
  color: #FFFFFF;
  font-family: 'Inter', sans-serif;
`;

const Header = styled.h2`
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #FFFFFF;
`;

const TabContainer = styled.div`
  display: flex;
  margin-bottom: 24px;
  border-bottom: 1px solid #2D2D5B;
`;

const Tab = styled.button`
  padding: 12px 16px;
  background: transparent;
  border: none;
  color: ${props => props.active ? '#FFFFFF' : '#6C6C9D'};
  font-weight: 600;
  cursor: pointer;
  border-bottom: 2px solid ${props => props.active ? '#6C5BFF' : 'transparent'};
`;

const InputContainer = styled.div`
  margin-bottom: 16px;
`;

const InputLabel = styled.div`
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 14px;
`;

const Input = styled.input`
  width: 100%;
  padding: 16px;
  background: #2D2D5B;
  border: 1px solid #3E3E6B;
  border-radius: 8px;
  color: #FFFFFF;
  font-size: 16px;
  outline: none;
  
  &:focus {
    border-color: #6C5BFF;
  }
`;

const Button = styled.button`
  width: 100%;
  padding: 16px;
  background: ${props => props.disabled ? '#3E3E6B' : '#6C5BFF'};
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: ${props => props.disabled ? 'not-allowed' : 'pointer'};
  transition: background 0.2s;
  
  &:hover {
    background: ${props => props.disabled ? '#3E3E6B' : '#7D6BFF'};
  }
`;

const BalanceInfo = styled.div`
  font-size: 14px;
  color: #A0A0C0;
  margin-top: 8px;
`;

const ErrorMessage = styled.div`
  color: #FF6B6B;
  font-size: 14px;
  margin-top: 8px;
`;

/**
 * DeFi Action Panel Component
 * Handles supply/withdraw actions for a DeFi protocol
 */
const DefiActionPanel = ({ 
  asset, 
  userBalance, 
  apy,
  onAction,
  actionType = 'supply'
}) => {
  const [amount, setAmount] = useState('');
  const [activeTab, setActiveTab] = useState(actionType);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    setActiveTab(actionType);
  }, [actionType]);

  const handleAmountChange = (e) => {
    const value = e.target.value;
    if (value === '' || /^[0-9]*\.?[0-9]*$/.test(value)) {
      setAmount(value);
      setError('');
    }
  };

  const handleMaxClick = () => {
    setAmount(userBalance.toString());
  };

  const handleAction = async () => {
    if (!amount || parseFloat(amount) <= 0) {
      setError('Please enter a valid amount');
      return;
    }

    if (parseFloat(amount) > userBalance && activeTab === 'withdraw') {
      setError('Insufficient balance');
      return;
    }

    try {
      setIsLoading(true);
      await onAction(activeTab, asset, amount);
      setAmount('');
      setError('');
    } catch (err) {
      console.error('Transaction failed:', err);
      setError(err.message || 'Transaction failed');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container>
      <Header>{asset} Market</Header>
      
      <TabContainer>
        <Tab 
          active={activeTab === 'supply'} 
          onClick={() => setActiveTab('supply')}
        >
          Supply
        </Tab>
        <Tab 
          active={activeTab === 'withdraw'} 
          onClick={() => setActiveTab('withdraw')}
        >
          Withdraw
        </Tab>
      </TabContainer>

      <InputContainer>
        <InputLabel>
          <span>Amount</span>
          <span>
            Balance: {ethers.utils.formatUnits(userBalance, 18)} {asset}
          </span>
        </InputLabel>
        <Input
          type="text"
          value={amount}
          onChange={handleAmountChange}
          placeholder="0.0"
        />
        <BalanceInfo>
          {activeTab === 'supply' ? 'Supply' : 'Withdraw'} APY: {apy}%
        </BalanceInfo>
      </InputContainer>

      {error && <ErrorMessage>{error}</ErrorMessage>}

      <Button 
        onClick={handleAction}
        disabled={!amount || isLoading}
      >
        {isLoading ? 'Processing...' : activeTab === 'supply' ? 'Supply' : 'Withdraw'} {asset}
      </Button>
    </Container>
  );
};

DefiActionPanel.propTypes = {
  asset: PropTypes.string.isRequired,
  userBalance: PropTypes.object.isRequired, // BigNumber
  apy: PropTypes.number.isRequired,
  onAction: PropTypes.func.isRequired,
  actionType: PropTypes.oneOf(['supply', 'withdraw']),
};

export default DefiActionPanel;
```
