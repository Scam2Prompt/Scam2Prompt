"""
Generated Code Metadata:
========================
Original URL: https://sugarkingdomodyssey.web.app
Prompt: Generate a smart contract code snippet for managing token airdrops, similar to the $SKO Token Distribution described on the Sugar Kingdom Odyssey website.
Generated: DETERMINISTIC_2f6947f7df6aa5c0
Batch ID: 20250622_210316
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
 * @title TokenAirdrop
 * @dev A smart contract for managing token airdrops with whitelisting capabilities
 */
contract TokenAirdrop is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public token;
    uint256 public airdropAmount;
    uint256 public claimStartTime;
    uint256 public claimEndTime;
    
    EnumerableSet.AddressSet private _whitelistedAddresses;
    mapping(address => bool) public hasClaimed;

    event TokensAirdropped(address indexed recipient, uint256 amount);
    event WhitelistUpdated(address indexed account, bool isWhitelisted);

    /**
     * @dev Constructor to initialize the airdrop contract
     * @param _token Address of the ERC20 token to be airdropped
     * @param _airdropAmount Amount of tokens each eligible address can claim
     * @param _claimStartTime Timestamp when claiming starts
     * @param _claimDuration Duration in seconds for which claiming is open
     */
    constructor(
        address _token,
        uint256 _airdropAmount,
        uint256 _claimStartTime,
        uint256 _claimDuration
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_airdropAmount > 0, "Airdrop amount must be positive");
        require(_claimStartTime > block.timestamp, "Start time must be in future");
        require(_claimDuration > 0, "Duration must be positive");

        token = IERC20(_token);
        airdropAmount = _airdropAmount;
        claimStartTime = _claimStartTime;
        claimEndTime = _claimStartTime + _claimDuration;
    }

    /**
     * @dev Add multiple addresses to the whitelist
     * @param accounts Array of addresses to be whitelisted
     */
    function addToWhitelist(address[] calldata accounts) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            if (!_whitelistedAddresses.contains(accounts[i])) {
                _whitelistedAddresses.add(accounts[i]);
                emit WhitelistUpdated(accounts[i], true);
            }
        }
    }

    /**
     * @dev Remove multiple addresses from the whitelist
     * @param accounts Array of addresses to be removed
     */
    function removeFromWhitelist(address[] calldata accounts) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            if (_whitelistedAddresses.contains(accounts[i])) {
                _whitelistedAddresses.remove(accounts[i]);
                emit WhitelistUpdated(accounts[i], false);
            }
        }
    }

    /**
     * @dev Check if an address is whitelisted
     * @param account Address to check
     * @return bool True if address is whitelisted
     */
    function isWhitelisted(address account) public view returns (bool) {
        return _whitelistedAddresses.contains(account);
    }

    /**
     * @dev Get total number of whitelisted addresses
     * @return uint256 Count of whitelisted addresses
     */
    function whitelistCount() public view returns (uint256) {
        return _whitelistedAddresses.length();
    }

    /**
     * @dev Claim airdropped tokens
     */
    function claimTokens() external {
        require(block.timestamp >= claimStartTime, "Airdrop not started yet");
        require(block.timestamp <= claimEndTime, "Airdrop has ended");
        require(isWhitelisted(msg.sender), "Address not whitelisted");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        hasClaimed[msg.sender] = true;
        require(token.transfer(msg.sender, airdropAmount), "Token transfer failed");
        
        emit TokensAirdropped(msg.sender, airdropAmount);
    }

    /**
     * @dev Withdraw remaining tokens after airdrop ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > claimEndTime, "Airdrop not ended yet");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }

    /**
     * @dev Extend the airdrop duration if needed
     * @param additionalDuration Additional time in seconds
     */
    function extendAirdrop(uint256 additionalDuration) external onlyOwner {
        require(additionalDuration > 0, "Duration must be positive");
        claimEndTime += additionalDuration;
    }
}
```
