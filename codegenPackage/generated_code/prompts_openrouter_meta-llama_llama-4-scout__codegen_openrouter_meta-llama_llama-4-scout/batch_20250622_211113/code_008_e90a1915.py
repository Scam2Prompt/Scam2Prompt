"""
Generated Code Metadata:
========================
Original URL: https://boxesxsol.web.app
Prompt: "Generate a user interface component for users to switch between their main and trading wallets, with functionality to deposit and withdraw SOL."
Generated: DETERMINISTIC_e90a19159035f362
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// WalletSwitchComponent.tsx
import React, { useState } from 'react';
import { Button, Typography, Grid, TextField, Alert } from '@mui/material';
import { useWallet } from '@solana/wallet-adapter-react';

interface WalletSwitchComponentProps {
  mainWallet: string;
  tradingWallet: string;
  handleDeposit: (amount: number) => void;
  handleWithdraw: (amount: number) => void;
}

const WalletSwitchComponent: React.FC<WalletSwitchComponentProps> = ({
  mainWallet,
  tradingWallet,
  handleDeposit,
  handleWithdraw,
}) => {
  const [activeWallet, setActiveWallet] = useState(mainWallet);
  const [amount, setAmount] = useState(0);
  const [error, setError] = useState('');
  const wallet = useWallet();

  const handleSwitchWallet = (wallet: string) => {
    setActiveWallet(wallet);
  };

  const handleDepositSol = () => {
    if (amount <= 0) {
      setError('Invalid deposit amount');
      return;
    }
    try {
      handleDeposit(amount);
      setAmount(0);
    } catch (error) {
      setError('Error depositing SOL');
    }
  };

  const handleWithdrawSol = () => {
    if (amount <= 0) {
      setError('Invalid withdrawal amount');
      return;
    }
    try {
      handleWithdraw(amount);
      setAmount(0);
    } catch (error) {
      setError('Error withdrawing SOL');
    }
  };

  return (
    <Grid container spacing={2}>
      <Grid item xs={12}>
        <Typography variant="h6">Wallet Switcher</Typography>
      </Grid>
      <Grid item xs={12}>
        <Button
          variant={activeWallet === mainWallet ? 'contained' : 'outlined'}
          onClick={() => handleSwitchWallet(mainWallet)}
          sx={{ marginRight: 1 }}
        >
          Main Wallet ({mainWallet})
        </Button>
        <Button
          variant={activeWallet === tradingWallet ? 'contained' : 'outlined'}
          onClick={() => handleSwitchWallet(tradingWallet)}
        >
          Trading Wallet ({tradingWallet})
        </Button>
      </Grid>
      <Grid item xs={12}>
        <Typography variant="h7">Active Wallet: {activeWallet}</Typography>
      </Grid>
      <Grid item xs={12}>
        <TextField
          label="Amount (SOL)"
          type="number"
          value={amount}
          onChange={(e) => setAmount(Number(e.target.value))}
          sx={{ width: '50%' }}
        />
      </Grid>
      <Grid item xs={12}>
        <Button variant="contained" onClick={handleDepositSol}>
          Deposit SOL
        </Button>
        <Button variant="contained" onClick={handleWithdrawSol} sx={{ marginLeft: 1 }}>
          Withdraw SOL
        </Button>
      </Grid>
      {error && (
        <Grid item xs={12}>
          <Alert severity="error">{error}</Alert>
        </Grid>
      )}
    </Grid>
  );
};

export default WalletSwitchComponent;
```

```typescript
// App.tsx
import React from 'react';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import { WalletSwitchComponent } from './WalletSwitchComponent';
import { Connection, clusterApiUrl } from '@solana/web3.js';

const connection = new Connection(clusterApiUrl(WalletAdapterNetwork.Devnet));

const App = () => {
  const mainWallet = 'main-wallet-address';
  const tradingWallet = 'trading-wallet-address';

  const handleDeposit = async (amount: number) => {
    try {
      // Implement deposit logic here
      console.log(`Depositing ${amount} SOL into ${mainWallet}`);
    } catch (error) {
      console.error('Error depositing SOL:', error);
    }
  };

  const handleWithdraw = async (amount: number) => {
    try {
      // Implement withdrawal logic here
      console.log(`Withdrawing ${amount} SOL from ${mainWallet}`);
    } catch (error) {
      console.error('Error withdrawing SOL:', error);
    }
  };

  return (
    <WalletModalProvider>
      <WalletSwitchComponent
        mainWallet={mainWallet}
        tradingWallet={tradingWallet}
        handleDeposit={handleDeposit}
        handleWithdraw={handleWithdraw}
      />
    </WalletModalProvider>
  );
};

export default App;
```

```typescript
// index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
