"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate Solidity code for a smart contract that implements the "Stake-to-Mine" mechanism, where users stake BTCMTX tokens to earn non-transferable mining credits that can be burned for Bitcoin cloud mining power.
Generated: DETERMINISTIC_1c186e1408c93e4e
Batch ID: 20250612_151648
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
 * @title StakeToMine
 * @dev A smart contract for staking BTCMTX tokens to earn non-transferable mining credits
 *      that can be burned for Bitcoin cloud mining power.
 */
interface IBTCMTX {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakeToMine {
    // Address of the BTCMTX token contract
    IBTCMTX public btcmtxToken;

    // Mapping of user address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to their mining credits
    mapping(address => uint256) public miningCredits;

    // Event emitted when a user stakes tokens
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user burns mining credits for mining power
    event MiningCreditsBurned(address indexed user, uint256 amount);

    // Constructor to set the BTCMTX token contract address
    constructor(address _btcmtxTokenAddress) {
        require(_btcmtxTokenAddress != address(0), "Invalid BTCMTX token address");
        btcmtxToken = IBTCMTX(_btcmtxTokenAddress);
    }

    /**
     * @dev Stake BTCMTX tokens to earn mining credits.
     * @param amount The number of BTCMTX tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer BTCMTX tokens from the user to the contract
        bool success = btcmtxToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's staked balance and mining credits
        stakedBalances[msg.sender] += amount;
        miningCredits[msg.sender] += calculateMiningCredits(amount);

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Burn mining credits to claim Bitcoin cloud mining power.
     * @param amount The number of mining credits to burn.
     */
    function burnMiningCredits(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(miningCredits[msg.sender] >= amount, "Insufficient mining credits");

        // Deduct the mining credits from the user's balance
        miningCredits[msg.sender] -= amount;

        emit MiningCreditsBurned(msg.sender, amount);

        // Logic to provide Bitcoin cloud mining power can be implemented here
        // (e.g., interacting with off-chain systems or third-party services).
    }

    /**
     * @dev Calculate mining credits based on staked tokens.
     * @param amount The number of BTCMTX tokens staked.
     * @return The number of mining credits earned.
     */
    function calculateMiningCredits(uint256 amount) internal pure returns (uint256) {
        // Example calculation: 1 BTCMTX token = 10 mining credits
        return amount * 10;
    }

    /**
     * @dev Unstake tokens. Allows user to retrieve their staked BTCMTX tokens.
     */
    function unstakeTokens() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens found");

        // Reset user's staked balance and mining credits
        stakedBalances[msg.sender] = 0;
        miningCredits[msg.sender] = 0;

        // Transfer BTCMTX tokens back to the user
        bool success = btcmtxToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");
    }
}
```
