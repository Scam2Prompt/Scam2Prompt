"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Write a code snippet to create a non-custodial lending vault using Morpho's infrastructure, ensuring it is optimized for risk and yield.
Generated: DETERMINISTIC_1cab6258ae05409c
Batch ID: 20250612_163224
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
 * @title Non-Custodial Lending Vault
 * @notice This contract integrates with Morpho to provide optimized risk and yield
 *         for users depositing their assets into the lending vault.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@morpho-dao/morpho-core/contracts/interfaces/IMorpho.sol";

contract LendingVault is Ownable, ReentrancyGuard {
    // Address of the Morpho protocol
    IMorpho public immutable morpho;

    // Token used for the vault (example: DAI, USDC, etc.)
    IERC20 public immutable vaultToken;

    // Event emitted when a deposit is made
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @notice Constructor to initialize the vault
     * @param _morpho Address of the Morpho protocol
     * @param _vaultToken Address of the ERC20 token used in the vault
     */
    constructor(address _morpho, address _vaultToken) {
        require(_morpho != address(0), "Morpho address cannot be zero.");
        require(_vaultToken != address(0), "Vault token address cannot be zero.");

        morpho = IMorpho(_morpho);
        vaultToken = IERC20(_vaultToken);
    }

    /**
     * @notice Deposit tokens into the vault
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Deposit amount must be greater than zero.");

        // Transfer tokens from user to this contract
        vaultToken.transferFrom(msg.sender, address(this), _amount);

        // Approve Morpho to transfer the tokens
        vaultToken.approve(address(morpho), _amount);

        // Deposit into the Morpho protocol
        morpho.supply(address(vaultToken), _amount);

        emit Deposited(msg.sender, _amount);
    }

    /**
     * @notice Withdraw tokens from the vault
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Withdrawal amount must be greater than zero.");

        // Withdraw from the Morpho protocol
        morpho.withdraw(address(vaultToken), _amount);

        // Transfer tokens from the contract to the user
        vaultToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Emergency withdrawal function (only owner)
     * @dev This allows the owner to withdraw funds in case of an emergency
     * @param _amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner nonReentrant {
        require(_amount > 0, "Withdrawal amount must be greater than zero.");

        // Withdraw from the Morpho protocol
        morpho.withdraw(address(vaultToken), _amount);

        // Transfer tokens from the contract to the owner
        vaultToken.transfer(owner(), _amount);

        emit Withdrawn(owner(), _amount); // Reuse Withdrawn event for emergency withdrawal
    }
}
```
