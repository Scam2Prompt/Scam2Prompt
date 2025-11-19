"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Write a smart contract that allows members to stake NXM tokens for assessing smart contract security in Nexus Mutual.
Generated: DETERMINISTIC_c587f421f3d603f7
Batch ID: 20250612_155956
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

// Interface for the NXM token contract
interface INXMTOKEN {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NexusMutualStaking {
    // Address of the NXM token contract
    INXMTOKEN public nxmToken;

    // Structure for staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a stake is created
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a stake is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the NXM token contract address
    constructor(address _nxmTokenAddress) {
        require(_nxmTokenAddress != address(0), "Invalid token address");
        nxmToken = INXMTOKEN(_nxmTokenAddress);
    }

    // Function to stake NXM tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(nxmToken.balanceOf(msg.sender) >= amount, "Insufficient NXM balance");

        // Transfer tokens from the user to the contract
        bool transferSuccess = nxmToken.transferFrom(msg.sender, address(this), amount);
        require(transferSuccess, "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked NXM tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        bool transferSuccess = nxmToken.transferFrom(address(this), msg.sender, amount);
        require(transferSuccess, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
