"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-ia.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring compatibility with Ethereum Layer 2 standards.
Generated: DETERMINISTIC_e2c3c6390c335515
Batch ID: 20250612_150347
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PepeStaking
 * @dev A smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain.
 */
contract PepeStaking is ReentrancyGuard, Ownable {
    // The ERC20 token being staked
    IERC20 public pepuToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the staking
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor to set the $PEPU token address.
     * @param _pepuToken Address of the $PEPU token contract
     */
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    /**
     * @dev Function to stake $PEPU tokens.
     * @param amount Amount of $PEPU tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer $PEPU tokens from the user to the contract
        pepuToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $PEPU tokens.
     * @param amount Amount of $PEPU tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's staked amount
        userStake.amount -= amount;

        // Transfer $PEPU tokens back to the user
        pepuToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to get the staked amount of a user.
     * @param user Address of the user
     * @return The amount of tokens staked by the user
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Function to get the staking timestamp of a user.
     * @param user Address of the user
     * @return The timestamp when the user last staked
     */
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }
}
```
