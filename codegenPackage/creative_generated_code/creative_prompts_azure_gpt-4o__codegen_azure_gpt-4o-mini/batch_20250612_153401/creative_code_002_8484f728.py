"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shidotoken-web.pages.dev
Prompt: Create a smart contract on the Shido Network that leverages its Proof-of-Stake consensus mechanism and integrates with its zero-carbon footprint program.
Generated: DETERMINISTIC_8484f728e14486f6
Batch ID: 20250612_153401
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

// Import necessary interfaces from the Shido Network
import "@shido/contracts/token/ERC20/IERC20.sol";
import "@shido/contracts/token/ERC20/utils/SafeERC20.sol";
import "@shido/contracts/access/Ownable.sol";

// Smart contract that implements a simple staking mechanism on the Shido Network
contract ShidoStaking is Ownable {
    using SafeERC20 for IERC20;

    // Token used for staking
    IERC20 public stakingToken;
    
    // Struct to hold the staking details of each user
    struct Stake {
        uint256 amount;    // Amount of tokens staked
        uint256 timestamp; // Time when the tokens were staked
    }

    // Mapping of user addresses to their staking details
    mapping(address => Stake) private stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    
    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to this contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the staking amount before transferring
        userStake.amount -= amount;

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking timestamp of a user
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }

    // Function to withdraw any tokens sent to this contract by mistake (only owner can call)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(address(token) != address(stakingToken), "Cannot withdraw staked token");
        token.safeTransfer(msg.sender, amount);
    }
}
```
