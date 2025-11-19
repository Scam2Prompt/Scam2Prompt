"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tideprotocol-lamboonbase-giveaway.pages.dev
Prompt: Develop a smart contract that allows users to enter the Tide protocol's raffle by connecting their wallets and holding the specified amount of CATA tokens.
Generated: DETERMINISTIC_77b6af4373f52530
Batch ID: 20250612_162504
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
 * @title TideRaffle
 * @dev Smart contract for Tide protocol's raffle system.
 * Users can participate in the raffle by holding the required amount of CATA tokens.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract TideRaffle {
    // Address of the CATA token contract
    IERC20 public cataToken;

    // Minimum amount of CATA tokens required to enter the raffle
    uint256 public minimumCATA;

    // Owner of the contract
    address public owner;

    // Mapping to track registered participants
    mapping(address => bool) public participants;

    // Event emitted when a user enters the raffle
    event RaffleEntered(address indexed participant);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _cataToken Address of the CATA token contract.
     * @param _minimumCATA Minimum number of CATA tokens required to enter the raffle.
     */
    constructor(IERC20 _cataToken, uint256 _minimumCATA) {
        require(address(_cataToken) != address(0), "Invalid token address");
        require(_minimumCATA > 0, "Minimum CATA must be greater than zero");

        cataToken = _cataToken;
        minimumCATA = _minimumCATA;
        owner = msg.sender;
    }

    /**
     * @dev Function for users to enter the raffle.
     * Checks whether the user holds the required amount of CATA tokens.
     */
    function enterRaffle() external {
        require(!participants[msg.sender], "Already entered the raffle");
        require(
            cataToken.balanceOf(msg.sender) >= minimumCATA,
            "Insufficient CATA tokens"
        );

        // Register the user as a participant
        participants[msg.sender] = true;

        // Emit the RaffleEntered event
        emit RaffleEntered(msg.sender);
    }

    /**
     * @dev Function for the owner to update the minimum CATA requirement.
     * @param _minimumCATA New minimum CATA token requirement.
     */
    function updateMinimumCATA(uint256 _minimumCATA) external onlyOwner {
        require(_minimumCATA > 0, "Minimum CATA must be greater than zero");
        minimumCATA = _minimumCATA;
    }

    /**
     * @dev Function for the owner to transfer ownership.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
