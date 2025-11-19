"""
Generated Code Metadata:
========================
Original URL: https://bafybeibqsvjqfvqtsrjjykxkbbgwkxnz32gxfxyrhaa4y5d3xr67l6gnzq.ipfs.dweb.link
Prompt: Design a smart contract for distributing FantasyTop Packs to eligible users, incorporating wallet connection and rewards tracking.
Generated: DETERMINISTIC_8506457f396d76c3
Batch ID: 20250622_205751
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// FantasyTopPacks contract for distributing packs to eligible users
contract FantasyTopPacks is Ownable {
    using SafeMath for uint256;

    // Event emitted when a pack is distributed
    event PackDistributed(address indexed user, uint256 packId);

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Total number of packs available
    uint256 public totalPacks;

    // Struct to represent a pack
    struct Pack {
        uint256 id;
        string name;
        uint256 rewardAmount;
        bool isAvailable;
    }

    // Array to store packs
    Pack[] public packs;

    // Constructor to initialize the contract with a specified number of packs
    constructor(uint256 _totalPacks) {
        totalPacks = _totalPacks;
        for (uint256 i = 0; i < totalPacks; i++) {
            packs.push(Pack(i, string(abi.encodePacked("Pack ", uint2str(i))), 100 * (i + 1), true));
        }
    }

    // Function to distribute a pack to an eligible user
    function distributePack(address user, uint256 packId) external onlyOwner {
        require(packId < totalPacks, "Pack does not exist");
        require(packs[packId].isAvailable, "Pack is not available");

        // Update user rewards
        userRewards[user] = userRewards[user].add(packs[packId].rewardAmount);

        // Mark the pack as distributed
        packs[packId].isAvailable = false;

        // Emit event for pack distribution
        emit PackDistributed(user, packId);
    }

    // Function to get the total rewards of a user
    function getUserRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }

    // Utility function to convert uint256 to string
    function uint2str(uint256 _i) internal pure returns (string memory) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint256 k = len;
        while (_i != 0) {
            bstr[--k] = bytes1(uint8(48 + _i % 10));
            _i /= 10;
        }
        return string(bstr);
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
