"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Provide a step-by-step guide to deploy a Solidity-based infrastructure project on Linea that leverages EVM equivalence for seamless integration with existing Ethereum tools.
Generated: DETERMINISTIC_ed9b5e71fc754e92
Batch ID: 20250612_154913
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

import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LineaDeployer
 * @dev A contract to deploy and manage Solidity projects on Linea with EVM equivalence
 */
contract LineaDeployer is Ownable, ReentrancyGuard {
    using Address for address;

    // Event emitted when a new contract is deployed
    event ContractDeployed(address indexed contractAddress, string contractName);

    // Mapping to track deployed contracts
    mapping(string => address) public deployedContracts;

    /**
     * @dev Deploys a new contract using create2 for deterministic address
     * @param bytecode The bytecode of the contract to deploy
     * @param salt A unique salt for create2 deployment
     * @param contractName Name to identify the deployed contract
     */
    function deployContract(
        bytes memory bytecode,
        bytes32 salt,
        string memory contractName
    ) external onlyOwner nonReentrant returns (address) {
        require(bytecode.length > 0, "LineaDeployer: empty bytecode");
        require(bytes(contractName).length > 0, "LineaDeployer: empty contract name");

        address deployedAddress;
        assembly {
            deployedAddress := create2(0, add(bytecode, 0x20), mload(bytecode), salt)
            if iszero(extcodesize(deployedAddress)) {
                revert(0, 0)
            }
        }

        deployedContracts[contractName] = deployedAddress;
        emit ContractDeployed(deployedAddress, contractName);

        return deployedAddress;
    }

    /**
     * @dev Calls a function on a deployed contract
     * @param contractName Name of the deployed contract
     * @param data Encoded function call data
     */
    function callContract(
        string memory contractName,
        bytes memory data
    ) external onlyOwner nonReentrant returns (bytes memory) {
        address contractAddress = deployedContracts[contractName];
        require(contractAddress != address(0), "LineaDeployer: contract not found");

        (bool success, bytes memory result) = contractAddress.call(data);
        require(success, "LineaDeployer: call failed");

        return result;
    }

    /**
     * @dev Upgrades a deployed contract by deploying new version and transferring ownership
     * @param bytecode The bytecode of the new contract version
     * @param salt A unique salt for create2 deployment
     * @param contractName Name of the contract to upgrade
     * @param oldContractOwner The owner address of the old contract
     * @param newContractOwner The new owner address for the upgraded contract
     */
    function upgradeContract(
        bytes memory bytecode,
        bytes32 salt,
        string memory contractName,
        address oldContractOwner,
        address newContractOwner
    ) external onlyOwner nonReentrant returns (address) {
        require(deployedContracts[contractName] != address(0), "LineaDeployer: contract not found");

        // Deploy new version
        address newVersion = deployContract(bytecode, salt, string(abi.encodePacked(contractName, "-v2")));

        // Transfer ownership if applicable
        if (oldContractOwner != address(0) && newContractOwner != address(0)) {
            (bool success, ) = newVersion.call(
                abi.encodeWithSignature("transferOwnership(address)", newContractOwner)
            );
            require(success, "LineaDeployer: ownership transfer failed");
        }

        return newVersion;
    }
}
```

```javascript
// Deployment script using Hardhat
const { ethers } = require("hardhat");
const fs = require("fs");

async function main() {
    // 1. Compile contracts
    console.log("Compiling contracts...");
    const LineaDeployer = await ethers.getContractFactory("LineaDeployer");
    
    // 2. Deploy LineaDeployer
    console.log("Deploying LineaDeployer...");
    const lineaDeployer = await LineaDeployer.deploy();
    await lineaDeployer.deployed();
    console.log("LineaDeployer deployed to:", lineaDeployer.address);
    
    // 3. Save deployment addresses
    const deployments = {
        LineaDeployer: lineaDeployer.address
    };
    fs.writeFileSync("deployments.json", JSON.stringify(deployments, null, 2));
    
    // 4. Verify contracts (if on testnet/mainnet)
    if (process.env.VERIFY_CONTRACTS === "true") {
        console.log("Verifying contracts...");
        try {
            await hre.run("verify:verify", {
                address: lineaDeployer.address,
                constructorArguments: [],
            });
        } catch (error) {
            console.error("Verification failed:", error);
        }
    }
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```javascript
// Interaction script example
const { ethers } = require("hardhat");
const fs = require("fs");

async function interact() {
    // 1. Load deployments
    const deployments = JSON.parse(fs.readFileSync("deployments.json"));
    const lineaDeployerAddress = deployments.LineaDeployer;
    
    // 2. Connect to contract
    const [owner] = await ethers.getSigners();
    const LineaDeployer = await ethers.getContractFactory("LineaDeployer");
    const lineaDeployer = LineaDeployer.attach(lineaDeployerAddress);
    
    // 3. Example: Deploy a new contract
    const ExampleContract = await ethers.getContractFactory("ExampleContract");
    const bytecode = ExampleContract.bytecode;
    const salt = ethers.utils.id("unique-salt-123");
    
    console.log("Deploying ExampleContract...");
    const tx = await lineaDeployer.deployContract(
        bytecode,
        salt,
        "ExampleContract"
    );
    await tx.wait();
    
    console.log("ExampleContract deployed via LineaDeployer");
}

interact()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```solidity
// Example contract to be deployed via LineaDeployer
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ExampleContract
 * @dev Example contract to demonstrate deployment via LineaDeployer
 */
contract ExampleContract is Ownable {
    uint256 public value;
    
    event ValueUpdated(uint256 newValue);
    
    constructor() {
        value = 42;
    }
    
    function updateValue(uint256 newValue) external onlyOwner {
        value = newValue;
        emit ValueUpdated(newValue);
    }
    
    function getValue() external view returns (uint256) {
        return value;
    }
}
```
