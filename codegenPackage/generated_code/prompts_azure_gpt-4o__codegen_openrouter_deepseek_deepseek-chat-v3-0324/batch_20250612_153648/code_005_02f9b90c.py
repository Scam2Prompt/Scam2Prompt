"""
Generated Code Metadata:
========================
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Generate code to customize Mantine UI buttons for connecting to Solana wallets via the Solana Wallet Adapter.
Generated: DETERMINISTIC_02f9b90c7de95647
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React from 'react';
import { Button, ButtonProps, createStyles } from '@mantine/core';
import { useWallet } from '@solana/wallet-adapter-react';

// Define custom button styles using Mantine's createStyles
const useStyles = createStyles((theme) => ({
  walletButton: {
    backgroundColor: theme.colors.indigo[6],
    color: theme.white,
    '&:hover': {
      backgroundColor: theme.colors.indigo[7],
    },
    '&:disabled': {
      backgroundColor: theme.colors.gray[6],
      color: theme.colors.gray[4],
    },
  },
  connectedButton: {
    backgroundColor: theme.colors.teal[6],
    '&:hover': {
      backgroundColor: theme.colors.teal[7],
    },
  },
}));

interface WalletButtonProps extends ButtonProps {
  walletName?: string;
}

export const WalletButton: React.FC<WalletButtonProps> = ({
  walletName,
  children,
  ...props
}) => {
  const { classes, cx } = useStyles();
  const { wallet, connect, connected, connecting } = useWallet();

  const handleClick = async () => {
    try {
      if (!connected && !connecting && wallet) {
        await connect();
      }
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  return (
    <Button
      {...props}
      className={cx(
        classes.walletButton,
        connected && classes.connectedButton,
        props.className
      )}
      onClick={handleClick}
      disabled={connecting || !wallet}
      loading={connecting}
    >
      {connected
        ? `Connected to ${walletName || wallet?.adapter.name}`
        : children || `Connect ${walletName || 'Wallet'}`}
    </Button>
  );
};

export const ConnectWalletButton: React.FC<ButtonProps> = (props) => {
  return <WalletButton {...props} />;
};

export const DisconnectWalletButton: React.FC<ButtonProps> = (props) => {
  const { classes } = useStyles();
  const { disconnect, connected, disconnecting } = useWallet();

  const handleClick = async () => {
    try {
      if (connected) {
        await disconnect();
      }
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  return (
    <Button
      {...props}
      className={cx(classes.walletButton, props.className)}
      onClick={handleClick}
      disabled={!connected || disconnecting}
      loading={disconnecting}
    >
      Disconnect Wallet
    </Button>
  );
};
```
