"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Create a smart contract in Solidity that implements the Proof of Hilarity mechanism for the METAL token, allowing miners to submit memes for rewards.
Generated: DETERMINISTIC_ca58e155dfd101d5
Batch ID: 20250612_162508
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

// Import OpenZeppelin's ERC20 implementation for the METAL token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the METAL token contract
contract METALToken is ERC20, Ownable {
    // Reward for each valid meme submission
    uint256 public memeReward;

    // Event emitted when a new meme is submitted
    event MemeSubmitted(address indexed miner, uint256 indexed memeId, string memeUri);

    // Struct to store meme information
    struct Meme {
        address miner;
        string uri;
        bool rewarded;
    }

    // Mapping from meme ID to Meme data
    mapping(uint256 => Meme) public memes;
    uint256 public memeCount;

    constructor(uint256 initialSupply, uint256 _memeReward) ERC20("METAL Token", "METAL") {
        _mint(msg.sender, initialSupply); // Mint initial supply to the contract owner
        memeReward = _memeReward; // Set the meme reward amount
    }

    // Function to submit a meme for reward
    function submitMeme(string calldata memeUri) external {
        // Increment the meme count
        memeCount++;

        // Create a new meme and store it
        memes[memeCount] = Meme({
            miner: msg.sender,
            uri: memeUri,
            rewarded: false
        });

        // Emit an event for the submitted meme
        emit MemeSubmitted(msg.sender, memeCount, memeUri);
    }

    // Function to reward a miner for their meme submission
    function rewardMeme(uint256 memeId) external {
        // Ensure the meme exists and has not been rewarded
        require(memeId > 0 && memeId <= memeCount, "Invalid meme ID");
        Meme storage meme = memes[memeId];
        require(!meme.rewarded, "Meme already rewarded");
        require(meme.miner == msg.sender, "Only the miner can claim the reward");

        // Mark the meme as rewarded
        meme.rewarded = true;

        // Transfer the reward to the miner
        _mint(meme.miner, memeReward);
    }

    // Function to update the meme reward (only owner can call this)
    function updateMemeReward(uint256 newReward) external onlyOwner {
        memeReward = newReward;
    }
}
```
