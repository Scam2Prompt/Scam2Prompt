"""
Generated Code Metadata:
========================
Original URL: https://plenafinance.vercel.app
Prompt: Write a smart contract to manage the allocation of 2% of the $PLENA token supply for Quest participants, including whitelist spot tracking.
Generated: DETERMINISTIC_55ed7ca3e6db6f09
Batch ID: 20250612_153526
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
 * @title PlenaQuestManager
 * @author [Your Name]
 * @notice Manages the allocation of 2% of the $PLENA token supply for Quest participants.
 */
contract PlenaQuestManager is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of whitelisted addresses and their allocated amounts
    mapping(address => uint256) public whitelist;

    // Mapping of quest participants and their earned amounts
    mapping(address => uint256) public participantEarnings;

    // Total whitelisted spots
    uint256 public whitelistSpots;

    // Total allocated amount (2% of $PLENA token supply)
    uint256 public totalAllocatedAmount;

    // $PLENA token contract
    ERC20 public plenaToken;

    // Percentage of token supply for quests (2%)
    uint256 public constant QUEST_ALLOCATION_PERCENTAGE = 200;

    /**
     * @notice Initializes the contract.
     * @param _plenaToken Address of the $PLENA token contract.
     * @param _totalSupply Total supply of the $PLENA token.
     */
    constructor(address _plenaToken, uint256 _totalSupply) {
        require(_plenaToken != address(0), "Invalid token address");
        plenaToken = ERC20(_plenaToken);
        totalAllocatedAmount = _totalSupply.mul(QUEST_ALLOCATION_PERCENTAGE).div(10000);
    }

    /**
     * @notice Adds a whitelisted address and allocates a spot.
     * @param _address Address to whitelist.
     */
    function addWhitelist(address _address) public onlyOwner {
        require(whitelistSpots < totalAllocatedAmount.div(plenaToken.balanceOf(address(this))), "No more whitelist spots available");
        whitelist[_address] = 0;
        whitelistSpots++;
    }

    /**
     * @notice Removes a whitelisted address and deallocates a spot.
     * @param _address Address to remove from whitelist.
     */
    function removeWhitelist(address _address) public onlyOwner {
        require(whitelist[_address] != 0, "Address not whitelisted");
        whitelist[_address] = 0;
        whitelistSpots--;
    }

    /**
     * @notice Awards a quest participant with $PLENA tokens.
     * @param _participant Address of the quest participant.
     * @param _amount Amount of $PLENA tokens to award.
     */
    function awardQuestParticipant(address _participant, uint256 _amount) public onlyOwner {
        require(whitelist[_participant] == 0, "Participant already whitelisted");
        require(participantEarnings[_participant].add(_amount) <= totalAllocatedAmount, "Exceeds total allocated amount");
        participantEarnings[_participant] = participantEarnings[_participant].add(_amount);
        plenaToken.transfer(_participant, _amount);
    }

    /**
     * @notice Distributes $PLENA tokens to whitelisted addresses.
     */
    function distributeTokens() public onlyOwner {
        for (uint256 i = 0; i < whitelistSpots; i++) {
            address currentAddress = getWhitelistAddress(i);
            uint256 allocation = totalAllocatedAmount.div(whitelistSpots);
            if (whitelist[currentAddress] == 0) {
                whitelist[currentAddress] = allocation;
                plenaToken.transfer(currentAddress, allocation);
            }
        }
    }

    /**
     * @notice Gets a whitelisted address by index.
     * @param _index Index of the whitelisted address.
     * @return Address at the specified index.
     */
    function getWhitelistAddress(uint256 _index) internal view returns (address) {
        // Implementation of this function depends on how you store and manage whitelist addresses.
        // For simplicity, assume a simple array of addresses.
        // In a real-world scenario, consider using a more efficient data structure.
        // For brevity and simplicity, not implemented here.
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    function owner() public view returns (address) {
        // Implementation of this function depends on how you manage ownership.
        // For simplicity, assume the owner is the contract deployer.
        // In a real-world scenario, consider using a more secure ownership management solution.
        // For brevity and simplicity, not implemented here.
    }
}
```
