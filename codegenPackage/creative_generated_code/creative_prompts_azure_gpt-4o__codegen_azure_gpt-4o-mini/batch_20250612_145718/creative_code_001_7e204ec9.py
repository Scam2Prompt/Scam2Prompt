"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multihubresolve.pages.dev
Prompt: Generate code to create a staking pool using the DebugDappNode platform, ensuring decentralized support for wallets and integration with blockchain and DeFi applications.
Generated: DETERMINISTIC_7e204ec97371e47f
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
const { ethers } = require('hardhat'); // Ethers.js for Ethereum interactions
const { BigNumber } = require('ethers'); // BigNumber for handling large numbers

// Define the StakingPool contract
contract StakingPool {
    // State variables
    address public owner; // Owner of the staking pool
    mapping(address => uint256) public stakes; // Mapping to track user stakes
    uint256 public totalStaked; // Total amount staked in the pool
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock; // Last block number when rewards were updated

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate) {
        owner = msg.sender; // Set the contract deployer as the owner
        rewardRate = _rewardRate; // Set the reward rate
        totalStaked = 0; // Initialize total staked amount
        lastUpdateBlock = block.number; // Set the last update block to current block
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        // Ensure the contract has sufficient allowance to spend user tokens
        require(IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stakes and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update stakes and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Transfer failed");

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update the last update block
        lastUpdateBlock = block.number;

        // Transfer rewards to the user
        require(IERC20(tokenAddress).transfer(msg.sender, rewards), "Transfer failed");

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = stakes[user];
        uint256 blocksStaked = block.number - lastUpdateBlock;

        // Calculate rewards based on staked amount and reward rate
        return stakedAmount * rewardRate * blocksStaked;
    }

    // Function to withdraw remaining tokens (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= IERC20(tokenAddress).balanceOf(address(this)), "Insufficient balance");

        // Transfer tokens to the owner
        require(IERC20(tokenAddress).transfer(owner, amount), "Transfer failed");
    }
}

// Interface for ERC20 token interactions
interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Note: Ensure proper testing and deployment scripts are created for production readiness.
// This contract assumes the existence of an ERC20 token deployed and specified by tokenAddress.
```
