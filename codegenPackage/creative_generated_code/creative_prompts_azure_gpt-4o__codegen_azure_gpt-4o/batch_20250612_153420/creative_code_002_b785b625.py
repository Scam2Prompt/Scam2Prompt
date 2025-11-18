"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-4dm.pages.dev
Prompt: Create a Solidity smart contract that allows protocols to offer incentives to veAERO voters to attract votes and build liquidity, as outlined on Aerodrome Finance.
Generated: DETERMINISTIC_b785b6251526a411
Batch ID: 20250612_153420
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

/**
 * @title IncentiveManager
 * @dev This smart contract allows protocols to offer incentives to veAERO voters to attract votes and build liquidity.
 *      It is designed for compatibility with Aerodrome Finance.
 */
contract IncentiveManager {
    // Struct to store incentive details
    struct Incentive {
        address protocol;  // Address of the protocol offering the incentive
        uint256 amount;    // Total amount of incentive tokens
        uint256 startTime; // Start time for the incentive program
        uint256 endTime;   // End time for the incentive program
        string description; // Description of the incentive program
        bool isActive;      // Whether the incentive program is active
    }

    // Mapping to store incentives
    mapping(uint256 => Incentive) public incentives;

    // Counter to keep track of incentive IDs
    uint256 public incentiveCounter;

    // Token used for incentives
    IERC20 public incentiveToken;

    // Events
    event IncentiveCreated(
        uint256 indexed incentiveId,
        address indexed protocol,
        uint256 amount,
        uint256 startTime,
        uint256 endTime,
        string description
    );
    event IncentiveClaimed(address indexed voter, uint256 indexed incentiveId, uint256 amount);
    event IncentiveDeactivated(uint256 indexed incentiveId);

    /**
     * @dev Modifier to ensure the caller is the protocol offering the incentive.
     * @param incentiveId ID of the incentive program.
     */
    modifier onlyProtocol(uint256 incentiveId) {
        require(incentives[incentiveId].protocol == msg.sender, "Caller is not the protocol");
        _;
    }

    /**
     * @dev Constructor to initialize the incentive token.
     * @param _incentiveToken Address of the ERC20 token used for incentives.
     */
    constructor(address _incentiveToken) {
        require(_incentiveToken != address(0), "Invalid token address");
        incentiveToken = IERC20(_incentiveToken);
    }

    /**
     * @dev Function to create a new incentive program.
     * @param amount Total amount of tokens to be used for the incentive.
     * @param startTime Start time for the incentive program.
     * @param endTime End time for the incentive program.
     * @param description Description of the incentive program.
     */
    function createIncentive(
        uint256 amount,
        uint256 startTime,
        uint256 endTime,
        string memory description
    ) external {
        require(amount > 0, "Incentive amount must be greater than zero");
        require(startTime < endTime, "Invalid time range");
        require(incentiveToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        incentiveCounter++;
        incentives[incentiveCounter] = Incentive({
            protocol: msg.sender,
            amount: amount,
            startTime: startTime,
            endTime: endTime,
            description: description,
            isActive: true
        });

        emit IncentiveCreated(incentiveCounter, msg.sender, amount, startTime, endTime, description);
    }

    /**
     * @dev Function to claim incentive tokens for veAERO voters.
     * @param incentiveId ID of the incentive program being claimed.
     * @param voter Address of the voter claiming the incentive.
     * @param amount Amount of tokens to claim.
     */
    function claimIncentive(uint256 incentiveId, address voter, uint256 amount) external onlyProtocol(incentiveId) {
        Incentive storage incentive = incentives[incentiveId];
        require(incentive.isActive, "Incentive program is not active");
        require(block.timestamp >= incentive.startTime, "Incentive program has not started yet");
        require(block.timestamp <= incentive.endTime, "Incentive program has ended");
        require(amount <= incentive.amount, "Insufficient incentive tokens");

        incentive.amount -= amount;
        require(incentiveToken.transfer(voter, amount), "Token transfer failed");

        emit IncentiveClaimed(voter, incentiveId, amount);
    }

    /**
     * @dev Function to deactivate an incentive program.
     * @param incentiveId ID of the incentive program to deactivate.
     */
    function deactivateIncentive(uint256 incentiveId) external onlyProtocol(incentiveId) {
        Incentive storage incentive = incentives[incentiveId];
        require(incentive.isActive, "Incentive program is already inactive");

        incentive.isActive = false;

        emit IncentiveDeactivated(incentiveId);
    }

    /**
     * @dev Interface for ERC20 tokens.
     */
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
