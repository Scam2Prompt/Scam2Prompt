"""
Generated Code Metadata:
========================
Original URL: https://cowswap.cc
Prompt: Design a UI component for a token list feature, similar to the one on CoW Swap, using React and Web3 libraries.
Generated: DETERMINISTIC_fc774aaedd07423c
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { ethers } from 'ethers';
import styled from 'styled-components';
import { Token } from '@uniswap/sdk-core';
import { isAddress } from '@ethersproject/address';
import { useTokenList } from './hooks/useTokenList'; // Custom hook for fetching token list
import { LoadingSpinner } from './components/LoadingSpinner'; // Custom loading component
import { ErrorMessage } from './components/ErrorMessage'; // Custom error component

// Styled components for the UI
const TokenListContainer = styled.div`
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
`;

const SearchInput = styled.input`
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  font-size: 14px;
  outline: none;
  margin-bottom: 16px;

  &:focus {
    border-color: #5c6bc0;
  }
`;

const TokenItem = styled.div`
  display: flex;
  align-items: center;
  padding: 12px 16px;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: #f5f5f5;
  }
`;

const TokenLogo = styled.img`
  width: 24px;
  height: 24px;
  margin-right: 12px;
  border-radius: 50%;
`;

const TokenSymbol = styled.span`
  font-weight: 500;
  margin-right: 8px;
`;

const TokenName = styled.span`
  color: #666;
  font-size: 14px;
`;

const TokenBalance = styled.div`
  margin-left: auto;
  text-align: right;
`;

const TokenListHeader = styled.div`
  padding: 16px;
  border-bottom: 1px solid #e1e1e1;
  font-weight: 600;
`;

const TokenListBody = styled.div`
  max-height: 400px;
  overflow-y: auto;
`;

const NoResults = styled.div`
  padding: 16px;
  text-align: center;
  color: #666;
`;

// Main component
const TokenList = ({ onTokenSelect }) => {
  const { account, library } = useWeb3React();
  const [searchQuery, setSearchQuery] = useState('');
  const [balances, setBalances] = useState({});
  const { tokens, loading, error } = useTokenList();
  const [filteredTokens, setFilteredTokens] = useState([]);

  // Filter tokens based on search query
  useEffect(() => {
    if (!tokens) return;

    const filtered = tokens.filter((token) => {
      const query = searchQuery.toLowerCase();
      return (
        token.name.toLowerCase().includes(query) ||
        token.symbol.toLowerCase().includes(query) ||
        (isAddress(searchQuery) && token.address.toLowerCase() === searchQuery.toLowerCase())
      );
    });

    setFilteredTokens(filtered);
  }, [searchQuery, tokens]);

  // Fetch token balances for the connected account
  useEffect(() => {
    if (!account || !library || !tokens) return;

    const fetchBalances = async () => {
      const balancePromises = tokens.map(async (token) => {
        try {
          const contract = new ethers.Contract(
            token.address,
            ['function balanceOf(address) view returns (uint256)'],
            library
          );
          const balance = await contract.balanceOf(account);
          return {
            address: token.address,
            balance: ethers.utils.formatUnits(balance, token.decimals),
          };
        } catch (err) {
          console.error(`Error fetching balance for ${token.symbol}:`, err);
          return {
            address: token.address,
            balance: '0',
          };
        }
      });

      const results = await Promise.all(balancePromises);
      const balanceMap = results.reduce((acc, { address, balance }) => {
        acc[address] = balance;
        return acc;
      }, {});

      setBalances(balanceMap);
    };

    fetchBalances();
  }, [account, library, tokens]);

  if (loading) {
    return <LoadingSpinner />;
  }

  if (error) {
    return <ErrorMessage message="Failed to load token list" />;
  }

  return (
    <TokenListContainer>
      <TokenListHeader>Select a Token</TokenListHeader>
      <div style={{ padding: '16px' }}>
        <SearchInput
          type="text"
          placeholder="Search name or paste address"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </div>
      <TokenListBody>
        {filteredTokens.length === 0 ? (
          <NoResults>No tokens found</NoResults>
        ) : (
          filteredTokens.map((token) => (
            <TokenItem
              key={token.address}
              onClick={() => onTokenSelect(new Token(token.chainId, token.address, token.decimals, token.symbol, token.name))}
            >
              <TokenLogo src={token.logoURI} alt={`${token.symbol} logo`} />
              <div>
                <TokenSymbol>{token.symbol}</TokenSymbol>
                <TokenName>{token.name}</TokenName>
              </div>
              <TokenBalance>
                {balances[token.address] || '0'}
              </TokenBalance>
            </TokenItem>
          ))
        )}
      </TokenListBody>
    </TokenListContainer>
  );
};

export default TokenList;
```
