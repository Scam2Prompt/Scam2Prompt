"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Generate a smart contract for the PLR Token (PLRT) based on the ERC20 standard, including features for token allocation and a burn policy.
Generated: DETERMINISTIC_70bfbd96ae431b9e
Batch ID: 20250612_160254
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

/**
 * @title PLR Token (PLRT) - ERC20 Token with Allocation and Burn Features
 * @dev Implementation of the ERC20 standard with additional functionality for token allocation and burning.
 */
contract PLRToken is ERC20, Ownable {
    // Struct to hold allocation details
    struct Allocation {
        address recipient;
        uint256 amount;
        uint256 releaseTime;
        bool claimed;
    }

    // Mapping to track allocations
    mapping(address => Allocation) public allocations;

    // Burn address
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Burn percentage (e.g., 100 = 1%)
    uint256 public burnPercentage;

    // Events
    event AllocationCreated(address indexed recipient, uint256 amount, uint256 releaseTime);
    event AllocationClaimed(address indexed recipient, uint256 amount);
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply and burn percentage.
     * @param initialSupply The initial token supply.
     * @param _burnPercentage The percentage of tokens to burn on transfers (100 = 1%).
     */
    constructor(uint256 initialSupply, uint256 _burnPercentage) ERC20("PLR Token", "PLRT") {
        require(_burnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Creates a new token allocation.
     * @param recipient The address to receive the allocated tokens.
     * @param amount The amount of tokens to allocate.
     * @param releaseTime The timestamp when the allocation can be claimed.
     */
    function createAllocation(address recipient, uint256 amount, uint256 releaseTime) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(releaseTime > block.timestamp, "Release time must be in the future");
        require(allocations[recipient].amount == 0, "Recipient already has an allocation");

        allocations[recipient] = Allocation({
            recipient: recipient,
            amount: amount,
            releaseTime: releaseTime,
            claimed: false
        });

        emit AllocationCreated(recipient, amount, releaseTime);
    }

    /**
     * @dev Allows a recipient to claim their allocated tokens.
     */
    function claimAllocation() external {
        Allocation storage allocation = allocations[msg.sender];
        require(allocation.amount > 0, "No allocation found");
        require(!allocation.claimed, "Allocation already claimed");
        require(block.timestamp >= allocation.releaseTime, "Release time not reached");

        allocation.claimed = true;
        _transfer(owner(), msg.sender, allocation.amount);

        emit AllocationClaimed(msg.sender, allocation.amount);
    }

    /**
     * @dev Overrides the ERC20 transfer function to implement burn on transfer.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (burnPercentage > 0) {
            uint256 burnAmount = (amount * burnPercentage) / 10000;
            if (burnAmount > 0) {
                _burn(msg.sender, burnAmount);
                amount -= burnAmount;
                emit TokensBurned(msg.sender, burnAmount);
            }
        }
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Overrides the ERC20 transferFrom function to implement burn on transfer.
     * @param sender The address to send the tokens from.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        if (burnPercentage > 0) {
            uint256 burnAmount = (amount * burnPercentage) / 10000;
            if (burnAmount > 0) {
                _burn(sender, burnAmount);
                amount -= burnAmount;
                emit TokensBurned(sender, burnAmount);
            }
        }
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Updates the burn percentage.
     * @param newBurnPercentage The new burn percentage (100 = 1%).
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = newBurnPercentage;
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified address (only callable by owner).
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
        emit TokensBurned(account, amount);
    }
}
```
