"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: "Create a basic Fuel dApp with a Sway contract and a TypeScript frontend using the provided template."
Generated: DETERMINISTIC_3614a3c402497526
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// frontend/src/App.tsx
import React, { useState } from 'react';
import { Wallet } from 'fuels';
import { FuelProvider } from '@fuel-wallet/react';
import { ContractAbi__factory } from './contracts';

// Initialize the Fuel wallet
const wallet = Wallet.generate();

// Contract ID (replace with your deployed contract ID)
const CONTRACT_ID = '0x...';

function App() {
  const [connected, setConnected] = useState(false);
  const [balance, setBalance] = useState<string>('0');
  const [amount, setAmount] = useState<string>('');

  const connectWallet = async () => {
    try {
      await wallet.connect();
      setConnected(true);
      await getBalance();
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  const getBalance = async () => {
    try {
      const contract = ContractAbi__factory.connect(CONTRACT_ID, wallet);
      const { value } = await contract.functions.get_balance().get();
      setBalance(value.toString());
    } catch (error) {
      console.error('Error getting balance:', error);
    }
  };

  const addFuel = async () => {
    if (!amount) return;
    try {
      const contract = ContractAbi__factory.connect(CONTRACT_ID, wallet);
      await contract.functions.add_fuel(parseInt(amount)).call();
      await getBalance();
      setAmount('');
    } catch (error) {
      console.error('Error adding fuel:', error);
    }
  };

  return (
    <FuelProvider>
      <div className="App">
        <header>
          <h1>Fuel dApp</h1>
        </header>
        <main>
          {!connected ? (
            <button onClick={connectWallet}>Connect Wallet</button>
          ) : (
            <div>
              <p>Current Balance: {balance}</p>
              <div>
                <input
                  type="number"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                  placeholder="Amount to add"
                />
                <button onClick={addFuel}>Add Fuel</button>
              </div>
            </div>
          )}
        </main>
      </div>
    </FuelProvider>
  );
}

export default App;
```

```sway
// contract/src/main.sw
contract;

use std::{
    constants::ZERO_B256,
    storage::StorageMap,
};

storage {
    balances: StorageMap<Identity, u64> = StorageMap {},
}

abi FuelContract {
    #[storage(read)]
    fn get_balance() -> u64;

    #[storage(read, write)]
    fn add_fuel(amount: u64);
}

impl FuelContract for Contract {
    #[storage(read)]
    fn get_balance() -> u64 {
        let sender = msg_sender().unwrap();
        storage.balances.get(sender).try_read().unwrap_or(0)
    }

    #[storage(read, write)]
    fn add_fuel(amount: u64) {
        let sender = msg_sender().unwrap();
        let current_balance = storage.balances.get(sender).try_read().unwrap_or(0);
        storage.balances.insert(sender, current_balance + amount);
    }
}
```

```typescript
// frontend/src/contracts/index.ts
import { ContractAbi__factory } from './FuelContract';

export { ContractAbi__factory } from './FuelContract';
export type { ContractAbi } from './FuelContract';
```

```typescript
// frontend/src/contracts/FuelContract.ts
import type { Contract } from 'fuels';
import type { Interface } from '@fuel-wallet/abi-coder';

export const __contract__ = '0x...';
export const __abi__: Interface = {
  types: [
    {
      typeId: 0,
      type: 'u64',
      components: null,
      typeParameters: null,
    },
    {
      typeId: 1,
      type: 'struct Identity',
      components: [
        {
          name: 'Address',
          type: 2,
          typeArguments: null,
        },
        {
          name: 'ContractId',
          type: 3,
          typeArguments: null,
        },
      ],
      typeParameters: null,
    },
    {
      typeId: 2,
      type: 'struct Address',
      components: [
        {
          name: 'value',
          type: 4,
          typeArguments: null,
        },
      ],
      typeParameters: null,
    },
    {
      typeId: 3,
      type: 'struct ContractId',
      components: [
        {
          name: 'value',
          type: 4,
          typeArguments: null,
        },
      ],
      typeParameters: null,
    },
    {
      typeId: 4,
      type: 'b256',
      components: null,
      typeParameters: null,
    },
  ],
  functions: [
    {
      inputs: [],
      name: 'get_balance',
      output: {
        name: '',
        type: 0,
        typeArguments: null,
      },
    },
    {
      inputs: [
        {
          name: 'amount',
          type: 0,
          typeArguments: null,
        },
      ],
      name: 'add_fuel',
      output: {
        name: '',
        type: 0,
        typeArguments: null,
      },
    },
  ],
  loggedTypes: [],
};

export class ContractAbi__factory {
  static connect(id: string, wallet: Wallet): Contract {
    return new Contract(id, __abi__, wallet);
  }
}

export interface ContractAbi extends Contract {
  functions: {
    get_balance: () => Promise<{ value: bigint }>;
    add_fuel: (amount: bigint) => Promise<void>;
  };
}
```
