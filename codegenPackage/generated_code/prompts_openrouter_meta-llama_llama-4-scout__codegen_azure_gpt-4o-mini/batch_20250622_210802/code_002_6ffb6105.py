"""
Generated Code Metadata:
========================
Original URL: https://stake-etuktuk-io.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the staking and withdrawal of $TUK tokens, including the calculation of rewards and gas fees, as described on the eTukTuk website.
Generated: DETERMINISTIC_6ffb61054b970f5b
Batch ID: 20250622_210802
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public tukToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // Example: 1 TUK per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the contract with the TUK token address
    constructor(IERC20 _tukToken) {
        tukToken = _tukToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(tukToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Update user's rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from user to contract
        tukToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update user's rewards before withdrawal
        updateRewards(msg.sender);

        uint256 amountToWithdraw = userStake.amount;
        uint256 rewardsToWithdraw = userStake.rewards;

        // Reset user's stake information
        userStake.amount = 0;
        userStake.rewards = 0;

        // Transfer staked tokens and rewards to user
        tukToken.transfer(msg.sender, amountToWithdraw.add(rewardsToWithdraw));

        emit Withdrawn(msg.sender, amountToWithdraw, rewardsToWithdraw);
    }

    // Internal function to update rewards for a user
    function updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 timeStaked = block.timestamp.sub(userStake.timestamp);
            uint256 rewards = timeStaked.mul(rewardRate).mul(userStake.amount).div(1e18);
            userStake.rewards = userStake.rewards.add(rewards);
            userStake.timestamp = block.timestamp; // Reset timestamp
        }
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(tukToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        tukToken.transfer(msg.sender, _amount);
    }
}
```
