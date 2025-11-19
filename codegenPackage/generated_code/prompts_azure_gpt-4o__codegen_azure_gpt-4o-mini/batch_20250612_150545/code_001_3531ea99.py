"""
Generated Code Metadata:
========================
Original URL: https://jelybaby.web.app
Prompt: Create a smart contract for staking $Jelly tokens, incorporating utilities like Jellotto and Jelly Flip as mentioned on the Jelly platform.
Generated: DETERMINISTIC_3531ea99de7f423e
Batch ID: 20250612_150545
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Jellotto and Jelly Flip contracts
interface IJellotto {
    function participateInJellotto(address user, uint256 amount) external;
}

interface IJellyFlip {
    function flipTokens(address user, uint256 amount) external;
}

// Staking contract for $Jelly tokens
contract JellyStaking is Ownable {
    // State variables
    IERC20 public jellyToken; // The $Jelly token contract
    IJellotto public jellotto; // Jellotto contract
    IJellyFlip public jellyFlip; // Jelly Flip contract

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ParticipatedInJellotto(address indexed user, uint256 amount);
    event FlippedTokens(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(IERC20 _jellyToken, IJellotto _jellotto, IJellyFlip _jellyFlip) {
        jellyToken = _jellyToken;
        jellotto = _jellotto;
        jellyFlip = _jellyFlip;
    }

    // Function to stake $Jelly tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(jellyToken.balanceOf(msg.sender) >= amount, "Insufficient $Jelly balance");

        // Transfer tokens from user to this contract
        jellyToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $Jelly tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        jellyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to participate in Jellotto
    function participateInJellotto(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Call the Jellotto contract to participate
        jellotto.participateInJellotto(msg.sender, amount);

        emit ParticipatedInJellotto(msg.sender, amount);
    }

    // Function to flip tokens using Jelly Flip
    function flipTokens(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Call the Jelly Flip contract to flip tokens
        jellyFlip.flipTokens(msg.sender, amount);

        emit FlippedTokens(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
