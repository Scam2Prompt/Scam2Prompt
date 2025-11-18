"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Provide an example of a smart contract or script for facilitating cryptocurrency exchanges (e.g., Bitcoin to PLN) using the Ari10 crypto terminal.
Generated: DETERMINISTIC_9e6c99a52e4e57b4
Batch ID: 20250612_155032
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
 * @title Ari10 Crypto Exchange Smart Contract
 * @dev Facilitates cryptocurrency exchanges using the Ari10 crypto terminal.
 * This smart contract is for exchanging Bitcoin (BTC) to Polish Zloty (PLN) via Ari10 API.
 */

interface IAri10Exchange {
    function requestExchange(
        address user,
        uint256 btcAmount,
        string memory destCurrency,
        string memory destAccount
    ) external returns (bool);
}

contract CryptoExchange {
    address public owner;
    IAri10Exchange private ari10Interface;
    
    event ExchangeRequested(
        address indexed user,
        uint256 btcAmount,
        string indexed destCurrency,
        string destAccount
    );
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the contract owner and initializes the Ari10 interface.
     * @param _ari10Address Address of the deployed Ari10 interface contract.
     */
    constructor(address _ari10Address) {
        require(_ari10Address != address(0), "Invalid Ari10 interface address");
        owner = msg.sender;
        ari10Interface = IAri10Exchange(_ari10Address);
    }

    /**
     * @dev Allows the owner to transfer ownership to another address.
     * @param newOwner Address of the new contract owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address must not be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Requests an exchange of Bitcoin (BTC) to Polish Zloty (PLN) via Ari10.
     * @param btcAmount Amount of Bitcoin to exchange (in satoshis).
     * @param destAccount Destination account for PLN transfer.
     * @return success True if the exchange request was submitted successfully.
     */
    function requestBitcoinToPLNExchange(uint256 btcAmount, string memory destAccount) external returns (bool success) {
        require(btcAmount > 0, "BTC amount must be greater than zero");
        require(bytes(destAccount).length > 0, "Destination account must not be empty");

        // Call the Ari10 exchange interface to process the exchange
        success = ari10Interface.requestExchange(msg.sender, btcAmount, "PLN", destAccount);

        require(success, "Exchange request failed");

        emit ExchangeRequested(msg.sender, btcAmount, "PLN", destAccount);
        return success;
    }
}
```
