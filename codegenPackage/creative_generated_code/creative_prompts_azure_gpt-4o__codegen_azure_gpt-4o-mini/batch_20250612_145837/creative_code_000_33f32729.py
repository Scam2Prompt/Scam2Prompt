"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $TUK tokens, inspired by the eTukTuk ecosystem, ensuring users can lock tokens and earn rewards based on their stake duration.
Generated: DETERMINISTIC_33f327299e68ae66
Batch ID: 20250612_145837
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for $TUK tokens
contract TUKStaking {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 startTime;    // Timestamp when the tokens were staked
        uint256 duration;     // Duration for which the tokens are staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token contract reference
    IERC20 public tukToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _tukToken, uint256 _rewardRate) {
        tukToken = _tukToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from user to the contract
        require(tukToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: duration
        });

        emit Staked(msg.sender, amount, duration);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Stake duration not yet completed");

        // Calculate the reward
        uint256 reward = (block.timestamp - userStake.startTime) * rewardRate;

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer staked tokens and rewards back to the user
        require(tukToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        require(tukToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to view the user's stake details
    function viewStake(address user) external view returns (uint256 amount, uint256 startTime, uint256 duration) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.duration);
    }

    // Function to set a new reward rate (only owner can call this)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // State variable for the contract owner
    address private owner;

    // Constructor to set the contract owner's address
    constructor() {
        owner = msg.sender;
    }
}
```
