"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a Solidity contract that dynamically adjusts the composition of the Meme Frenzy index based on trending meme coins, as voted by $MEMEX token holders.
Generated: DETERMINISTIC_e98c3dd998b76549
Batch ID: 20250612_145633
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the $MEMEX token
interface IMemexToken is IERC20 {
    function totalSupply() external view returns (uint256);
}

// Struct to represent a meme coin in the index
struct MemeCoin {
    address tokenAddress; // Address of the meme coin token
    uint256 weight;       // Weight of the meme coin in the index
}

// Main contract for the Meme Frenzy index
contract MemeFrenzyIndex is Ownable {
    using SafeMath for uint256;

    IMemexToken public memexToken; // Reference to the $MEMEX token
    MemeCoin[] public memeCoins;    // Array of meme coins in the index
    mapping(address => uint256) public votes; // Mapping to track votes for meme coins

    // Event emitted when the index is updated
    event IndexUpdated(MemeCoin[] newMemeCoins);

    // Constructor to initialize the contract with the $MEMEX token address
    constructor(address _memexToken) {
        require(_memexToken != address(0), "Invalid MEMEX token address");
        memexToken = IMemexToken(_memexToken);
    }

    // Function to add a meme coin to the index
    function addMemeCoin(address _tokenAddress, uint256 _weight) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_weight > 0, "Weight must be greater than zero");

        memeCoins.push(MemeCoin({
            tokenAddress: _tokenAddress,
            weight: _weight
        }));
    }

    // Function to vote for a meme coin
    function voteForMemeCoin(uint256 index) external {
        require(index < memeCoins.length, "Invalid meme coin index");
        require(memexToken.balanceOf(msg.sender) > 0, "Must hold $MEMEX tokens to vote");

        // Increment the vote count for the selected meme coin
        votes[memeCoins[index].tokenAddress] = votes[memeCoins[index].tokenAddress].add(1);
    }

    // Function to update the index based on votes
    function updateIndex() external onlyOwner {
        // Logic to determine the top meme coins based on votes
        // This is a placeholder for the actual implementation
        // In a real scenario, you would implement a sorting mechanism
        // and adjust the weights accordingly.

        emit IndexUpdated(memeCoins);
    }

    // Function to get the current meme coins in the index
    function getMemeCoins() external view returns (MemeCoin[] memory) {
        return memeCoins;
    }

    // Function to get the vote count for a specific meme coin
    function getVoteCount(address _tokenAddress) external view returns (uint256) {
        return votes[_tokenAddress];
    }
}
```
