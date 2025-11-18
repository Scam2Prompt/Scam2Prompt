"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchifi-dapprotocol.pages.dev
Prompt: Create a smart contract for staking and unstaking tokens on the Fix-path platform, ensuring support for multi-chain functionality.
Generated: DETERMINISTIC_92b4ce6c4a3a6cc1
Batch ID: 20250612_145826
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking and unstaking tokens
contract MultiChainStaking is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Staker information structure
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block (to be set)
    uint256 public rewardPerBlock;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Modifier to check if the address is a valid staker
    modifier isStaker() {
        require(stakers[msg.sender].amountStaked > 0, "Not a staker");
        _;
    }

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external isStaker {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Not enough staked");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to get reward (simple implementation, can be enhanced)
    function getReward() external view isStaker returns (uint256) {
        Staker storage staker = stakers[msg.sender];
        return (staker.amountStaked * rewardPerBlock); // simplistically calculate reward
    }

    // Function to set new reward rate (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to withdraw tokens (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Not enough balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
