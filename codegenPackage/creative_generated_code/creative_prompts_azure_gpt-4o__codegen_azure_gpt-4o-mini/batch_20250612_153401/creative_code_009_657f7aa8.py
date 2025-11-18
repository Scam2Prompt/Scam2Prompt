"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Write a smart contract on Aleph Zero that facilitates private fundraising for enterprises using zero-knowledge proof solutions.
Generated: DETERMINISTIC_657f7aa8a8bf5d7b
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PrivateFundraising
 * @dev A smart contract to facilitate private fundraising for enterprises using zero-knowledge proofs.
 */
contract PrivateFundraising is Ownable {
    // Struct to hold fundraising details
    struct Fundraiser {
        uint256 targetAmount;
        uint256 raisedAmount;
        bool isActive;
        address payable enterprise;
    }

    // Mapping for fundraisers by their ID
    mapping(uint256 => Fundraiser) public fundraisers;
    uint256 public fundraiserCount;

    // Event emitted when a fundraiser is created
    event FundraiserCreated(uint256 indexed fundraiserId, address indexed enterprise, uint256 targetAmount);
    
    // Event emitted when a contribution is made
    event ContributionMade(uint256 indexed fundraiserId, address indexed contributor, uint256 amount);
    
    // Event emitted when a fundraiser is completed successfully
    event FundraiserCompleted(uint256 indexed fundraiserId);

    /**
     * @dev Creates a new fundraiser.
     * @param _targetAmount The target amount for the fundraiser.
     */
    function createFundraiser(uint256 _targetAmount) external onlyOwner {
        require(_targetAmount > 0, "Target amount must be greater than zero");
        
        // Increment fundraiser count and create a new fundraiser
        fundraiserCount++;
        fundraisers[fundraiserCount] = Fundraiser({
            targetAmount: _targetAmount,
            raisedAmount: 0,
            isActive: true,
            enterprise: payable(msg.sender)
        });

        emit FundraiserCreated(fundraiserCount, msg.sender, _targetAmount);
    }

    /**
     * @dev Allows contributions to a fundraiser.
     * @param _fundraiserId The ID of the fundraiser.
     */
    function contribute(uint256 _fundraiserId) external payable {
        Fundraiser storage fundraiser = fundraisers[_fundraiserId];
        
        // Ensure the fundraiser exists and is active
        require(_fundraiserId > 0 && _fundraiserId <= fundraiserCount, "Invalid fundraiser ID");
        require(fundraiser.isActive, "Fundraiser is not active");
        require(msg.value > 0, "Contribution must be greater than zero");
        
        // Update the raised amount
        fundraiser.raisedAmount += msg.value;

        // Check if the fundraising target has been reached
        if (fundraiser.raisedAmount >= fundraiser.targetAmount) {
            fundraiser.isActive = false; // Mark the fundraiser as completed
            emit FundraiserCompleted(_fundraiserId);
        }

        emit ContributionMade(_fundraiserId, msg.sender, msg.value);
    }

    /**
     * @dev Withdraws funds to the enterprise once the fundraising is complete.
     * @param _fundraiserId The ID of the fundraiser.
     */
    function withdrawFunds(uint256 _fundraiserId) external {
        Fundraiser storage fundraiser = fundraisers[_fundraiserId];

        // Ensure the fundraiser is completed and the caller is the enterprise
        require(!fundraiser.isActive, "Fundraiser is still active");
        require(msg.sender == fundraiser.enterprise, "Only the enterprise can withdraw");

        // Transfer the raised amount to the enterprise
        uint256 amount = fundraiser.raisedAmount;
        fundraiser.raisedAmount = 0; // Reset raised amount to prevent re-entrancy
        (bool success, ) = fundraiser.enterprise.call{value: amount}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("Direct ether transfers not allowed");
    }

    /**
     * @dev Function to get the details of a fundraiser.
     * @param _fundraiserId The ID of the fundraiser.
     * @return targetAmount The target amount for the fundraiser.
     * @return raisedAmount The amount raised so far.
     * @return isActive The active status of the fundraiser.
     * @return enterprise The address of the enterprise managing the fundraiser.
     */
    function getFundraiserDetails(uint256 _fundraiserId) external view returns (
        uint256 targetAmount,
        uint256 raisedAmount,
        bool isActive,
        address enterprise
    ) {
        Fundraiser memory fundraiser = fundraisers[_fundraiserId];
        return (fundraiser.targetAmount, fundraiser.raisedAmount, fundraiser.isActive, fundraiser.enterprise);
    }
}
```
