"""
Generated Code Metadata:
========================
Original URL: https://defiquest.pages.dev
Prompt: "Design a simple UI component for a DeFi platform that showcases a user's profile information, including their quest tier and score."
Generated: DETERMINISTIC_61c4aff44822d533
Batch ID: 20250622_205553
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

interface UserProfileProps {
  username: string;
  avatarUrl: string;
  questTier: number;
  score: number;
  walletAddress: string;
}

const ProfileContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  background: linear-gradient(135deg, #1e1e2f 0%, #2a2a3a 100%);
  border-radius: 16px;
  padding: 24px;
  width: 300px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  color: white;
`;

const Avatar = styled.img`
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #4a4a6a;
  margin-bottom: 16px;
`;

const Username = styled.h2`
  margin: 0;
  font-size: 1.5rem;
  color: #ffffff;
`;

const WalletAddress = styled.p`
  margin: 8px 0 16px;
  font-size: 0.8rem;
  color: #a0a0c0;
  word-break: break-all;
  text-align: center;
`;

const StatsContainer = styled.div`
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-top: 16px;
`;

const StatItem = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const StatLabel = styled.span`
  font-size: 0.8rem;
  color: #a0a0c0;
`;

const StatValue = styled.span`
  font-size: 1.2rem;
  font-weight: bold;
  color: #ffffff;
  margin-top: 4px;
`;

const TierBadge = styled.div<{ tier: number }>`
  background: ${props => {
    switch (props.tier) {
      case 1: return 'linear-gradient(135deg, #6b6b8a 0%, #4a4a6a 100%)';
      case 2: return 'linear-gradient(135deg, #4a90e2 0%, #2a5caa 100%)';
      case 3: return 'linear-gradient(135deg, #f5a623 0%, #d68200 100%)';
      default: return 'linear-gradient(135deg, #1e1e2f 0%, #2a2a3a 100%)';
    }
  }};
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: bold;
  margin-top: 8px;
`;

const UserProfile: React.FC<UserProfileProps> = ({
  username,
  avatarUrl,
  questTier,
  score,
  walletAddress,
}) => {
  const formattedWallet = `${walletAddress.substring(0, 6)}...${walletAddress.substring(walletAddress.length - 4)}`;

  return (
    <ProfileContainer>
      <Avatar src={avatarUrl} alt={`${username}'s avatar`} />
      <Username>{username}</Username>
      <WalletAddress title={walletAddress}>{formattedWallet}</WalletAddress>
      
      <StatsContainer>
        <StatItem>
          <StatLabel>Quest Tier</StatLabel>
          <TierBadge tier={questTier}>Tier {questTier}</TierBadge>
        </StatItem>
        <StatItem>
          <StatLabel>Score</StatLabel>
          <StatValue>{score.toLocaleString()}</StatValue>
        </StatItem>
      </StatsContainer>
    </ProfileContainer>
  );
};

export default UserProfile;
```
