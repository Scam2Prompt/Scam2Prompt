"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Write a Solidity-based smart contract (if applicable for cross-chain compatibility) to implement a token similar to $LIBRA that supports decentralized funding for small businesses.
Generated: DETERMINISTIC_c62718fa73069150
Batch ID: 20250612_150135
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title LibraToken
 * @dev ERC20 token with additional functionality for decentralized funding of small businesses
 */
contract LibraToken is ERC20, Ownable, Pausable {
    struct Business {
        address owner;
        string name;
        string description;
        uint256 fundingGoal;
        uint256 fundsRaised;
        bool isActive;
    }

    mapping(uint256 => Business) public businesses;
    uint256 public businessCount;
    uint256 public fundingFeePercentage; // Percentage fee taken from funding transactions

    event BusinessCreated(uint256 indexed businessId, address indexed owner, string name, uint256 fundingGoal);
    event FundsContributed(uint256 indexed businessId, address indexed contributor, uint256 amount);
    event FundingGoalReached(uint256 indexed businessId, uint256 totalRaised);
    event BusinessDeactivated(uint256 indexed businessId);
    event FundingFeeChanged(uint256 newFeePercentage);

    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply Initial token supply
     * @param _fundingFeePercentage Initial funding fee percentage
     */
    constructor(uint256 initialSupply, uint256 _fundingFeePercentage) ERC20("LibraToken", "LIBRA") {
        _mint(msg.sender, initialSupply);
        fundingFeePercentage = _fundingFeePercentage;
    }

    /**
     * @dev Creates a new business funding campaign
     * @param name Name of the business
     * @param description Description of the business
     * @param fundingGoal Funding goal in LIBRA tokens
     */
    function createBusiness(
        string memory name,
        string memory description,
        uint256 fundingGoal
    ) external whenNotPaused {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(fundingGoal > 0, "Funding goal must be greater than 0");

        businessCount++;
        businesses[businessCount] = Business({
            owner: msg.sender,
            name: name,
            description: description,
            fundingGoal: fundingGoal,
            fundsRaised: 0,
            isActive: true
        });

        emit BusinessCreated(businessCount, msg.sender, name, fundingGoal);
    }

    /**
     * @dev Contributes funds to a business
     * @param businessId ID of the business to contribute to
     * @param amount Amount of LIBRA tokens to contribute
     */
    function contributeToBusiness(uint256 businessId, uint256 amount) external whenNotPaused {
        require(businessId > 0 && businessId <= businessCount, "Invalid business ID");
        Business storage business = businesses[businessId];
        require(business.isActive, "Business is not active");
        require(amount > 0, "Amount must be greater than 0");
        require(business.fundsRaised < business.fundingGoal, "Funding goal already reached");

        uint256 fee = (amount * fundingFeePercentage) / 100;
        uint256 netAmount = amount - fee;

        _transfer(msg.sender, business.owner, netAmount);
        _transfer(msg.sender, owner(), fee);

        business.fundsRaised += netAmount;

        emit FundsContributed(businessId, msg.sender, netAmount);

        if (business.fundsRaised >= business.fundingGoal) {
            emit FundingGoalReached(businessId, business.fundsRaised);
        }
    }

    /**
     * @dev Deactivates a business funding campaign
     * @param businessId ID of the business to deactivate
     */
    function deactivateBusiness(uint256 businessId) external {
        require(businessId > 0 && businessId <= businessCount, "Invalid business ID");
        Business storage business = businesses[businessId];
        require(msg.sender == business.owner || msg.sender == owner(), "Not authorized");
        business.isActive = false;
        emit BusinessDeactivated(businessId);
    }

    /**
     * @dev Changes the funding fee percentage (owner only)
     * @param newFeePercentage New fee percentage
     */
    function setFundingFeePercentage(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 10, "Fee cannot exceed 10%");
        fundingFeePercentage = newFeePercentage;
        emit FundingFeeChanged(newFeePercentage);
    }

    /**
     * @dev Pauses all token transfers (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
