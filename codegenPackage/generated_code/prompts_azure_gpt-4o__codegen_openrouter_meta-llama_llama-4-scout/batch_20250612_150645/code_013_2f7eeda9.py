"""
Generated Code Metadata:
========================
Original URL: https://claim-pandoshi.web.app
Prompt: Write a Solidity contract for a token presale with bonus programs and tracking platforms, similar to the PAMBO token presale.
Generated: DETERMINISTIC_2f7eeda9102f3b68
Batch ID: 20250612_150645
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
 * @title PAMBO Token Presale Contract
 * @author [Your Name]
 * @notice This contract manages the PAMBO token presale with bonus programs and tracking platforms.
 */
contract PAMBOPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of platform to its tracking information
    mapping (address => Platform) public platforms;

    // Mapping of user to its purchase information
    mapping (address => User) public users;

    // Token contract instance
    ERC20 public token;

    // Presale start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Presale phases with corresponding bonuses
    mapping (uint256 => Phase) public phases;

    // Total tokens allocated for presale
    uint256 public totalTokens;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Event emitted when user purchases tokens
    event Purchase(address indexed user, uint256 amount);

    // Event emitted when platform is added
    event PlatformAdded(address indexed platform, string name);

    // Event emitted when presale phase is added
    event PhaseAdded(uint256 phase, uint256 bonus);

    /**
     * @param _token Token contract address
     * @param _startTime Presale start timestamp
     * @param _endTime Presale end timestamp
     * @param _totalTokens Total tokens allocated for presale
     */
    constructor(
        address _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _totalTokens
    ) public {
        require(_token != address(0), "Invalid token address");
        require(_startTime > block.timestamp, "Invalid start time");
        require(_endTime > _startTime, "Invalid end time");
        require(_totalTokens > 0, "Invalid total tokens");

        token = ERC20(_token);
        startTime = _startTime;
        endTime = _endTime;
        totalTokens = _totalTokens;
    }

    /**
     * @dev Add a new platform for tracking
     * @param _platform Platform address
     * @param _name Platform name
     */
    function addPlatform(address _platform, string memory _name) public {
        require(msg.sender == owner(), "Only owner can add platforms");
        require(_platform != address(0), "Invalid platform address");

        platforms[_platform] = Platform(_name, 0);
        emit PlatformAdded(_platform, _name);
    }

    /**
     * @dev Add a new presale phase with bonus
     * @param _phase Phase number
     * @param _bonus Bonus percentage
     */
    function addPhase(uint256 _phase, uint256 _bonus) public {
        require(msg.sender == owner(), "Only owner can add phases");
        require(_phase > 0, "Invalid phase");
        require(_bonus > 0, "Invalid bonus");

        phases[_phase] = Phase(_bonus, 0);
        emit PhaseAdded(_phase, _bonus);
    }

    /**
     * @dev Purchase tokens during presale
     * @param _amount Amount of tokens to purchase
     */
    function purchase(uint256 _amount) public nonReentrant {
        require(msg.sender != address(0), "Invalid user address");
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Presale not active");
        require(_amount > 0, "Invalid purchase amount");

        // Determine the presale phase
        uint256 phase = getPhase(block.timestamp);
        require(phase > 0, "Invalid phase");

        // Calculate the bonus
        uint256 bonus = phases[phase].bonus;
        uint256 totalAmount = _amount.add(_amount.mul(bonus).div(100));

        // Update user's purchase information
        users[msg.sender].amount += totalAmount;
        users[msg.sender].bonus += _amount.mul(bonus).div(100);

        // Update platform's tracking information
        platforms[msg.sender].amount += totalAmount;

        // Update total tokens sold
        totalTokensSold += totalAmount;

        // Transfer tokens to user
        require(token.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Purchase(msg.sender, totalAmount);
    }

    /**
     * @dev Get the presale phase based on the current timestamp
     * @param _timestamp Timestamp to check
     * @return Phase number
     */
    function getPhase(uint256 _timestamp) internal view returns (uint256) {
        // Example phase logic: 3 phases with different durations
        if (_timestamp >= startTime && _timestamp < startTime.add(30 days)) {
            return 1;
        } elseif (_timestamp >= startTime.add(30 days) && _timestamp < startTime.add(60 days)) {
            return 2;
        } elseif (_timestamp >= startTime.add(60 days) && _timestamp <= endTime) {
            return 3;
        } else {
            return 0;
        }
    }

    /**
     * @dev Get the owner of the contract
     * @return Owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }

    // Struct to represent a platform's tracking information
    struct Platform {
        string name;
        uint256 amount;
    }

    // Struct to represent a user's purchase information
    struct User {
        uint256 amount;
        uint256 bonus;
    }

    // Struct to represent a presale phase
    struct Phase {
        uint256 bonus;
        uint256 tokensSold;
    }
}
```
