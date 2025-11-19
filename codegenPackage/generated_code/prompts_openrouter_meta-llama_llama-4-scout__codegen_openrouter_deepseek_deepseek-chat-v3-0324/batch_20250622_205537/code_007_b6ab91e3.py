"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: "Write a Solidity contract that enables miners to utilize staked energy, represented by eosGAS tokens, to process transactions within the top 20 cryptocurrencies."
Generated: DETERMINISTIC_b6ab91e3746cbbef
Batch ID: 20250622_205537
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MinerEnergyContract
 * @dev A contract that allows miners to stake eosGAS tokens to process transactions
 * for the top 20 cryptocurrencies.
 */
contract MinerEnergyContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Address of the eosGAS token contract
    IERC20 public immutable eosGAS;

    // Mapping of miner addresses to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of supported cryptocurrency IDs (1-20) to their processing rates (eosGAS per transaction)
    mapping(uint8 => uint256) public processingRates;

    // Events
    event Staked(address indexed miner, uint256 amount);
    event Unstaked(address indexed miner, uint256 amount);
    event TransactionProcessed(address indexed miner, uint8 cryptocurrencyId, uint256 eosGASUsed);

    /**
     * @dev Constructor initializes the contract with the eosGAS token address.
     * @param _eosGASAddress Address of the eosGAS token contract.
     */
    constructor(address _eosGASAddress) {
        require(_eosGASAddress != address(0), "Invalid token address");
        eosGAS = IERC20(_eosGASAddress);
    }

    /**
     * @dev Stake eosGAS tokens to participate in transaction processing.
     * @param amount The amount of eosGAS tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        stakedBalances[msg.sender] += amount;
        eosGAS.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake eosGAS tokens.
     * @param amount The amount of eosGAS tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= amount;
        eosGAS.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Process a transaction for a specific cryptocurrency.
     * @param cryptocurrencyId The ID of the cryptocurrency (1-20).
     */
    function processTransaction(uint8 cryptocurrencyId) external nonReentrant {
        require(cryptocurrencyId >= 1 && cryptocurrencyId <= 20, "Invalid cryptocurrency ID");
        uint256 rate = processingRates[cryptocurrencyId];
        require(rate > 0, "Processing rate not set for this cryptocurrency");
        require(stakedBalances[msg.sender] >= rate, "Insufficient staked balance");

        stakedBalances[msg.sender] -= rate;

        emit TransactionProcessed(msg.sender, cryptocurrencyId, rate);
    }

    /**
     * @dev Set the processing rate for a cryptocurrency.
     * @param cryptocurrencyId The ID of the cryptocurrency (1-20).
     * @param rate The amount of eosGAS required to process a transaction.
     */
    function setProcessingRate(uint8 cryptocurrencyId, uint256 rate) external onlyOwner {
        require(cryptocurrencyId >= 1 && cryptocurrencyId <= 20, "Invalid cryptocurrency ID");
        processingRates[cryptocurrencyId] = rate;
    }

    /**
     * @dev Withdraw any accidentally sent ERC20 tokens (except eosGAS).
     * @param tokenAddress Address of the ERC20 token to withdraw.
     * @param amount Amount to withdraw.
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(eosGAS), "Cannot withdraw eosGAS");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
