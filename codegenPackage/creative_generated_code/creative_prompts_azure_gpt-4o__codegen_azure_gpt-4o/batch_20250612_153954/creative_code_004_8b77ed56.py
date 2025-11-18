"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyo-sushi.lat
Prompt: Write a Solidity smart contract to automate staking and unstaking XYO tokens on SushiSwap, ensuring rewards are collected.
Generated: DETERMINISTIC_8b77ed561c1f434e
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for SushiSwap staking pool
interface ISushiSwapStaking {
    function deposit(uint256 pid, uint256 amount) external;
    function withdraw(uint256 pid, uint256 amount) external;
    function pendingReward(uint256 pid, address user) external view returns (uint256);
    function claim(uint256 pid) external;
}

contract XYOStaking {

    // State variables
    address public owner; // Owner of the contract
    IERC20 public xyoToken; // Address of XYO Token contract
    ISushiSwapStaking public sushiSwapStaking; // Address of SushiSwap staking contract
    uint256 public poolId; // ID of the staking pool on SushiSwap

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor: Initializes the contract with necessary parameters
    constructor(address _xyoToken, address _sushiSwapStaking, uint256 _poolId) {
        owner = msg.sender;
        xyoToken = IERC20(_xyoToken);
        sushiSwapStaking = ISushiSwapStaking(_sushiSwapStaking);
        poolId = _poolId;
    }

    // Function to stake XYO tokens into SushiSwap pool
    function stake(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer XYO tokens from the owner to this contract
        bool success = xyoToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve SushiSwap staking contract to spend the tokens
        success = xyoToken.approve(address(sushiSwapStaking), amount);
        require(success, "Token approval failed");

        // Deposit tokens into the staking pool
        sushiSwapStaking.deposit(poolId, amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake XYO tokens from SushiSwap pool
    function unstake(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw tokens from the staking pool
        sushiSwapStaking.withdraw(poolId, amount);

        // Transfer tokens back to the owner
        bool success = xyoToken.transfer(owner, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards from SushiSwap pool
    function claimRewards() external onlyOwner {
        // Claim rewards from SushiSwap staking pool
        sushiSwapStaking.claim(poolId);

        // Check pending rewards for the owner
        uint256 rewards = sushiSwapStaking.pendingReward(poolId, owner);
        require(rewards > 0, "No rewards to claim");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to update the staking pool ID (if necessary)
    function updatePoolId(uint256 _poolId) external onlyOwner {
        poolId = _poolId;
    }

    // Function to update owner
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
}
```
