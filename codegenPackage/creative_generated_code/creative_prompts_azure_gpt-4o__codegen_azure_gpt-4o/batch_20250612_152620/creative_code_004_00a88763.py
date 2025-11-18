"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orchaii.web.app
Prompt: Write a smart contract that interacts with Orchai's Auto Trader feature to implement automatic investment strategies based on real-time market data.
Generated: DETERMINISTIC_00a887639a117c56
Batch ID: 20250612_152620
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
 * @title AutoTraderInvestmentContract
 * @dev A smart contract to interact with Orchai's Auto Trader feature for automatic investment strategies
 */
contract AutoTraderInvestmentContract {
    // Orchai Auto Trader contract address
    address public orchaiAutoTrader;

    // Owner of the contract
    address public owner;

    // Event emitted when an investment strategy is executed
    event InvestmentExecuted(address indexed user, uint256 amount, string strategy, uint256 timestamp);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Orchai Auto Trader address.
     * @param _orchaiAutoTrader Address of the Orchai Auto Trader contract
     */
    constructor(address _orchaiAutoTrader) {
        require(_orchaiAutoTrader != address(0), "Invalid Orchai Auto Trader address");
        orchaiAutoTrader = _orchaiAutoTrader;
        owner = msg.sender;
    }

    /**
     * @dev Function to update the Orchai Auto Trader contract address.
     * @param _newAddress New address of the Orchai Auto Trader contract
     */
    function updateOrchaiAutoTraderAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        orchaiAutoTrader = _newAddress;
    }

    /**
     * @dev Function to execute an investment strategy using the Orchai Auto Trader feature.
     * @param amount The amount to invest
     * @param strategy The name of the investment strategy (e.g., "Strategy1", "Strategy2")
     */
    function executeInvestment(uint256 amount, string calldata strategy) external {
        require(amount > 0, "Investment amount must be greater than zero");
        require(bytes(strategy).length > 0, "Investment strategy cannot be empty");

        // Call Orchai Auto Trader to execute the investment strategy
        (bool success, ) = orchaiAutoTrader.call(
            abi.encodeWithSignature("executeStrategy(address,uint256,string)", msg.sender, amount, strategy)
        );

        // Ensure the call is successful
        require(success, "Investment execution failed");

        // Emit the event for successful execution
        emit InvestmentExecuted(msg.sender, amount, strategy, block.timestamp);
    }

    /**
     * @dev Fallback function to handle unexpected ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Fallback function to handle unexpected function calls.
     */
    fallback() external payable {
        revert("Invalid function call");
    }
}
```
