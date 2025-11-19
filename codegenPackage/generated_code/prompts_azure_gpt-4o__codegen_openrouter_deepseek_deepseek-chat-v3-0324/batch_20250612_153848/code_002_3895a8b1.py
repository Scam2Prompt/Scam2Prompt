"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Implement a Web3 application that utilizes Flare's decentralized data feeds to trustlessly trigger smart contracts using data from Web2 APIs.
Generated: DETERMINISTIC_3895a8b1a7d7b87f
Batch ID: 20250612_153848
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

// Import necessary interfaces from Flare's FTSO system
import "@flarenetwork/flare-periphery-contracts/coston/implementation/FtsoRegistry.sol";
import "@flarenetwork/flare-periphery-contracts/coston/implementation/Ftso.sol";
import "@flarenetwork/flare-periphery-contracts/coston/implementation/PriceSubmitter.sol";

contract Web3Trigger {
    // Flare FTSO registry contract
    FtsoRegistry public ftsoRegistry;
    
    // Event to log trigger execution
    event TriggerExecuted(
        address indexed contractAddress,
        bytes4 indexed functionSelector,
        uint256 indexed timestamp,
        uint256 price
    );

    /**
     * @dev Constructor initializes the FTSO registry
     * @param _ftsoRegistryAddress Address of the Flare FTSO registry contract
     */
    constructor(address _ftsoRegistryAddress) {
        require(_ftsoRegistryAddress != address(0), "Invalid registry address");
        ftsoRegistry = FtsoRegistry(_ftsoRegistryAddress);
    }

    /**
     * @dev Checks price feed and triggers target contract if conditions are met
     * @param _symbol The symbol of the price feed (e.g., "BTC")
     * @param _threshold The price threshold to trigger the action
     * @param _targetContract The address of the contract to trigger
     * @param _functionSelector The function selector to call on the target contract
     * @param _data Additional data to pass to the target function
     */
    function checkAndTrigger(
        string memory _symbol,
        uint256 _threshold,
        address _targetContract,
        bytes4 _functionSelector,
        bytes memory _data
    ) external {
        require(_targetContract != address(0), "Invalid target contract");
        require(_functionSelector != bytes4(0), "Invalid function selector");

        // Get the FTSO contract for the given symbol
        IFtso ftso = ftsoRegistry.getFtso(_symbol);
        require(address(ftso) != address(0), "FTSO not found for symbol");

        // Get the current price
        (uint256 price, ) = ftso.getCurrentPrice();
        require(price > 0, "Invalid price received");

        // Check if price meets threshold
        if (price >= _threshold) {
            // Prepare full calldata
            bytes memory callData = abi.encodePacked(_functionSelector, _data);
            
            // Execute the call
            (bool success, ) = _targetContract.call(callData);
            require(success, "Target contract call failed");

            emit TriggerExecuted(_targetContract, _functionSelector, block.timestamp, price);
        }
    }

    /**
     * @dev Gets the current price for a given symbol
     * @param _symbol The symbol to query
     * @return price The current price
     */
    function getCurrentPrice(string memory _symbol) external view returns (uint256 price) {
        IFtso ftso = ftsoRegistry.getFtso(_symbol);
        require(address(ftso) != address(0), "FTSO not found for symbol");
        (price, ) = ftso.getCurrentPrice();
    }
}
```

```javascript
// Web3 frontend interaction code
import Web3 from 'web3';
import Web3TriggerABI from './Web3TriggerABI.json';

const web3 = new Web3(window.ethereum);
const TRIGGER_CONTRACT_ADDRESS = "0x..."; // Deployed contract address

export class Web3TriggerClient {
    constructor() {
        this.triggerContract = new web3.eth.Contract(
            Web3TriggerABI,
            TRIGGER_CONTRACT_ADDRESS
        );
    }

    /**
     * Setup price trigger
     * @param {string} symbol - Price feed symbol (e.g. "BTC")
     * @param {number} threshold - Price threshold to trigger
     * @param {string} targetContract - Address of contract to trigger
     * @param {string} functionSignature - Function signature (e.g. "transfer(address,uint256)")
     * @param {Array} params - Parameters for the target function
     * @returns {Promise} Transaction receipt
     */
    async setupTrigger(
        symbol,
        threshold,
        targetContract,
        functionSignature,
        params
    ) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const functionSelector = web3.eth.abi.encodeFunctionSignature(functionSignature);
            const encodedParams = web3.eth.abi.encodeParameters(
                functionSignature.split('(')[1].split(')')[0].split(','),
                params
            );
            
            return await this.triggerContract.methods
                .checkAndTrigger(
                    symbol,
                    threshold,
                    targetContract,
                    functionSelector,
                    encodedParams
                )
                .send({ from: accounts[0] });
        } catch (error) {
            console.error("Trigger setup failed:", error);
            throw error;
        }
    }

    /**
     * Get current price for a symbol
     * @param {string} symbol - Price feed symbol
     * @returns {Promise<number>} Current price
     */
    async getCurrentPrice(symbol) {
        try {
            return await this.triggerContract.methods
                .getCurrentPrice(symbol)
                .call();
        } catch (error) {
            console.error("Price fetch failed:", error);
            throw error;
        }
    }
}
```

```javascript
// Example test script using Hardhat
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Web3Trigger", function () {
  let Web3Trigger, trigger, owner, addr1;

  beforeEach(async function () {
    [owner, addr1] = await ethers.getSigners();
    
    // Mock FTSO Registry
    const FtsoRegistry = await ethers.getContractFactory("FtsoRegistry");
    const ftsoRegistry = await FtsoRegistry.deploy();
    await ftsoRegistry.deployed();

    // Deploy our trigger contract
    Web3Trigger = await ethers.getContractFactory("Web3Trigger");
    trigger = await Web3Trigger.deploy(ftsoRegistry.address);
    await trigger.deployed();
  });

  it("Should get current price", async function () {
    // Test would need mock FTSO setup here
    // const price = await trigger.getCurrentPrice("BTC");
    // expect(price).to.be.gt(0);
  });

  it("Should reject invalid target contract", async function () {
    await expect(
      trigger.checkAndTrigger(
        "BTC",
        10000,
        ethers.constants.AddressZero,
        "0x12345678",
        "0x"
      )
    ).to.be.revertedWith("Invalid target contract");
  });
});
```
