"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring fixed supply allocation: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_19ca8108ad663341
Batch ID: 20250612_152109
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

// Importing OpenZeppelin's ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token
 * @dev This contract implements the DOGE20 token with fixed supply and specific allocation for various purposes.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 25) / 100;
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 25) / 100;
    uint256 public constant TREASURY_ALLOCATION = (TOTAL_SUPPLY * 25) / 100;
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 15) / 100;
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100;

    // Addresses for allocations
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    /**
     * @dev Constructor that initializes the token supply and allocates tokens accordingly.
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20", "DOGE20") {
        // Validate wallet addresses
        require(_presaleWallet != address(0), "Invalid presale wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");
        require(_treasuryWallet != address(0), "Invalid treasury wallet address");
        require(_stakingRewardsWallet != address(0), "Invalid staking rewards wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint token allocations
        _mint(presaleWallet, PRESALE_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(treasuryWallet, TREASURY_ALLOCATION);
        _mint(stakingRewardsWallet, STAKING_REWARDS_ALLOCATION);
        _mint(liquidityWallet, LIQUIDITY_ALLOCATION);
    }

    /**
     * @dev Override the _transfer function to include checks if necessary.
     * In this case, it is left unchanged, but can be customized as needed.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Function to withdraw ERC20 tokens sent to the contract by mistake.
     * Only the owner can call this function.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        // Validate the token and amount
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(owner(), amount);
    }
}
```
