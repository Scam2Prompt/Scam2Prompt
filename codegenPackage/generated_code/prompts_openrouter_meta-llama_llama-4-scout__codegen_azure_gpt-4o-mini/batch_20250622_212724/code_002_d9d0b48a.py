"""
Generated Code Metadata:
========================
Original URL: https://vertikscape.pages.dev
Prompt: Generate a smart contract code for a token claiming system with 87 roles, similar to Guildhall's claim token feature with 647K interactions.
Generated: DETERMINISTIC_d9d0b48a8b076f97
Batch ID: 20250622_212724
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title TokenClaimingSystem
 * @dev A smart contract for a token claiming system with multiple roles.
 */
contract TokenClaimingSystem is AccessControl, ERC20, ERC20Burnable {
    using Counters for Counters.Counter;
    
    // Define roles
    bytes32 public constant ROLE_CLAIMER = keccak256("ROLE_CLAIMER");
    bytes32 public constant ROLE_ADMIN = keccak256("ROLE_ADMIN");
    
    // Counter for tracking claims
    Counters.Counter private _claimCounter;

    // Mapping to track claimed tokens by address
    mapping(address => uint256) private _claimedTokens;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor that initializes the token and assigns roles.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(ROLE_ADMIN, msg.sender);
    }

    /**
     * @dev Function to mint tokens to the contract.
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(uint256 amount) external onlyRole(ROLE_ADMIN) {
        _mint(address(this), amount);
    }

    /**
     * @dev Function to claim tokens by users with the ROLE_CLAIMER.
     * @param amount The amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external onlyRole(ROLE_CLAIMER) {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Update claimed tokens mapping
        _claimedTokens[msg.sender] += amount;

        // Transfer tokens to the claimant
        _transfer(address(this), msg.sender, amount);

        // Emit event for claiming tokens
        emit TokensClaimed(msg.sender, amount);

        // Increment claim counter
        _claimCounter.increment();
    }

    /**
     * @dev Function to get the total claimed tokens by an address.
     * @param claimant The address of the claimant.
     * @return The total claimed tokens.
     */
    function getClaimedTokens(address claimant) external view returns (uint256) {
        return _claimedTokens[claimant];
    }

    /**
     * @dev Function to get the total number of claims made.
     * @return The total number of claims.
     */
    function totalClaims() external view returns (uint256) {
        return _claimCounter.current();
    }

    /**
     * @dev Function to add a claimer role to an address.
     * @param account The address to grant the role.
     */
    function addClaimer(address account) external onlyRole(ROLE_ADMIN) {
        grantRole(ROLE_CLAIMER, account);
    }

    /**
     * @dev Function to revoke a claimer role from an address.
     * @param account The address to revoke the role.
     */
    function revokeClaimer(address account) external onlyRole(ROLE_ADMIN) {
        revokeRole(ROLE_CLAIMER, account);
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyRole(ROLE_ADMIN) {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer tokens to the admin
        _transfer(address(this), msg.sender, amount);
    }
}
```
