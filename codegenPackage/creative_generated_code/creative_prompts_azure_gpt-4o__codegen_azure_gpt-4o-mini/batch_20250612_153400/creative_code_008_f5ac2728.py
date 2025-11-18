"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1-merlinstarter.pages.dev
Prompt: Generate a Solidity smart contract that interacts with MerlinChain to enable staking of $MP tokens in the $HUHU pool.
Generated: DETERMINISTIC_f5ac272864252eef
Batch ID: 20250612_153400
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title HuHuStake
 * @dev This contract allows users to stake $MP tokens in the $HUHU pool on MerlinChain.
 */
contract HuHuStake is Ownable {
    // State variables
    IERC20 public mpToken; // $MP token contract
    IERC20 public huhuToken; // $HUHU token contract
    mapping(address => uint256) public stakes; // Mapping of user addresses to their staked amounts
    
    event Staked(address indexed user, uint256 amount); // Event emitted on successful staking
    event Unstaked(address indexed user, uint256 amount); // Event emitted on successful unstaking

    /**
     * @dev Constructor to set the $MP and $HUHU token addresses.
     * @param _mpToken Address of the $MP token contract.
     * @param _huhuToken Address of the $HUHU token contract.
     */
    constructor(address _mpToken, address _huhuToken) {
        require(_mpToken != address(0), "Invalid $MP token address");
        require(_huhuToken != address(0), "Invalid $HUHU token address");

        mpToken = IERC20(_mpToken);
        huhuToken = IERC20(_huhuToken);
    }

    /**
     * @dev Function to stake $MP tokens in the $HUHU pool.
     * @param amount Amount of $MP tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer $MP tokens from user to this contract
        bool success = mpToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user's stake
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount); // Emit staking event
    }

    /**
     * @dev Function to unstake $MP tokens from the pool.
     * @param amount Amount of $MP tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's stake
        stakes[msg.sender] -= amount;

        // Transfer $MP tokens back to user
        bool success = mpToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount); // Emit unstaking event
    }

    /**
     * @dev Function to check the stake of a user.
     * @param user Address of the user to check.
     * @return The staked amount of $MP tokens for the user.
     */
    function checkStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Function to recover any ERC20 tokens sent to this contract accidentally.
     * @param tokenAddress Address of the token to recover.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
