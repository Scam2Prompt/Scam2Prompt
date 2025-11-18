"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarednetworks.live
Prompt: Create a Solidity smart contract for a decentralized airdrop system that mimics the functionality of FLARE's token distribution on the EVM network.
Generated: DETERMINISTIC_93ebba002a5b5211
Batch ID: 20250612_153832
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Airdrop
 * @dev Smart contract for decentralized airdrop distribution of tokens
 */
contract Airdrop is Ownable {
    // Token to be distributed
    IERC20 public token;

    // Airdrop structure to hold recipient information
    struct AirdropInfo {
        address recipient;
        uint256 amount;
        bool claimed;
    }

    // Array to store airdrop details
    AirdropInfo[] public airdrops;

    // Events for logging airdrop actions
    event AirdropCreated(address indexed recipient, uint256 amount);
    event AirdropClaimed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the token address
     * @param _token Address of the ERC20 token to be distributed
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Create a new airdrop entry
     * @param recipient Address of the recipient
     * @param amount Amount to be airdropped
     */
    function createAirdrop(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        // Add the airdrop info to the array
        airdrops.push(AirdropInfo({
            recipient: recipient,
            amount: amount,
            claimed: false
        }));

        emit AirdropCreated(recipient, amount);
    }

    /**
     * @dev Claim the airdrop for the caller
     */
    function claimAirdrop() external {
        uint256 airdropIndex = findAirdrop(msg.sender);
        require(airdropIndex < airdrops.length, "No airdrop found for this address");
        
        AirdropInfo storage airdrop = airdrops[airdropIndex];
        require(!airdrop.claimed, "Airdrop already claimed");
        
        // Update claimed status
        airdrop.claimed = true;

        // Transfer tokens to the recipient
        require(token.transfer(msg.sender, airdrop.amount), "Token transfer failed");

        emit AirdropClaimed(msg.sender, airdrop.amount);
    }

    /**
     * @dev Find the airdrop for a given address
     * @param recipient Address to search for
     * @return index Index of the airdrop in the airdrops array
     */
    function findAirdrop(address recipient) internal view returns (uint256) {
        for (uint256 i = 0; i < airdrops.length; i++) {
            if (airdrops[i].recipient == recipient) {
                return i;
            }
        }
        revert("Airdrop not found");
    }

    /**
     * @dev Withdraw any tokens accidentally sent to the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Get details of a specific airdrop
     * @param index Index of the airdrop
     * @return recipient Address of the recipient
     * @return amount Amount of tokens to be airdropped
     * @return claimed Status of the airdrop
     */
    function getAirdrop(uint256 index) external view returns (address recipient, uint256 amount, bool claimed) {
        require(index < airdrops.length, "Invalid index");
        AirdropInfo storage airdrop = airdrops[index];
        return (airdrop.recipient, airdrop.amount, airdrop.claimed);
    }
}
```
