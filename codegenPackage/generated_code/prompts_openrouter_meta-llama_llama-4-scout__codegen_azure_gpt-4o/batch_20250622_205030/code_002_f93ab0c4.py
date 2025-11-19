"""
Generated Code Metadata:
========================
Original URL: https://corntoken.pages.dev
Prompt: Generate a smart contract in Solidity for a cryptocurrency similar to $CORN, with features like token migration and claiming.
Generated: DETERMINISTIC_f93ab0c4b25194e3
Batch ID: 20250622_205030
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

/**
 * @title CornToken
 * @dev ERC20-like token with migration and claiming functionality.
 */
contract CornToken {
    // Token details
    string public name = "CornToken";
    string public symbol = "CORN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Migration-related variables
    address public migrationTarget;
    bool public migrationEnabled;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event MigrationEnabled(address indexed target);
    event TokensMigrated(address indexed user, uint256 amount);
    event TokensClaimed(address indexed user, uint256 amount);

    // Modifier to check migration status
    modifier migrationActive() {
        require(migrationEnabled, "Migration is not enabled");
        _;
    }

    // Constructor to initialize the token supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC20-like transfer function
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // ERC20-like approve function
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // ERC20-like transferFrom function
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // ERC20-like balanceOf function
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    // ERC20-like allowance function
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    // Enable migration to a new contract
    function enableMigration(address _migrationTarget) external {
        require(_migrationTarget != address(0), "Invalid migration target");
        require(!migrationEnabled, "Migration already enabled");

        migrationTarget = _migrationTarget;
        migrationEnabled = true;
        emit MigrationEnabled(_migrationTarget);
    }

    // Migrate tokens to the new contract
    function migrateTokens(uint256 _amount) external migrationActive {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        totalSupply -= _amount;

        // Notify the migration target contract
        (bool success, ) = migrationTarget.call(
            abi.encodeWithSignature("receiveMigration(address,uint256)", msg.sender, _amount)
        );
        require(success, "Migration failed");

        emit TokensMigrated(msg.sender, _amount);
    }

    // Claim tokens (example use case: airdrop or rewards)
    function claimTokens(uint256 _amount) external {
        require(_amount > 0, "Invalid claim amount");

        balances[msg.sender] += _amount;
        totalSupply += _amount;

        emit TokensClaimed(msg.sender, _amount);
    }
}
```
