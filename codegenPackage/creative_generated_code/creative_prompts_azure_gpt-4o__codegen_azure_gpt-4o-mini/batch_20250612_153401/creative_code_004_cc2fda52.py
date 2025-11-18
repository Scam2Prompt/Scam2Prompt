"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-in.web.app
Prompt: Write a Solidity function for the DOGE20 staking smart contract that prevents inflation by enforcing a fixed token supply and distributes rewards to stakers.
Generated: DETERMINISTIC_cc2fda5279f9f90f
Batch ID: 20250612_153401
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

contract DOGE20Staking {
    // State variables
    string public constant name = "DOGE20";
    string public constant symbol = "DOGE20";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1000000 * (10 ** uint256(decimals)); // Fixed total supply of tokens

    mapping(address => uint256) public balances; // Mapping of user balances
    mapping(address => uint256) public stakingBalances; // Mapping of user staking balances
    mapping(address => uint256) public lastUpdated; // Last updated timestamp for each user
    uint256 public rewardRate; // Reward rate for stakers
    uint256 public totalStaked; // Total staked amount
    
    constructor(uint256 _rewardRate) {
        balances[msg.sender] = totalSupply; // Assign total supply to the contract deployer
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Event declarations
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);

    // Modifier to check if the user has staked tokens
    modifier hasStakedTokens() {
        require(stakingBalances[msg.sender] > 0, "No staked tokens");
        _;
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user's balance and total staked amount
        balances[msg.sender] -= amount;
        stakingBalances[msg.sender] += amount;
        totalStaked += amount;
        lastUpdated[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external hasStakedTokens {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate and distribute rewards before unstaking
        distributeRewards();

        // Update user's balance and total staked amount
        stakingBalances[msg.sender] -= amount;
        totalStaked -= amount;
        balances[msg.sender] += amount;

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to distribute rewards
    function distributeRewards() public hasStakedTokens {
        uint256 timeStaked = block.timestamp - lastUpdated[msg.sender];
        uint256 reward = (stakingBalances[msg.sender] * rewardRate * timeStaked) / 1 days;

        // Update last updated timestamp
        lastUpdated[msg.sender] = block.timestamp;

        // Ensure we do not exceed the total supply
        require(balances[address(this)] >= reward, "Insufficient contract balance for rewards");

        // Transfer reward to the user
        balances[address(this)] -= reward;
        balances[msg.sender] += reward;

        emit RewardsDistributed(msg.sender, reward);
    }

    // Function to view the staked balance of a user
    function viewStakedBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    // Function to view the reward balance of a user
    function viewRewardBalance(address user) external view returns (uint256) {
        uint256 timeStaked = block.timestamp - lastUpdated[user];
        uint256 reward = (stakingBalances[user] * rewardRate * timeStaked) / 1 days;
        return reward;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
