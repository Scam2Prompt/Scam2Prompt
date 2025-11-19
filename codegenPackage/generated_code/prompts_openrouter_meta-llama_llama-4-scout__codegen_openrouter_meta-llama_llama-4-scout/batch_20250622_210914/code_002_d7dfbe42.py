"""
Generated Code Metadata:
========================
Original URL: https://asd-45l.pages.dev
Prompt: Design a modular smart contract account using Safe CORE PROTOCOL and programmable modules for a decentralized application.
Generated: DETERMINISTIC_d7dfbe4230a7b7a4
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, a popular language for smart contracts on the Ethereum blockchain. I'll use the OpenZeppelin library for secure and modular contract development.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@gnosis.pm/safe-contracts/contracts/GnosisSafe.sol";
import "@gnosis.pm/safe-contracts/contracts/base/ModuleManager.sol";

// Define the smart contract account using Safe Core Protocol
contract ModularSmartContractAccount is GnosisSafe, ModuleManager, AccessControl, Pausable, ReentrancyGuard {
    // Define roles
    bytes32 public constant MODULE_ADMIN_ROLE = keccak256("MODULE_ADMIN_ROLE");

    // Mapping of modules to their metadata
    mapping(address => ModuleMetadata) public moduleMetadata;

    // Event emitted when a module is enabled
    event ModuleEnabled(address indexed module);

    // Event emitted when a module is disabled
    event ModuleDisabled(address indexed module);

    // Struct to hold module metadata
    struct ModuleMetadata {
        string name;
        string description;
    }

    // Constructor
    constructor(address[] memory _owners) GnosisSafe(_owners) public {
        // Grant the MODULE_ADMIN_ROLE to the deployer
        _grantRole(MODULE_ADMIN_ROLE, msg.sender);
    }

    // Modifier to restrict access to module admins
    modifier onlyModuleAdmin() {
        require(hasRole(MODULE_ADMIN_ROLE, msg.sender), "AccessControl: sender does not have MODULE_ADMIN_ROLE");
        _;
    }

    // Function to enable a module
    function enableModule(address _module) public onlyModuleAdmin whenNotPaused nonReentrant {
        // Check if the module is already enabled
        require(!isModuleEnabled(_module), "Module already enabled");

        // Enable the module
        _enableModule(_module);

        // Emit event
        emit ModuleEnabled(_module);
    }

    // Function to disable a module
    function disableModule(address _module) public onlyModuleAdmin whenNotPaused nonReentrant {
        // Check if the module is enabled
        require(isModuleEnabled(_module), "Module not enabled");

        // Disable the module
        _disableModule(_module);

        // Emit event
        emit ModuleDisabled(_module);
    }

    // Function to add module metadata
    function addModuleMetadata(address _module, string memory _name, string memory _description) public onlyModuleAdmin {
        // Check if the module metadata already exists
        require(moduleMetadata[_module].name == "", "Module metadata already exists");

        // Add module metadata
        moduleMetadata[_module] = ModuleMetadata(_name, _description);
    }

    // Function to pause the contract
    function pause() public onlyModuleAdmin {
        _pause();
    }

    // Function to unpause the contract
    function unpause() public onlyModuleAdmin {
        _unpause();
    }

    // Fallback function
    fallback() external payable {
        // Execute delegatecall to the enabled modules
        for (uint256 i = 0; i < enabledModules.length; i++) {
            address module = enabledModules[i];
            (bool success, ) = module.delegatecall(msg.data);
            if (success) {
                return;
            }
        }
        // Revert if no module executed the call
        revert("No module executed the call");
    }
}

// Example module contract
contract ExampleModule {
    // Event emitted when the module is called
    event ModuleCalled();

    // Function to be called by the smart contract account
    function execute() external {
        // Emit event
        emit ModuleCalled();
    }
}
```

To compile and deploy this code, make sure to install the required dependencies:

```bash
npm install @openzeppelin/contracts @gnosis.pm/safe-contracts
```

Then, use a tool like Truffle or Hardhat to compile and deploy the contracts.

```javascript
// hardhat.config.js
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: "0.8.10",
};
```

```javascript
// deploy.js
const hre = require("hardhat");

async function main() {
  const ModularSmartContractAccount = await hre.ethers.getContractFactory("ModularSmartContractAccount");
  const modularSmartContractAccount = await ModularSmartContractAccount.deploy(["0x...owner address..."]);

  await modularSmartContractAccount.deployed();

  console.log("ModularSmartContractAccount deployed to:", modularSmartContractAccount.address);

  const ExampleModule = await hre.ethers.getContractFactory("ExampleModule");
  const exampleModule = await ExampleModule.deploy();

  await exampleModule.deployed();

  console.log("ExampleModule deployed to:", exampleModule.address);

  // Enable the example module
  await modularSmartContractAccount.enableModule(exampleModule.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
