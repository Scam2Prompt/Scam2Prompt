"""
Generated Code Metadata:
========================
Original URL: https://connectsflrsync.online
Prompt: Develop a trustless exchange on Flare Network that utilizes its EVM+ compatibility and integrates data from external sources using the State Connector.
Generated: DETERMINISTIC_612caa0d2856cb2b
Batch ID: 20250612_154029
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@flarenetwork/state-connector/StateConnector.sol";

// TrustlessExchange contract
contract TrustlessExchange is Ownable {
    // State variables
    StateConnector public stateConnector; // State Connector instance
    mapping(address => mapping(address => uint256)) public userBalances; // User balances for each token

    // Events
    event ExchangeExecuted(address indexed user, address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);
    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);

    // Constructor to initialize the State Connector
    constructor(address _stateConnector) {
        require(_stateConnector != address(0), "Invalid State Connector address");
        stateConnector = StateConnector(_stateConnector);
    }

    // Deposit function to allow users to deposit tokens into the exchange
    function deposit(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        userBalances[msg.sender][token] += amount;
        emit Deposit(msg.sender, token, amount);
    }

    // Withdraw function to allow users to withdraw tokens from the exchange
    function withdraw(address token, uint256 amount) external {
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");

        userBalances[msg.sender][token] -= amount;
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
        emit Withdraw(msg.sender, token, amount);
    }

    // Exchange function to swap tokens using external data from the State Connector
    function exchange(address fromToken, address toToken, uint256 amountIn) external {
        require(userBalances[msg.sender][fromToken] >= amountIn, "Insufficient balance for exchange");

        // Fetch external price data using State Connector
        uint256 amountOut = getExchangeRate(fromToken, toToken, amountIn);
        require(amountOut > 0, "Invalid exchange rate");

        // Update user balances
        userBalances[msg.sender][fromToken] -= amountIn;
        userBalances[msg.sender][toToken] += amountOut;

        emit ExchangeExecuted(msg.sender, fromToken, toToken, amountIn, amountOut);
    }

    // Internal function to get the exchange rate from the State Connector
    function getExchangeRate(address fromToken, address toToken, uint256 amountIn) internal view returns (uint256) {
        // Placeholder for actual implementation to fetch data from State Connector
        // This should include logic to interact with the State Connector and retrieve the price
        // For now, we return a mock value
        return amountIn; // Mock exchange rate (1:1 for demonstration)
    }

    // Function to set a new State Connector address (only owner)
    function setStateConnector(address _stateConnector) external onlyOwner {
        require(_stateConnector != address(0), "Invalid State Connector address");
        stateConnector = StateConnector(_stateConnector);
    }
}
```
