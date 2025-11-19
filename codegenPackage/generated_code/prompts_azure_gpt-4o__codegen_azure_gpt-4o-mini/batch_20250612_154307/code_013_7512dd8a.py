"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that allows users to stake their meme coins but requires holding $STARS tokens to maximize rewards, as outlined in the Crypto All-Stars staking mechanism.
Generated: DETERMINISTIC_7512dd8a38328d0d
Batch ID: 20250612_154307
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for meme coins with $STARS token requirement
contract MemeCoinStaking is ReentrancyGuard, Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of meme coins staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token for meme coins
    IERC20 public memeCoin;
    // ERC20 token for $STARS
    IERC20 public starsToken;

    // Minimum amount of $STARS required to stake
    uint256 public constant MIN_STARS_REQUIRED = 100 * 10**18; // Example: 100 $STARS

    // Event emitted when a user stakes meme coins
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes meme coins
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with meme coin and $STARS token addresses
    constructor(address _memeCoin, address _starsToken) {
        memeCoin = IERC20(_memeCoin);
        starsToken = IERC20(_starsToken);
    }

    // Function to stake meme coins
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(starsToken.balanceOf(msg.sender) >= MIN_STARS_REQUIRED, "Insufficient $STARS tokens");

        // Transfer meme coins from user to the contract
        memeCoin.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake meme coins
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes found");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake information
        userStake.amount = 0;

        // Transfer meme coins back to the user
        memeCoin.transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to check the user's stake amount
    function getStakeAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to check if a user meets the $STARS requirement
    function hasMinimumStars(address user) external view returns (bool) {
        return starsToken.balanceOf(user) >= MIN_STARS_REQUIRED;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(memeCoin) && tokenAddress != address(starsToken), "Cannot withdraw staked tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
