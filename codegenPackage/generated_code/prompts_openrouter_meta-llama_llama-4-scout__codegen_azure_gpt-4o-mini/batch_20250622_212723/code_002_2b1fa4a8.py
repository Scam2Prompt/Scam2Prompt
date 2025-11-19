"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: "Generate a smart contract in Solidity for managing WMTx token transactions, including earning rewards for EarthNode operators and stakers."
Generated: DETERMINISTIC_2b1fa4a8f00d29dd
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for WMTx token
contract WMTxToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Reward rate for EarthNode operators and stakers
    uint256 public rewardRate;
    
    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _rewardRate) 
        ERC20(name, symbol) 
    {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract owner
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to set the reward rate (only owner can call)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        // Simple reward calculation based on balance and reward rate
        return balanceOf(user).mul(rewardRate).div(100);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards available to claim");

        // Update the rewards mapping
        rewards[msg.sender] = rewards[msg.sender].add(rewardAmount);
        
        // Mint new tokens as rewards
        _mint(msg.sender, rewardAmount);
        
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to transfer tokens with reward calculation
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate rewards before transfer
        uint256 rewardAmount = calculateRewards(msg.sender);
        if (rewardAmount > 0) {
            rewards[msg.sender] = rewards[msg.sender].add(rewardAmount);
        }

        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // Function to transfer tokens from one address to another with reward calculation
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate rewards before transfer
        uint256 rewardAmount = calculateRewards(sender);
        if (rewardAmount > 0) {
            rewards[sender] = rewards[sender].add(rewardAmount);
        }

        // Call the parent transferFrom function
        return super.transferFrom(sender, recipient, amount);
    }
}
```
