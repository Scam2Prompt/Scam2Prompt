"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Generate a smart contract code on Flare that triggers using data from Web2 APIs and the Flare Time Series Oracle (FTSO).
Generated: DETERMINISTIC_2383e012e0b684cc
Batch ID: 20250622_212621
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

import "@flarenetwork/flare-contracts/contracts/ftso/user/IFtso.sol";
import "@flarenetwork/flare-contracts/contracts/ftso/user/IFtsoRegistry.sol";
import "@flarenetwork/flare-contracts/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Web2Trigger is Ownable {
    using Address for address;

    IFtsoRegistry public ftsoRegistry;
    address public web2DataProvider;
    mapping(string => uint256) public lastTriggered;

    event TriggerExecuted(string indexed apiEndpoint, uint256 price, uint256 timestamp);

    constructor(address _ftsoRegistry, address _web2DataProvider) {
        require(_ftsoRegistry != address(0), "Invalid FTSO registry address");
        require(_web2DataProvider != address(0), "Invalid Web2 provider address");
        ftsoRegistry = IFtsoRegistry(_ftsoRegistry);
        web2DataProvider = _web2DataProvider;
    }

    function setWeb2DataProvider(address _web2DataProvider) external onlyOwner {
        require(_web2DataProvider != address(0), "Invalid Web2 provider address");
        web2DataProvider = _web2DataProvider;
    }

    function checkAndTrigger(
        string memory apiEndpoint,
        string memory symbol,
        uint256 threshold,
        uint256 cooldown
    ) external {
        require(bytes(apiEndpoint).length > 0, "Empty API endpoint");
        require(bytes(symbol).length > 0, "Empty symbol");
        require(threshold > 0, "Threshold must be positive");

        // Check cooldown period
        require(
            block.timestamp >= lastTriggered[apiEndpoint] + cooldown,
            "Cooldown period not elapsed"
        );

        // Get FTSO price
        IFtso ftso = ftsoRegistry.getFtso(symbol);
        require(address(ftso) != address(0), "FTSO not found for symbol");
        (uint256 price, ) = ftso.getCurrentPrice();

        // Simulate Web2 API call (in production this would be an oracle)
        uint256 web2Value = _simulateWeb2Call(apiEndpoint);

        // Check trigger condition
        if (web2Value >= threshold) {
            lastTriggered[apiEndpoint] = block.timestamp;
            emit TriggerExecuted(apiEndpoint, price, block.timestamp);
        }
    }

    function _simulateWeb2Call(string memory apiEndpoint) internal view returns (uint256) {
        // In a real implementation, this would call an oracle contract
        // that fetches data from Web2 APIs
        require(web2DataProvider.isContract(), "Web2 provider not a contract");
        
        // Mock implementation - returns a pseudo-random value based on the endpoint
        return uint256(keccak256(abi.encodePacked(apiEndpoint, block.timestamp))) % 1000;
    }

    function getFtsoPrice(string memory symbol) external view returns (uint256) {
        IFtso ftso = ftsoRegistry.getFtso(symbol);
        require(address(ftso) != address(0), "FTSO not found for symbol");
        (uint256 price, ) = ftso.getCurrentPrice();
        return price;
    }
}
```
