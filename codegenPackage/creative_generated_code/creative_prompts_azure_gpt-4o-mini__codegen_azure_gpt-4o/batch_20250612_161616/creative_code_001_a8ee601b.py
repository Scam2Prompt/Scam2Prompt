"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-st.web.app
Prompt: Generate a sample smart contract for staking $MGLS tokens in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_a8ee601b79758787
Batch ID: 20250612_161616
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

/**
 * @title Meme Moguls Staking Contract
 * @dev A smart contract that allows users to stake $MGLS tokens in the Meme Moguls ecosystem.
 */
contract MGLSStaking {
    // Interface for the ERC20 token
    IERC20 public mglsToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was created
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total amount of $MGLS tokens staked in the contract
    uint256 public totalStaked;

    // Events for logging contract activities
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the staking contract
    constructor(IERC20 _mglsToken) {
        mglsToken = _mglsToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $MGLS tokens.
     * @param _amount The amount of $MGLS tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        
        // Transfer $MGLS tokens from the user to the contract
        bool success = mglsToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the user's staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Update the total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        uint256 stakedAmount = userStake.amount;

        // Calculate rewards (for simplicity, fixed 10% annual reward rate)
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (stakedAmount * 10 * stakingDuration) / (365 days * 100);

        // Reset user stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Update total staked amount
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards back to the user
        bool success = mglsToken.transfer(msg.sender, stakedAmount + reward);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, block.timestamp);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        uint256 contractBalance = mglsToken.balanceOf(address(this));
        require(_amount <= contractBalance - totalStaked, "Insufficient excess tokens");

        bool success = mglsToken.transfer(owner, _amount);
        require(success, "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
