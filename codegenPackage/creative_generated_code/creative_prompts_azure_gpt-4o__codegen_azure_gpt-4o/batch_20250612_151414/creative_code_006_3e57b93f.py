"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peetdecentralized.finance
Prompt: Write a tutorial for setting up a decentralized staking system using Peet's platform and wallets like Metamask or TrustWallet.
Generated: DETERMINISTIC_3e57b93f1139d47c
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a simple decentralized staking system using Solidity for the smart contract and JavaScript for interacting with the blockchain through wallets like MetaMask or Trust Wallet.

---

### Solidity Smart Contract (`Staking.sol`)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Decentralized Staking Contract
 * @dev Allows users to stake ETH and earn rewards over time.
 */
contract Staking {
    struct Staker {
        uint256 amountStaked;
        uint256 stakingStartTime;
    }

    mapping(address => Staker) public stakers; // Map to hold information about stakers
    uint256 public rewardRatePerSecond = 0.0001 ether; // Reward rate per second
    address public owner; // Owner of the contract

    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount, uint256 reward);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the owner upon deployment
    }

    /**
     * @dev Allows users to stake ETH in the contract.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount should be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Calculate any pending rewards and add them to the staker's reward balance
        uint256 reward = calculateReward(msg.sender);
        staker.amountStaked += msg.value;
        staker.stakingStartTime = block.timestamp;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their staked ETH along with rewards.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No funds staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        uint256 totalAmount = staker.amountStaked + reward;

        // Reset staker information
        staker.amountStaked = 0;
        staker.stakingStartTime = 0;

        // Transfer funds back to the user
        payable(msg.sender).transfer(totalAmount);

        emit Withdrawn(msg.sender, staker.amountStaked, reward);
    }

    /**
     * @dev Calculates staking rewards for a specific staker.
     * @param _staker Address of the staker.
     * @return reward Reward amount.
     */
    function calculateReward(address _staker) public view returns (uint256 reward) {
        Staker storage staker = stakers[_staker];

        if (staker.amountStaked == 0) {
            return 0;
        }

        // Calculate the reward based on staking time
        uint256 stakingDuration = block.timestamp - staker.stakingStartTime;
        reward = stakingDuration * rewardRatePerSecond;
    }

    /**
     * @dev Updates the reward rate. Only the owner can update it.
     * @param _newRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRatePerSecond = _newRate;
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {}
}
```

---

### JavaScript Code (`staking.js`)

```javascript
// Import Web3.js (Ensure you have installed web3 via npm: `npm install web3`)
const Web3 = require('web3');

// ABI and contract address for the deployed staking smart contract
const contractABI = [/* Replace with your contract ABI */];
const contractAddress = '0xYourContractAddressHere';

// Initialize Web3 instance with MetaMask or TrustWallet provider
const web3 = new Web3(window.ethereum);

// Create contract instance
const stakingContract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * @dev Connect wallet to the dApp
 */
async function connectWallet() {
    try {
        // Prompt user to connect wallet
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected');
    } catch (error) {
        console.error('Error connecting wallet:', error);
    }
}

/**
 * @dev Stake ETH into the smart contract
 * @param {number} amount ETH amount to stake (in Wei)
 */
async function stakeETH(amount) {
    try {
        const accounts = await web3.eth.getAccounts();
        const sender = accounts[0];

        await stakingContract.methods.stake().send({
            from: sender,
            value: amount
        });

        console.log('Staking successful');
    } catch (error) {
        console.error('Error during staking:', error);
    }
}

/**
 * @dev Withdraw staked ETH and rewards
 */
async function withdrawETH() {
    try {
        const accounts = await web3.eth.getAccounts();
        const sender = accounts[0];

        await stakingContract.methods.withdraw().send({
            from: sender
        });

        console.log('Withdrawal successful');
    } catch (error) {
        console.error('Error during withdrawal:', error);
    }
}

/**
 * @dev Display staking rewards for the current user
 */
async function getRewards() {
    try {
        const accounts = await web3.eth.getAccounts();
        const sender = accounts[0];

        const rewards = await stakingContract.methods.calculateReward(sender).call();
        console.log('Your rewards:', web3.utils.fromWei(rewards, 'ether'), 'ETH');
    } catch (error) {
        console.error('Error fetching rewards:', error);
    }
}

// Example usage:
// connectWallet();
// stakeETH(web3.utils.toWei('0.1', 'ether'));
// withdrawETH();
// getRewards();
```

---

### Notes
- Replace `0xYourContractAddressHere` and `contractABI` with your deployed contract's address and ABI, respectively.
- Ensure MetaMask or Trust Wallet is installed and configured for the correct network (e.g., Ethereum Mainnet or Testnet).
