"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoins-io.web.app
Prompt: Create a smart contract using Ethereum's Web3.js library to manage the tokenomics of Green Bitcoin ($GBTC), including the 40% presale allocation and 27.50% staking rewards.
Generated: DETERMINISTIC_77c21bef3d5e6ef3
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract for managing Green Bitcoin ($GBTC) tokenomics with presale allocation and staking rewards:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract GreenBitcoin is ERC20, Ownable, Pausable {
    // Token distribution percentages
    uint256 public constant PRESALE_PERCENT = 40;
    uint256 public constant STAKING_PERCENT = 27.5 * 10; // Adjusted for decimal precision
    uint256 public constant LIQUIDITY_PERCENT = 15;
    uint256 public constant TEAM_PERCENT = 10;
    uint256 public constant MARKETING_PERCENT = 7.5 * 10; // Adjusted for decimal precision

    // Addresses for allocations
    address public presaleAddress;
    address public stakingAddress;
    address public liquidityAddress;
    address public teamAddress;
    address public marketingAddress;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens

    // Staking rewards tracking
    uint256 public stakingRewardsReleased;
    uint256 public stakingRewardsCap;

    // Events
    event PresaleAllocated(address indexed presaleContract, uint256 amount);
    event StakingRewardsAllocated(address indexed stakingContract, uint256 amount);
    event LiquidityProvided(address indexed liquidityPool, uint256 amount);
    event TeamTokensReleased(address indexed teamWallet, uint256 amount);
    event MarketingTokensReleased(address indexed marketingWallet, uint256 amount);

    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _liquidityAddress,
        address _teamAddress,
        address _marketingAddress
    ) ERC20("Green Bitcoin", "GBTC") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;

        stakingRewardsCap = (TOTAL_SUPPLY * STAKING_PERCENT) / 1000; // Using 1000 for decimal adjustment

        // Mint initial allocations
        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_PERCENT) / 100);
        _mint(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 100);
        _mint(teamAddress, (TOTAL_SUPPLY * TEAM_PERCENT) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENT) / 1000); // Using 1000 for decimal adjustment

        emit PresaleAllocated(presaleAddress, (TOTAL_SUPPLY * PRESALE_PERCENT) / 100);
        emit LiquidityProvided(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 100);
        emit TeamTokensReleased(teamAddress, (TOTAL_SUPPLY * TEAM_PERCENT) / 100);
        emit MarketingTokensReleased(marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENT) / 1000);
    }

    /**
     * @dev Release staking rewards to the staking contract
     * @param amount Amount of tokens to release
     */
    function releaseStakingRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingRewardsReleased + amount <= stakingRewardsCap, "Exceeds staking rewards cap");

        stakingRewardsReleased += amount;
        _mint(stakingAddress, amount);

        emit StakingRewardsAllocated(stakingAddress, amount);
    }

    /**
     * @dev Update staking contract address
     * @param newStakingAddress New staking contract address
     */
    function updateStakingAddress(address newStakingAddress) external onlyOwner {
        require(newStakingAddress != address(0), "Staking address cannot be zero");
        stakingAddress = newStakingAddress;
    }

    /**
     * @dev Update presale contract address
     * @param newPresaleAddress New presale contract address
     */
    function updatePresaleAddress(address newPresaleAddress) external onlyOwner {
        require(newPresaleAddress != address(0), "Presale address cannot be zero");
        presaleAddress = newPresaleAddress;
    }

    /**
     * @dev Pause token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Get remaining staking rewards
     */
    function getRemainingStakingRewards() external view returns (uint256) {
        return stakingRewardsCap - stakingRewardsReleased;
    }
}
```

And here's a JavaScript file using Web3.js to interact with the contract:

```javascript
const Web3 = require('web3');
const contractAbi = require('./GreenBitcoinABI.json');

class GreenBitcoinManager {
    constructor(web3Provider, contractAddress) {
        this.web3 = new Web3(web3Provider);
        this.contract = new this.web3.eth.Contract(contractAbi, contractAddress);
    }

    /**
     * Release staking rewards
     * @param {string} ownerAddress - Address of the contract owner
     * @param {string} privateKey - Private key of the owner
     * @param {number} amount - Amount of tokens to release
     * @returns {Promise} Transaction receipt
     */
    async releaseStakingRewards(ownerAddress, privateKey, amount) {
        try {
            const txData = this.contract.methods.releaseStakingRewards(amount).encodeABI();
            const gasEstimate = await this.contract.methods.releaseStakingRewards(amount).estimateGas({ from: ownerAddress });
            
            const tx = {
                from: ownerAddress,
                to: this.contract.options.address,
                data: txData,
                gas: gasEstimate,
            };
            
            const signedTx = await this.web3.eth.accounts.signTransaction(tx, privateKey);
            return await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        } catch (error) {
            console.error('Error releasing staking rewards:', error);
            throw error;
        }
    }

    /**
     * Get remaining staking rewards
     * @returns {Promise<number>} Remaining staking rewards
     */
    async getRemainingStakingRewards() {
        try {
            return await this.contract.methods.getRemainingStakingRewards().call();
        } catch (error) {
            console.error('Error getting remaining staking rewards:', error);
            throw error;
        }
    }

    /**
     * Update staking address
     * @param {string} ownerAddress - Address of the contract owner
     * @param {string} privateKey - Private key of the owner
     * @param {string} newStakingAddress - New staking contract address
     * @returns {Promise} Transaction receipt
     */
    async updateStakingAddress(ownerAddress, privateKey, newStakingAddress) {
        try {
            const txData = this.contract.methods.updateStakingAddress(newStakingAddress).encodeABI();
            const gasEstimate = await this.contract.methods.updateStakingAddress(newStakingAddress).estimateGas({ from: ownerAddress });
            
            const tx = {
                from: ownerAddress,
                to: this.contract.options.address,
                data: txData,
                gas: gasEstimate,
            };
            
            const signedTx = await this.web3.eth.accounts.signTransaction(tx, privateKey);
            return await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        } catch (error) {
            console.error('Error updating staking address:', error);
            throw error;
        }
    }

    /**
     * Get token balance
     * @param {string
