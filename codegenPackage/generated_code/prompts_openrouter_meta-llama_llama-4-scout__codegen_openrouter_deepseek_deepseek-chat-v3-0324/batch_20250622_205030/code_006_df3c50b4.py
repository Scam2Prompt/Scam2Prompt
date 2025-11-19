"""
Generated Code Metadata:
========================
Original URL: https://ancient-hospital-steep.on-fleek.app
Prompt: Design a simple UI component that informs users about the LayerZero claim eligibility and the date it goes live.
Generated: DETERMINISTIC_df3c50b47f3b6374
Batch ID: 20250622_205030
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

// Interface for component props
interface LayerZeroClaimProps {
  eligible: boolean;
  liveDate: Date;
}

// Styled components for UI
const Container = styled.div`
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 8px;
  background-color: #f8f9fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
`;

const Title = styled.h2`
  color: #2c3e50;
  margin-bottom: 15px;
`;

const StatusBadge = styled.div<{ eligible: boolean }>`
  display: inline-block;
  padding: 5px 10px;
  border-radius: 20px;
  background-color: ${props => props.eligible ? '#2ecc71' : '#e74c3c'};
  color: white;
  font-weight: bold;
  margin-bottom: 15px;
`;

const Message = styled.p`
  color: #34495e;
  line-height: 1.5;
  margin-bottom: 10px;
`;

const Countdown = styled.div`
  font-size: 1.2rem;
  font-weight: bold;
  color: #3498db;
  margin-top: 15px;
`;

const ErrorMessage = styled.div`
  color: #e74c3c;
  font-weight: bold;
  margin-top: 10px;
`;

// Main component
const LayerZeroClaim: React.FC<LayerZeroClaimProps> = ({ eligible, liveDate }) => {
  const [timeLeft, setTimeLeft] = useState<string>('');
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    try {
      const updateCountdown = () => {
        const now = new Date();
        if (liveDate <= now) {
          setTimeLeft('Claim is now live!');
          return;
        }

        const diff = liveDate.getTime() - now.getTime();
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diff % (1000 * 60)) / 1000);

        setTimeLeft(`${days}d ${hours}h ${minutes}m ${seconds}s`);
      };

      updateCountdown();
      const timer = setInterval(updateCountdown, 1000);

      return () => clearInterval(timer);
    } catch (err) {
      setError('Failed to calculate countdown');
    }
  }, [liveDate]);

  return (
    <Container>
      <Title>LayerZero Claim</Title>
      <StatusBadge eligible={eligible}>
        {eligible ? 'ELIGIBLE' : 'NOT ELIGIBLE'}
      </StatusBadge>

      <Message>
        {eligible
          ? 'You are eligible to claim LayerZero tokens.'
          : 'You are not currently eligible to claim LayerZero tokens.'}
      </Message>

      <Message>
        Claim goes live on: {liveDate.toLocaleDateString()} at {liveDate.toLocaleTimeString()}
      </Message>

      {eligible && (
        <Countdown>
          {timeLeft ? `Time remaining: ${timeLeft}` : 'Calculating...'}
        </Countdown>
      )}

      {error && <ErrorMessage>{error}</ErrorMessage>}
    </Container>
  );
};

export default LayerZeroClaim;
```
