"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secured-greenbitcoin.pages.dev
Prompt: Write a Solidity contract to implement the tokenomics outlined for $GBTC, including allocations for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_889c52c2c6c00eb0
Batch ID: 20250612_153401
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

// Import the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GBTC Token
 * @dev Implementation of the GBTC token with specific tokenomics
 */
contract GBTC is ERC20, Ownable {
    // Allocation percentages (represented in basis points, 1% = 100 basis points)
    uint256 public constant PRESALE_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 3000; // 30%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 2000; // 20%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 1500; // 15%

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10 ** decimals(); // 100 million tokens

    // Track allocations
    mapping(address => uint256) public presaleWallets;
    address public stakingRewardsWallet;
    address public marketingWallet;
    address public liquidityWallet;
    address public communityRewardsWallet;

    /**
     * @dev Constructor that initializes the token with the total supply and allocates it according to the tokenomics
     */
    constructor(
        address _stakingRewardsWallet,
        address _marketingWallet,
        address _liquidityWallet,
        address _communityRewardsWallet
    ) ERC20("GBTC Token", "GBTC") {
        // Set the wallet addresses for allocations
        stakingRewardsWallet = _stakingRewardsWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        communityRewardsWallet = _communityRewardsWallet;

        // Mint the total supply to the contract owner
        _mint(owner(), TOTAL_SUPPLY);

        // Allocate tokens to the respective wallets
        _allocateTokens();
    }

    /**
     * @dev Allocates tokens to the specified wallets according to the defined tokenomics
     */
    function _allocateTokens() internal {
        // Presale allocation
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10_000;
        presaleWallets[msg.sender] = presaleAmount;

        // Staking rewards allocation
        uint256 stakingRewardsAmount = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 10_000;
        _transfer(owner(), stakingRewardsWallet, stakingRewardsAmount);

        // Marketing allocation
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10_000;
        _transfer(owner(), marketingWallet, marketingAmount);

        // Liquidity allocation
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10_000;
        _transfer(owner(), liquidityWallet, liquidityAmount);

        // Community rewards allocation
        uint256 communityRewardsAmount = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 10_000;
        _transfer(owner(), communityRewardsWallet, communityRewardsAmount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract
     * @param _token The address of the token to withdraw
     * @param _amount The amount of tokens to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(this), "Cannot withdraw GBTC tokens");
        require(IERC20(_token).balanceOf(address(this)) >= _amount, "Insufficient balance");

        IERC20(_token).transfer(owner(), _amount);
    }

    /**
     * @dev Set presale wallet allocation
     * @param _wallet Address of the presale wallet
     * @param _amount Amount to allocate
     */
    function setPresaleWallet(address _wallet, uint256 _amount) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        presaleWallets[_wallet] = _amount;
    }
}
```
