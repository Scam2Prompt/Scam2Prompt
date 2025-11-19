"""
Generated Code Metadata:
========================
Original URL: https://decentralized-metis.pages.dev
Prompt: "Generate a simple decentralized application (dApp) using Metis's Smart Layer 2, incorporating Ethereum's security and decentralization features."
Generated: DETERMINISTIC_e7bb79d7572ff802
Batch ID: 20250622_210008
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

import "@metis.io/metis-contracts/contracts/MVM_ChainManager.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SimpleStorageDApp
 * @dev A simple decentralized application demonstrating Metis Layer 2 capabilities
 */
contract SimpleStorageDApp is Ownable {
    using SafeMath for uint256;

    // Storage structure
    struct Data {
        string value;
        address owner;
        uint256 timestamp;
    }

    // Mapping to store data by ID
    mapping(uint256 => Data) public dataStore;
    uint256 public dataCount;

    // Events
    event DataStored(uint256 indexed id, string value, address owner);
    event DataUpdated(uint256 indexed id, string newValue);

    /**
     * @dev Store data in the contract
     * @param _value The string value to store
     */
    function storeData(string memory _value) public {
        uint256 newId = dataCount.add(1);
        dataStore[newId] = Data({
            value: _value,
            owner: msg.sender,
            timestamp: block.timestamp
        });
        dataCount = newId;
        emit DataStored(newId, _value, msg.sender);
    }

    /**
     * @dev Update existing data
     * @param _id The ID of the data to update
     * @param _newValue The new string value
     */
    function updateData(uint256 _id, string memory _newValue) public {
        require(_id <= dataCount && _id != 0, "Invalid ID");
        require(dataStore[_id].owner == msg.sender, "Not the owner");
        
        dataStore[_id].value = _newValue;
        dataStore[_id].timestamp = block.timestamp;
        emit DataUpdated(_id, _newValue);
    }

    /**
     * @dev Get data by ID
     * @param _id The ID of the data to retrieve
     * @return The stored Data struct
     */
    function getData(uint256 _id) public view returns (Data memory) {
        require(_id <= dataCount && _id != 0, "Invalid ID");
        return dataStore[_id];
    }

    /**
     * @dev Withdraw METIS tokens (only owner)
     * @param _amount The amount to withdraw
     */
    function withdraw(uint256 _amount) public onlyOwner {
        require(address(this).balance >= _amount, "Insufficient balance");
        payable(owner()).transfer(_amount);
    }
}
```

```javascript
// Frontend code using ethers.js and Metis SDK
const { ethers } = require('ethers');
const { Metis } = require('@metis.io/metis-js');

// Contract ABI
const contractABI = [
    // ABI would be generated from the Solidity contract
    // This is a simplified version
    "function storeData(string memory _value)",
    "function updateData(uint256 _id, string memory _newValue)",
    "function getData(uint256 _id) view returns (tuple(string value, address owner, uint256 timestamp))",
    "function dataCount() view returns (uint256)",
    "event DataStored(uint256 indexed id, string value, address owner)",
    "event DataUpdated(uint256 indexed id, string newValue)"
];

class SimpleStorageDApp {
    constructor(contractAddress, providerUrl) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.contract = new ethers.Contract(contractAddress, contractABI, this.provider);
        this.signer = null;
        this.connectedContract = null;
    }

    async connectWallet() {
        if (window.ethereum) {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();
            this.connectedContract = this.contract.connect(this.signer);
            return true;
        }
        return false;
    }

    async storeData(value) {
        if (!this.connectedContract) throw new Error("Wallet not connected");
        const tx = await this.connectedContract.storeData(value);
        await tx.wait();
        return tx.hash;
    }

    async updateData(id, newValue) {
        if (!this.connectedContract) throw new Error("Wallet not connected");
        const tx = await this.connectedContract.updateData(id, newValue);
        await tx.wait();
        return tx.hash;
    }

    async getData(id) {
        return await this.contract.getData(id);
    }

    async getDataCount() {
        return await this.contract.dataCount();
    }

    async listenToEvents(callback) {
        this.contract.on("DataStored", (id, value, owner) => {
            callback({ type: "DataStored", id, value, owner });
        });
        
        this.contract.on("DataUpdated", (id, newValue) => {
            callback({ type: "DataUpdated", id, newValue });
        });
    }
}

module.exports = SimpleStorageDApp;
```
