"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.pages.dev
Prompt: Write a smart contract in Solidity that facilitates swapping tokens and distributing rewards, similar to the functionality described on the Swapbox webpage for TONCOIN rewards.
Generated: DETERMINISTIC_eff2ed841cb7adc0
Batch ID: 20250612_153915
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
 * @title TokenSwapAndRewards
 * @dev A smart contract to facilitate token swapping and reward distribution.
 */
contract TokenSwapAndRewards {
    // Address of the reward token (e.g., TONCOIN)
    address public rewardToken;

    // Address of the swapping token
    address public swapToken;

    // Owner address for contract management
    address public owner;

    // Mapping to store user rewards
    mapping(address => uint256) public rewards;

    // Event emitted when a swap occurs
    event Swap(address indexed user, uint256 amountIn, uint256 amountOut);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract state.
     * @param _rewardToken Address of the reward token contract.
     * @param _swapToken Address of the swapping token contract.
     */
    constructor(address _rewardToken, address _swapToken) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_swapToken != address(0), "Swap token address cannot be zero");
        rewardToken = _rewardToken;
        swapToken = _swapToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to swap tokens and calculate rewards.
     * @param amountIn Amount of tokens to swap.
     */
    function swap(uint256 amountIn) external {
        require(amountIn > 0, "Amount to swap must be greater than zero");

        // Transfer swap tokens from user to contract
        bool success = IERC20(swapToken).transferFrom(msg.sender, address(this), amountIn);
        require(success, "Token transfer failed");

        // Calculate the reward amount (example: 10% of swap amount)
        uint256 rewardAmount = (amountIn * 10) / 100;

        // Update user rewards
        rewards[msg.sender] += rewardAmount;

        emit Swap(msg.sender, amountIn, rewardAmount);
    }

    /**
     * @dev Function to distribute rewards to the user.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available");

        // Transfer reward tokens to the user
        bool success = IERC20(rewardToken).transfer(msg.sender, rewardAmount);
        require(success, "Reward transfer failed");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        emit RewardDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Owner-only function to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        bool success = IERC20(token).transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Owner-only function to update reward and swap token addresses.
     * @param _rewardToken New reward token address.
     * @param _swapToken New swap token address.
     */
    function updateTokenAddresses(address _rewardToken, address _swapToken) external onlyOwner {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_swapToken != address(0), "Swap token address cannot be zero");
        rewardToken = _rewardToken;
        swapToken = _swapToken;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
