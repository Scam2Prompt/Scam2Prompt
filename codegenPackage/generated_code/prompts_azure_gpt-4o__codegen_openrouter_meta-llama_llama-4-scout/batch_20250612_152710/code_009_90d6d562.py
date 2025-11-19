"""
Generated Code Metadata:
========================
Original URL: https://roostcoinclaim.pages.dev
Prompt: Write a Solidity contract that mimics the presale breakdown of $ROOST, ensuring 50% of the raise goes to LP and 50% to expenses, development, and distribution.
Generated: DETERMINISTIC_90d6d56275fd9e10
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RoostPresaleContract
 * @author [Your Name]
 * @notice A contract to manage the presale of $ROOST token.
 */
contract RoostPresaleContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of contributors and their contributions
    mapping(address => uint256) public contributors;

    // Total amount raised
    uint256 public totalRaised;

    // Total amount allocated to LP
    uint256 public lpAllocation;

    // Total amount allocated to expenses, development, and distribution
    uint256 public expensesAllocation;

    // $ROOST token contract
    ERC20Burnable public roostToken;

    // Address of the LP wallet
    address public lpWallet;

    // Address of the expenses, development, and distribution wallet
    address public expensesWallet;

    // Presale end block
    uint256 public presaleEndBlock;

    // Flag to check if presale is active
    bool public isPresaleActive;

    /**
     * @notice Constructor for the RoostPresaleContract
     * @param _roostToken Address of the $ROOST token contract
     * @param _lpWallet Address of the LP wallet
     * @param _expensesWallet Address of the expenses, development, and distribution wallet
     * @param _presaleEndBlock Presale end block
     */
    constructor(
        address _roostToken,
        address _lpWallet,
        address _expensesWallet,
        uint256 _presaleEndBlock
    ) public {
        require(_roostToken != address(0), "Invalid token address");
        require(_lpWallet != address(0), "Invalid LP wallet address");
        require(_expensesWallet != address(0), "Invalid expenses wallet address");
        require(_presaleEndBlock > block.number, "Invalid presale end block");

        roostToken = ERC20Burnable(_roostToken);
        lpWallet = _lpWallet;
        expensesWallet = _expensesWallet;
        presaleEndBlock = _presaleEndBlock;
        isPresaleActive = true;
    }

    /**
     * @notice Contribute to the presale
     * @param _amount Amount to contribute
     */
    function contribute(uint256 _amount) external nonReentrant {
        require(isPresaleActive, "Presale is not active");
        require(block.number <= presaleEndBlock, "Presale has ended");
        require(_amount > 0, "Invalid contribution amount");

        contributors[msg.sender] = contributors[msg.sender].add(_amount);
        totalRaised = totalRaised.add(_amount);

        // Transfer $ROOST tokens to the contributor
        require(roostToken.transfer(msg.sender, _amount), "Failed to transfer $ROOST tokens");
    }

    /**
     * @notice Finalize the presale
     */
    function finalizePresale() external nonReentrant {
        require(isPresaleActive, "Presale is not active");
        require(block.number > presaleEndBlock, "Presale has not ended");

        // Calculate LP and expenses allocations
        lpAllocation = totalRaised.div(2);
        expensesAllocation = totalRaised.sub(lpAllocation);

        // Transfer LP allocation to LP wallet
        require(roostToken.transfer(lpWallet, lpAllocation), "Failed to transfer LP allocation");

        // Transfer expenses allocation to expenses wallet
        require(roostToken.transfer(expensesWallet, expensesAllocation), "Failed to transfer expenses allocation");

        // Deactivate presale
        isPresaleActive = false;
    }

    /**
     * @notice Claim $ROOST tokens for a contributor
     * @param _amount Amount of $ROOST tokens to claim
     */
    function claimTokens(uint256 _amount) external nonReentrant {
        require(!isPresaleActive, "Presale is still active");
        require(contributors[msg.sender] >= _amount, "Insufficient contribution");

        // Burn $ROOST tokens from the contract
        require(roostToken.burn(_amount), "Failed to burn $ROOST tokens");

        // Reset contributor's balance
        contributors[msg.sender] = contributors[msg.sender].sub(_amount);
    }
}
```
