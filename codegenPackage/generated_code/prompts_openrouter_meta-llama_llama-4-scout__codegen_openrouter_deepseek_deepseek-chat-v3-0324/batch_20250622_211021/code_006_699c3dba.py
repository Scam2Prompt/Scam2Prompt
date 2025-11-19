"""
Generated Code Metadata:
========================
Original URL: https://app-chainbase.com
Prompt: Write a smart contract that leverages Chainbase's omnichain connectivity, enabling programmable and interoperable data intelligence for decentralized finance (DeFi) use cases.
Generated: DETERMINISTIC_699c3dbae8422c75
Batch ID: 20250622_211021
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title OmnichainDataOracle
 * @dev A smart contract for decentralized cross-chain data intelligence in DeFi applications
 */
contract OmnichainDataOracle is Ownable, Pausable {
    using SafeMath for uint256;

    // Struct to hold cross-chain data with metadata
    struct DataPoint {
        bytes32 dataId;
        uint256 timestamp;
        uint256 chainId;
        bytes data;
        address provider;
    }

    // Mapping from data ID to DataPoint
    mapping(bytes32 => DataPoint) private dataRegistry;

    // Mapping of authorized data providers
    mapping(address => bool) private authorizedProviders;

    // Mapping of supported chain IDs
    mapping(uint256 => bool) private supportedChains;

    // Fee for data queries (in wei)
    uint256 public queryFee;

    // Events
    event DataUpdated(
        bytes32 indexed dataId,
        uint256 timestamp,
        uint256 chainId,
        address provider
    );
    event ProviderAuthorized(address provider);
    event ProviderRevoked(address provider);
    event ChainSupported(uint256 chainId);
    event ChainUnsupported(uint256 chainId);
    event QueryFeeUpdated(uint256 newFee);
    event QueryExecuted(address requester, bytes32 dataId, bytes data);

    /**
     * @dev Constructor initializes the contract with supported chains
     * @param _initialChains Array of chain IDs to support initially
     * @param _initialFee Initial query fee in wei
     */
    constructor(uint256[] memory _initialChains, uint256 _initialFee) {
        queryFee = _initialFee;
        for (uint256 i = 0; i < _initialChains.length; i++) {
            supportedChains[_initialChains[i]] = true;
            emit ChainSupported(_initialChains[i]);
        }
    }

    /**
     * @dev Update or insert data point
     * @param _dataId Unique identifier for the data
     * @param _chainId Source chain ID
     * @param _data The actual data payload
     */
    function updateData(
        bytes32 _dataId,
        uint256 _chainId,
        bytes memory _data
    ) external whenNotPaused {
        require(authorizedProviders[msg.sender], "Unauthorized provider");
        require(supportedChains[_chainId], "Unsupported chain");

        dataRegistry[_dataId] = DataPoint({
            dataId: _dataId,
            timestamp: block.timestamp,
            chainId: _chainId,
            data: _data,
            provider: msg.sender
        });

        emit DataUpdated(_dataId, block.timestamp, _chainId, msg.sender);
    }

    /**
     * @dev Query data by ID
     * @param _dataId Unique identifier for the data
     * @return DataPoint The requested data point
     */
    function queryData(bytes32 _dataId)
        external
        payable
        whenNotPaused
        returns (DataPoint memory)
    {
        require(msg.value >= queryFee, "Insufficient query fee");
        require(dataRegistry[_dataId].timestamp != 0, "Data not found");

        emit QueryExecuted(msg.sender, _dataId, dataRegistry[_dataId].data);
        return dataRegistry[_dataId];
    }

    /**
     * @dev Authorize a new data provider
     * @param _provider Address of the provider to authorize
     */
    function authorizeProvider(address _provider) external onlyOwner {
        authorizedProviders[_provider] = true;
        emit ProviderAuthorized(_provider);
    }

    /**
     * @dev Revoke a data provider's authorization
     * @param _provider Address of the provider to revoke
     */
    function revokeProvider(address _provider) external onlyOwner {
        authorizedProviders[_provider] = false;
        emit ProviderRevoked(_provider);
    }

    /**
     * @dev Add a supported chain
     * @param _chainId Chain ID to support
     */
    function supportChain(uint256 _chainId) external onlyOwner {
        supportedChains[_chainId] = true;
        emit ChainSupported(_chainId);
    }

    /**
     * @dev Remove a supported chain
     * @param _chainId Chain ID to remove support for
     */
    function unsupportChain(uint256 _chainId) external onlyOwner {
        supportedChains[_chainId] = false;
        emit ChainUnsupported(_chainId);
    }

    /**
     * @dev Update the query fee
     * @param _newFee New query fee in wei
     */
    function updateQueryFee(uint256 _newFee) external onlyOwner {
        queryFee = _newFee;
        emit QueryFeeUpdated(_newFee);
    }

    /**
     * @dev Withdraw collected fees
     */
    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Check if an address is an authorized provider
     * @param _provider Address to check
     * @return bool True if authorized
     */
    function isAuthorizedProvider(address _provider)
        external
        view
        returns (bool)
    {
        return authorizedProviders[_provider];
    }

    /**
     * @dev Check if a chain is supported
     * @param _chainId Chain ID to check
     * @return bool True if supported
     */
    function isSupportedChain(uint256 _chainId) external view returns (bool) {
        return supportedChains[_chainId];
    }

    /**
     * @dev Pause contract operations
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
