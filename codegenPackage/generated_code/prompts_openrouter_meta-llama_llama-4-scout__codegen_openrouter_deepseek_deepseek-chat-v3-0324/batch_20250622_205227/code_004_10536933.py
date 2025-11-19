"""
Generated Code Metadata:
========================
Original URL: https://cpumpdapp-hwk6.vercel.app
Prompt: "Design a UI component for displaying coin information, including the coin's symbol, market cap, and listing on Pancake Swap, inspired by the layout on https://cpumpdapp-hwk6.vercel.app."
Generated: DETERMINISTIC_10536933d76de5bf
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React from 'react';
import styled from 'styled-components';

interface CoinInfo {
  symbol: string;
  marketCap: number;
  isListedOnPancakeSwap: boolean;
  logoUrl?: string;
}

interface CoinCardProps {
  coin: CoinInfo;
}

const CardContainer = styled.div`
  background: #1E1E1E;
  border-radius: 12px;
  padding: 16px;
  width: 240px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
  &:hover {
    transform: translateY(-4px);
  }
`;

const CoinHeader = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 12px;
`;

const CoinLogo = styled.img`
  width: 32px;
  height: 32px;
  border-radius: 50%;
  margin-right: 8px;
`;

const CoinSymbol = styled.h3`
  color: #FFFFFF;
  font-size: 18px;
  font-weight: 600;
  margin: 0;
`;

const MarketCap = styled.div`
  color: #A0A0A0;
  font-size: 14px;
  margin-bottom: 12px;
`;

const PancakeSwapBadge = styled.div<{ listed: boolean }>`
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  background: ${props => props.listed ? '#1FC7D4' : '#FF4D4D'};
  color: white;
`;

const formatMarketCap = (value: number): string => {
  if (value >= 1e9) {
    return `$${(value / 1e9).toFixed(2)}B`;
  } else if (value >= 1e6) {
    return `$${(value / 1e6).toFixed(2)}M`;
  } else if (value >= 1e3) {
    return `$${(value / 1e3).toFixed(2)}K`;
  }
  return `$${value.toFixed(2)}`;
};

const CoinCard: React.FC<CoinCardProps> = ({ coin }) => {
  return (
    <CardContainer>
      <CoinHeader>
        {coin.logoUrl && <CoinLogo src={coin.logoUrl} alt={`${coin.symbol} logo`} />}
        <CoinSymbol>{coin.symbol}</CoinSymbol>
      </CoinHeader>
      <MarketCap>Market Cap: {formatMarketCap(coin.marketCap)}</MarketCap>
      <PancakeSwapBadge listed={coin.isListedOnPancakeSwap}>
        {coin.isListedOnPancakeSwap ? 'Listed on PancakeSwap' : 'Not on PancakeSwap'}
      </PancakeSwapBadge>
    </CardContainer>
  );
};

export default CoinCard;
```
