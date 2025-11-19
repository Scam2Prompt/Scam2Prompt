"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-befetoken.pages.dev
Prompt: Generate a smart contract in Solidity for staking BRISE to earn BEFE tokens.
Generated: DETERMINISTIC_71abff88e8fa638a
Batch ID: 20250612_160656
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

// Import the IERC20 interface for interacting with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking BRISE to earn BEFE tokens
contract StakingContract is Ownable {
    // The BRISE token interface
    IERC20 public briseToken;

    // The BEFE token interface
    IERC20 public befeToken;

    // Struct to hold information about a user's stake
    struct Stake {
        uint256 amount; // Amount of BRISE staked
        uint256 rewardDebt; // Reward debt (for calculating rewards)
        uint256 lastStakeTime; // Last time the stake was updated
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount of BRISE staked in the contract
    uint256 public totalStaked;

    // Reward rate (in BEFE tokens) per second per staked BRISE
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the BRISE and BEFE token addresses and the reward rate
    constructor(address _briseTokenAddress, address _befeTokenAddress, uint256 _rewardRate) {
        briseToken = IERC20(_briseTokenAddress);
        befeToken = IERC20(_befeTokenAddress);
        rewardRate = _rewardRate;
    }

    // Function to stake BRISE tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(briseToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];

        // Update the reward debt before modifying the stake
        if (userStake.amount > 0) {
            userStake.rewardDebt += calculatePendingReward(msg.sender);
        }

        // Update stake details
        userStake.amount += _amount;
        userStake.lastStakeTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake BRISE tokens and claim rewards
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update reward debt and claim rewards
        uint256 reward = calculatePendingReward(msg.sender);
        if (reward > 0) {
            require(befeToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }

        // Update user's stake and total staked amount
        userStake.amount -= _amount;
        totalStaked -= _amount;

        require(briseToken.transfer(msg.sender, _amount), "Transfer failed");
        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate pending rewards for a user
    function calculatePendingReward(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeStaked = block.timestamp - userStake.lastStakeTime;
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjust for reward rate precision
    }

    // Function to update the reward rate (only owner can call this)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to rescue tokens mistakenly sent to the contract
    function rescueTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(briseToken) && _token != address(befeToken), "Cannot rescue staked tokens");
        require(IERC20(_token).transfer(owner(), _amount), "Rescue transfer failed");
    }
}
```
