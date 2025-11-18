"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity function to implement staking for $GNS tokens, allowing users to earn real yield, as outlined in the Gains Network ecosystem.
Generated: DETERMINISTIC_9dbac38ac0e16f34
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

// Import the ERC20 interface to interact with the $GNS token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Contract for staking $GNS tokens
contract GNSStaking is ReentrancyGuard {
    // ERC20 token interface
    IERC20 public gnsToken;

    // Staking data structure
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Time when the user staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $GNS token address
    constructor(address _gnsTokenAddress) {
        require(_gnsTokenAddress != address(0), "Invalid token address");
        gnsToken = IERC20(_gnsTokenAddress);
    }

    // Function to stake $GNS tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(gnsToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $GNS tokens
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update total staked and user stake
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(gnsToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
