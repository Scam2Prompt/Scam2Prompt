"""
Generated Code Metadata:
========================
Original URL: https://puffmypanda.pages.dev
Prompt: Write a Solidity contract for the Puff Like A Panda P2E game that includes race mechanics, token rewards, and a mechanism to split 4.20% of the tokens between burns and DAO wallet donations.
Generated: DETERMINISTIC_c008a7482fa4cfc9
Batch ID: 20250612_152235
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

contract PuffLikeAPanda is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Game variables
    uint256 public totalRaces;
    uint256 public totalPlayers;
    mapping(address => Player) public players;

    // Tokenomics
    uint256 public constant TOKEN_REWARD = 100 ether;
    uint256 public constant DAO_DONATION_PERCENTAGE = 4.20;
    uint256 public constant BURN_PERCENTAGE = 2.10;
    address public daoWallet;
    address public burnAddress;

    // Events
    event NewPlayer(address indexed player);
    event NewRace(address indexed player, uint256 reward);
    event DonationSent(address indexed to, uint256 amount);

    // Structs
    struct Player {
        uint256 wins;
        uint256 losses;
        uint256 balance;
    }

    // Constructor
    constructor(address _daoWallet, address _burnAddress) ERC20("PuffLikeAPanda", "PLAP") {
        daoWallet = _daoWallet;
        burnAddress = _burnAddress;
    }

    // Functions
    function createPlayer() external {
        require(players[msg.sender].balance == 0, "Player already exists");
        players[msg.sender] = Player(0, 0, 0);
        totalPlayers++;
        emit NewPlayer(msg.sender);
    }

    function participateInRace() external {
        require(players[msg.sender].balance >= TOKEN_REWARD, "Insufficient balance");
        players[msg.sender].balance -= TOKEN_REWARD;
        uint256 outcome = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))) % 2;
        if (outcome == 0) {
            players[msg.sender].wins++;
            players[msg.sender].balance += TOKEN_REWARD * 2;
            emit NewRace(msg.sender, TOKEN_REWARD * 2);
        } else {
            players[msg.sender].losses++;
            emit NewRace(msg.sender, 0);
        }
        totalRaces++;
    }

    function claimReward() external {
        require(players[msg.sender].balance > 0, "No reward to claim");
        uint256 reward = players[msg.sender].balance;
        players[msg.sender].balance = 0;
        _mint(msg.sender, reward);
    }

    function distributeTokens() external {
        uint256 balance = balanceOf(address(this));
        uint256 daoDonation = balance.mul(DAO_DONATION_PERCENTAGE).div(100);
        uint256 burnAmount = balance.mul(BURN_PERCENTAGE).div(100);
        _transfer(address(this), daoWallet, daoDonation);
        _burn(address(this), burnAmount);
        emit DonationSent(daoWallet, daoDonation);
    }

    // Overrides
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal override {
        for (uint256 i = 0; i < ids.length; i++) {
            require(players[from].balance >= ids[i], "Insufficient balance");
            players[from].balance -= ids[i];
            players[to].balance += ids[i];
        }
    }
}
```
