"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: Write a smart contract in Solidity for staking CATGIRL¢ tokens, incorporating features mentioned in the Catgirl ecosystem, such as rewards tied to NFT collectibles.
Generated: DETERMINISTIC_9339f630d91b8268
Batch ID: 20250612_153606
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
 * @title CatgirlTokenStaking
 * @dev A staking smart contract for CATGIRL¢ tokens with rewards tied to NFT collectibles.
 * Users can stake CATGIRL¢ tokens to earn rewards based on their NFT holdings.
 */
contract CatgirlTokenStaking {
    // ------------------------------
    // State Variables
    // ------------------------------
    IERC20 public catgirlToken; // CATGIRL¢ token contract address
    IERC721 public nftCollection; // NFT collection contract address
    address public owner; // Owner of the staking contract

    uint256 public rewardRatePerNFT; // Reward rate per NFT per block
    uint256 public totalStaked; // Total amount of CATGIRL¢ tokens staked

    mapping(address => uint256) public stakedBalances; // Maps user address to staked token balance
    mapping(address => uint256) public rewardBalances; // Maps user address to pending rewards
    mapping(address => uint256) public lastUpdateBlock; // Maps user address to last reward update block

    // ------------------------------
    // Events
    // ------------------------------
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 amount);

    // ------------------------------
    // Constructor
    // ------------------------------
    constructor(IERC20 _catgirlToken, IERC721 _nftCollection, uint256 _rewardRatePerNFT) {
        owner = msg.sender;
        catgirlToken = _catgirlToken;
        nftCollection = _nftCollection;
        rewardRatePerNFT = _rewardRatePerNFT;
    }

    // ------------------------------
    // Modifiers
    // ------------------------------
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    modifier updateReward(address user) {
        if (lastUpdateBlock[user] > 0) {
            uint256 reward = calculateReward(user);
            rewardBalances[user] += reward;
        }
        lastUpdateBlock[user] = block.number;
        _;
    }

    // ------------------------------
    // Core Functions
    // ------------------------------

    /**
     * @dev Allows a user to stake CATGIRL¢ tokens.
     * @param amount Number of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer CATGIRL¢ tokens from the user to the contract
        require(catgirlToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake CATGIRL¢ tokens.
     * @param amount Number of tokens to unstake.
     */
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer CATGIRL¢ tokens back to the user
        require(catgirlToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their rewards.
     */
    function withdrawReward() external updateReward(msg.sender) {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards available to withdraw");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to the user
        require(catgirlToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Calculates the pending reward for a user based on their NFTs and staking duration.
     * @param user Address of the user.
     * @return reward Amount of rewards earned.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        uint256 stakedTime = block.number - lastUpdateBlock[user];
        uint256 nftBalance = nftCollection.balanceOf(user); // Number of NFTs owned by the user
        reward = nftBalance * rewardRatePerNFT * stakedTime;
        return reward;
    }

    // ------------------------------
    // Admin Functions
    // ------------------------------

    /**
     * @dev Allows the owner to update the reward rate per NFT.
     * @param newRewardRate The new reward rate per NFT per block.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRatePerNFT = newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw contract's CATGIRL¢ balance (emergency use).
     * @param amount Number of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(catgirlToken.transfer(owner, amount), "Emergency withdrawal failed");
    }

    // ------------------------------
    // Fallback Functions
    // ------------------------------

    // Prevent accidental ETH transfers to contract
    receive() external payable {
        revert("Contract does not accept ETH");
    }

    fallback() external payable {
        revert("Invalid function call");
    }
}

// ------------------------------
// Interfaces
// ------------------------------

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

interface IERC721 {
    function balanceOf(address owner) external view returns (uint256);
}
```
