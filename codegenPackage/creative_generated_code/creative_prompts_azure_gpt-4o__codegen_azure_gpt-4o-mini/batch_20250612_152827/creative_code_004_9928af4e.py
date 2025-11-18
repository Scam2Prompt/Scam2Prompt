"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Provide an example of tokenomics implementation in an ERC-20 smart contract, including fixed supply allocation for presale, marketing, staking rewards, and liquidity pools, as outlined for DOGE20.
Generated: DETERMINISTIC_9928af4eb3a60144
Batch ID: 20250612_152827
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
 * @title DOGE20 Token
 * @dev Implementation of the ERC20 token with fixed supply allocation.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Allocation percentages (in basis points)
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10**18; // 20%
    uint256 public constant MARKETING_ALLOCATION = 100_000_000 * 10**18; // 10%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 150_000_000 * 10**18; // 15%
    uint256 public constant LIQUIDITY_POOL_ALLOCATION = 150_000_000 * 10**18; // 15%
    uint256 public constant TEAM_ALLOCATION = 200_000_000 * 10**18; // 20%
    uint256 public constant RESERVE_ALLOCATION = 200_000_000 * 10**18; // 20%

    // Addresses for allocation
    address public presaleAddress;
    address public marketingAddress;
    address public stakingRewardsAddress;
    address public liquidityPoolAddress;
    address public teamAddress;
    address public reserveAddress;

    /**
     * @dev Constructor that initializes the token and allocates tokens
     * to different addresses based on the predefined allocations.
     */
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _stakingRewardsAddress,
        address _liquidityPoolAddress,
        address _teamAddress,
        address _reserveAddress
    ) ERC20("DOGE20", "DOGE20") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");
        require(_stakingRewardsAddress != address(0), "Staking rewards address cannot be zero");
        require(_liquidityPoolAddress != address(0), "Liquidity pool address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");
        require(_reserveAddress != address(0), "Reserve address cannot be zero");

        // Assigning addresses
        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityPoolAddress = _liquidityPoolAddress;
        teamAddress = _teamAddress;
        reserveAddress = _reserveAddress;

        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens to respective addresses
        _transfer(msg.sender, presaleAddress, PRESALE_ALLOCATION);
        _transfer(msg.sender, marketingAddress, MARKETING_ALLOCATION);
        _transfer(msg.sender, stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);
        _transfer(msg.sender, liquidityPoolAddress, LIQUIDITY_POOL_ALLOCATION);
        _transfer(msg.sender, teamAddress, TEAM_ALLOCATION);
        _transfer(msg.sender, reserveAddress, RESERVE_ALLOCATION);
    }

    /**
     * @dev Overrides the _transfer function to prevent transfers 
     * until the presale is completed (if applicable). 
     * Uncomment the next lines if needed.
     */
    // function _transfer(address sender, address recipient, uint256 amount) internal override {
    //     require(!isPresaleActive, "Transfers are restricted during presale");
    //     super._transfer(sender, recipient, amount);
    // }

    /**
     * @dev Allows the owner to withdraw any accidentally sent tokens.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw native tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
