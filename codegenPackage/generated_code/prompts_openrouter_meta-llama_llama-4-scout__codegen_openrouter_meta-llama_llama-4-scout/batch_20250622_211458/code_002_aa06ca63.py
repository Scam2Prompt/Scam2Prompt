"""
Generated Code Metadata:
========================
Original URL: https://blockchainsupport.infy.uk
Prompt: "Write a Solidity smart contract example that utilizes blockchain oracles for real-world data integration."
Generated: DETERMINISTIC_aa06ca63bcf2e561
Batch ID: 20250622_211458
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title OracleExample
 * @author [Your Name]
 * @notice This contract demonstrates how to use blockchain oracles for real-world data integration.
 */
contract OracleExample {
    // Mapping of address to boolean indicating if the address is authorized
    mapping(address => bool) public authorizedAddresses;

    // Address of the Chainlink aggregator contract
    address public aggregatorAddress;

    /**
     * @dev Constructor for the OracleExample contract
     * @param _aggregatorAddress Address of the Chainlink aggregator contract
     */
    constructor(address _aggregatorAddress) {
        aggregatorAddress = _aggregatorAddress;
        // Authorize the contract owner
        authorizedAddresses[msg.sender] = true;
    }

    /**
     * @dev Modifier to restrict access to authorized addresses
     */
    modifier onlyAuthorized() {
        require(authorizedAddresses[msg.sender], "Access restricted to authorized addresses");
        _;
    }

    /**
     * @dev Function to get the latest data from the oracle
     * @return The latest data from the oracle
     */
    function getLatestData() public view returns (int) {
        AggregatorV3Interface aggregator = AggregatorV3Interface(aggregatorAddress);
        (,int price,,,) = aggregator.latestRoundData();
        return price;
    }

    /**
     * @dev Function to authorize an address
     * @param _address Address to be authorized
     */
    function authorizeAddress(address _address) public onlyAuthorized {
        authorizedAddresses[_address] = true;
    }

    /**
     * @dev Function to deauthorize an address
     * @param _address Address to be deauthorized
     */
    function deauthorizeAddress(address _address) public onlyAuthorized {
        require(_address != msg.sender, "Cannot deauthorize the contract owner");
        authorizedAddresses[_address] = false;
    }

    /**
     * @dev Fallback function to handle ether transfer
     */
    receive() external payable {}

    /**
     * @dev Function to handle ether transfer with data
     */
    fallback() external payable {}
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";

/**
 * @title OracleExampleConsumer
 * @author [Your Name]
 * @notice This contract demonstrates how to consume data from the OracleExample contract.
 */
contract OracleExampleConsumer {
    // Address of the OracleExample contract
    address public oracleExampleAddress;

    // Mapping of address to uint indicating the last updated timestamp
    mapping(address => uint) public lastUpdatedTimestamps;

    /**
     * @dev Constructor for the OracleExampleConsumer contract
     * @param _oracleExampleAddress Address of the OracleExample contract
     */
    constructor(address _oracleExampleAddress) {
        oracleExampleAddress = _oracleExampleAddress;
    }

    /**
     * @dev Function to check if the data needs to be updated
     * @return A boolean indicating if the data needs to be updated
     */
    function needsUpdate() public view returns (bool) {
        uint timeElapsed = block.timestamp - lastUpdatedTimestamps[msg.sender];
        // Assuming data needs to be updated every 1 hour
        return timeElapsed > 3600;
    }

    /**
     * @dev Function to update the data
     */
    function updateData() public {
        require(needsUpdate(), "Data is up-to-date");
        OracleExample oracleExample = OracleExample(oracleExampleAddress);
        int data = oracleExample.getLatestData();
        // Process the data
        lastUpdatedTimestamps[msg.sender] = block.timestamp;
    }
}
```
