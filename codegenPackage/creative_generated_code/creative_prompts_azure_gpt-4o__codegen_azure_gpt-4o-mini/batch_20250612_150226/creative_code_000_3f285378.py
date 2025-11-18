"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-io.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring double staking rewards functionality.
Generated: DETERMINISTIC_3f28537827c35bee
Batch ID: 20250612_150226
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

// Interface for ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// Staking contract for PEPU tokens
contract PepuStaking {
    // Token to be staked
    IERC20 public pepuToken;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Timestamp of staking
        bool doubleReward;     // Flag for double rewards eligibility
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, bool doubleReward);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the PEPU token address
    constructor(IERC20 _pepuToken) {
        pepuToken = _pepuToken;
    }

    // Function to stake tokens
    function stake(uint256 amount, bool doubleReward) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient PEPU balance");

        // Transfer tokens from user to the contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staking information
        stakes[msg.sender] = Stake(amount, block.timestamp, doubleReward);
        
        emit Staked(msg.sender, amount, doubleReward);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate and mint reward
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp, userStake.doubleReward);

        // Reset user's stake information
        delete stakes[msg.sender];

        // Transfer staked amount and reward back to user
        pepuToken.transfer(msg.sender, userStake.amount + reward);
        
        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Helper function to calculate rewards
    function calculateReward(uint256 amount, uint256 timestamp, bool doubleReward) internal view returns (uint256) {
        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - timestamp;

        // Reward rate: 1% per month (approx. 30 days)
        uint256 rewardRate = (amount * stakingDuration) / (30 days) / 100;

        // Apply double reward if flagged
        if (doubleReward) {
            rewardRate *= 2;
        }

        return rewardRate;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
