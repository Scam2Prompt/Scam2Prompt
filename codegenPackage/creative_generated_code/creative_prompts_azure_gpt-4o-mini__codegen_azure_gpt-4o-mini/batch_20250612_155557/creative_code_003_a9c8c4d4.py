"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Create a sample code snippet for a smart contract that could facilitate the staking of $FROP tokens based on the information provided on the Popo The Frog site.
Generated: DETERMINISTIC_a9c8c4d4ba8429ce
Batch ID: 20250612_155557
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

// Importing the OpenZeppelin ERC20 interface for our $FROP token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $FROP tokens
contract FropStaking is Ownable {
    // Structure to hold staking information for each user
    struct Stake {
        uint256 amount;      // Amount of $FROP tokens staked
        uint256 timestamp;   // Timestamp of when the tokens were staked
    }

    // Mapping from user addresses to their stakes
    mapping(address => Stake) private stakes;

    IERC20 public fropToken; // Instance of the $FROP token contract

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $FROP token address
    constructor(address _fropToken) {
        require(_fropToken != address(0), "Invalid token address");
        fropToken = IERC20(_fropToken);
    }

    // Function to stake $FROP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(fropToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens from the user to the contract
        fropToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $FROP tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        fropToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to get the current stake of a user
    function getStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking timestamp of a user
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(fropToken), "Cannot withdraw staked tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
