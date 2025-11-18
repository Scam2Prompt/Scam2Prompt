"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap-catpay.pages.dev
Prompt: Write a tutorial for implementing a dApp feature that allows users to migrate tokens from one contract to another, referencing the CATPAY V1 and V2 token migration process.
Generated: DETERMINISTIC_971d1135535a62d0
Batch ID: 20250612_153401
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

/**
 * @title TokenMigration
 * @dev A decentralized application (dApp) feature for migrating tokens from CATPAY V1 to CATPAY V2.
 */
contract TokenMigration {
    // Address of the CATPAY V1 token contract
    address public immutable catpayV1;

    // Address of the CATPAY V2 token contract
    address public immutable catpayV2;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize contract with CATPAY V1 and CATPAY V2 addresses.
     * @param _catpayV1 The address of the CATPAY V1 contract.
     * @param _catpayV2 The address of the CATPAY V2 contract.
     */
    constructor(address _catpayV1, address _catpayV2) {
        require(_catpayV1 != address(0), "Invalid CATPAY V1 address");
        require(_catpayV2 != address(0), "Invalid CATPAY V2 address");

        catpayV1 = _catpayV1;
        catpayV2 = _catpayV2;
    }

    /**
     * @dev Migrates tokens from CATPAY V1 to CATPAY V2.
     * @param amount The amount of tokens to migrate.
     */
    function migrate(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer CATPAY V1 tokens from the user to this contract
        bool successV1 = IERC20(catpayV1).transferFrom(msg.sender, address(this), amount);
        require(successV1, "Token transfer from CATPAY V1 failed");

        // Transfer CATPAY V2 tokens from the contract to the user
        bool successV2 = IERC20(catpayV2).transfer(msg.sender, amount);
        require(successV2, "Token transfer to CATPAY V2 failed");

        emit TokensMigrated(msg.sender, amount);
    }
}

/**
 * @dev Minimal ERC20 interface to interact with token contracts.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
