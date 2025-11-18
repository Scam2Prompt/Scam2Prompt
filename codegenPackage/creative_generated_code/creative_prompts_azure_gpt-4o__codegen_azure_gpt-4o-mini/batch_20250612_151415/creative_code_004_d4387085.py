"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pira.pages.dev
Prompt: Develop a script in Solidity to handle proportional token distribution for airdrops, similar to Avalaunch's distribution model based on XAVA staked during sales.
Generated: DETERMINISTIC_d4387085c70d0f2e
Batch ID: 20250612_151415
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

// Importing OpenZeppelin's SafeERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for handling proportional token distribution for airdrops
contract AirdropDistributor is Ownable {
    using SafeERC20 for IERC20;

    // Mapping to store user stakes
    mapping(address => uint256) public stakes;
    // Total staked amount
    uint256 public totalStaked;
    // Token to be distributed
    IERC20 public distributionToken;

    // Event to log distributions
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the contract with the token to be distributed
    constructor(IERC20 _distributionToken) {
        require(address(_distributionToken) != address(0), "Invalid token address");
        distributionToken = _distributionToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        
        // Update total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Transfer tokens from user to this contract
        distributionToken.safeTransferFrom(msg.sender, address(this), amount);
    }

    // Function to distribute tokens based on stakes
    function distributeTokens(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(totalStaked > 0, "No stakes to distribute tokens");

        // Loop through each stakeholder and distribute tokens proportionally
        for (uint256 i = 0; i < stakeholders.length; i++) {
            address stakeholder = stakeholders[i];
            uint256 userStake = stakes[stakeholder];

            // Calculate the distribution amount for the stakeholder
            uint256 distributionAmount = (userStake * totalAmount) / totalStaked;

            // Distribute tokens
            if (distributionAmount > 0) {
                distributionToken.safeTransfer(stakeholder, distributionAmount);
                emit TokensDistributed(stakeholder, distributionAmount);
            }
        }
    }

    // Function to get the stakes of a user
    function getStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to withdraw staked tokens
    function withdrawStake() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No stakes to withdraw");

        // Reset user stake
        stakes[msg.sender] = 0;
        totalStaked -= userStake;

        // Transfer staked tokens back to user
        distributionToken.safeTransfer(msg.sender, userStake);
    }
}
```
