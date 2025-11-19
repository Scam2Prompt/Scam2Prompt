"""
Generated Code Metadata:
========================
Original URL: https://zapper-frontend-next-mh2dokjx4-zapper-fi.vercel.app
Prompt: Design a user interface for a Web3 wallet tracker inspired by Zapper's features and user experience.
Generated: DETERMINISTIC_371f4f8f50971618
Batch ID: 20250622_205335
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wallettracker.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
// WalletTracker.tsx - Main component for the Web3 wallet tracker
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import styled from 'styled-components';
import { WalletOverview, AssetList, TransactionHistory, PortfolioChart } from './components';
import { fetchWalletData, fetchTokenPrices } from './api';
import { ThemeProvider, lightTheme } from './theme';
import { LoadingSpinner, ErrorMessage } from './components/common';

interface WalletData {
  address: string;
  balance: string;
  tokens: Token[];
  nfts: NFT[];
  transactions: Transaction[];
  netWorth: number;
  chains: Chain[];
}

interface Token {
  symbol: string;
  balance: string;
  value: number;
  price: number;
  change24h: number;
  contractAddress: string;
}

interface NFT {
  name: string;
  contractAddress: string;
  tokenId: string;
  imageUrl: string;
}

interface Transaction {
  hash: string;
  timestamp: number;
  value: string;
  from: string;
  to: string;
  status: 'pending' | 'confirmed' | 'failed';
}

interface Chain {
  id: number;
  name: string;
  nativeBalance: string;
}

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: ${props => props.theme.fonts.main};
`;

const Header = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
`;

const Title = styled.h1`
  color: ${props => props.theme.colors.primary};
  font-size: 2rem;
`;

const SearchBar = styled.div`
  display: flex;
  gap: 1rem;
`;

const Input = styled.input`
  padding: 0.75rem 1rem;
  border: 1px solid ${props => props.theme.colors.border};
  border-radius: 8px;
  width: 300px;
  font-size: 1rem;
`;

const Button = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: ${props => props.theme.colors.primary};
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;

  &:hover {
    background-color: ${props => props.theme.colors.primaryDark};
  }
`;

const Dashboard = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-top: 2rem;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
`;

const WalletTracker: React.FC = () => {
  const [walletAddress, setWalletAddress] = useState<string>('');
  const [walletData, setWalletData] = useState<WalletData | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async () => {
    if (!ethers.utils.isAddress(walletAddress)) {
      setError('Invalid Ethereum address');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const data = await fetchWalletData(walletAddress);
      setWalletData(data);
    } catch (err) {
      setError('Failed to fetch wallet data. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (walletData) {
      const fetchPrices = async () => {
        try {
          const prices = await fetchTokenPrices(
            walletData.tokens.map(t => t.contractAddress)
          );
          setWalletData(prev => ({
            ...prev!,
            tokens: prev!.tokens.map(token => ({
              ...token,
              price: prices[token.contractAddress]?.price || token.price,
              change24h: prices[token.contractAddress]?.change24h || token.change24h
            }))
          }));
        } catch (err) {
          console.error('Failed to update token prices', err);
        }
      };

      fetchPrices();
      const interval = setInterval(fetchPrices, 60000); // Update prices every minute
      return () => clearInterval(interval);
    }
  }, [walletData]);

  return (
    <ThemeProvider theme={lightTheme}>
      <Container>
        <Header>
          <Title>Web3 Wallet Tracker</Title>
          <SearchBar>
            <Input
              type="text"
              placeholder="Enter wallet address (0x...)"
              value={walletAddress}
              onChange={(e) => setWalletAddress(e.target.value)}
            />
            <Button onClick={handleSearch}>Search</Button>
          </SearchBar>
        </Header>

        {error && <ErrorMessage message={error} />}
        {loading && <LoadingSpinner />}

        {walletData && !loading && (
          <>
            <WalletOverview
              address={walletData.address}
              balance={walletData.balance}
              netWorth={walletData.netWorth}
              chains={walletData.chains}
            />

            <Dashboard>
              <PortfolioChart tokens={walletData.tokens} />

              <div>
                <AssetList
                  tokens={walletData.tokens}
                  nfts={walletData.nfts}
                />
                <TransactionHistory transactions={walletData.transactions} />
              </div>
            </Dashboard>
          </>
        )}
      </Container>
    </ThemeProvider>
  );
};

export default WalletTracker;
```

```typescript
// api.ts - API service functions
import axios from 'axios';

const API_BASE_URL = 'https://api.wallettracker.com/v1';

export const fetchWalletData = async (address: string): Promise<WalletData> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/wallet/${address}`);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message || 'Failed to fetch wallet data');
    }
    throw new Error('Unknown error occurred');
  }
};

export const fetchTokenPrices = async (contractAddresses: string[]): Promise<Record<string, { price: number; change24h: number }>> => {
  if (contractAddresses.length === 0) return {};

  try {
    const response = await axios.post(`${API_BASE_URL}/tokens/prices`, {
      addresses: contractAddresses
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message || 'Failed to fetch token prices');
    }
    throw new Error('Unknown error occurred');
  }
};
```

```typescript
// components/WalletOverview.tsx
import React from 'react';
import styled from 'styled-components';

interface WalletOverviewProps {
  address: string;
  balance: string;
  netWorth: number;
  chains: Chain[];
}

const OverviewContainer = styled.div`
  background: ${props => props.theme.colors.cardBackground};
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: ${props => props.theme.shadows.card};
`;

const Address = styled.div`
  font-family: ${props => props.theme.fonts.mono};
  color: ${props => props.theme.colors.textSecondary};
  margin-bottom: 1rem;
`;

const BalanceContainer = styled.div`
  display: flex;
  align-items: baseline;
  gap: 1rem;
  margin-bottom: 1rem;
`;

const Balance = styled.h2`
  font-size: 2.5rem;
  color: ${props => props.theme.colors.textPrimary};
`;

const NetWorth = styled.div`
  font-size: 1.25rem;
  color: ${props => props.theme.colors.textSecondary};
`;

const ChainsList = styled.div`
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
`;

const ChainBadge = styled.div`
  background: ${props => props.theme.colors.background};
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
`;

const WalletOverview: React.FC<WalletOverviewProps> = ({
  address,
  balance,
  netWorth,
  chains
}) => {
  const shortenedAddress = `${address.substring(0, 6)}...${address.substring(38)}`;

  return (
    <OverviewContainer>
      <Address>{shortenedAddress}</Address>
      <BalanceContainer>
        <Balance>{balance} ETH</Balance>
        <NetWorth>${netWorth.toLocaleString()}</NetWorth>
      </BalanceContainer>
      <ChainsList>
        {chains.map(chain => (
          <ChainBadge key={chain.id}>{chain.name}</ChainBad
