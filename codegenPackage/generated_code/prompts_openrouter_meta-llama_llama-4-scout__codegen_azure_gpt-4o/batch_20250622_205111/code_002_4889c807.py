"""
Generated Code Metadata:
========================
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Generate a smart contract code for a yield farming strategy on Pencils Protocol's Vaults using Solidity.
Generated: DETERMINISTIC_4889c8079c91209a
Batch ID: 20250622_205111
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
 * @title Yield Farming Strategy for Pencils Protocol Vaults
 * @dev This contract interacts with Pencils Protocol Vaults to deposit funds, earn yield, and withdraw funds.
 *      It includes proper error handling and follows best practices for Solidity development.
 */
contract YieldFarmingStrategy {
    // Address of the Pencils Protocol Vault
    address public immutable vault;

    // Address of the token being deposited
    address public immutable depositToken;

    // Address of the owner (admin) of the strategy
    address public owner;

    // Events for logging important actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event EmergencyWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the strategy contract.
     * @param _vault Address of the Pencils Protocol Vault.
     * @param _depositToken Address of the token to be deposited.
     */
    constructor(address _vault, address _depositToken) {
        require(_vault != address(0), "Invalid vault address");
        require(_depositToken != address(0), "Invalid deposit token address");

        vault = _vault;
        depositToken = _depositToken;
        owner = msg.sender;
    }

    /**
     * @dev Deposit tokens into the Pencils Protocol Vault.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer deposit tokens from the user to this contract
        bool success = IERC20(depositToken).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve the vault to spend the tokens
        success = IERC20(depositToken).approve(vault, amount);
        require(success, "Token approval failed");

        // Interact with the vault to deposit tokens
        IPencilsVault(vault).deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the Pencils Protocol Vault.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the vault to withdraw tokens
        IPencilsVault(vault).withdraw(amount);

        // Transfer withdrawn tokens to the owner
        bool success = IERC20(depositToken).transfer(owner, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(owner, amount);
    }

    /**
     * @dev Emergency withdraw all tokens from the vault.
     *      This function is only callable by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        // Interact with the vault to withdraw all tokens
        uint256 balance = IPencilsVault(vault).balanceOf(address(this));
        IPencilsVault(vault).withdraw(balance);

        // Transfer all withdrawn tokens to the owner
        bool success = IERC20(depositToken).transfer(owner, balance);
        require(success, "Token transfer failed");

        emit EmergencyWithdrawn(owner, balance);
    }

    /**
     * @dev Update the owner of the contract.
     * @param newOwner Address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @dev Interface for Pencils Protocol Vault.
 */
interface IPencilsVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}
```
