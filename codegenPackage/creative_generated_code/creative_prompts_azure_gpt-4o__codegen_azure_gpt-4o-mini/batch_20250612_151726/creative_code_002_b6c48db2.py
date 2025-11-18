"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-etuktuk.pages.dev
Prompt: Create a function in Solidity to enable staking of $TUK tokens and calculate rewards based on the duration of staking, as described in the eTukTuk ecosystem.
Generated: DETERMINISTIC_b6c48db208cd3929
Batch ID: 20250612_151726
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

// Import ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $TUK token
contract TUKStaking is Ownable {
    // State variables
    IERC20 public tukToken; // The $TUK token contract
    uint256 public rewardRate; // Reward rate per second
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        bool isActive; // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    // Constructor to set the $TUK token address and reward rate
    constructor(address _tukToken, uint256 _rewardRate) {
        require(_tukToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");
        tukToken = IERC20(_tukToken);
        rewardRate = _rewardRate;
    }

    // Function to stake $TUK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(tukToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(tukToken.allowance(msg.sender, address(this)) >= amount, "Token allowance is required");

        // Transfer $TUK tokens from user to the contract
        tukToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        Stake memory stakeData = Stake({
            amount: amount,
            startTime: block.timestamp,
            isActive: true
        });

        stakes[msg.sender] = stakeData;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards
    function calculateReward(address user) public view returns (uint256) {
        Stake storage stakeData = stakes[user];

        // Check if the stake is active
        require(stakeData.isActive, "No active stake found");

        // Calculate the duration of staking
        uint256 duration = block.timestamp - stakeData.startTime;
        
        // Calculate reward based on duration and reward rate
        return (stakeData.amount * rewardRate * duration) / 1e18; // Assuming rewardRate is scaled with 1e18
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage stakeData = stakes[msg.sender];

        // Check if the stake is active
        require(stakeData.isActive, "No active stake found");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's stake
        stakeData.isActive = false;

        // Transfer staked amount back to the user
        tukToken.transfer(msg.sender, stakeData.amount);

        // Transfer calculated rewards to the user
        // Assuming the contract has enough balance to cover the rewards
        require(address(this).balance >= reward, "Insufficient contract balance for rewards");
        payable(msg.sender).transfer(reward);

        emit Unstaked(msg.sender, stakeData.amount, reward);
    }

    // Function to withdraw contract's ETH balance (if rewards are paid in ETH)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
