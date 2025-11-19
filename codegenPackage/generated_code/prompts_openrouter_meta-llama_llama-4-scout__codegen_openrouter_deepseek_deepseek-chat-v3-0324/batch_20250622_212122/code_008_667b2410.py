"""
Generated Code Metadata:
========================
Original URL: https://aave.network
Prompt: "What are the key considerations for deploying a DeFi application on multiple EVM-compatible networks using Aave Protocol?"
Generated: DETERMINISTIC_667b24102d26d264
Batch ID: 20250622_212122
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

import "@aave/core-v3/contracts/interfaces/IPool.sol";
import "@aave/core-v3/contracts/interfaces/IPoolAddressesProvider.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MultiChainDeFiDeployer
 * @notice A contract for deploying and managing DeFi applications across multiple EVM-compatible networks using Aave Protocol
 * @dev Handles cross-chain deployments and ensures consistent configuration across networks
 */
contract MultiChainDeFiDeployer is Ownable, ReentrancyGuard {
    // Mapping to track deployed contracts across different chains
    mapping(uint256 => address) public chainIdToDeployment;
    
    // Mapping to store Aave Pool Address Providers for different networks
    mapping(uint256 => address) public chainIdToAaveProvider;
    
    // Supported networks configuration
    struct NetworkConfig {
        uint256 chainId;
        address aaveProviderAddress;
        bool isSupported;
    }
    
    NetworkConfig[] public supportedNetworks;
    
    event DeploymentCreated(uint256 chainId, address deploymentAddress);
    event NetworkAdded(uint256 chainId, address aaveProviderAddress);
    event NetworkRemoved(uint256 chainId);
    
    /**
     * @dev Initialize with initial supported networks
     * @param initialNetworks Array of initial network configurations
     */
    constructor(NetworkConfig[] memory initialNetworks) {
        for (uint i = 0; i < initialNetworks.length; i++) {
            _addSupportedNetwork(
                initialNetworks[i].chainId,
                initialNetworks[i].aaveProviderAddress
            );
        }
    }
    
    /**
     * @dev Add a supported network with its Aave provider
     * @param chainId The chain ID of the network
     * @param aaveProviderAddress The address of Aave's PoolAddressesProvider for this network
     */
    function addSupportedNetwork(uint256 chainId, address aaveProviderAddress) external onlyOwner {
        _addSupportedNetwork(chainId, aaveProviderAddress);
    }
    
    function _addSupportedNetwork(uint256 chainId, address aaveProviderAddress) internal {
        require(aaveProviderAddress != address(0), "Invalid Aave provider address");
        require(chainIdToAaveProvider[chainId] == address(0), "Network already supported");
        
        chainIdToAaveProvider[chainId] = aaveProviderAddress;
        supportedNetworks.push(NetworkConfig({
            chainId: chainId,
            aaveProviderAddress: aaveProviderAddress,
            isSupported: true
        }));
        
        emit NetworkAdded(chainId, aaveProviderAddress);
    }
    
    /**
     * @dev Remove a supported network
     * @param chainId The chain ID of the network to remove
     */
    function removeSupportedNetwork(uint256 chainId) external onlyOwner {
        require(chainIdToAaveProvider[chainId] != address(0), "Network not supported");
        
        delete chainIdToAaveProvider[chainId];
        
        for (uint i = 0; i < supportedNetworks.length; i++) {
            if (supportedNetworks[i].chainId == chainId) {
                supportedNetworks[i].isSupported = false;
                break;
            }
        }
        
        emit NetworkRemoved(chainId);
    }
    
    /**
     * @dev Deploy a new instance on a specific network
     * @param chainId The chain ID to deploy to
     * @param implementation The address of the implementation contract
     */
    function deployOnNetwork(uint256 chainId, address implementation) external onlyOwner nonReentrant {
        require(chainIdToAaveProvider[chainId] != address(0), "Network not supported");
        require(implementation != address(0), "Invalid implementation address");
        require(chainIdToDeployment[chainId] == address(0), "Already deployed on this network");
        
        // In a real implementation, you would deploy your contract here
        // This is a placeholder for the deployment logic
        address deployedAddress = _deployContract(chainId, implementation);
        
        chainIdToDeployment[chainId] = deployedAddress;
        emit DeploymentCreated(chainId, deployedAddress);
    }
    
    /**
     * @dev Internal function to handle contract deployment
     * @param chainId The chain ID to deploy to
     * @param implementation The implementation address
     * @return The address of the deployed contract
     */
    function _deployContract(uint256 chainId, address implementation) internal virtual returns (address) {
        // This would be replaced with actual deployment logic
        // For demonstration, we return the implementation address
        return implementation;
    }
    
    /**
     * @dev Get the Aave Pool address for a specific network
     * @param chainId The chain ID to query
     * @return The address of the Aave Pool
     */
    function getAavePool(uint256 chainId) public view returns (address) {
        address provider = chainIdToAaveProvider[chainId];
        require(provider != address(0), "Network not supported");
        
        return IPoolAddressesProvider(provider).getPool();
    }
    
    /**
     * @dev Check if a network is supported
     * @param chainId The chain ID to check
     * @return True if the network is supported
     */
    function isNetworkSupported(uint256 chainId) public view returns (bool) {
        return chainIdToAaveProvider[chainId] != address(0);
    }
    
    /**
     * @dev Get all supported networks
     * @return Array of supported network configurations
     */
    function getAllSupportedNetworks() external view returns (NetworkConfig[] memory) {
        return supportedNetworks;
    }
}
```
