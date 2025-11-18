"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Write a smart contract in Solidity that mimics the functionality of Tenderize's liquid staking process, where users deposit tokens, receive ERC-20 compliant tenderized tokens, and accrue staking rewards dynamically.
Generated: DETERMINISTIC_0b1808712c218d7e
Batch ID: 20250612_145913
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

// Import the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the staking rewards system
interface IStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getRewards(address account) external view returns (uint256);
}

// The TenderizeLiquidStaking contract
contract TenderizeLiquidStaking is Ownable {
    IERC20 public immutable depositToken; // Token to be deposited
    IERC20 public immutable tenderizedToken; // Token representing staked assets
    IStaking public stakingContract; // Staking contract for rewards

    mapping(address => uint256) public balances; // User balances for deposits
    mapping(address => uint256) public lastClaimed; // Last claimed rewards

    // Events for tracking actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Constructor to initialize the contract
    constructor(
        address _depositToken,
        address _tenderizedToken,
        address _stakingContract
    ) {
        depositToken = IERC20(_depositToken);
        tenderizedToken = IERC20(_tenderizedToken);
        stakingContract = IStaking(_stakingContract);
    }

    // Deposit tokens to receive tenderized tokens
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer deposit tokens from user to the contract
        depositToken.transferFrom(msg.sender, address(this), amount);
        
        // Stake the deposited tokens
        stakingContract.stake(amount);
        
        // Update user's balance and last claimed time
        balances[msg.sender] += amount;
        lastClaimed[msg.sender] = block.timestamp;

        // Mint tenderized tokens for the user
        tenderizedToken.mint(msg.sender, amount);

        emit Deposited(msg.sender, amount);
    }

    // Withdraw tokens and claim rewards
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update rewards before withdrawal
        claimRewards();

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Unstake the tokens
        stakingContract.unstake(amount);

        // Transfer the deposit tokens back to the user
        depositToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim staking rewards for the user
    function claimRewards() public {
        uint256 rewards = stakingContract.getRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        depositToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Get the user's pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        return stakingContract.getRewards(user);
    }

    // Admin function to change the staking contract
    function setStakingContract(address _stakingContract) external onlyOwner {
        stakingContract = IStaking(_stakingContract);
    }
}
```
