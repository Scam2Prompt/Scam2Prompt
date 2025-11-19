"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Write a Solidity smart contract for an EVM-compatible Layer 2 blockchain that tokenizes AI compute resources into yield-bearing assets, ensuring compliance with KYC/AML regulations. Use concepts from Singularity Finance's tokenization framework.
Generated: DETERMINISTIC_d420d00f8443732c
Batch ID: 20250612_145831
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ComputeToken
 * @author [Your Name]
 * @notice Tokenizes AI compute resources into yield-bearing assets, ensuring compliance with KYC/AML regulations.
 */
contract ComputeToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of user addresses to their KYC/AML verification status
    mapping(address => bool) public kycVerified;

    // Mapping of user addresses to their compute resource allocation
    mapping(address => uint256) public computeResourceAllocation;

    // Mapping of compute resource providers to their reputation scores
    mapping(address => uint256) public providerReputation;

    // Event emitted when a user is KYC/AML verified
    event KycVerified(address indexed user, bool verified);

    // Event emitted when compute resources are allocated to a user
    event ComputeResourceAllocated(address indexed user, uint256 amount);

    // Event emitted when a compute resource provider's reputation score is updated
    event ProviderReputationUpdated(address indexed provider, uint256 score);

    /**
     * @notice Constructor for the ComputeToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Verifies a user's KYC/AML status.
     * @param user The address of the user to verify.
     * @param verified The verification status of the user.
     */
    function verifyKyc(address user, bool verified) public onlyOwner {
        kycVerified[user] = verified;
        emit KycVerified(user, verified);
    }

    /**
     * @notice Allocates compute resources to a user.
     * @param user The address of the user to allocate resources to.
     * @param amount The amount of compute resources to allocate.
     */
    function allocateComputeResource(address user, uint256 amount) public onlyOwner {
        computeResourceAllocation[user] += amount;
        emit ComputeResourceAllocated(user, amount);
    }

    /**
     * @notice Updates a compute resource provider's reputation score.
     * @param provider The address of the provider to update.
     * @param score The new reputation score of the provider.
     */
    function updateProviderReputation(address provider, uint256 score) public onlyOwner {
        providerReputation[provider] = score;
        emit ProviderReputationUpdated(provider, score);
    }

    /**
     * @notice Mints new tokens to a user.
     * @param user The address of the user to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address user, uint256 amount) public onlyOwner {
        _mint(user, amount);
    }

    /**
     * @notice Burns tokens from a user.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        require(kycVerified[msg.sender], "KYC/AML verification required");
        super.burn(amount);
    }

    /**
     * @notice Transfers tokens from one user to another.
     * @param from The address of the user to transfer tokens from.
     * @param to The address of the user to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(kycVerified[msg.sender], "KYC/AML verification required");
        require(kycVerified[to], "Recipient KYC/AML verification required");
        return super.transfer(to, amount);
    }

    /**
     * @notice Transfers tokens from one user to another on behalf of the token owner.
     * @param from The address of the user to transfer tokens from.
     * @param to The address of the user to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(kycVerified[from], "Sender KYC/AML verification required");
        require(kycVerified[to], "Recipient KYC/AML verification required");
        return super.transferFrom(from, to, amount);
    }
}
```
