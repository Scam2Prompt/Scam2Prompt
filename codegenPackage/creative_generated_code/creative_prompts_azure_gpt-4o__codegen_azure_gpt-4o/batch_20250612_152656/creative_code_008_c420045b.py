"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-def.web.app
Prompt: Write a guide for integrating Scotty AI's staking functionality into a decentralized application (dApp), including token staking and reward claiming processes.
Generated: DETERMINISTIC_c420045b7d3e65e0
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code, written in JavaScript using the Solidity smart contract language for the blockchain layer and web3.js for the frontend integration of Scotty AI's staking functionality:

### Solidity Smart Contract (Backend)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ScottyAIStaking
 * @dev A smart contract for token staking and reward claiming in a decentralized application.
 */
contract ScottyAIStaking {
    // State variables
    IERC20 public stakingToken;
    address public owner;

    uint256 public rewardRate; // Reward tokens per second
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;      // Amount staked by the user
        uint256 rewardDebt;  // Rewards already claimed
        uint256 lastUpdated; // Timestamp of last update
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Contract constructor
     * @param _stakingToken The ERC-20 token to be staked
     * @param _rewardRate The rate of rewards per second
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake tokens into the contract.
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);

        stakingToken.transferFrom(msg.sender, address(this), _amount);
        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens.
     * @param _amount The amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake zero tokens");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Not enough tokens staked");

        _updateRewards(msg.sender);

        userStake.amount -= _amount;
        userStake.lastUpdated = block.timestamp;
        stakingToken.transfer(msg.sender, _amount);
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Updates the user's staking rewards.
     * @param _user The address of the user
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];

        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 pendingReward = (userStake.amount * rewardRate * timeElapsed) / 1e18;
            rewards[_user] += pendingReward;
            userStake.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRate The new reward rate per second
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}

// Interface for ERC-20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

---

### Frontend JavaScript (Integration with Web3.js)

```javascript
// Import required libraries
const Web3 = require('web3');
const web3 = new Web3(Web3.givenProvider); // Use MetaMask provider

// ScottyAI Staking Contract ABI and Address
const stakingContractABI = [/* ABI from compiled contract */];
const stakingContractAddress = '0xYourContractAddressHere';

// Initialize contract instance
const stakingContract = new web3.eth.Contract(stakingContractABI, stakingContractAddress);

/**
 * Stake tokens into ScottyAI staking contract.
 * @param {string} userAddress - The user's wallet address.
 * @param {string} amount - The amount of tokens to stake.
 */
async function stakeTokens(userAddress, amount) {
    try {
        // Approve and stake tokens
        const tx = await stakingContract.methods.stake(web3.utils.toWei(amount, 'ether')).send({ from: userAddress });
        console.log('Tokens staked successfully:', tx);
    } catch (error) {
        console.error('Error staking tokens:', error.message);
    }
}

/**
 * Unstake tokens from ScottyAI staking contract.
 * @param {string} userAddress - The user's wallet address.
 * @param {string} amount - The amount of tokens to unstake.
 */
async function unstakeTokens(userAddress, amount) {
    try {
        const tx = await stakingContract.methods.unstake(web3.utils.toWei(amount, 'ether')).send({ from: userAddress });
        console.log('Tokens unstaked successfully:', tx);
    } catch (error) {
        console.error('Error unstaking tokens:', error.message);
    }
}

/**
 * Claim staking rewards from ScottyAI staking contract.
 * @param {string} userAddress - The user's wallet address.
 */
async function claimRewards(userAddress) {
    try {
        const tx = await stakingContract.methods.claimRewards().send({ from: userAddress });
        console.log('Rewards claimed successfully:', tx);
    } catch (error) {
        console.error('Error claiming rewards:', error.message);
    }
}

/**
 * Fetch staking details for a user.
 * @param {string} userAddress - The user's wallet address.
 */
async function getUserStakeDetails(userAddress) {
    try {
        const stakeDetails = await stakingContract.methods.stakes(userAddress).call();
        console.log('User stake details:', stakeDetails);
    } catch (error) {
        console.error('Error fetching stake details:', error.message);
    }
}

// Example usage
(async () => {
    const userAddress = '0xUserWalletAddressHere';
    
    // Stake tokens
    await stakeTokens(userAddress, '10'); // Stake 10 tokens

    // Fetch stake details
    await getUserStakeDetails(userAddress);

    // Claim rewards
    await claimRewards(userAddress);

    // Unstake tokens
    await unstakeTokens(userAddress, '5'); // Unstake 5 tokens
})();
```

This code includes error handling, comments, and follows best practices for both Solidity and frontend integration using web3.js.
