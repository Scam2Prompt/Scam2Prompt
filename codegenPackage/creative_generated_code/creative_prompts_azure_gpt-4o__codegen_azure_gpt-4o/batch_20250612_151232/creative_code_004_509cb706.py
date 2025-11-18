"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asi-singularitydao.pages.dev
Prompt: Provide an example of a decentralized application (dApp) interface for token migration, incorporating the rebranding and merging process described in SingularityDAO's Artificial Superintelligence Alliance (ASI) migration phase.
Generated: DETERMINISTIC_509cb7061dd9e1c2
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenMigrationDApp
 * @dev A decentralized application (dApp) for token migration during the ASI rebranding and merging process.
 * Users can migrate their old tokens to new tokens following the SingularityDAO migration policy.
 */
contract TokenMigrationDApp {
    // Address of the old token contract
    address public oldTokenAddress;

    // Address of the new token contract
    address public newTokenAddress;

    // Address of the admin responsible for managing migrations
    address public admin;

    // Event emitted when a successful migration occurs
    event TokenMigrated(address indexed user, uint256 amount);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token addresses and admin.
     * @param _oldTokenAddress Address of the old token contract
     * @param _newTokenAddress Address of the new token contract
     */
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address");
        require(_newTokenAddress != address(0), "Invalid new token address");
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
        admin = msg.sender; // Set the deployer as admin
    }

    /**
     * @dev Function to migrate old tokens to new tokens.
     * The user must approve this contract to spend their old tokens beforehand.
     * @param amount The amount of old tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Interaction with the old token contract
        IERC20 oldToken = IERC20(oldTokenAddress);
        IERC20 newToken = IERC20(newTokenAddress);

        // Ensure the user has enough balance
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old token balance");
        
        // Transfer old tokens from the user to this contract
        require(oldToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Mint equivalent new tokens to the user
        require(newToken.mint(msg.sender, amount), "Minting new tokens failed");

        // Emit an event for successful migration
        emit TokenMigrated(msg.sender, amount);
    }

    /**
     * @dev Emergency function to withdraw tokens in case of an issue.
     * Only callable by the admin.
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyAdmin {
        require(amount > 0, "Amount must be greater than zero");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(admin, amount), "Token transfer failed");
    }

    /**
     * @dev Function for the admin to update token addresses in case of a change.
     * @param _oldTokenAddress New address for the old token
     * @param _newTokenAddress New address for the new token
     */
    function updateTokenAddresses(address _oldTokenAddress, address _newTokenAddress) external onlyAdmin {
        require(_oldTokenAddress != address(0), "Invalid old token address");
        require(_newTokenAddress != address(0), "Invalid new token address");
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
    }
}

/**
 * @dev Interface for interacting with ERC20 token contracts.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function mint(address recipient, uint256 amount) external returns (bool);
}
```
