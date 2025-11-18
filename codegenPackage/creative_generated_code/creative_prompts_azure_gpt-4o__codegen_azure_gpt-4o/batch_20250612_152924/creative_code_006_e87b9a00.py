"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-dao.pages.dev
Prompt: Develop a smart contract snippet that facilitates token migration from RJV OLD to RJV NEW, ensuring compatibility with the SingularityDAO system.
Generated: DETERMINISTIC_e87b9a009d7b3718
Batch ID: 20250612_152924
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
 * @notice This smart contract facilitates the migration of tokens from RJV OLD to RJV NEW.
 * It ensures compatibility with the SingularityDAO system.
 */
contract TokenMigration {
    // Address of the old token contract (RJV OLD)
    address public immutable oldToken;

    // Address of the new token contract (RJV NEW)
    address public immutable newToken;

    // Address of the SingularityDAO system for compatibility checks
    address public immutable singularityDAO;

    // Mapping to track migrated tokens for each user
    mapping(address => uint256) public migratedBalances;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Modifier to ensure the caller is not a contract
     */
    modifier onlyEOA() {
        require(msg.sender == tx.origin, "Contract calls not allowed");
        _;
    }

    /**
     * @param _oldToken Address of the RJV OLD token contract
     * @param _newToken Address of the RJV NEW token contract
     * @param _singularityDAO Address of the SingularityDAO system
     */
    constructor(
        address _oldToken,
        address _newToken,
        address _singularityDAO
    ) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");
        require(_singularityDAO != address(0), "Invalid SingularityDAO address");

        oldToken = _oldToken;
        newToken = _newToken;
        singularityDAO = _singularityDAO;
    }

    /**
     * @notice Migrates tokens from RJV OLD to RJV NEW.
     * @param amount Amount of tokens to migrate
     */
    function migrate(uint256 amount) external onlyEOA {
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the old token contract (Assumes standard ERC20 interface)
        IERC20 oldTokenContract = IERC20(oldToken);
        require(
            oldTokenContract.balanceOf(msg.sender) >= amount,
            "Insufficient balance in RJV OLD"
        );

        // Transfer RJV OLD tokens to this contract
        require(
            oldTokenContract.transferFrom(msg.sender, address(this), amount),
            "Failed to transfer RJV OLD tokens"
        );

        // Interact with the new token contract (Assumes standard ERC20 interface)
        IERC20 newTokenContract = IERC20(newToken);
        require(
            newTokenContract.balanceOf(address(this)) >= amount,
            "Insufficient balance in RJV NEW"
        );

        // Transfer RJV NEW tokens to the user
        require(
            newTokenContract.transfer(msg.sender, amount),
            "Failed to transfer RJV NEW tokens"
        );

        // Update the migrated balances
        migratedBalances[msg.sender] += amount;

        // Emit the migration event
        emit TokensMigrated(msg.sender, amount);
    }
}

/**
 * @dev Standard ERC20 interface for token interaction
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
