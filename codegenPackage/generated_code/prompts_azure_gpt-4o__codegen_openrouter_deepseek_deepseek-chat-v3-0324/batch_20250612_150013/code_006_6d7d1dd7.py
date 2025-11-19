"""
Generated Code Metadata:
========================
Original URL: https://precipitateai.web.app
Prompt: Develop a smart contract that interacts with the Precipitate Protocol to enable seamless data exchange between AI services and blockchain nodes.
Generated: DETERMINISTIC_6d7d1dd7a85d62fd
Batch ID: 20250612_150013
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PrecipitateProtocol
 * @dev Smart contract for enabling data exchange between AI services and blockchain nodes
 */
contract PrecipitateProtocol is Ownable, ReentrancyGuard {
    using Address for address payable;

    // Struct to represent a data request
    struct DataRequest {
        address requester;
        string dataType;
        uint256 timestamp;
        uint256 reward;
        bool fulfilled;
    }

    // Struct to represent a data provider
    struct DataProvider {
        address providerAddress;
        string[] supportedDataTypes;
        uint256 reputation;
        bool isActive;
    }

    // Mapping of request IDs to DataRequest
    mapping(uint256 => DataRequest) public dataRequests;

    // Mapping of provider addresses to DataProvider
    mapping(address => DataProvider) public dataProviders;

    // Mapping of data types to providers who support them
    mapping(string => address[]) public dataTypeToProviders;

    // Counter for request IDs
    uint256 public requestCounter;

    // Events
    event DataRequestCreated(
        uint256 indexed requestId,
        address indexed requester,
        string dataType,
        uint256 reward
    );
    event DataRequestFulfilled(
        uint256 indexed requestId,
        address indexed provider,
        string data
    );
    event ProviderRegistered(
        address indexed provider,
        string[] dataTypes
    );
    event ProviderDeregistered(address indexed provider);
    event RewardClaimed(
        address indexed provider,
        uint256 amount
    );

    /**
     * @dev Modifier to check if the caller is a registered provider
     */
    modifier onlyProvider() {
        require(
            dataProviders[msg.sender].isActive,
            "PrecipitateProtocol: Caller is not a registered provider"
        );
        _;
    }

    /**
     * @dev Create a new data request
     * @param dataType The type of data being requested
     */
    function createDataRequest(string memory dataType) external payable nonReentrant {
        require(msg.value > 0, "PrecipitateProtocol: Reward must be greater than 0");
        require(
            dataTypeToProviders[dataType].length > 0,
            "PrecipitateProtocol: No providers for this data type"
        );

        uint256 requestId = requestCounter++;
        dataRequests[requestId] = DataRequest({
            requester: msg.sender,
            dataType: dataType,
            timestamp: block.timestamp,
            reward: msg.value,
            fulfilled: false
        });

        emit DataRequestCreated(requestId, msg.sender, dataType, msg.value);
    }

    /**
     * @dev Fulfill a data request
     * @param requestId The ID of the request to fulfill
     * @param data The data being provided
     */
    function fulfillDataRequest(uint256 requestId, string memory data) external onlyProvider nonReentrant {
        DataRequest storage request = dataRequests[requestId];
        require(
            !request.fulfilled,
            "PrecipitateProtocol: Request already fulfilled"
        );
        require(
            _providerSupportsDataType(msg.sender, request.dataType),
            "PrecipitateProtocol: Provider doesn't support this data type"
        );

        request.fulfilled = true;
        dataProviders[msg.sender].reputation += 1;

        // Transfer reward to provider
        payable(msg.sender).sendValue(request.reward);

        emit DataRequestFulfilled(requestId, msg.sender, data);
    }

    /**
     * @dev Register as a data provider
     * @param dataTypes Array of data types the provider supports
     */
    function registerProvider(string[] memory dataTypes) external {
        require(
            !dataProviders[msg.sender].isActive,
            "PrecipitateProtocol: Provider already registered"
        );

        dataProviders[msg.sender] = DataProvider({
            providerAddress: msg.sender,
            supportedDataTypes: dataTypes,
            reputation: 0,
            isActive: true
        });

        // Update data type to providers mapping
        for (uint256 i = 0; i < dataTypes.length; i++) {
            dataTypeToProviders[dataTypes[i]].push(msg.sender);
        }

        emit ProviderRegistered(msg.sender, dataTypes);
    }

    /**
     * @dev Deregister as a data provider
     */
    function deregisterProvider() external onlyProvider {
        DataProvider storage provider = dataProviders[msg.sender];
        provider.isActive = false;

        // Remove provider from data type mappings
        for (uint256 i = 0; i < provider.supportedDataTypes.length; i++) {
            string memory dataType = provider.supportedDataTypes[i];
            _removeProviderFromDataType(dataType, msg.sender);
        }

        emit ProviderDeregistered(msg.sender);
    }

    /**
     * @dev Internal function to check if provider supports a data type
     * @param provider Address of the provider
     * @param dataType Data type to check
     * @return bool True if provider supports the data type
     */
    function _providerSupportsDataType(address provider, string memory dataType) internal view returns (bool) {
        string[] memory supportedTypes = dataProviders[provider].supportedDataTypes;
        for (uint256 i = 0; i < supportedTypes.length; i++) {
            if (keccak256(bytes(supportedTypes[i])) == keccak256(bytes(dataType))) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Internal function to remove provider from data type mapping
     * @param dataType Data type to remove from
     * @param provider Address of the provider to remove
     */
    function _removeProviderFromDataType(string memory dataType, address provider) internal {
        address[] storage providers = dataTypeToProviders[dataType];
        for (uint256 i = 0; i < providers.length; i++) {
            if (providers[i] == provider) {
                providers[i] = providers[providers.length - 1];
                providers.pop();
                break;
            }
        }
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        payable(owner()).sendValue(address(this).balance);
    }
}
```
