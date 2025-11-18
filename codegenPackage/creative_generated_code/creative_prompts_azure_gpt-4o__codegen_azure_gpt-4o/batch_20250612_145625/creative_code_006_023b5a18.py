"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.web.app
Prompt: Provide a Solidity implementation for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as described in the tokenomics.
Generated: DETERMINISTIC_023b5a180e3c9726
Batch ID: 20250612_145625
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

/**
 * @title FROP Token Contract
 * @dev Implementation of a fixed-total-supply ERC20 token with allocations for presale, staking, marketing, rewards, and liquidity.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FROPToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages (must sum to 100%)
    uint256 private constant PRESALE_PERCENTAGE = 30;  // 30% of total supply
    uint256 private constant STAKING_PERCENTAGE = 25;  // 25% of total supply
    uint256 private constant MARKETING_PERCENTAGE = 20; // 20% of total supply
    uint256 private constant REWARDS_PERCENTAGE = 15;   // 15% of total supply
    uint256 private constant LIQUIDITY_PERCENTAGE = 10; // 10% of total supply

    // Addresses for allocations
    address public presaleWallet;
    address public stakingWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public liquidityWallet;

    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) ERC20("FROP Token", "FROP") {
        require(_presaleWallet != address(0), "Presale wallet address cannot be zero");
        require(_stakingWallet != address(0), "Staking wallet address cannot be zero");
        require(_marketingWallet != address(0), "Marketing wallet address cannot be zero");
        require(_rewardsWallet != address(0), "Rewards wallet address cannot be zero");
        require(_liquidityWallet != address(0), "Liquidity wallet address cannot be zero");

        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint allocations to respective wallets
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100);
        _mint(stakingWallet, (TOTAL_SUPPLY * STAKING_PERCENTAGE) / 100);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100);
        _mint(rewardsWallet, (TOTAL_SUPPLY * REWARDS_PERCENTAGE) / 100);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_PERCENTAGE) / 100);
    }

    /**
     * @dev Overrides the decimals function to set the decimal places to 18.
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }

    /**
     * @dev Allows the owner to update wallet addresses for allocations.
     */
    function updateWalletAddresses(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) external onlyOwner {
        require(_presaleWallet != address(0), "Presale wallet address cannot be zero");
        require(_stakingWallet != address(0), "Staking wallet address cannot be zero");
        require(_marketingWallet != address(0), "Marketing wallet address cannot be zero");
        require(_rewardsWallet != address(0), "Rewards wallet address cannot be zero");
        require(_liquidityWallet != address(0), "Liquidity wallet address cannot be zero");

        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;
    }
}
```
