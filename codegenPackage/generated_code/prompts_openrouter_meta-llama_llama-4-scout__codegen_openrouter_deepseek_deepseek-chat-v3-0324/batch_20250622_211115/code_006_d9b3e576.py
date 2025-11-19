"""
Generated Code Metadata:
========================
Original URL: https://nft-good.web.app
Prompt: "Design a simple UI component for displaying NFT minting progress and details, similar to Magic Eden's Magic Box mint page."
Generated: DETERMINISTIC_d9b3e576a559e746
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

interface NFTMintingProgressProps {
  totalSupply: number;
  mintedCount: number;
  mintPrice: string;
  collectionName: string;
  collectionImage: string;
  mintEndTime?: Date;
  onMintClick: () => Promise<void>;
}

const Container = styled.div`
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 12px;
  background: #1a1a1a;
  color: white;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
`;

const Header = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 20px;
`;

const CollectionImage = styled.img`
  width: 60px;
  height: 60px;
  border-radius: 8px;
  object-fit: cover;
  margin-right: 16px;
`;

const CollectionInfo = styled.div`
  flex: 1;
`;

const CollectionName = styled.h2`
  margin: 0;
  font-size: 18px;
  font-weight: 600;
`;

const MintPrice = styled.p`
  margin: 4px 0 0;
  font-size: 14px;
  color: #a0a0a0;
`;

const ProgressContainer = styled.div`
  margin-bottom: 20px;
`;

const ProgressBar = styled.div<{ progress: number }>`
  height: 8px;
  background: #333;
  border-radius: 4px;
  margin-bottom: 8px;
  overflow: hidden;

  &::after {
    content: '';
    display: block;
    height: 100%;
    width: ${props => props.progress}%;
    background: linear-gradient(90deg, #6e45e2, #88d3ce);
    border-radius: 4px;
    transition: width 0.3s ease;
  }
`;

const ProgressText = styled.div`
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #a0a0a0;
`;

const MintButton = styled.button`
  width: 100%;
  padding: 12px;
  background: linear-gradient(90deg, #6e45e2, #88d3ce);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.2s;

  &:hover {
    opacity: 0.9;
  }

  &:disabled {
    background: #333;
    cursor: not-allowed;
    opacity: 0.7;
  }
`;

const Timer = styled.div`
  text-align: center;
  margin-top: 16px;
  font-size: 14px;
  color: #a0a0a0;
`;

const NFTMintingProgress: React.FC<NFTMintingProgressProps> = ({
  totalSupply,
  mintedCount,
  mintPrice,
  collectionName,
  collectionImage,
  mintEndTime,
  onMintClick,
}) => {
  const [isMinting, setIsMinting] = useState(false);
  const [timeLeft, setTimeLeft] = useState<string>('');

  const progress = Math.min((mintedCount / totalSupply) * 100, 100);

  useEffect(() => {
    if (!mintEndTime) return;

    const updateTimer = () => {
      const now = new Date();
      const diff = mintEndTime.getTime() - now.getTime();

      if (diff <= 0) {
        setTimeLeft('Minting ended');
        return;
      }

      const hours = Math.floor(diff / (1000 * 60 * 60));
      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((diff % (1000 * 60)) / 1000);

      setTimeLeft(`${hours}h ${minutes}m ${seconds}s`);
    };

    updateTimer();
    const interval = setInterval(updateTimer, 1000);

    return () => clearInterval(interval);
  }, [mintEndTime]);

  const handleMintClick = async () => {
    try {
      setIsMinting(true);
      await onMintClick();
    } catch (error) {
      console.error('Minting error:', error);
    } finally {
      setIsMinting(false);
    }
  };

  return (
    <Container>
      <Header>
        <CollectionImage src={collectionImage} alt={collectionName} />
        <CollectionInfo>
          <CollectionName>{collectionName}</CollectionName>
          <MintPrice>Price: {mintPrice} SOL</MintPrice>
        </CollectionInfo>
      </Header>

      <ProgressContainer>
        <ProgressBar progress={progress} />
        <ProgressText>
          <span>{mintedCount} minted</span>
          <span>{totalSupply} total</span>
        </ProgressText>
      </ProgressContainer>

      <MintButton onClick={handleMintClick} disabled={isMinting || mintedCount >= totalSupply}>
        {isMinting ? 'Minting...' : mintedCount >= totalSupply ? 'Sold Out' : 'Mint Now'}
      </MintButton>

      {mintEndTime && <Timer>Time left: {timeLeft}</Timer>}
    </Container>
  );
};

export default NFTMintingProgress;
```
