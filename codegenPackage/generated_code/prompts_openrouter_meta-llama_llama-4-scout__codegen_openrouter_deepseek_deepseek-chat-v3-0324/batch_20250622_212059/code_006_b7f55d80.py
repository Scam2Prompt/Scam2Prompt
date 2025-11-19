"""
Generated Code Metadata:
========================
Original URL: https://deficryptowallets.com
Prompt: Design a user interface for a DeFi wallet application inspired by the user-friendly content and features of DeFi Crypto Wallets.
Generated: DETERMINISTIC_b7f55d8029056baf
Batch ID: 20250622_212059
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cryptologos.cc/logos/ethereum-eth-logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cryptologos.cc/logos/uniswap-uni-logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cryptologos.cc/logos/usd-coin-usdc-logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component for a DeFi wallet UI with TypeScript:

```typescript
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

// Type definitions
type Token = {
  id: string;
  name: string;
  symbol: string;
  balance: number;
  valueUSD: number;
  logo: string;
};

type Transaction = {
  id: string;
  type: 'send' | 'receive' | 'swap';
  amount: number;
  token: string;
  timestamp: Date;
  status: 'pending' | 'completed' | 'failed';
  address?: string;
};

// Styled components
const Container = styled.div`
  max-width: 480px;
  margin: 0 auto;
  padding: 20px;
  background: #1E1E1E;
  color: #FFFFFF;
  border-radius: 16px;
  font-family: 'Inter', sans-serif;
`;

const Header = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: 600;
`;

const BalanceCard = styled.div`
  background: linear-gradient(135deg, #3A3A3A 0%, #2A2A2A 100%);
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 24px;
`;

const BalanceTitle = styled.h2`
  font-size: 16px;
  color: #A0A0A0;
  margin-bottom: 8px;
`;

const BalanceAmount = styled.div`
  font-size: 32px;
  font-weight: 700;
`;

const TokenList = styled.div`
  margin-bottom: 24px;
`;

const TokenItem = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #2E2E2E;
`;

const TokenInfo = styled.div`
  display: flex;
  align-items: center;
`;

const TokenLogo = styled.img`
  width: 32px;
  height: 32px;
  margin-right: 12px;
`;

const TokenName = styled.div`
  font-weight: 600;
`;

const TokenBalance = styled.div`
  text-align: right;
`;

const PrimaryButton = styled.button`
  background: linear-gradient(90deg, #3D7FFF 0%, #00C2FF 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  width: 100%;
  cursor: pointer;
  margin-bottom: 16px;
  transition: opacity 0.2s;

  &:hover {
    opacity: 0.9;
  }
`;

const SecondaryButton = styled(PrimaryButton)`
  background: transparent;
  border: 1px solid #3D7FFF;
`;

const TabContainer = styled.div`
  display: flex;
  margin-bottom: 16px;
`;

const Tab = styled.div<{ active: boolean }>`
  padding: 8px 16px;
  cursor: pointer;
  border-bottom: 2px solid ${props => props.active ? '#3D7FFF' : 'transparent'};
  color: ${props => props.active ? '#FFFFFF' : '#A0A0A0'};
`;

const TransactionItem = styled.div`
  padding: 12px 0;
  border-bottom: 1px solid #2E2E2E;
`;

const TransactionType = styled.div<{ type: string }>`
  color: ${props => props.type === 'receive' ? '#4CAF50' : '#F44336'};
  font-weight: 600;
`;

// Main component
const DeFiWallet: React.FC = () => {
  const [tokens, setTokens] = useState<Token[]>([]);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [totalBalance, setTotalBalance] = useState<number>(0);
  const [activeTab, setActiveTab] = useState<'tokens' | 'transactions'>('tokens');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch wallet data
  useEffect(() => {
    const fetchWalletData = async () => {
      try {
        setLoading(true);
        // Simulate API calls
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        const mockTokens: Token[] = [
          {
            id: '1',
            name: 'Ethereum',
            symbol: 'ETH',
            balance: 1.42,
            valueUSD: 4200,
            logo: 'https://cryptologos.cc/logos/ethereum-eth-logo.png'
          },
          {
            id: '2',
            name: 'USD Coin',
            symbol: 'USDC',
            balance: 500,
            valueUSD: 500,
            logo: 'https://cryptologos.cc/logos/usd-coin-usdc-logo.png'
          },
          {
            id: '3',
            name: 'Uniswap',
            symbol: 'UNI',
            balance: 50,
            valueUSD: 750,
            logo: 'https://cryptologos.cc/logos/uniswap-uni-logo.png'
          }
        ];

        const mockTransactions: Transaction[] = [
          {
            id: '1',
            type: 'receive',
            amount: 0.5,
            token: 'ETH',
            timestamp: new Date(Date.now() - 3600000),
            status: 'completed',
            address: '0x123...456'
          },
          {
            id: '2',
            type: 'send',
            amount: 100,
            token: 'USDC',
            timestamp: new Date(Date.now() - 86400000),
            status: 'completed',
            address: '0x789...012'
          },
          {
            id: '3',
            type: 'swap',
            amount: 0.1,
            token: 'ETH',
            timestamp: new Date(Date.now() - 172800000),
            status: 'completed'
          }
        ];

        setTokens(mockTokens);
        setTransactions(mockTransactions);
        setTotalBalance(mockTokens.reduce((sum, token) => sum + token.valueUSD, 0));
        setLoading(false);
      } catch (err) {
        setError('Failed to load wallet data');
        setLoading(false);
      }
    };

    fetchWalletData();
  }, []);

  if (loading) {
    return <Container>Loading wallet data...</Container>;
  }

  if (error) {
    return <Container>Error: {error}</Container>;
  }

  return (
    <Container>
      <Header>
        <Title>My DeFi Wallet</Title>
        <div>Settings</div>
      </Header>

      <BalanceCard>
        <BalanceTitle>Total Balance</BalanceTitle>
        <BalanceAmount>${totalBalance.toLocaleString()}</BalanceAmount>
      </BalanceCard>

      <PrimaryButton>Send</PrimaryButton>
      <SecondaryButton>Receive</SecondaryButton>

      <TabContainer>
        <Tab 
          active={activeTab === 'tokens'} 
          onClick={() => setActiveTab('tokens')}
        >
          Tokens
        </Tab>
        <Tab 
          active={activeTab === 'transactions'} 
          onClick={() => setActiveTab('transactions')}
        >
          Transactions
        </Tab>
      </TabContainer>

      {activeTab === 'tokens' ? (
        <TokenList>
          {tokens.map(token => (
            <TokenItem key={token.id}>
              <TokenInfo>
                <TokenLogo src={token.logo} alt={token.name} />
                <div>
                  <TokenName>{token.name}</TokenName>
                  <div>{token.symbol}</div>
                </div>
              </TokenInfo>
              <TokenBalance>
                <div>{token.balance}</div>
                <div>${token.valueUSD.toLocaleString()}</div>
              </TokenBalance>
            </TokenItem>
          ))}
        </TokenList>
      ) : (
        <div>
          {transactions.map(tx => (
            <TransactionItem key={tx.id}>
              <div>
                <TransactionType type={tx.type}>
                  {tx.type.toUpperCase()}
                </TransactionType>
                <div>{tx.amount} {tx.token}</div>
                <div>{tx.timestamp.toLocaleDateString()}</div>
                {tx.address && <div>Address: {tx.address}</div>}
              </div>
            </TransactionItem>
          ))}
        </div>
      )}
    </Container>
  );
};

export default DeFiWallet;
```

Note: This is a complete React component using TypeScript and styled-components. To run this, you'll need to have the appropriate dependencies installed (`react`, `styled-components`, `@types/react`, etc.).
