"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hieroglyphics.com
Prompt: Create a smart contract in Solidity for a DAO token like $BAR, ensuring it includes features for farming and governance.
Generated: DETERMINISTIC_c013fc4dbb53c973
Batch ID: 20250612_145121
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

// Import OpenZeppelin Contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for the DAO token
contract BarToken is ERC20, Ownable {
    // Mapping from user address to staked amount
    mapping(address => uint256) public stakedAmount;
    // Total staked amount
    uint256 public totalStaked;
    // Reward rate (in tokens per block)
    uint256 public rewardRate;
    // Last update block for rewards
    mapping(address => uint256) public lastUpdateBlock;
    // Mapping to store rewards per user
    mapping(address => uint256) public rewards;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply, uint256 _rewardRate) ERC20("BarToken", "BAR") {
        _mint(msg.sender, initialSupply * 10 ** decimals());
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action
    modifier updateRewards(address user) {
        // Calculate and update rewards for the user
        rewards[user] += earned(user);
        lastUpdateBlock[user] = block.number;
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");
        _transfer(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external updateRewards(msg.sender) {
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0; // Reset rewards
        _mint(msg.sender, reward); // Mint rewards to the user

        emit RewardClaimed(msg.sender, reward);
    }

    // Calculate the amount of reward earned by the user
    function earned(address user) public view returns (uint256) {
        uint256 stakedDuration = block.number - lastUpdateBlock[user];
        return stakedAmount[user] * rewardRate * stakedDuration;
    }

    // Function to withdraw tokens by the owner (for emergency or treasury purposes)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), msg.sender, amount);
    }
}
```
