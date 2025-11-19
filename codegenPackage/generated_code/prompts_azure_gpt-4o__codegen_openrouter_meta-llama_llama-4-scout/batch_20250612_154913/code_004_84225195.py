"""
Generated Code Metadata:
========================
Original URL: https://permasolution.pages.dev
Prompt: Write a script to deploy a smart contract on the peaq blockchain for managing community nodes, inspired by Teneo Protocol's use case.
Generated: DETERMINISTIC_8422519501f00e33
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { mnemonicGenerate } = require('@polkadot/util-crypto');
const fs = require('fs');

// Set up constants
const PEAQ_WS_URL = 'wss://testnet.peaq.network';
const CONTRACT_NAME = 'CommunityNodes';
const CONTRACT_SOURCE_FILE = './contracts/community_nodes.rs';
const CONTRACT_WASM_FILE = './contracts/community_nodes.wasm';

// Generate a new mnemonic for the deployer account
async function generateMnemonic() {
  return mnemonicGenerate();
}

// Create a new account from the mnemonic
async function createAccount(mnemonic) {
  const keyring = new Keyring();
  const account = keyring.addFromMnemonic(mnemonic);
  return account;
}

// Connect to the Peaq blockchain
async function connectToPeaq() {
  const wsProvider = new WsProvider(PEAQ_WS_URL);
  const api = await ApiPromise.create({ provider: wsProvider });
  return api;
}

// Compile and deploy the smart contract
async function deployContract(api, account, wasmFile) {
  // Read the compiled contract wasm
  const wasm = fs.readFileSync(wasmFile);

  // Get the contract ABI
  const abi = JSON.parse(fs.readFileSync(`${CONTRACT_NAME}.json`, 'utf8'));

  // Deploy the contract
  const tx = api.tx.contracts.instantiateWithCode(
    wasm,
    abi,
    '0x',
    { value: 0 }
  );

  // Sign and send the transaction
  const txHash = await tx.signAndSend(account);
  console.log(`Contract deployment transaction hash: ${txHash}`);

  // Wait for the transaction to be included
  await api.rpc.chain.waitForFinalizedBlock();

  // Get the contract address
  const contractAddress = await api.query.contracts.instantiates(txHash);

  return contractAddress;
}

// Main deployment script
async function main() {
  try {
    // Generate a new mnemonic and create an account
    const mnemonic = await generateMnemonic();
    const account = await createAccount(mnemonic);
    console.log(`Deployer account address: ${account.address}`);

    // Connect to the Peaq blockchain
    const api = await connectToPeaq();

    // Deploy the contract
    const contractAddress = await deployContract(api, account, CONTRACT_WASM_FILE);
    console.log(`Contract address: ${contractAddress}`);

  } catch (error) {
    console.error(error);
  }
}

main();
```

```rust
// contracts/community_nodes.rs
use ink_lang as ink;

#[ink::contract]
mod community_nodes {
    use ink_lang as ink;

    #[ink(storage)]
    pub struct CommunityNodes {
        pub node_count: u32,
        pub nodes: Vec<AccountId>,
    }

    impl CommunityNodes {
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                node_count: 0,
                nodes: Vec::new(),
            }
        }

        #[ink(message)]
        pub fn add_node(&mut self, node: AccountId) {
            self.nodes.push(node);
            self.node_count += 1;
        }

        #[ink(message)]
        pub fn remove_node(&mut self, node: AccountId) {
            self.nodes.retain(|n| *n != node);
            self.node_count -= 1;
        }

        #[ink(message)]
        pub fn get_node_count(&self) -> u32 {
            self.node_count
        }

        #[ink(message)]
        pub fn get_nodes(&self) -> Vec<AccountId> {
            self.nodes.clone()
        }
    }
}
```

To compile the smart contract, use the `cargo-contract` tool:

```bash
cargo-contract build
```

This will generate the `community_nodes.wasm` and `community_nodes.json` files in the `contracts` directory. 

Make sure to install the required dependencies:

```bash
npm install @polkadot/api @polkadot/util-crypto
```
