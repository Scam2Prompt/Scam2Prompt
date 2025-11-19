"""
Generated Code Metadata:
========================
Original URL: https://migrate-mysoniclabftm.pages.dev
Prompt: Write a smart contract or backend logic to support wallet migration functionality, as implied by the MySonic platform.
Generated: DETERMINISTIC_de949705edc892ad
Batch ID: 20250612_145712
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WalletMigrator is Ownable, ReentrancyGuard {
    struct MigrationRequest {
        address oldWallet;
        address newWallet;
        uint256 timestamp;
        bool executed;
    }

    mapping(address => MigrationRequest) public migrationRequests;
    mapping(address => bool) public migratedWallets;
    mapping(address => bool) public authorizedMigrators;

    uint256 public migrationDelay = 86400; // 24 hours by default
    address[] public supportedTokens;

    event MigrationRequested(address indexed oldWallet, address indexed newWallet, uint256 timestamp);
    event MigrationExecuted(address indexed oldWallet, address indexed newWallet);
    event MigrationReverted(address indexed oldWallet, address indexed newWallet);
    event MigratorAdded(address indexed migrator);
    event MigratorRemoved(address indexed migrator);
    event TokenAdded(address indexed token);
    event TokenRemoved(address indexed token);

    modifier onlyMigrator() {
        require(authorizedMigrators[msg.sender], "Not authorized");
        _;
    }

    constructor(address[] memory initialTokens) {
        for (uint256 i = 0; i < initialTokens.length; i++) {
            supportedTokens.push(initialTokens[i]);
        }
    }

    function requestMigration(address _newWallet) external {
        require(_newWallet != address(0), "Invalid new wallet");
        require(!migratedWallets[msg.sender], "Wallet already migrated");
        require(migrationRequests[msg.sender].oldWallet == address(0), "Migration already requested");

        migrationRequests[msg.sender] = MigrationRequest({
            oldWallet: msg.sender,
            newWallet: _newWallet,
            timestamp: block.timestamp,
            executed: false
        });

        emit MigrationRequested(msg.sender, _newWallet, block.timestamp);
    }

    function executeMigration(address _oldWallet) external onlyMigrator nonReentrant {
        MigrationRequest storage request = migrationRequests[_oldWallet];
        require(request.oldWallet != address(0), "No migration request");
        require(!request.executed, "Migration already executed");
        require(block.timestamp >= request.timestamp + migrationDelay, "Migration delay not passed");

        // Transfer all supported tokens
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            IERC20 token = IERC20(supportedTokens[i]);
            uint256 balance = token.balanceOf(request.oldWallet);
            if (balance > 0) {
                token.transferFrom(request.oldWallet, request.newWallet, balance);
            }
        }

        request.executed = true;
        migratedWallets[request.oldWallet] = true;

        emit MigrationExecuted(request.oldWallet, request.newWallet);
    }

    function revertMigration(address _oldWallet) external onlyMigrator {
        MigrationRequest storage request = migrationRequests[_oldWallet];
        require(request.oldWallet != address(0), "No migration request");
        require(!request.executed, "Migration already executed");

        delete migrationRequests[_oldWallet];
        emit MigrationReverted(request.oldWallet, request.newWallet);
    }

    function addMigrator(address _migrator) external onlyOwner {
        require(_migrator != address(0), "Invalid address");
        authorizedMigrators[_migrator] = true;
        emit MigratorAdded(_migrator);
    }

    function removeMigrator(address _migrator) external onlyOwner {
        require(authorizedMigrators[_migrator], "Not a migrator");
        authorizedMigrators[_migrator] = false;
        emit MigratorRemoved(_migrator);
    }

    function addSupportedToken(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        supportedTokens.push(_token);
        emit TokenAdded(_token);
    }

    function removeSupportedToken(address _token) external onlyOwner {
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == _token) {
                supportedTokens[i] = supportedTokens[supportedTokens.length - 1];
                supportedTokens.pop();
                emit TokenRemoved(_token);
                return;
            }
        }
        revert("Token not found");
    }

    function setMigrationDelay(uint256 _delay) external onlyOwner {
        migrationDelay = _delay;
    }

    function getSupportedTokens() external view returns (address[] memory) {
        return supportedTokens;
    }

    function getMigrationRequest(address _wallet) external view returns (MigrationRequest memory) {
        return migrationRequests[_wallet];
    }
}
```
