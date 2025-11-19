"""
Generated Code Metadata:
========================
Original URL: https://sale-humanizedai.web.app
Prompt: "Design a staking mechanism for a cryptocurrency token, allowing users to claim and stake their tokens on a platform like HumanizedAi."
Generated: DETERMINISTIC_392efe642c16981a
Batch ID: 20250622_205709
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a cryptocurrency token
contract StakingContract is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging staking and claiming actions
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to claim staked tokens
    function claim() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the amount to claim (for simplicity, we will just return the staked amount)
        uint256 claimableAmount = userStake.amount;

        // Reset user's stake before transferring to prevent re-entrancy
        userStake.amount = 0;

        // Transfer the claimable amount back to the user
        stakingToken.transfer(msg.sender, claimableAmount);

        emit Claimed(msg.sender, claimableAmount);
    }

    // Function to check the staked amount of a user
    function stakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(msg.sender, _amount);
    }
}
```
