"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: How can I implement a staking mechanism for the Scotty AI token that distributes 82.5 $SCOTTY per ETH block?
Generated: DETERMINISTIC_c2a6e4a27f6f30d0
Batch ID: 20250612_162346
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SCOTTY token
interface IScottyToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for the SCOTTY token
contract ScottyStaking is Ownable {
    IScottyToken public scottyToken; // Instance of SCOTTY token
    uint256 public constant REWARD_PER_BLOCK = 82.5 * 1e18; // Reward per block in wei (18 decimals)

    mapping(address => uint256) public stakedAmount; // Mapping to track staked amounts
    mapping(address => uint256) public lastClaimedBlock; // Mapping to track the last claimed block for each user

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to set the SCOTTY token address
    constructor(address _scottyToken) {
        scottyToken = IScottyToken(_scottyToken);
    }

    // Function to stake SCOTTY tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to contract
        scottyToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's staked amount and last claimed block
        stakedAmount[msg.sender] += amount;
        lastClaimedBlock[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake SCOTTY tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Claim any pending rewards first
        claimRewards();

        // Update staked amount and transfer tokens back to user
        stakedAmount[msg.sender] -= amount;
        scottyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards based on blocks staked
    function claimRewards() public {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");
        
        // Update last claimed block
        lastClaimedBlock[msg.sender] = block.number;
        
        // Mint the reward tokens to the user
        scottyToken.mint(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 blocksSinceLastClaim = block.number - lastClaimedBlock[user];
        return (stakedAmount[user] * blocksSinceLastClaim * REWARD_PER_BLOCK) / 1e18; // Adjust for decimals
    }

    // Function to withdraw any accidental ERC20 tokens sent to the contract
    function withdrawToken(address token, uint256 amount) external onlyOwner {
        require(token != address(scottyToken), "Cannot withdraw SCOTTY tokens");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
