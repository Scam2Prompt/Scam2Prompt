"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.web.app
Prompt: Create a Solidity contract for DOGE20 tokenomics that allocates 25% of the supply to presale, 25% to marketing, 25% to treasury, 15% to staking rewards, and 10% to liquidity.
Generated: DETERMINISTIC_d9a5aedf77717ae8
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token Contract
 * @notice This contract implements the DOGE20 tokenomics with specified allocations.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the DOGE20 token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18;

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 25; // 25%
    uint256 public constant MARKETING_ALLOCATION = 25; // 25%
    uint256 public constant TREASURY_ALLOCATION = 25; // 25%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 15; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10%

    // Mappings to track allocations
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    /**
     * @dev Constructor that mints the total supply and allocates it appropriately.
     * @param _presaleWallet Address to receive the presale allocation.
     * @param _marketingWallet Address to receive the marketing allocation.
     * @param _treasuryWallet Address to receive the treasury allocation.
     * @param _stakingRewardsWallet Address to receive the staking rewards allocation.
     * @param _liquidityWallet Address to receive the liquidity allocation.
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20", "DOGE20") {
        require(
            _presaleWallet != address(0) && 
            _marketingWallet != address(0) && 
            _treasuryWallet != address(0) && 
            _stakingRewardsWallet != address(0) && 
            _liquidityWallet != address(0),
            "Wallet addresses cannot be zero address"
        );

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint the total supply and distribute allocations
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
        _mint(treasuryWallet, (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100);
        _mint(stakingRewardsWallet, (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100);
    }

    /**
     * @dev Allows the owner to recover any ERC20 tokens sent to this contract by mistake.
     * @param tokenAddress The address of the token contract.
     * @param recipient The address to send the recovered tokens to.
     * @param amount The amount of tokens to recover.
     */
    function recoverTokens(address tokenAddress, address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(recipient, amount);
    }
}
```

This Solidity contract implements the DOGE20 tokenomics as specified, including the necessary comments and error handling.
