"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Design a smart contract for the MIND of Pepe tokenomics, allocating tokens according to the specified distribution (10% for exchanges, 25% for the AI agent, 20% for marketing, 15% for rewards, and 30% for development).
Generated: DETERMINISTIC_c54875108cffaf47
Batch ID: 20250622_211643
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract MindOfPepe is ERC20, Ownable {
    // Token distribution percentages
    uint256 public constant EXCHANGES_PERCENT = 10;
    uint256 public constant AI_AGENT_PERCENT = 25;
    uint256 public constant MARKETING_PERCENT = 20;
    uint256 public constant REWARDS_PERCENT = 15;
    uint256 public constant DEVELOPMENT_PERCENT = 30;

    // Addresses for allocated funds
    address public exchangesAddress;
    address public aiAgentAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public developmentAddress;

    // Total supply constant
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    /**
     * @dev Constructor that initializes the token and allocates funds according to the distribution.
     * @param _exchangesAddress Address for exchanges allocation
     * @param _aiAgentAddress Address for AI agent allocation
     * @param _marketingAddress Address for marketing allocation
     * @param _rewardsAddress Address for rewards allocation
     * @param _developmentAddress Address for development allocation
     */
    constructor(
        address _exchangesAddress,
        address _aiAgentAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _developmentAddress
    ) ERC20("Mind of Pepe", "MIND") {
        require(
            _exchangesAddress != address(0) &&
            _aiAgentAddress != address(0) &&
            _marketingAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _developmentAddress != address(0),
            "Invalid address(es) provided"
        );

        // Set allocation addresses
        exchangesAddress = _exchangesAddress;
        aiAgentAddress = _aiAgentAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        developmentAddress = _developmentAddress;

        // Mint total supply to the contract
        _mint(address(this), TOTAL_SUPPLY);

        // Allocate tokens according to distribution
        _allocateTokens();
    }

    /**
     * @dev Internal function to allocate tokens according to the specified distribution.
     */
    function _allocateTokens() internal {
        _transfer(address(this), exchangesAddress, (TOTAL_SUPPLY * EXCHANGES_PERCENT) / 100);
        _transfer(address(this), aiAgentAddress, (TOTAL_SUPPLY * AI_AGENT_PERCENT) / 100);
        _transfer(address(this), marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENT) / 100);
        _transfer(address(this), rewardsAddress, (TOTAL_SUPPLY * REWARDS_PERCENT) / 100);
        _transfer(address(this), developmentAddress, (TOTAL_SUPPLY * DEVELOPMENT_PERCENT) / 100);
    }

    /**
     * @dev Allows the owner to update allocation addresses.
     * @param _exchangesAddress New exchanges address
     * @param _aiAgentAddress New AI agent address
     * @param _marketingAddress New marketing address
     * @param _rewardsAddress New rewards address
     * @param _developmentAddress New development address
     */
    function updateAllocationAddresses(
        address _exchangesAddress,
        address _aiAgentAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _developmentAddress
    ) external onlyOwner {
        require(
            _exchangesAddress != address(0) &&
            _aiAgentAddress != address(0) &&
            _marketingAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _developmentAddress != address(0),
            "Invalid address(es) provided"
        );

        exchangesAddress = _exchangesAddress;
        aiAgentAddress = _aiAgentAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        developmentAddress = _developmentAddress;
    }
}
```
