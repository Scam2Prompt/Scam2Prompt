"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Develop a dapp on Flare Network that utilizes data acquisition from multiple blockchains and Web2 APIs, leveraging the State Connector and enshrined oracles.
Generated: DETERMINISTIC_34fe58a784df4c03
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, as Flare Network is an EVM-compatible blockchain. I'll create a basic DApp that utilizes the State Connector and enshrined oracles to fetch data from multiple blockchains and Web2 APIs.

**DApp Contract**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { StateConnector } from "@flare-network/state-connector/contracts/StateConnector.sol";
import { IStateConnector } from "@flare-network/state-connector/contracts/interfaces/IStateConnector.sol";

/**
 * @title MultiChainDataAggregator
 * @author [Your Name]
 * @notice Aggregates data from multiple blockchains and Web2 APIs using State Connector and enshrined oracles.
 */
contract MultiChainDataAggregator {
    // State Connector instance
    StateConnector public stateConnector;

    // Mapping of blockchain IDs to their respective data
    mapping(uint256 => bytes) public blockchainData;

    // Mapping of Web2 API URLs to their respective data
    mapping(string => bytes) public web2Data;

    /**
     * @param _stateConnectorAddress Address of the State Connector contract
     */
    constructor(address _stateConnectorAddress) {
        stateConnector = StateConnector(_stateConnectorAddress);
    }

    /**
     * @notice Fetch data from another blockchain using State Connector
     * @param _blockchainId ID of the blockchain to fetch data from
     * @param _dataHash Hash of the data to fetch
     */
    function fetchBlockchainData(uint256 _blockchainId, bytes32 _dataHash) public {
        // Get the blockchain data from State Connector
        bytes memory data = stateConnector.getBlockchainData(_blockchainId, _dataHash);

        // Store the data in the mapping
        blockchainData[_blockchainId] = data;
    }

    /**
     * @notice Fetch data from a Web2 API using an enshrined oracle
     * @param _apiUrl URL of the Web2 API to fetch data from
     */
    function fetchWeb2Data(string memory _apiUrl) public {
        // Get the Web2 API data from the enshrined oracle
        bytes memory data = stateConnector.getWeb2Data(_apiUrl);

        // Store the data in the mapping
        web2Data[_apiUrl] = data;
    }

    /**
     * @notice Handle State Connector callback
     * @param _blockchainId ID of the blockchain that triggered the callback
     * @param _dataHash Hash of the data that was fetched
     * @param _data Data that was fetched
     */
    function stateConnectorCallback(uint256 _blockchainId, bytes32 _dataHash, bytes memory _data) external {
        // Only accept callbacks from State Connector
        require(msg.sender == address(stateConnector), "Invalid callback sender");

        // Store the data in the mapping
        blockchainData[_blockchainId] = _data;
    }

    /**
     * @notice Handle Web2 API callback
     * @param _apiUrl URL of the Web2 API that triggered the callback
     * @param _data Data that was fetched
     */
    function web2Callback(string memory _apiUrl, bytes memory _data) external {
        // Only accept callbacks from enshrined oracles
        require(stateConnector.isOracle(msg.sender), "Invalid callback sender");

        // Store the data in the mapping
        web2Data[_apiUrl] = _data;
    }
}
```

**State Connector Mock Contract (for testing purposes)**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IStateConnector } from "@flare-network/state-connector/contracts/interfaces/IStateConnector.sol";

/**
 * @title StateConnectorMock
 * @author [Your Name]
 * @notice Mock implementation of State Connector for testing purposes.
 */
contract StateConnectorMock {
    // Mapping of blockchain IDs to their respective data
    mapping(uint256 => bytes) public blockchainData;

    // Mapping of Web2 API URLs to their respective data
    mapping(string => bytes) public web2Data;

    // Mapping of oracles to their respective status
    mapping(address => bool) public oracles;

    /**
     * @notice Get blockchain data
     * @param _blockchainId ID of the blockchain to fetch data from
     * @param _dataHash Hash of the data to fetch
     */
    function getBlockchainData(uint256 _blockchainId, bytes32 _dataHash) external view returns (bytes memory) {
        return blockchainData[_blockchainId];
    }

    /**
     * @notice Get Web2 API data
     * @param _apiUrl URL of the Web2 API to fetch data from
     */
    function getWeb2Data(string memory _apiUrl) external view returns (bytes memory) {
        return web2Data[_apiUrl];
    }

    /**
     * @notice Check if an address is an oracle
     * @param _oracle Address to check
     */
    function isOracle(address _oracle) external view returns (bool) {
        return oracles[_oracle];
    }

    /**
     * @notice Set blockchain data for testing purposes
     * @param _blockchainId ID of the blockchain to set data for
     * @param _data Data to set
     */
    function setBlockchainData(uint256 _blockchainId, bytes memory _data) external {
        blockchainData[_blockchainId] = _data;
    }

    /**
     * @notice Set Web2 API data for testing purposes
     * @param _apiUrl URL of the Web2 API to set data for
     * @param _data Data to set
     */
    function setWeb2Data(string memory _apiUrl, bytes memory _data) external {
        web2Data[_apiUrl] = _data;
    }

    /**
     * @notice Set oracle status for testing purposes
     * @param _oracle Address of the oracle to set
     * @param _status Status to set
     */
    function setOracle(address _oracle, bool _status) external {
        oracles[_oracle] = _status;
    }
}
```

**Web2 API Oracle Contract (example)**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IStateConnector } from "@flare-network/state-connector/contracts/interfaces/IStateConnector.sol";

/**
 * @title Web2ApiOracle
 * @author [Your Name]
 * @notice Example oracle contract that fetches data from a Web2 API.
 */
contract Web2ApiOracle {
    // Web2 API URL
    string public apiUrl;

    // State Connector instance
    IStateConnector public stateConnector;

    /**
     * @param _apiUrl URL of the Web2 API to fetch data from
     * @param _stateConnectorAddress Address of the State Connector contract
     */
    constructor(string memory _apiUrl, address _stateConnectorAddress) {
        apiUrl = _apiUrl;
        stateConnector = IStateConnector(_stateConnectorAddress);
    }

    /**
     * @notice Fetch data from Web2 API and send it to State Connector
     */
    function fetchData() public {
        // Fetch data from Web2 API
        bytes memory data = fetchDataFromApi(apiUrl);

        // Send data to State Connector
        stateConnector.web2Callback(apiUrl, data);
    }

    /**
     * @notice Fetch data from Web2 API (implementation omitted for brevity)
     * @param _apiUrl URL of the Web2 API to fetch data from
     */
    function fetchDataFromApi(string memory _apiUrl) internal returns (bytes memory) {
        // Implementation omitted for brevity
    }
}
```
