"""
Generated Code Metadata:
========================
Original URL: https://mintchaindapp.vercel.app
Prompt: Develop a smart contract to handle $MINT token airdrops, ensuring compliance with the Mint Blockchain's ERC7765 standard.
Generated: DETERMINISTIC_da5283795e62f030
Batch ID: 20250612_150613
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title MINTTokenAirdrop
 * @dev A smart contract for handling $MINT token airdrops compliant with Mint Blockchain's ERC7765 standard.
 */
contract MINTTokenAirdrop is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public mintToken;
    uint256 public airdropAmount;
    uint256 public airdropStartTime;
    uint256 public airdropEndTime;
    bool public isAirdropActive;

    EnumerableSet.AddressSet private _eligibleAddresses;
    mapping(address => bool) private _claimedAirdrops;

    event AirdropConfigured(uint256 amount, uint256 startTime, uint256 endTime);
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event AirdropStatusChanged(bool isActive);
    event EligibilityAdded(address[] addresses);
    event EligibilityRemoved(address[] addresses);

    /**
     * @dev Constructor initializes the airdrop contract
     * @param _mintToken Address of the $MINT token contract
     */
    constructor(address _mintToken) {
        require(_mintToken != address(0), "MINTTokenAirdrop: Invalid token address");
        mintToken = IERC20(_mintToken);
    }

    /**
     * @dev Configure the airdrop parameters
     * @param amount Amount of tokens to airdrop per eligible address
     * @param startTime Timestamp when airdrop starts
     * @param endTime Timestamp when airdrop ends
     */
    function configureAirdrop(
        uint256 amount,
        uint256 startTime,
        uint256 endTime
    ) external onlyOwner {
        require(amount > 0, "MINTTokenAirdrop: Amount must be greater than 0");
        require(
            startTime < endTime,
            "MINTTokenAirdrop: Start time must be before end time"
        );
        require(
            endTime > block.timestamp,
            "MINTTokenAirdrop: End time must be in the future"
        );

        airdropAmount = amount;
        airdropStartTime = startTime;
        airdropEndTime = endTime;

        emit AirdropConfigured(amount, startTime, endTime);
    }

    /**
     * @dev Toggle airdrop active status
     * @param active Boolean indicating whether airdrop should be active
     */
    function setAirdropActive(bool active) external onlyOwner {
        isAirdropActive = active;
        emit AirdropStatusChanged(active);
    }

    /**
     * @dev Add addresses to eligibility list
     * @param addresses Array of addresses to add
     */
    function addEligibleAddresses(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            if (addresses[i] != address(0) && !_eligibleAddresses.contains(addresses[i])) {
                _eligibleAddresses.add(addresses[i]);
            }
        }
        emit EligibilityAdded(addresses);
    }

    /**
     * @dev Remove addresses from eligibility list
     * @param addresses Array of addresses to remove
     */
    function removeEligibleAddresses(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            if (_eligibleAddresses.contains(addresses[i])) {
                _eligibleAddresses.remove(addresses[i]);
            }
        }
        emit EligibilityRemoved(addresses);
    }

    /**
     * @dev Check if an address is eligible for airdrop
     * @param account Address to check
     * @return Boolean indicating eligibility
     */
    function isEligible(address account) public view returns (bool) {
        return _eligibleAddresses.contains(account);
    }

    /**
     * @dev Check if an address has claimed their airdrop
     * @param account Address to check
     * @return Boolean indicating claim status
     */
    function hasClaimed(address account) public view returns (bool) {
        return _claimedAirdrops[account];
    }

    /**
     * @dev Claim airdrop tokens
     */
    function claimAirdrop() external {
        require(isAirdropActive, "MINTTokenAirdrop: Airdrop is not active");
        require(
            block.timestamp >= airdropStartTime,
            "MINTTokenAirdrop: Airdrop has not started"
        );
        require(
            block.timestamp <= airdropEndTime,
            "MINTTokenAirdrop: Airdrop has ended"
        );
        require(
            isEligible(msg.sender),
            "MINTTokenAirdrop: Address not eligible for airdrop"
        );
        require(
            !hasClaimed(msg.sender),
            "MINTTokenAirdrop: Airdrop already claimed"
        );

        _claimedAirdrops[msg.sender] = true;
        require(
            mintToken.transfer(msg.sender, airdropAmount),
            "MINTTokenAirdrop: Token transfer failed"
        );

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Withdraw remaining tokens after airdrop ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(
            block.timestamp > airdropEndTime,
            "MINTTokenAirdrop: Airdrop has not ended"
        );

        uint256 remainingBalance = mintToken.balanceOf(address(this));
        require(
            mintToken.transfer(owner(), remainingBalance),
            "MINTTokenAirdrop: Token transfer failed"
        );
    }

    /**
     * @dev Get total number of eligible addresses
     * @return uint256 count of eligible addresses
     */
    function getEligibleAddressCount() external view returns (uint256) {
        return _eligibleAddresses.length();
    }

    /**
     * @dev Get eligible address at specific index
     * @param index Index to query
     * @return address at the given index
     */
    function getEligibleAddressAt(uint256 index) external view returns (address) {
        return _eligibleAddresses.at(index);
    }
}
```
