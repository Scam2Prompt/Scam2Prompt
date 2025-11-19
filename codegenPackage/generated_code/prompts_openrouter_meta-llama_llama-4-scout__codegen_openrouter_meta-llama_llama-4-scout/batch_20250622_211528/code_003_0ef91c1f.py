"""
Generated Code Metadata:
========================
Original URL: https://bonkbaker.pages.dev
Prompt: Design a smart contract for empowering early-stage projects through community power, similar to BONK.live.
Generated: DETERMINISTIC_0ef91c1f9af69b75
Batch ID: 20250622_211528
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

/**
 * @title CommunityPowerToken
 * @author [Your Name]
 * @notice A token contract for empowering early-stage projects through community power.
 */
contract CommunityPowerToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user vote power
    mapping(address => uint256) private _votePower;

    // Mapping of project votes
    mapping(string => mapping(address => bool)) private _projectVotes;

    // Mapping of project vote counts
    mapping(string => uint256) private _projectVoteCounts;

    // Event emitted when a user votes for a project
    event ProjectVoted(string indexed projectId, address indexed voter);

    // Event emitted when a user's vote power is updated
    event VotePowerUpdated(address indexed user, uint256 newPower);

    /**
     * @notice Constructor for the CommunityPowerToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Updates a user's vote power.
     * @param user The address of the user.
     * @param newPower The new vote power of the user.
     */
    function updateVotePower(address user, uint256 newPower) public onlyOwner {
        _votePower[user] = newPower;
        emit VotePowerUpdated(user, newPower);
    }

    /**
     * @notice Gets a user's vote power.
     * @param user The address of the user.
     * @return The user's vote power.
     */
    function getVotePower(address user) public view returns (uint256) {
        return _votePower[user];
    }

    /**
     * @notice Votes for a project.
     * @param projectId The ID of the project.
     */
    function voteForProject(string memory projectId) public nonReentrant {
        require(_votePower[msg.sender] > 0, "User has no vote power");

        // Check if user has already voted for the project
        require(!_projectVotes[projectId][msg.sender], "User has already voted for this project");

        // Update project vote count
        _projectVoteCounts[projectId] = _projectVoteCounts[projectId].add(_votePower[msg.sender]);

        // Update user's vote history
        _projectVotes[projectId][msg.sender] = true;

        emit ProjectVoted(projectId, msg.sender);
    }

    /**
     * @notice Gets the vote count for a project.
     * @param projectId The ID of the project.
     * @return The vote count for the project.
     */
    function getProjectVoteCount(string memory projectId) public view returns (uint256) {
        return _projectVoteCounts[projectId];
    }

    /**
     * @notice Transfers tokens and updates vote power.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        // Update vote power of sender and recipient
        _updateVotePowerOnTransfer(msg.sender, to, amount);

        return super.transfer(to, amount);
    }

    /**
     * @notice Transfers tokens from one address to another and updates vote power.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        // Update vote power of sender and recipient
        _updateVotePowerOnTransfer(from, to, amount);

        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Updates vote power when tokens are transferred.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function _updateVotePowerOnTransfer(
        address from,
        address to,
        uint256 amount
    ) internal {
        // Update vote power of sender
        _votePower[from] = _votePower[from].sub(amount);

        // Update vote power of recipient
        _votePower[to] = _votePower[to].add(amount);

        emit VotePowerUpdated(from, _votePower[from]);
        emit VotePowerUpdated(to, _votePower[to]);
    }

    /**
     * @notice Burns tokens and updates vote power.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        // Update vote power of sender
        _votePower[msg.sender] = _votePower[msg.sender].sub(amount);

        emit VotePowerUpdated(msg.sender, _votePower[msg.sender]);

        super.burn(amount);
    }
}
```
