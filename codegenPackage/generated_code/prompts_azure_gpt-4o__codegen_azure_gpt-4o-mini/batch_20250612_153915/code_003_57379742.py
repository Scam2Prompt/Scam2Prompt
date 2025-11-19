"""
Generated Code Metadata:
========================
Original URL: https://tgdrop.cc
Prompt: Create a smart contract in Solidity for a TON-based reward system that distributes rewards based on NFT or USDT qualifications.
Generated: DETERMINISTIC_573797429fbaa59a
Batch ID: 20250612_153915
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

// Importing the ERC721 interface for NFT interactions
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
// Importing the ERC20 interface for USDT interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for the TON-based reward system
contract RewardSystem {
    // Address of the USDT token contract
    IERC20 public usdtToken;
    // Address of the NFT contract
    IERC721 public nftContract;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with USDT and NFT contract addresses
    constructor(address _usdtToken, address _nftContract) {
        usdtToken = IERC20(_usdtToken);
        nftContract = IERC721(_nftContract);
    }

    // Function to distribute rewards based on NFT ownership or USDT balance
    function distributeRewards() external {
        // Check if the user owns at least one NFT
        uint256 nftBalance = nftContract.balanceOf(msg.sender);
        require(nftBalance > 0, "You must own at least one NFT to receive rewards.");

        // Check if the user has a minimum USDT balance (e.g., 100 USDT)
        uint256 usdtBalance = usdtToken.balanceOf(msg.sender);
        require(usdtBalance >= 100 * 10**18, "You must hold at least 100 USDT to receive rewards.");

        // Calculate rewards based on NFT count and USDT balance
        uint256 rewardAmount = calculateReward(nftBalance, usdtBalance);

        // Update the user's rewards
        rewards[msg.sender] += rewardAmount;

        // Emit an event for the rewards distribution
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Internal function to calculate rewards based on NFT count and USDT balance
    function calculateReward(uint256 nftCount, uint256 usdtBalance) internal pure returns (uint256) {
        // Example reward calculation: 10 USDT per NFT and 1 USDT for every 10 USDT held
        uint256 nftReward = nftCount * 10 * 10**18; // 10 USDT per NFT
        uint256 usdtReward = usdtBalance / 10; // 1 USDT for every 10 USDT

        return nftReward + usdtReward;
    }

    // Function to withdraw accumulated rewards
    function withdrawRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to withdraw.");

        // Reset the user's rewards before transferring to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        require(usdtToken.transfer(msg.sender, rewardAmount), "Transfer failed.");
    }
}
```
