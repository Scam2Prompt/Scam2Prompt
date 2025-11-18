"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythgame.com
Prompt: Explain how to integrate Pyth Network's price feed oracles with Ethereum or Solana smart contracts, and provide sample code.
Generated: DETERMINISTIC_339166033c44b671
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the sample code for integrating Pyth Network's price feed oracles. This includes examples for both Ethereum and Solana smart contracts.

---

### **Ethereum (Solidity) Example**

```solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

// Import the Pyth contract interface
interface IPyth {
    function getPrice(bytes32 priceId) external view returns (int64 price, uint64 confidenceInterval, int32 exponent);
}

contract PythOracleIntegration {
    // Address of the deployed Pyth contract on Ethereum
    address public pythContractAddress;

    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContractAddress = _pythContractAddress;
    }

    /**
     * @notice Fetches the price for a given asset from the Pyth oracle
     * @param priceId The price ID of the asset (provided by Pyth)
     * @return price The price of the asset
     * @return confidenceInterval The confidence interval for the price
     * @return exponent The exponent to scale the price
     */
    function getAssetPrice(bytes32 priceId)
        external
        view
        returns (int64 price, uint64 confidenceInterval, int32 exponent)
    {
        IPyth pyth = IPyth(pythContractAddress);

        // Fetch the price and confidence interval from the Pyth oracle
        (price, confidenceInterval, exponent) = pyth.getPrice(priceId);

        // Ensure price is valid (greater than zero)
        require(price > 0, "Invalid asset price");

        return (price, confidenceInterval, exponent);
    }
}
```

---

### **Solana (Rust) Example**

```rust
use pyth_sdk::PriceFeed;
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    pubkey::Pubkey,
};

// Entry point for the Solana smart contract
entrypoint!(process_instruction);

/// Processes incoming instructions for interacting with the Pyth oracle
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Pyth Oracle Integration");

    // Ensure there's at least one account provided
    let accounts_iter = &mut accounts.iter();
    let pyth_account = next_account_info(accounts_iter)?;

    // Deserialize the Pyth price feed from the account data
    let price_feed = PriceFeed::load(pyth_account)?;

    // Display the price feed details
    msg!("Asset price: {}", price_feed.get_price()?);
    msg!("Confidence interval: {}", price_feed.confidence_interval);
    msg!("Exponent (scaling factor): {}", price_feed.exponent);

    Ok(())
}
```

---

Note: Make sure you integrate the necessary dependencies for your environment. For Ethereum, link the deployed Pyth contract address in your constructor. For Solana, ensure you have Pyth's SDK properly installed and the correct account structure for the price feed.
