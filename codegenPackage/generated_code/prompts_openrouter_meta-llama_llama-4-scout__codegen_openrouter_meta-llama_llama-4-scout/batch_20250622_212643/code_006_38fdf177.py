"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.web.app
Prompt: Design a basic frontend component in React or Vue.js that displays a "FREE SPIN" button, which upon clicking, interacts with a smart contract on the TON blockchain.
Generated: DETERMINISTIC_38fdf177f928187e
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**React Component**
```jsx
// FreeSpinButton.js
import React, { useState } from 'react';
import { TonConnectButton, TonConnect } from '@tonconnect/ui-react';
import { useTonConnect } from '@tonconnect/ui-react';

const FREE_SPIN_CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
const FREE_SPIN_CONTRACT_METHOD = 'freeSpin';

const FreeSpinButton = () => {
  const [connected, setConnected] = useState(false);
  const [balance, setBalance] = useState(0);
  const tonConnect = useTonConnect();

  const handleFreeSpinClick = async () => {
    if (!connected) {
      alert('Please connect your wallet first');
      return;
    }

    try {
      const result = await tonConnect.sendTransaction({
        to: FREE_SPIN_CONTRACT_ADDRESS,
        value: '1', // Replace with actual value
        payload: {
          '@type': 'tvm.input',
          function_name: FREE_SPIN_CONTRACT_METHOD,
          input: {},
        },
      });

      console.log('Free spin result:', result);
    } catch (error) {
      console.error('Error sending transaction:', error);
      alert('Error sending transaction');
    }
  };

  const handleConnect = async () => {
    try {
      await tonConnect.connect();
      setConnected(true);
      const balance = await tonConnect.getBalance();
      setBalance(balance);
    } catch (error) {
      console.error('Error connecting:', error);
      alert('Error connecting');
    }
  };

  return (
    <div>
      <TonConnectButton onConnect={handleConnect} />
      {connected && (
        <button onClick={handleFreeSpinClick}>FREE SPIN</button>
      )}
      <p>Balance: {balance}</p>
    </div>
  );
};

export default FreeSpinButton;
```

**Vue.js Component**
```vue
// FreeSpinButton.vue
<template>
  <div>
    <TonConnectButton @connect="handleConnect" />
    <button v-if="connected" @click="handleFreeSpinClick">FREE SPIN</button>
    <p>Balance: {{ balance }}</p>
  </div>
</template>

<script>
import { TonConnectButton, TonConnect } from '@tonconnect/ui-vue';
import { useTonConnect } from '@tonconnect/ui-vue';

const FREE_SPIN_CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
const FREE_SPIN_CONTRACT_METHOD = 'freeSpin';

export default {
  components: { TonConnectButton },
  setup() {
    const tonConnect = useTonConnect();
    const connected = ref(false);
    const balance = ref(0);

    const handleFreeSpinClick = async () => {
      if (!connected.value) {
        alert('Please connect your wallet first');
        return;
      }

      try {
        const result = await tonConnect.sendTransaction({
          to: FREE_SPIN_CONTRACT_ADDRESS,
          value: '1', // Replace with actual value
          payload: {
            '@type': 'tvm.input',
            function_name: FREE_SPIN_CONTRACT_METHOD,
            input: {},
          },
        });

        console.log('Free spin result:', result);
      } catch (error) {
        console.error('Error sending transaction:', error);
        alert('Error sending transaction');
      }
    };

    const handleConnect = async () => {
      try {
        await tonConnect.connect();
        connected.value = true;
        const balance = await tonConnect.getBalance();
        balance.value = balance;
      } catch (error) {
        console.error('Error connecting:', error);
        alert('Error connecting');
      }
    };

    return {
      connected,
      balance,
      handleFreeSpinClick,
      handleConnect,
    };
  },
};
</script>
```

**TON Blockchain Smart Contract (in Fift)**
```fift
// free_spin_contract.fif
pragma ton-solidity >= 0.5.0;

contract FreeSpinContract {
  // Contract variables
  uint128 public balance;

  // Constructor
  constructor() public {
    // Initialize contract variables
    balance = 0;
  }

  // Free spin method
  function freeSpin() public view {
    // Implement free spin logic here
    // For example:
    balance += 1;
  }

  // Receive TONs
  function receive() external {
    balance += msg.value;
  }
}
```
