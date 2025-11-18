"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.berafi.xyz
Prompt: Develop a smart contract function to automate token vesting for users claiming tokens through the BERAFI Claim Portal.
Generated: DETERMINISTIC_fae2d45007b4dc49
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the implementation of a Solidity smart contract function for token vesting as part of a claim portal, adhering to the requested requirements.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenVesting
 * @dev A smart contract to automate token vesting for users claiming tokens.
 */
contract TokenVesting {
    // ERC20 Token interface
    IERC20 private immutable token;

    // Struct to store vesting data for each user
    struct Vesting {
        uint256 amount;       // Total amount of tokens to vest
        uint256 claimed;      // Amount of tokens already claimed
        uint256 startTime;    // Vesting start time
        uint256 duration;     // Vesting duration in seconds
    }

    // Mapping from user address to their vesting details
    mapping(address => Vesting) private vestings;

    // Events
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor for initializing the token contract.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Function to set up vesting for a user.
     * @param _user Address of the user.
     * @param _amount Total amount of tokens to vest.
     * @param _startTime Vesting start time (timestamp).
     * @param _duration Vesting duration in seconds.
     */
    function setupVesting(
        address _user,
        uint256 _amount,
        uint256 _startTime,
        uint256 _duration
    ) external {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");
        require(_startTime >= block.timestamp, "Start time must be in the future");
        require(_duration > 0, "Duration must be greater than zero");

        // Ensure the user does not already have an active vesting setup
        require(vestings[_user].amount == 0, "Vesting already set for this user");

        // Transfer tokens to the contract for vesting
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record vesting details
        vestings[_user] = Vesting({
            amount: _amount,
            claimed: 0,
            startTime: _startTime,
            duration: _duration
        });
    }

    /**
     * @dev Function for users to claim vested tokens.
     */
    function claimTokens() external {
        Vesting storage vesting = vestings[msg.sender];
        
        // Ensure the user has an active vesting setup
        require(vesting.amount > 0, "No active vesting found");
        
        // Calculate the amount of tokens available for claiming
        uint256 elapsedTime = block.timestamp > vesting.startTime
            ? block.timestamp - vesting.startTime
            : 0;
        uint256 totalVested = (vesting.amount * elapsedTime) / vesting.duration;
        uint256 claimable = totalVested - vesting.claimed;

        // Ensure there are tokens available to claim
        require(claimable > 0, "No tokens available for claiming");
        
        // Update the claimed amount
        vesting.claimed += claimable;
        
        // Transfer the claimable tokens to the user
        require(token.transfer(msg.sender, claimable), "Token transfer failed");
        
        // Emit an event
        emit TokensClaimed(msg.sender, claimable);
    }

    /**
     * @dev Function to retrieve vesting details.
     * @param _user Address of the user whose vesting details are requested.
     * @return amount Total amount of tokens to vest.
     * @return claimed Amount of tokens already claimed.
     * @return startTime Vesting start time.
     * @return duration Vesting duration in seconds.
     */
    function getVestingDetails(address _user)
        external
        view
        returns (
            uint256 amount,
            uint256 claimed,
            uint256 startTime,
            uint256 duration
        )
    {
        Vesting memory vesting = vestings[_user];
        return (vesting.amount, vesting.claimed, vesting.startTime, vesting.duration);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
