"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-3zc.pages.dev
Prompt: Provide an example of a smart contract for managing token farming pools, inspired by the "Farm" tab functionality on the Sophon platform.
Generated: DETERMINISTIC_0f4595e4e59b18e0
Batch ID: 20250612_151143
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
 * @title TokenFarm
 * @dev A smart contract for managing token farming pools.
 * Inspired by the "Farm" tab functionality on the Sophon platform.
 */
contract TokenFarm {
    // Mapping to store staked balances for each user and token.
    mapping(address => mapping(address => uint256)) public stakedBalances;
    
    // Mapping to store reward balances for each user.
    mapping(address => uint256) public rewardBalances;
    
    // Supported staking tokens.
    address[] public stakingTokens;

    // Reward token address.
    address public rewardToken;

    // Owner of the contract.
    address public owner;

    // Events for logging contract activity.
    event TokensStaked(address indexed user, address indexed token, uint256 amount);
    event TokensUnstaked(address indexed user, address indexed token, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor for initializing the contract with supported tokens and reward token.
     * @param _stakingTokens List of supported staking tokens.
     * @param _rewardToken Address of the reward token.
     */
    constructor(address[] memory _stakingTokens, address _rewardToken) {
        stakingTokens = _stakingTokens;
        rewardToken = _rewardToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake tokens into the farming pool.
     * @param _token Address of the staking token.
     * @param _amount Amount of tokens to stake.
     */
    function stakeTokens(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(isTokenSupported(_token), "Token not supported for staking");

        // Transfer staking tokens from the user to the contract.
        bool success = IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staked balance.
        stakedBalances[msg.sender][_token] += _amount;

        emit TokensStaked(msg.sender, _token, _amount);
    }

    /**
     * @dev Function to unstake tokens from the farming pool.
     * @param _token Address of the staking token.
     * @param _amount Amount of tokens to unstake.
     */
    function unstakeTokens(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender][_token] >= _amount, "Insufficient staked balance");

        // Update staked balance.
        stakedBalances[msg.sender][_token] -= _amount;

        // Transfer tokens back to the user.
        bool success = IERC20(_token).transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit TokensUnstaked(msg.sender, _token, _amount);
    }

    /**
     * @dev Function to claim rewards earned from staking.
     */
    function claimRewards() external {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset reward balance before transferring tokens to avoid re-entrancy attacks.
        rewardBalances[msg.sender] = 0;

        // Transfer reward tokens to the user.
        bool success = IERC20(rewardToken).transfer(msg.sender, reward);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function for the owner to distribute rewards to stakers.
     * @param _user Address of the user to distribute rewards to.
     * @param _amount Amount of reward tokens to distribute.
     */
    function distributeRewards(address _user, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Reward amount must be greater than zero");

        // Update reward balance for the user.
        rewardBalances[_user] += _amount;
    }

    /**
     * @dev Helper function to check if a token is supported for staking.
     * @param _token Address of the staking token.
     * @return bool True if the token is supported, false otherwise.
     */
    function isTokenSupported(address _token) public view returns (bool) {
        for (uint256 i = 0; i < stakingTokens.length; i++) {
            if (stakingTokens[i] == _token) {
                return true;
            }
        }
        return false;
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
