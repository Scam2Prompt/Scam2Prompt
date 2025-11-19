"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-minetrix.web.app
Prompt: Write a smart contract in Solidity that implements the tokenomics described for BTCMTX, including allocation percentages for mining, marketing, community rewards, and staking rewards.
Generated: DETERMINISTIC_eaf34060f8ef8733
Batch ID: 20250612_152620
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCMTX Token
 * @dev This contract implements the BTCMTX token with specific tokenomics.
 */
contract BTCMTX is ERC20, Ownable {
    // Allocation percentages
    uint256 public constant MINING_ALLOCATION = 40; // 40% for mining
    uint256 public constant MARKETING_ALLOCATION = 20; // 20% for marketing
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 20; // 20% for community rewards
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20; // 20% for staking rewards

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Addresses for different allocations
    address public miningAddress;
    address public marketingAddress;
    address public communityRewardsAddress;
    address public stakingRewardsAddress;

    /**
     * @dev Constructor that initializes the token and allocates the initial supply.
     * @param _miningAddress Address for mining allocation
     * @param _marketingAddress Address for marketing allocation
     * @param _communityRewardsAddress Address for community rewards allocation
     * @param _stakingRewardsAddress Address for staking rewards allocation
     */
    constructor(
        address _miningAddress,
        address _marketingAddress,
        address _communityRewardsAddress,
        address _stakingRewardsAddress
    ) ERC20("BTCMTX", "BTCMTX") {
        require(_miningAddress != address(0), "Invalid mining address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");

        miningAddress = _miningAddress;
        marketingAddress = _marketingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        stakingRewardsAddress = _stakingRewardsAddress;

        // Minting the total supply and distributing according to the allocations
        _mint(miningAddress, (TOTAL_SUPPLY * MINING_ALLOCATION) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
        _mint(communityRewardsAddress, (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100);
        _mint(stakingRewardsAddress, (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100);
    }

    /**
     * @dev Function to transfer tokens. Overrides the default transfer function to include custom logic if needed.
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to transfer
     * @return success A boolean indicating the success of the transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to approve tokens for delegated transfer. Overrides the default approve function.
     * @param spender The address to approve for spending
     * @param amount The amount of tokens to approve
     * @return success A boolean indicating the success of the approval
     */
    function approve(address spender, uint256 amount) public override returns (bool success) {
        require(spender != address(0), "Approve to the zero address");
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another. Overrides the default transferFrom function.
     * @param sender The address to transfer tokens from
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return success A boolean indicating the success of the transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
