"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Provide an example of a decentralized application (dApp) that integrates DOGE20 staking rewards and token claiming functionality.
Generated: DETERMINISTIC_cd8a8f287ca94998
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready example of a decentralized application (dApp) smart contract written in Solidity that integrates DOGE20 (ERC-20 equivalent for Dogecoin-inspired tokens) staking rewards and token claiming functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC20 contract for handling DOGE20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for DOGE20 Token
contract Doge20Staking is Ownable {
    // State variables
    IERC20 public doge20Token; // Reference to the DOGE20 token contract
    uint256 public rewardRate; // Reward rate per second per staked token
    uint256 public totalStaked; // Total amount of tokens staked
    
    struct Stake {
        uint256 amount;         // Amount of tokens staked by the user
        uint256 rewardDebt;     // Rewards already paid to the user
        uint256 lastUpdated;    // Timestamp of the last interaction
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor initializes the contract with the DOGE20 token address and reward rate
    constructor(address _doge20Token, uint256 _rewardRate) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        doge20Token = IERC20(_doge20Token);
        rewardRate = _rewardRate;
    }

    // Modifier to ensure the user has staked tokens
    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No tokens staked by the user");
        _;
    }

    /**
     * @dev Allows users to stake DOGE20 tokens.
     * @param _amount The number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(doge20Token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        
        // Update rewards for the user before modifying stake information
        _updateRewards(msg.sender);

        // Transfer the tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking info
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake tokens they previously staked.
     */
    function unstake(uint256 _amount) external hasStake(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update rewards for the user before modifying stake information
        _updateRewards(msg.sender);

        // Update staking info
        stakes[msg.sender].amount -= _amount;

        // Transfer the tokens back to the user
        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");

        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        // Update rewards before payout
        _updateRewards(msg.sender);

        // Calculate pending rewards
        uint256 pendingRewards = stakes[msg.sender].rewardDebt;

        require(pendingRewards > 0, "No rewards available");

        // Reset reward debt for the user
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update user rewards.
     * @param _user The address of the user whose rewards are being updated.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];

        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 newRewards = (userStake.amount * rewardRate * timeElapsed) / 1e18;

        // Update reward debt and last updated timestamp
        userStake.rewardDebt += newRewards;
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate The new reward rate per second per staked token.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(doge20Token.balanceOf(address(this)) >= _amount, "Insufficient token balance in contract");
        require(doge20Token.transfer(owner(), _amount), "Token transfer failed");
    }
}
```

### Notes:
- This contract assumes DOGE20 token follows the ERC-20 standard.
- It uses OpenZeppelin's `Ownable` and `IERC20` for security and token interactions.
- Error handling is included for all critical operations such as transfers, staking, and claiming.
- Reward calculation uses `rewardRate` per second per staked token for scalability.
- Event logging is implemented for transparency and tracking.
