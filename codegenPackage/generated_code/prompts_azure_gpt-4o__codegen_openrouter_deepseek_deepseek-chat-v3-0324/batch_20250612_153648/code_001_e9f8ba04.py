"""
Generated Code Metadata:
========================
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Provide an example of using the Solana Wallet Adapter with Mantine UI to authenticate a user and retrieve their wallet address.
Generated: DETERMINISTIC_e9f8ba04eddd944c
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
import { useWallet } from '@solana/wallet-adapter-react';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { Button, Group, Text, Title } from '@mantine/core';
import { useEffect, useState } from 'react';

export const SolanaAuthComponent = () => {
  const { connected, publicKey } = useWallet();
  const [walletAddress, setWalletAddress] = useState<string | null>(null);

  useEffect(() => {
    if (connected && publicKey) {
      setWalletAddress(publicKey.toString());
    } else {
      setWalletAddress(null);
    }
  }, [connected, publicKey]);

  return (
    <Group direction="column" spacing="md" align="center">
      <Title order={3}>Solana Wallet Authentication</Title>
      
      <WalletMultiButton>
        {({ connected }) => (
          <Button variant="light" color="blue" size="lg">
            {connected ? 'Connected' : 'Connect Wallet'}
          </Button>
        )}
      </WalletMultiButton>

      {connected && walletAddress && (
        <Group direction="column" spacing="xs" align="center">
          <Text weight={500}>Wallet Address:</Text>
          <Text color="dimmed" style={{ wordBreak: 'break-all' }}>
            {walletAddress}
          </Text>
        </Group>
      )}
    </Group>
  );
};
```
