"""
Generated Code Metadata:
========================
Original URL: https://mercury-dusky-pi.vercel.app
Prompt: Design a function in Solidity to interact with a perpetual trading contract on a decentralized exchange, inspired by the "Perpetual Degen and Earn" feature on this platform.
Generated: DETERMINISTIC_a0429e5a5f2a1967
Batch ID: 20250622_211011
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

/**
 * @title PerpetualTradingInteractor
 * @dev A contract to interact with a perpetual trading contract on a decentralized exchange.
 */
contract PerpetualTradingInteractor {
    // Address of the perpetual trading contract
    address public perpetualContract;

    // Event emitted when a trade is executed
    event TradeExecuted(address indexed trader, uint256 amount, bool isLong);

    /**
     * @dev Constructor to initialize the perpetual trading contract address.
     * @param _perpetualContract Address of the perpetual trading contract.
     */
    constructor(address _perpetualContract) {
        require(_perpetualContract != address(0), "Invalid contract address");
        perpetualContract = _perpetualContract;
    }

    /**
     * @dev Function to execute a trade on the perpetual trading contract.
     * @param amount The amount to trade (in wei).
     * @param isLong True for a long position, false for a short position.
     */
    function executeTrade(uint256 amount, bool isLong) external payable {
        require(amount > 0, "Trade amount must be greater than zero");
        require(msg.value == amount, "Insufficient ETH sent for trade");

        // Interact with the perpetual trading contract
        (bool success, ) = perpetualContract.call{value: msg.value}(
            abi.encodeWithSignature("trade(uint256,bool)", amount, isLong)
        );

        // Check if the call was successful
        require(success, "Trade execution failed");

        // Emit the trade event
        emit TradeExecuted(msg.sender, amount, isLong);
    }

    /**
     * @dev Function to update the perpetual trading contract address.
     * @param _newPerpetualContract Address of the new perpetual trading contract.
     */
    function updatePerpetualContract(address _newPerpetualContract) external {
        require(_newPerpetualContract != address(0), "Invalid contract address");
        perpetualContract = _newPerpetualContract;
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any accidentally sent ETH to the contract.
     * @param to Address to send the ETH to.
     */
    function withdrawETH(address payable to) external {
        require(to != address(0), "Invalid address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        to.transfer(balance);
    }
}
```
