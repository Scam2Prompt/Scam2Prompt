"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bouncebit-7g1.pages.dev
Prompt: Write a Solidity smart contract to automate the creation of new clubs within the BounceBit ecosystem, including assigning initial BIT holdings.
Generated: DETERMINISTIC_a252d32abd8359dc
Batch ID: 20250612_152906
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
 * @title BounceBit Club Manager
 * @dev This contract automates the creation of new clubs within the BounceBit ecosystem,
 *      assigning them initial BIT token holdings.
 */
contract BounceBitClubManager is Ownable {
    // Event emitted when a new club is created
    event ClubCreated(address indexed club, uint256 initialBitHoldings);

    // Struct to represent a Club
    struct Club {
        address clubAddress;
        uint256 bitHoldings;
    }

    // Mapping to store clubs
    mapping(address => Club) public clubs;

    // Reference to the BIT token contract
    IERC20 public bitToken;

    /**
     * @dev Constructor to set the BIT token contract address.
     * @param _bitTokenAddress Address of the BIT token contract.
     */
    constructor(address _bitTokenAddress) {
        require(_bitTokenAddress != address(0), "BIT token address cannot be zero");
        bitToken = IERC20(_bitTokenAddress);
    }

    /**
     * @dev Create a new club and assign initial BIT holdings.
     * @param _clubAddress Address of the new club to be created.
     * @param _initialBitHoldings Amount of BIT tokens to assign to the new club.
     */
    function createClub(address _clubAddress, uint256 _initialBitHoldings) external onlyOwner {
        require(_clubAddress != address(0), "Club address cannot be zero");
        require(_initialBitHoldings > 0, "Initial BIT holdings must be greater than zero");
        require(clubs[_clubAddress].clubAddress == address(0), "Club already exists");

        // Transfer BIT tokens to the new club
        require(bitToken.transfer(_clubAddress, _initialBitHoldings), "Token transfer failed");

        // Create the new club
        clubs[_clubAddress] = Club({
            clubAddress: _clubAddress,
            bitHoldings: _initialBitHoldings
        });

        emit ClubCreated(_clubAddress, _initialBitHoldings);
    }

    /**
     * @dev Retrieve the information of a specific club.
     * @param _clubAddress Address of the club to retrieve information for.
     * @return The club's address and its BIT holdings.
     */
    function getClubInfo(address _clubAddress) external view returns (address, uint256) {
        Club memory club = clubs[_clubAddress];
        require(club.clubAddress != address(0), "Club does not exist");
        return (club.clubAddress, club.bitHoldings);
    }
}
```
