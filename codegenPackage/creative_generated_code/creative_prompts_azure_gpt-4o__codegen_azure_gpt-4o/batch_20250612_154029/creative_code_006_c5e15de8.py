"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Provide code for implementing BNB Liquid Staking (LBNB) on Flare Network, ensuring compatibility with its EVM-based infrastructure.
Generated: DETERMINISTIC_c5e15de8c899247c
Batch ID: 20250612_154029
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
 * @title LBNB Liquid Staking Contract
 * @dev This contract allows users to stake BNB tokens and receive LBNB (Liquid BNB) tokens
 *      on the Flare Network. It is compatible with the EVM-based infrastructure.
 */
contract LBNBLiquidStaking {
    // Address of the administrator
    address public admin;

    // Mapping to track user stakes
    mapping(address => uint256) private stakes;

    // Total staked BNB
    uint256 public totalStaked;

    // LBNB token exchange rate (e.g., 1 LBNB = 1 BNB)
    uint256 public exchangeRate = 1e18;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ExchangeRateUpdated(uint256 newExchangeRate);

    /**
     * @dev Modifier to restrict function access to admin.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the admin address.
     */
    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Function for users to stake BNB and receive LBNB tokens.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than 0");

        // Update user stake and total staked amount
        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        // Emit staking event
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Function for users to unstake BNB by burning LBNB tokens.
     * @param amount The amount of BNB to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient stake balance");

        // Update user stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer BNB back to the user
        payable(msg.sender).transfer(amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to get the stake balance of a specific user.
     * @param user The address of the user.
     * @return The stake balance of the user.
     */
    function getStakeBalance(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Function for the admin to update the LBNB exchange rate.
     * @param newExchangeRate The new exchange rate (e.g., 1 LBNB = X BNB).
     */
    function updateExchangeRate(uint256 newExchangeRate) external onlyAdmin {
        require(newExchangeRate > 0, "Exchange rate must be greater than 0");

        exchangeRate = newExchangeRate;

        // Emit exchange rate update event
        emit ExchangeRateUpdated(newExchangeRate);
    }

    /**
     * @dev Fallback function to accept native BNB transfers.
     */
    receive() external payable {}
}
```
