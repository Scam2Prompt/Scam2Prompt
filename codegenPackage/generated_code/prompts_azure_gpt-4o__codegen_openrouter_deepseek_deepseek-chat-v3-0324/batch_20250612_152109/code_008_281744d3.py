"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Create a Solidity function that distributes WL (whitelist) spots and airdrops to ERC-404 $GOD token holders, as outlined in the God Candle project.
Generated: DETERMINISTIC_281744d38f1a32d3
Batch ID: 20250612_152109
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

contract GODWhitelistDistributor is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public godToken;
    uint256 public whitelistThreshold;
    uint256 public airdropAmount;
    uint256 public whitelistSpots;
    uint256 public distributedWhitelistSpots;
    
    EnumerableSet.AddressSet private whitelistedAddresses;
    mapping(address => bool) public hasReceivedAirdrop;

    event WhitelistAdded(address indexed account);
    event AirdropDistributed(address indexed recipient, uint256 amount);

    constructor(
        address _godToken,
        uint256 _whitelistThreshold,
        uint256 _airdropAmount,
        uint256 _whitelistSpots
    ) {
        require(_godToken != address(0), "Invalid token address");
        godToken = IERC20(_godToken);
        whitelistThreshold = _whitelistThreshold;
        airdropAmount = _airdropAmount;
        whitelistSpots = _whitelistSpots;
    }

    function checkWhitelistEligibility(address account) public view returns (bool) {
        return godToken.balanceOf(account) >= whitelistThreshold && 
               distributedWhitelistSpots < whitelistSpots;
    }

    function addToWhitelist(address account) external onlyOwner {
        require(!whitelistedAddresses.contains(account), "Already whitelisted");
        require(distributedWhitelistSpots < whitelistSpots, "All spots allocated");
        
        whitelistedAddresses.add(account);
        distributedWhitelistSpots++;
        emit WhitelistAdded(account);
    }

    function batchAddToWhitelist(address[] calldata accounts) external onlyOwner {
        require(
            distributedWhitelistSpots + accounts.length <= whitelistSpots,
            "Exceeds available spots"
        );

        for (uint256 i = 0; i < accounts.length; i++) {
            if (!whitelistedAddresses.contains(accounts[i])) {
                whitelistedAddresses.add(accounts[i]);
                distributedWhitelistSpots++;
                emit WhitelistAdded(accounts[i]);
            }
        }
    }

    function distributeAirdrop(address recipient) external onlyOwner {
        require(!hasReceivedAirdrop[recipient], "Already received airdrop");
        require(
            godToken.transfer(recipient, airdropAmount),
            "Airdrop transfer failed"
        );

        hasReceivedAirdrop[recipient] = true;
        emit AirdropDistributed(recipient, airdropAmount);
    }

    function batchDistributeAirdrop(address[] calldata recipients) external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            if (!hasReceivedAirdrop[recipients[i]]) {
                require(
                    godToken.transfer(recipients[i], airdropAmount),
                    "Airdrop transfer failed"
                );
                hasReceivedAirdrop[recipients[i]] = true;
                emit AirdropDistributed(recipients[i], airdropAmount);
            }
        }
    }

    function isWhitelisted(address account) public view returns (bool) {
        return whitelistedAddresses.contains(account);
    }

    function getWhitelistedAddresses() public view returns (address[] memory) {
        return whitelistedAddresses.values();
    }

    function updateWhitelistThreshold(uint256 newThreshold) external onlyOwner {
        whitelistThreshold = newThreshold;
    }

    function updateAirdropAmount(uint256 newAmount) external onlyOwner {
        airdropAmount = newAmount;
    }

    function updateWhitelistSpots(uint256 newSpots) external onlyOwner {
        require(newSpots >= distributedWhitelistSpots, "Cannot reduce below allocated");
        whitelistSpots = newSpots;
    }

    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner(), amount), "Withdrawal failed");
    }
}
```
