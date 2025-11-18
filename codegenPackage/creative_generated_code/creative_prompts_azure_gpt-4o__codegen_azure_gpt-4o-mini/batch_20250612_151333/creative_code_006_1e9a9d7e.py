"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sakaivault-io.pages.dev
Prompt: Develop a smart contract function to allow users to stake SAKAI tokens and claim rewards, referencing the staking mechanism described in Sakai Vault.
Generated: DETERMINISTIC_1e9a9d7ea425616d
Batch ID: 20250612_151333
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

// Importing necessary OpenZeppelin contracts for ERC20 handling and safe math operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SakaiVault {
    using SafeMath for uint256;

    // Declaration of state variables
    IERC20 public sakaiToken; // ERC20 token contract reference
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakes; // User stakes mapping
    mapping(address => uint256) public rewards; // User rewards mapping
    uint256 public rewardRate; // Rate of reward distribution per token staked
    uint256 public lastUpdate; // Last time rewards were updated

    // Event declarations for logging purposes
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token and reward rate
    constructor(IERC20 _sakaiToken, uint256 _rewardRate) {
        sakaiToken = _sakaiToken;
        rewardRate = _rewardRate;
        lastUpdate = block.timestamp;
    }

    // Function to stake SAKAI tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(sakaiToken.balanceOf(msg.sender) >= _amount, "Insufficient SAKAI balance");
        require(sakaiToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance required");

        // Update the user's rewards before staking
        updateReward(msg.sender);

        // Transfer the SAKAI tokens from the user to the contract
        sakaiToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking information
        stakes[msg.sender] = stakes[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake SAKAI tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= _amount, "Insufficient staked amount");

        // Update the user's rewards before unstaking
        updateReward(msg.sender);

        // Update staking information
        stakes[msg.sender] = stakes[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer the SAKAI tokens back to the user
        sakaiToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimReward() external {
        // Update the user's rewards
        updateReward(msg.sender);
        
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        // Transfer the reward amount (in SAKAI) to the user
        sakaiToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards based on the current time and user's stake
    function updateReward(address _user) internal {
        if (totalStaked > 0) {
            // Calculate rewards for the user
            rewards[_user] = rewards[_user].add(
                stakes[_user].mul(rewardRate).mul(block.timestamp.sub(lastUpdate)).div(1e18)
            );
        }
        lastUpdate = block.timestamp; // Update the last update time
    }
}
```
