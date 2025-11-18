"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cagacrypto-en.web.app
Prompt: Create a Solidity contract for a bounty rewards system that incentivizes safeguarding a DAO, inspired by CAGA Crypto's community protection initiative.
Generated: DETERMINISTIC_ebe5f6fc6b7d50b3
Batch ID: 20250612_151539
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// BountyRewards is a smart contract for managing bounty rewards for a DAO
contract BountyRewards is Ownable {
    // State variables
    IERC20 public rewardToken; // The ERC20 token used for rewards
    uint256 public bountyAmount; // Amount of reward for each bounty
    mapping(address => uint256) public bountiesClaimed; // Tracks claimed bounties per address

    // Events
    event BountyCreated(address indexed creator, uint256 bountyAmount);
    event BountyClaimed(address indexed claimer, uint256 amount);

    // Constructor to set the reward token and bounty amount
    constructor(IERC20 _rewardToken, uint256 _bountyAmount) {
        rewardToken = _rewardToken;
        bountyAmount = _bountyAmount;
    }

    // Modifier to check if a bounty is claimable
    modifier isBountyClaimable() {
        require(bountiesClaimed[msg.sender] < 1, "Bounty already claimed by this address");
        _;
    }

    // Function to create a new bounty
    function createBounty() external onlyOwner {
        require(bountyAmount > 0, "Bounty amount must be greater than zero");
        emit BountyCreated(msg.sender, bountyAmount);
    }

    // Function for users to claim a bounty
    function claimBounty() external isBountyClaimable {
        // Transfer the reward token to the claimer
        require(rewardToken.balanceOf(address(this)) >= bountyAmount, "Insufficient tokens in contract");
        
        // Update the number of bounties claimed by the claimer
        bountiesClaimed[msg.sender]++;
        
        // Transfer the bounty to the claimer
        bool success = rewardToken.transfer(msg.sender, bountyAmount);
        require(success, "Token transfer failed");

        emit BountyClaimed(msg.sender, bountyAmount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to update the bounty amount (only owner)
    function updateBountyAmount(uint256 newBountyAmount) external onlyOwner {
        require(newBountyAmount > 0, "Bounty amount must be greater than zero");
        bountyAmount = newBountyAmount;
    }
}
```

Make sure to install OpenZeppelin contracts via npm if you're deploying this contract:

```bash
npm install @openzeppelin/contracts
```

This contract provides a basic structure for a bounty rewards system, allowing the owner to create bounties, and users to claim them while also ensuring proper token handling and security.
