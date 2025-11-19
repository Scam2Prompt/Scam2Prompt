"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egtoken-migrate-io.web.app
Prompt: How can I use EGMigrate to safely upgrade my tokens and smart contracts in an instant?
Generated: DETERMINISTIC_855fb042d0cf9ffa
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";

// Token contract that supports upgradeability using EIP-1967 proxy
contract Token is ERC20, Initializable, UUPSUpgradeable {
    // Address of the admin for upgrade permissions
    address private admin;

    // Event emitted when the token is upgraded
    event TokenUpgraded(address indexed newImplementation);

    // Modifier to check if the caller is the admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not the admin");
        _;
    }

    // Initialize function for the constructor logic
    function initialize(string memory name, string memory symbol, address _admin) external initializer {
        __ERC20_init(name, symbol);
        admin = _admin;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply
    }

    // Function to perform upgrade
    function upgrade(address newImplementation) external onlyAdmin {
        _authorizeUpgrade(newImplementation);
        emit TokenUpgraded(newImplementation);
    }

    // Override function for UUPS
    function _authorizeUpgrade(address newImplementation) internal override onlyAdmin {}
}

// Factory contract to deploy and manage token upgrades
contract TokenFactory {
    // Mapping to store deployed tokens
    mapping(address => address) public tokens;

    // Function to create and deploy a new token
    function createToken(string memory name, string memory symbol) external {
        Token token = new Token();
        token.initialize(name, symbol, msg.sender);
        tokens[msg.sender] = address(token);
    }

    // Function to upgrade an existing token
    function upgradeToken(address tokenAddress, address newImplementation) external {
        Token token = Token(tokenAddress);
        token.upgrade(newImplementation);
    }
}
```

This code includes a basic upgradeable token contract using OpenZeppelin's upgradeable contracts framework, alongside a factory to create and manage these tokens. Proper access control and event logging are implemented to ensure safe upgrades.
