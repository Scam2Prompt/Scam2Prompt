"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asi-singularitydao.pages.dev
Prompt: Write a smart contract in Solidity that facilitates token migration from AGIX to FET at a conversion rate of 1 AGIX to 0.43335 FET, as described in SingularityDAO's migration process.
Generated: DETERMINISTIC_a1aa9e022a202add
Batch ID: 20250612_151232
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
 * @dev A smart contract to facilitate token migration from AGIX to FET at a fixed conversion rate.
 */
contract TokenMigration {
    IERC20 public agixToken; // AGIX token contract
    IERC20 public fetToken;  // FET token contract
    address public owner;    // Contract owner
    uint256 public conversionRate = 43335; // Conversion rate: 1 AGIX = 0.43335 FET (scaled by 10^5)

    event TokensMigrated(address indexed user, uint256 agixAmount, uint256 fetAmount);

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Only owner allowed");
        _;
    }

    /**
     * @dev Constructor to set the AGIX and FET token addresses.
     * @param _agixToken Address of the AGIX token contract.
     * @param _fetToken Address of the FET token contract.
     */
    constructor(IERC20 _agixToken, IERC20 _fetToken) {
        require(address(_agixToken) != address(0), "Invalid AGIX token address");
        require(address(_fetToken) != address(0), "Invalid FET token address");

        agixToken = _agixToken;
        fetToken = _fetToken;
        owner = msg.sender; // Set the owner of the contract
    }

    /**
     * @dev Allows users to migrate their AGIX tokens to FET tokens.
     * @param agixAmount Amount of AGIX tokens to migrate.
     */
    function migrateTokens(uint256 agixAmount) external {
        require(agixAmount > 0, "AGIX amount must be greater than 0");

        // Calculate FET amount based on the conversion rate
        uint256 fetAmount = (agixAmount * conversionRate) / 100000;

        // Check user has enough AGIX tokens and the contract has enough FET tokens
        require(agixToken.balanceOf(msg.sender) >= agixAmount, "Insufficient AGIX balance");
        require(fetToken.balanceOf(address(this)) >= fetAmount, "Insufficient FET tokens in contract");

        // Transfer AGIX tokens from user to contract
        require(agixToken.transferFrom(msg.sender, address(this), agixAmount), "AGIX transfer failed");

        // Transfer FET tokens from contract to user
        require(fetToken.transfer(msg.sender, fetAmount), "FET transfer failed");

        // Emit migration event
        emit TokensMigrated(msg.sender, agixAmount, fetAmount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract (both AGIX and FET).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).transfer(owner, amount);
    }

    /**
     * @dev Allows the owner to update the conversion rate.
     * @param newConversionRate New conversion rate (scaled by 10^5).
     */
    function updateConversionRate(uint256 newConversionRate) external onlyOwner {
        require(newConversionRate > 0, "Conversion rate must be greater than 0");
        conversionRate = newConversionRate;
    }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
