"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Create a Solidity contract that facilitates the migration of solo Ethereum validators to Rocket Pool, converting 32 ETH validators to 8 ETH validators. Include functionality for interacting with Rocket Pool's migration tools.
Generated: DETERMINISTIC_a7b86ac6a6ae8c36
Batch ID: 20250612_153821
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IRocketStorage {
    function getAddress(bytes32 _key) external view returns (address);
}

interface IRocketDepositPool {
    function deposit() external payable;
}

interface IRocketTokenRETH {
    function getEthValue(uint256 _rethAmount) external view returns (uint256);
    function getRethValue(uint256 _ethAmount) external view returns (uint256);
}

contract ValidatorMigration is Ownable, ReentrancyGuard {
    IRocketStorage public rocketStorage;
    IERC20 public rETH;

    uint256 public constant REQUIRED_ETH = 32 ether;
    uint256 public constant MINI_POOL_ETH = 8 ether;

    event MigrationStarted(address indexed user, uint256 amount);
    event DepositCompleted(address indexed user, uint256 rEthReceived);
    event Withdrawn(address indexed user, uint256 amount);

    constructor(address _rocketStorageAddress) {
        rocketStorage = IRocketStorage(_rocketStorageAddress);
        _setRocketPoolContracts();
    }

    function _setRocketPoolContracts() private {
        bytes32 depositPoolKey = keccak256(abi.encodePacked("contract.address", "rocketDepositPool"));
        address depositPoolAddress = rocketStorage.getAddress(depositPoolKey);
        require(depositPoolAddress != address(0), "RocketPool deposit pool not found");

        bytes32 rethKey = keccak256(abi.encodePacked("contract.address", "rocketTokenRETH"));
        address rethAddress = rocketStorage.getAddress(rethKey);
        require(rethAddress != address(0), "RocketPool rETH token not found");
        rETH = IERC20(rethAddress);
    }

    function migrateToRocketPool() external payable nonReentrant {
        require(msg.value == REQUIRED_ETH, "Exactly 32 ETH required");
        require(address(this).balance >= REQUIRED_ETH, "Insufficient contract balance");

        // Convert 32 ETH to 4x 8 ETH mini-pools
        for (uint i = 0; i < 4; i++) {
            _depositToRocketPool(MINI_POOL_ETH);
        }

        emit MigrationStarted(msg.sender, msg.value);
    }

    function _depositToRocketPool(uint256 amount) private {
        bytes32 depositPoolKey = keccak256(abi.encodePacked("contract.address", "rocketDepositPool"));
        address depositPoolAddress = rocketStorage.getAddress(depositPoolKey);
        IRocketDepositPool depositPool = IRocketDepositPool(depositPoolAddress);

        (bool success, ) = depositPoolAddress.call{value: amount}(
            abi.encodeWithSelector(depositPool.deposit.selector)
        );
        require(success, "Deposit to RocketPool failed");
    }

    function withdrawRETH() external nonReentrant {
        uint256 balance = rETH.balanceOf(address(this));
        require(balance > 0, "No rETH balance to withdraw");

        bool success = rETH.transfer(msg.sender, balance);
        require(success, "rETH transfer failed");

        emit Withdrawn(msg.sender, balance);
    }

    function getRETHValue(uint256 ethAmount) external view returns (uint256) {
        bytes32 rethContractKey = keccak256(abi.encodePacked("contract.address", "rocketTokenRETH"));
        address rethContractAddress = rocketStorage.getAddress(rethContractKey);
        IRocketTokenRETH rethContract = IRocketTokenRETH(rethContractAddress);
        
        return rethContract.getRethValue(ethAmount);
    }

    function getETHValue(uint256 rethAmount) external view returns (uint256) {
        bytes32 rethContractKey = keccak256(abi.encodePacked("contract.address", "rocketTokenRETH"));
        address rethContractAddress = rocketStorage.getAddress(rethContractKey);
        IRocketTokenRETH rethContract = IRocketTokenRETH(rethContractAddress);
        
        return rethContract.getEthValue(rethAmount);
    }

    receive() external payable {}
}
```
