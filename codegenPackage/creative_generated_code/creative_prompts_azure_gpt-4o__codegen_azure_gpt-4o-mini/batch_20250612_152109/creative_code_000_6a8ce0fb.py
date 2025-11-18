"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisgamersguild.pages.dev
Prompt: Write a smart contract using Genesis Gamers Guild's Layer-2 EVM ZK-rollup framework to enable advanced gameplay mechanics for a Web3 game. Ensure the contract supports gas-free transactions and integrates with Celestia for data availability.
Generated: DETERMINISTIC_6a8ce0fb7b4c948a
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title GenesisGamersGuild
 * @dev Smart contract for a Web3 game using Layer-2 EVM ZK-rollup framework
 *      and integrates with Celestia for data availability.
 */
contract GenesisGamersGuild is Ownable {
    struct Player {
        uint256 id;
        string username;
        uint256 score;
    }

    mapping(address => Player) public players;
    mapping(uint256 => address) public playerById;
    uint256 public playerCount;

    event PlayerRegistered(address indexed playerAddress, string username);
    event ScoreUpdated(address indexed playerAddress, uint256 newScore);

    /**
     * @dev Registers a new player with a unique username
     * @param _username The username of the player
     */
    function registerPlayer(string calldata _username) external {
        require(bytes(_username).length > 0, "Username cannot be empty");
        require(players[msg.sender].id == 0, "Player already registered");

        playerCount++;
        players[msg.sender] = Player(playerCount, _username, 0);
        playerById[playerCount] = msg.sender;

        emit PlayerRegistered(msg.sender, _username);
    }

    /**
     * @dev Updates the score for a player
     * @param _score The new score to be set for the player
     */
    function updateScore(uint256 _score) external {
        require(players[msg.sender].id != 0, "Player not registered");
        require(_score >= 0, "Score must be non-negative");

        players[msg.sender].score = _score;

        emit ScoreUpdated(msg.sender, _score);
    }

    /**
     * @dev Gets the details of a player
     * @param _playerAddress The address of the player
     * @return id The ID of the player
     * @return username The username of the player
     * @return score The current score of the player
     */
    function getPlayerDetails(address _playerAddress) external view returns (uint256 id, string memory username, uint256 score) {
        require(players[_playerAddress].id != 0, "Player not registered");

        Player memory player = players[_playerAddress];
        return (player.id, player.username, player.score);
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens sent to the contract
     * @param tokenAddress The address of the ERC20 token contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");
        
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to receive Ether. msg.data must be empty
     */
    receive() external payable {}

    /**
     * @dev Fallback function. Can be used to receive Ether
     */
    fallback() external payable {}
}
```
