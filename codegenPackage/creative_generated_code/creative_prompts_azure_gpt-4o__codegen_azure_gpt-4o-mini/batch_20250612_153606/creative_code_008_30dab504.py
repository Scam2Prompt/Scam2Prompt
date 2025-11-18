"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Develop a smart contract for a Play-To-Earn gaming token that incorporates features to attract both traditional gamers and crypto enthusiasts, as outlined in ScapesMania's project goals.
Generated: DETERMINISTIC_30dab5045f408c8a
Batch ID: 20250612_153606
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

// Importing OpenZeppelin's ERC20 implementation for token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";

// Smart contract for the Play-To-Earn gaming token
contract ScapesManiaToken is ERC20, Ownable, ERC20Burnable, ERC20Pausable {
    // Event to log when rewards are distributed
    event RewardsDistributed(address indexed player, uint256 amount);
    // Mapping to track player rewards
    mapping(address => uint256) public rewards;

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("ScapesMania Token", "SCT") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rewards to players
    function distributeRewards(address[] calldata players, uint256[] calldata amounts) external onlyOwner {
        require(players.length == amounts.length, "Players and amounts length mismatch");

        for (uint256 i = 0; i < players.length; i++) {
            require(players[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");

            // Update the player's rewards
            rewards[players[i]] += amounts[i];
            _mint(players[i], amounts[i]); // Mint the rewards to the player's address

            emit RewardsDistributed(players[i], amounts[i]); // Emit the rewards event
        }
    }

    // Function for players to claim their accumulated rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the player's rewards to zero before transferring
        rewards[msg.sender] = 0;
        _mint(msg.sender, rewardAmount); // Mint the rewards to the player
    }

    // Function for the owner to pause token transfers
    function pause() external onlyOwner {
        _pause();
    }

    // Function for the owner to unpause token transfers
    function unpause() external onlyOwner {
        _unpause();
    }

    // Override _beforeTokenTransfer to add pause functionality
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override(ERC20, ERC20Pausable) {
        super._beforeTokenTransfer(from, to, amount);
    }

    // Function to burn tokens (can only be called by the token owner)
    function burn(uint256 amount) public override onlyOwner {
        super.burn(amount);
    }
}
```
