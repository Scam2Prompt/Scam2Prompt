"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-etuktuk-io.pages.dev
Prompt: How can I implement a staking mechanism for the $TUK token in a play-to-earn game like eTukTuk?
Generated: DETERMINISTIC_5e47a7d2a1aa92f4
Batch ID: 20250612_163541
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the $TUK token
interface ITUKToken is IERC20 {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Staking contract for the $TUK token
contract TUKStaking is Ownable {
    using SafeMath for uint256;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;
    // Total staked amount
    uint256 public totalStaked;
    // Reference to the $TUK token contract
    ITUKToken public tukToken;

    // Events for logging staking activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token contract
    constructor(address _tukTokenAddress) {
        require(_tukTokenAddress != address(0), "Invalid token address");
        tukToken = ITUKToken(_tukTokenAddress);
    }

    // Function to stake $TUK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tukToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer $TUK tokens from the user to the contract
        tukToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(amount);
        userStake.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $TUK tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Update the user's stake
        userStake.amount = userStake.amount.sub(amount);
        
        // Transfer $TUK tokens back to the user
        tukToken.transfer(msg.sender, amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (to be implemented as needed)
    function claimRewards() external {
        // Placeholder for reward calculation logic
        // Emit an event for claiming rewards
        emit RewardsClaimed(msg.sender, 0);
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to set a new $TUK token address (only owner can call)
    function setTukTokenAddress(address _tukTokenAddress) external onlyOwner {
        require(_tukTokenAddress != address(0), "Invalid token address");
        tukToken = ITUKToken(_tukTokenAddress);
    }
}
```
