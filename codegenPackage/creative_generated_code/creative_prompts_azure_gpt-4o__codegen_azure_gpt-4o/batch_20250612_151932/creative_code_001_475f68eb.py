"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Provide an example of deploying a smart contract to StarkNet using Cairo, and explain how to integrate it with a dApp frontend.
Generated: DETERMINISTIC_475f68eb6ff1f653
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Smart Contract Code (Cairo)

```cairo
# Save this file as `simple_contract.cairo`

%lang starknet

@contract_interface
namespace ERC20:
    func name() -> (res: felt) { }
    func symbol() -> (res: felt) { }
    func decimals() -> (res: felt) { }
    func totalSupply() -> (res: felt) { }
    func balanceOf(account: felt) -> (res: felt) { }
    func transfer(recipient: felt, amount: felt) -> (success: felt) { }
end

# Simple storage contract
@storage_var
func stored_value() -> (value: felt):
end

@external
func set_value{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(value: felt):
    # Store a value on the blockchain
    stored_value.write(value)
    return ()
end

@view
func get_value{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}() -> (value: felt):
    # Read the stored value
    let (value) = stored_value.read()
    return (value=value)
end
```

---

### Deployment Script (Python with StarkNet CLI Integration)

```python
# Save this script as deploy_contract.py

import subprocess

# Path to cairo file
CONTRACT_PATH = "simple_contract.cairo"

try:
    # Compile the smart contract
    print("Compiling the contract...")
    compile_process = subprocess.run(
        ["starknet-compile", CONTRACT_PATH, "--output", "simple_contract.json"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print("Compilation successful.")

    # Deploy the compiled contract
    print("Deploying the contract...")
    deploy_process = subprocess.run(
        ["starknet", "deploy", "--contract", "simple_contract.json"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    deployment_output = deploy_process.stdout.decode()
    
    # Extract contract address
    for line in deployment_output.split("\n"):
        if "Contract address" in line:
            contract_address = line.split(":")[1].strip()
            break

    print(f"Contract deployed successfully at address: {contract_address}")

except subprocess.CalledProcessError as e:
    print("Error during deployment process.")
    print("Output:", e.stdout.decode())
    print("Error:", e.stderr.decode())
```

---

### dApp Frontend Integration (JavaScript with StarkNet.js)

```javascript
// Save this as starknet_integration.js

import { Provider, Contract, defaultProvider } from "starknet";

// Contract details
const CONTRACT_ADDRESS = "0xCONTRACT_ADDRESS"; // Replace with the deployed contract address
const CONTRACT_ABI = [
  {
    name: "get_value",
    type: "function",
    stateMutability: "view",
    inputs: [],
    outputs: [{ type: "felt", name: "value" }],
  },
  {
    name: "set_value",
    type: "function",
    inputs: [{ type: "felt", name: "value" }],
    outputs: [],
  },
  // Add other functions if needed
];

// Initialize StarkNet.js Provider
const provider = new Provider({ sequencer: { network: "goerli-alpha" } });

async function interactWithContract() {
  try {
    // Initialize the contract
    const contract = new Contract(CONTRACT_ABI, CONTRACT_ADDRESS, provider);

    // Call a view function (get_value)
    console.log("Reading value from contract...");
    const { value } = await contract.get_value();
    console.log("Stored value:", value);

    // Send a transaction to set_value
    console.log("Setting value in contract...");
    const setValueReceipt = await contract.invoke("set_value", { value: 42 });
    console.log("Transaction receipt:", setValueReceipt);
  } catch (error) {
    console.error("Error interacting with contract:", error);
  }
}

// Call the function to interact with the contract
interactWithContract();
```

---

### Notes:
- Replace `"0xCONTRACT_ADDRESS"` in the JavaScript file with the actual contract address obtained after deployment.
- Install the required dependencies: `npm install starknet` for StarkNet.js.
- Ensure you have the StarkNet CLI and Python environment properly set up for deployment.
- The deployment process assumes you are connected to the StarkNet Testnet. Adjust the network configuration for Mainnet if required.
