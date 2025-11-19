"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-store-en.pages.dev
Prompt: Describe how to implement a rewards program in a decentralized application (dApp) using Pushd tokens to incentivize user engagement.
Generated: DETERMINISTIC_84ee17a711f48c58
Batch ID: 20250612_161617
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

// Import OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title RewardsProgram
// @notice Implements a rewards program using Pushd tokens
contract RewardsProgram is Ownable, ERC20 {
    // Mapping to track user rewards
    mapping(address => uint256) private userRewards;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // @dev Constructor to initialize the Pushd token with a name and symbol
    constructor() ERC20("Pushd Token", "PUSH") {
        // Mint initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1,000,000 tokens
    }

    // @dev Function to distribute rewards to a user
    // @param _user The address of the user to reward
    // @param _amount The amount of tokens to reward
    function distributeRewards(address _user, uint256 _amount) external onlyOwner {
        // Ensure the amount is positive
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer the specified amount of tokens from the owner to the user
        _transfer(msg.sender, _user, _amount);
        
        // Update user rewards mapping
        userRewards[_user] += _amount;

        // Emit rewards distribution event
        emit RewardsDistributed(_user, _amount);
    }

    // @dev Function to check the reward balance of a user
    // @param _user The address of the user to check
    // @return The total rewards of the user
    function checkUserRewards(address _user) external view returns (uint256) {
        return userRewards[_user];
    }

    // @dev Function to redeem rewards for tokens
    // @param _amount The amount of rewards to redeem
    function redeemRewards(uint256 _amount) external {
        // Ensure the user has enough rewards to redeem
        require(userRewards[msg.sender] >= _amount, "Insufficient rewards");

        // Update user rewards mapping
        userRewards[msg.sender] -= _amount;

        // Transfer the specified amount of tokens to the user
        _transfer(address(this), msg.sender, _amount);
    }

    // @dev Fallback function to prevent sending ETH directly to the contract
    receive() external payable {
        revert("Cannot send ETH to this contract");
    }
}
```
