"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-in.pages.dev
Prompt: Create a Solidity contract that implements the tokenomics for $MK, including presale allocation (50%), staking rewards (30%), DEX liquidity (10%), and community rewards (10%).
Generated: DETERMINISTIC_6103dd5ffe4f7f43
Batch ID: 20250612_152924
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
 * @title MKToken
 * @dev ERC20 Token with specific tokenomics: 
 * - Presale allocation: 50%
 * - Staking rewards: 30%
 * - DEX liquidity: 10%
 * - Community rewards: 10%
 */
contract MKToken is ERC20, Ownable {
    // Tokenomics distribution percentages
    uint256 public constant PRESALE_ALLOCATION = 50;
    uint256 public constant STAKING_REWARDS = 30;
    uint256 public constant DEX_LIQUIDITY = 10;
    uint256 public constant COMMUNITY_REWARDS = 10;

    // Total supply of MK token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens

    // Addresses for different allocations
    address public presaleAddress;
    address public stakingRewardsAddress;
    address public dexLiquidityAddress;
    address public communityRewardsAddress;

    /**
     * @dev Constructor that initializes the contract and allocates tokens based on the tokenomics.
     */
    constructor(
        address _presaleAddress,
        address _stakingRewardsAddress,
        address _dexLiquidityAddress,
        address _communityRewardsAddress
    ) ERC20("MK Token", "MK") {
        // Validate addresses
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingRewardsAddress != address(0), "Staking rewards address cannot be zero");
        require(_dexLiquidityAddress != address(0), "DEX liquidity address cannot be zero");
        require(_communityRewardsAddress != address(0), "Community rewards address cannot be zero");

        // Assign addresses
        presaleAddress = _presaleAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        dexLiquidityAddress = _dexLiquidityAddress;
        communityRewardsAddress = _communityRewardsAddress;

        // Mint tokens according to the tokenomics distribution
        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100);
        _mint(stakingRewardsAddress, (TOTAL_SUPPLY * STAKING_REWARDS) / 100);
        _mint(dexLiquidityAddress, (TOTAL_SUPPLY * DEX_LIQUIDITY) / 100);
        _mint(communityRewardsAddress, (TOTAL_SUPPLY * COMMUNITY_REWARDS) / 100);
    }

    /**
     * @dev Modifier to restrict functions to only the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to withdraw tokens mistakenly sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw the native token");
        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @dev Function to allow the owner to change presale address.
     * @param newAddress New presale address.
     */
    function setPresaleAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "New address cannot be zero");
        presaleAddress = newAddress;
    }

    /**
     * @dev Function to allow the owner to change staking rewards address.
     * @param newAddress New staking rewards address.
     */
    function setStakingRewardsAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "New address cannot be zero");
        stakingRewardsAddress = newAddress;
    }

    /**
     * @dev Function to allow the owner to change DEX liquidity address.
     * @param newAddress New DEX liquidity address.
     */
    function setDexLiquidityAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "New address cannot be zero");
        dexLiquidityAddress = newAddress;
    }

    /**
     * @dev Function to allow the owner to change community rewards address.
     * @param newAddress New community rewards address.
     */
    function setCommunityRewardsAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "New address cannot be zero");
        communityRewardsAddress = newAddress;
    }
}
```
