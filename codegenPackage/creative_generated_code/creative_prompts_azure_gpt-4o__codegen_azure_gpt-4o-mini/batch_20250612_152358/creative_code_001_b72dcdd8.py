"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everllodge-claim.pages.dev
Prompt: Generate code to interact with the Everlodge $ELDG token on the Ethereum blockchain, including functions for staking, claiming rewards, and checking balances.
Generated: DETERMINISTIC_b72dcdd871fd835e
Batch ID: 20250612_152358
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

// Importing the ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the staking contract
interface IStaking {
    function stake(uint256 amount) external;
    function claimRewards() external;
    function getStakedBalance(address user) external view returns (uint256);
    function getRewardBalance(address user) external view returns (uint256);
}

contract EverlodgeStaking is IStaking {
    IERC20 public eldgToken; // ERC20 token reference
    address public owner; // Contract owner
    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public rewardBalances; // User reward balances

    // Event declarations for logging
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _eldgToken) {
        eldgToken = _eldgToken; // Set the ELGD token address
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier for only owner functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than zero");
        require(eldgToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens from user to contract
        eldgToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked balance
        stakedBalances[msg.sender] += amount;
        
        emit Staked(msg.sender, amount); // Emit stake event
    }

    // Function to claim staking rewards
    function claimRewards() external override {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        // Reset user's reward balance
        rewardBalances[msg.sender] = 0;
        
        // Transfer rewards to user
        eldgToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward); // Emit rewards claimed event
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address user) external view override returns (uint256) {
        return stakedBalances[user];
    }

    // Function to get the reward balance of a user
    function getRewardBalance(address user) external view override returns (uint256) {
        return rewardBalances[user];
    }

    // Owner function to distribute rewards (for simplicity, rewards are just for demonstration)
    function distributeRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Array lengths must match");
        
        for (uint256 i = 0; i < users.length; i++) {
            // Update each user's reward balance
            rewardBalances[users[i]] += amounts[i];
        }
    }
}
```

### Notes
- Ensure you have the OpenZeppelin contracts library installed to compile this code.
- This contract is a basic implementation and should be tested thoroughly before deploying on the Ethereum mainnet.
- Implement additional security measures as required for your application's context.
