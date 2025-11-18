"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeapp-serverlaunch.com
Prompt: Write a smart contract to enable staking and unstaking of tokens, including error handling for staking-related issues.
Generated: DETERMINISTIC_44d2ae79b8fc68be
Batch ID: 20250612_145821
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

/**
 * @title StakingContract
 * @dev A contract for staking and unstaking ERC20 tokens with error handling.
 */
contract StakingContract is Ownable {
    IERC20 public stakingToken; // The token that will be staked
    mapping(address => uint256) public stakes; // Mapping of user addresses to their stakes
    mapping(address => uint256) public rewards; // Mapping of user addresses to their rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @notice Stakes a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        stakes[msg.sender] += amount; // Update the user's stake
        stakingToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to the contract

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstakes a specified amount of tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender] >= amount, "Insufficient stake to unstake");

        stakes[msg.sender] -= amount; // Update the user's stake
        stakingToken.transfer(msg.sender, amount); // Transfer tokens back to the user

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Allows the contract owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot withdraw 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        stakingToken.transfer(msg.sender, amount); // Transfer tokens to the owner
    }

    /**
     * @notice Retrieves the staking balance of a user.
     * @param user The address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @notice Retrieves the balance of the contract.
     * @return The total amount of tokens held by the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return stakingToken.balanceOf(address(this));
    }
}
```
