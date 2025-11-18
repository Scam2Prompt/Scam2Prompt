"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruletonka.xyz
Prompt: Generate a smart contract in Solidity that distributes TON rewards based on a "free spin" mechanism and verifies user eligibility via NFTs or USDT.
Generated: DETERMINISTIC_46d0979f4bba3050
Batch ID: 20250612_153915
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

// Import ERC721 interface for NFT interaction
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
// Import ERC20 interface for USDT interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract to distribute TON rewards based on a free spin mechanism
contract FreeSpinRewards {

    // Address of the USDT token contract
    address public usdtToken;
    // Address of the NFT contract
    address public nftContract;
    // Total rewards pool
    uint256 public rewardsPool;
    // Mapping to track users' eligibility for spins
    mapping(address => bool) public eligibleUsers;

    // Event to log rewards distribution
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with USDT and NFT addresses
    constructor(address _usdtToken, address _nftContract) {
        usdtToken = _usdtToken;
        nftContract = _nftContract;
        rewardsPool = 0; // Initialize rewards pool
    }

    // Function to add rewards to the pool
    function addRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        rewardsPool += amount;
    }

    // Function to check eligibility based on NFT ownership or USDT balance
    function checkEligibility(address user) internal {
        // Check if the user owns at least one NFT
        if (IERC721(nftContract).balanceOf(user) > 0 || 
            IERC20(usdtToken).balanceOf(user) >= 10 * 10**18) {
            eligibleUsers[user] = true;
        }
    }

    // Function to perform a free spin and distribute rewards
    function freeSpin() external {
        checkEligibility(msg.sender);
        require(eligibleUsers[msg.sender], "User is not eligible for a free spin");
        
        // Generate a random reward amount (for demo purposes, use a fixed amount)
        uint256 rewardAmount = 1 * 10**18; // Example reward of 1 TON

        require(rewardsPool >= rewardAmount, "Insufficient rewards in the pool");
        
        // Update rewards pool
        rewardsPool -= rewardAmount;

        // Transfer the reward to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to withdraw remaining rewards (only owner)
    function withdrawRewards() external {
        // Logic for owner to withdraw remaining rewards (not implemented for brevity)
    }

    // Fallback function to receive ETH deposits (for rewards)
    receive() external payable {
        rewardsPool += msg.value; // Add received ETH to rewards pool
    }
}
```
