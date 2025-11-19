"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: How can I implement a smart contract to stake $FOMO tokens in The Old Castle Defense ecosystem?
Generated: DETERMINISTIC_959f88756106e0a5
Batch ID: 20250612_163502
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

// Import the ERC20 interface to interact with the $FOMO token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract to stake $FOMO tokens in The Old Castle Defense ecosystem
 */
contract StakingContract is Ownable {
    // Address of the $FOMO token contract
    IERC20 public fomoToken;

    // Struct to store information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedTime;
    }

    // Mapping to track each staker's info
    mapping(address => Staker) public stakers;

    // Events to log staking activity
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $FOMO token address
     * @param _fomoToken Address of the $FOMO token contract
     */
    constructor(address _fomoToken) {
        require(_fomoToken != address(0), "Invalid token address");
        fomoToken = IERC20(_fomoToken);
    }

    /**
     * @dev Stake a certain amount of $FOMO tokens
     * @param amount Amount of $FOMO tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(fomoToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer $FOMO tokens from the staker to this contract
        fomoToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastStakedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake a certain amount of $FOMO tokens
     * @param amount Amount of $FOMO tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update staker's information
        stakers[msg.sender].amountStaked -= amount;

        // Transfer $FOMO tokens back to the staker
        fomoToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the amount of $FOMO tokens staked by an address
     * @param user Address of the user
     * @return Amount of tokens staked
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    /**
     * @dev Get the last staked time for an address
     * @param user Address of the user
     * @return Timestamp of the last staking activity
     */
    function getLastStakedTime(address user) external view returns (uint256) {
        return stakers[user].lastStakedTime;
    }

    /**
     * @dev Withdraw any tokens mistakenly sent to the contract by the owner
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(fomoToken), "Cannot withdraw staked tokens");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
