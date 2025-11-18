"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jelybaby.web.app
Prompt: Create a smart contract for staking $Jelly tokens, incorporating utilities like Jellotto and Jelly Flip as mentioned on the Jelly platform.
Generated: DETERMINISTIC_3531ea99de7f423e
Batch ID: 20250612_150545
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

// Import required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Jellotto and Jelly Flip contracts
interface IJellotto {
    function participate(uint256 amount) external;
}

interface IJellyFlip {
    function flipTokens(uint256 amount) external;
}

// Contract for staking Jelly tokens
contract JellyStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public jellyToken;

    // Staking details
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake) private stakes;

    // Events for logging user actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event JellottoParticipated(address indexed user, uint256 amount);
    event JellyFlipped(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the Jelly token address
    constructor(address _jellyToken) {
        require(_jellyToken != address(0), "Invalid Jelly token address");
        jellyToken = IERC20(_jellyToken);
    }

    // Function to stake Jelly tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(jellyToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens to the contract
        jellyToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake Jelly tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);

        // Transfer tokens back to the user
        jellyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to participate in Jellotto
    function participateInJellotto(uint256 amount, address jellottoAddress) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount for Jellotto");
        require(jellottoAddress != address(0), "Invalid Jellotto address");

        // Update stake before participating
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);

        // Call the Jellotto contract
        IJellotto(jellottoAddress).participate(amount);

        emit JellottoParticipated(msg.sender, amount);
    }

    // Function to flip Jelly tokens
    function flipTokens(uint256 amount, address jellyFlipAddress) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount for flipping");
        require(jellyFlipAddress != address(0), "Invalid Jelly Flip address");

        // Update stake before flipping
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);

        // Call the Jelly Flip contract
        IJellyFlip(jellyFlipAddress).flipTokens(amount);

        emit JellyFlipped(msg.sender, amount);
    }

    // Function to get the user's stake details
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory stakeInfo = stakes[user];
        return (stakeInfo.amount, stakeInfo.timestamp);
    }
}
```
