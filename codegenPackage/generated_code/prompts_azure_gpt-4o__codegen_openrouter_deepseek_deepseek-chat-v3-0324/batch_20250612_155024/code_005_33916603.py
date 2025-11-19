"""
Generated Code Metadata:
========================
Original URL: https://pythgame.com
Prompt: Explain how to integrate Pyth Network's price feed oracles with Ethereum or Solana smart contracts, and provide sample code.
Generated: DETERMINISTIC_339166033c44b671
Batch ID: 20250612_155024
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.devnet.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Pyth Network Integration Example for Ethereum and Solana Smart Contracts

# Ethereum Smart Contract Example (Solidity)
"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for Pyth Network Price Feed
interface IPyth {
    struct Price {
        // Price with 18 decimals
        int64 price;
        // Confidence interval around the price with 18 decimals
        uint64 conf;
        // Price exponent (usually -8 for most assets)
        int32 expo;
        // Timestamp when the price was published
        uint publishTime;
    }

    // Get the latest price for a given price feed ID
    function getPrice(bytes32 priceId) external view returns (Price memory price);
    
    // Get the latest price and confidence interval
    function getPriceNoOlderThan(
        bytes32 priceId,
        uint age
    ) external view returns (Price memory price);
    
    // Update the price feed (requires fee payment)
    function updatePriceFeeds(bytes[] calldata updateData) external payable;
}

contract PythConsumer {
    IPyth public pyth;
    bytes32 public priceFeedId;
    
    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }
    
    // Get the latest price from Pyth Network
    function getLatestPrice() public view returns (int64 price, uint64 conf, uint publishTime) {
        IPyth.Price memory pythPrice = pyth.getPrice(priceFeedId);
        return (pythPrice.price, pythPrice.conf, pythPrice.publishTime);
    }
    
    // Example function that uses the price feed
    function executeTrade(uint256 amount) external view returns (bool) {
        (int64 price, , ) = getLatestPrice();
        require(price > 0, "Invalid price");
        
        // Convert price to uint256 with proper decimals (example for 8 decimal assets)
        uint256 normalizedPrice = uint256(uint64(price)) * (10 ** 10); // Adjust for 18 decimals
        
        // Your trading logic here using the price
        // ...
        
        return true;
    }
    
    // Update price feed with new data (requires fee)
    function updatePrice(bytes[] calldata priceUpdateData) external payable {
        pyth.updatePriceFeeds{value: msg.value}(priceUpdateData);
    }
}
"""

# Solana Smart Contract Example (Rust)
"""
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

// Pyth program ID (mainnet)
const PYTH_PROGRAM_ID: Pubkey = solana_program::pubkey!("FsJ3A3u2vn5cTVofAjvy6y5kwABJAqYWpe4975bi2epH");

// Pyth price account structure (simplified)
#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq)]
pub struct PythPriceAccount {
    pub magic: u32,          // Magic number
    pub ver: u32,            // Version
    pub atype: u32,          // Account type
    pub size: u32,           // Size of account
    pub price_type: u32,     // Price or calculation type
    pub exponent: i32,       // Price exponent
    pub num_: u32,           // Number of component prices
    pub unused: u32,
    pub curr_slot: u64,      // Current slot
    pub valid_slot: u64,     // Valid slot
    pub twap: i64,           // Time-weighted average price
    pub twac: i64,           // Time-weighted average confidence
    pub agg_pubkey: Pubkey,  // Publisher's public key
    pub agg_price: i64,      // Aggregate price
    pub agg_conf: u64,       // Aggregate confidence
    pub agg_slot: u64,       // Aggregate slot
    // ... other fields omitted for brevity
}

entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // Accounts expected:
    // 0. Pyth price account
    let accounts_iter = &mut accounts.iter();
    let pyth_price_account = next_account_info(accounts_iter)?;
    
    // Verify this is a Pyth account
    if pyth_price_account.owner != &PYTH_PROGRAM_ID {
        msg!("Account is not owned by Pyth");
        return Err(ProgramError::IncorrectProgramId);
    }
    
    // Deserialize the Pyth price account
    let price_data = pyth_price_account.try_borrow_data()?;
    let price_account: &PythPriceAccount = bytemuck::try_from_bytes(&price_data)
        .map_err(|_| ProgramError::InvalidAccountData)?;
    
    // Get the current price
    let price = price_account.agg_price;
    let confidence = price_account.agg_conf;
    let exponent = price_account.exponent;
    
    msg!("Current price: {}", price);
    msg!("Confidence: {}", confidence);
    msg!("Exponent: {}", exponent);
    
    // Your logic using the price feed here
    // ...
    
    Ok(())
}
"""

# Python Example for Submitting Price Updates to Pyth
"""
from pythclient.pythaccounts import PythPriceAccount
from pythclient.utils import get_key
from solana.rpc.api import Client
import asyncio

async def get_pyth_price(solana_network: str, price_feed_id: str):
    # Initialize Solana client
    endpoint = "https://api.mainnet-beta.solana.com" if solana_network == "mainnet" else "https://api.devnet.solana.com"
    solana_client = Client(endpoint)
    
    # Get Pyth price account
    price_account_key = get_key(price_feed_id)
    price_account = PythPriceAccount(price_account_key, solana_client)
    
    try:
        await price_account.update()
        price = price_account.aggregate_price
        confidence = price_account.aggregate_price_confidence_interval
        exponent = price_account.exponent
        
        print(f"Price: {price} ± {confidence} (10^{exponent})")
        return price, confidence, exponent
    except Exception as e:
        print(f"Error fetching price: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # SOL/USD price feed on Solana mainnet
    SOL_USD_FEED = "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG"
    asyncio.run(get_pyth_price("mainnet", SOL_USD_FEED))
"""
```
