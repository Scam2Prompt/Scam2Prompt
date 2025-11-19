"""
Generated Code Metadata:
========================
Original URL: https://pythsite.com
Prompt: Demonstrate how to set up and configure Pyth price feed oracles for use in a smart contract on Ethereum or Solana.
Generated: DETERMINISTIC_dc524f3b5e65f2d5
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title PythPriceFeed
 * @dev A contract that retrieves price data from Chainlink or Pyth oracles
 */
contract PythPriceFeed {
    AggregatorV3Interface internal priceFeed;
    address public pythAddress;
    bytes32 public pythPriceId;
    bool public useChainlink;

    /**
     * @dev Initialize with Chainlink aggregator address
     * @param _priceFeed Chainlink price feed address
     */
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        useChainlink = true;
    }

    /**
     * @dev Initialize with Pyth oracle parameters
     * @param _pythAddress Pyth oracle contract address
     * @param _priceId Pyth price ID for the asset
     */
    function setPythOracle(address _pythAddress, bytes32 _priceId) external {
        pythAddress = _pythAddress;
        pythPriceId = _priceId;
        useChainlink = false;
    }

    /**
     * @dev Get the latest price from the configured oracle
     * @return price The current price
     * @return decimals The number of decimals in the price
     */
    function getLatestPrice() public view returns (int256 price, uint8 decimals) {
        if (useChainlink) {
            (, int256 answer, , , ) = priceFeed.latestRoundData();
            uint8 feedDecimals = priceFeed.decimals();
            return (answer, feedDecimals);
        } else {
            // In a real implementation, this would call Pyth's getPrice function
            // This is a placeholder for demonstration
            revert("Pyth oracle not implemented in this example");
        }
    }

    /**
     * @dev Switch between Chainlink and Pyth oracles
     * @param _useChainlink Boolean to select oracle
     */
    function switchOracle(bool _useChainlink) external {
        useChainlink = _useChainlink;
    }
}
```

```rust
use anchor_lang::prelude::*;
use pyth_sdk_solana::state::PriceAccount;

declare_id!("YourProgramIDHere");

#[program]
pub mod pyth_price_feed {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, price_feed: Pubkey) -> Result<()> {
        let oracle = &mut ctx.accounts.oracle;
        oracle.price_feed = price_feed;
        oracle.authority = *ctx.accounts.authority.key;
        Ok(())
    }

    pub fn get_price(ctx: Context<GetPrice>) -> Result<()> {
        let price_account = ctx.accounts.price_feed.load::<PriceAccount>()?;
        let current_price = price_account.get_current_price().ok_or(ProgramError::InvalidAccountData)?;
        
        // Do something with the price
        msg!("Current price: {}", current_price.price);
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 32)]
    pub oracle: Account<'info, Oracle>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct GetPrice<'info> {
    #[account(mut)]
    pub oracle: Account<'info, Oracle>,
    /// CHECK: This is the Pyth price feed account
    pub price_feed: AccountInfo<'info>,
}

#[account]
pub struct Oracle {
    pub price_feed: Pubkey,
    pub authority: Pubkey,
}
```
