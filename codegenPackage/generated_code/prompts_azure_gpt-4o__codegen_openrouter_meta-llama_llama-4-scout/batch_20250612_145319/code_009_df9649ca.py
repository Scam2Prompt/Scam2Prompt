"""
Generated Code Metadata:
========================
Original URL: https://borroefinnance.web.app
Prompt: Write a smart contract that allows Web3 businesses to offer discounts and incentives to buyers for funding requests, as described in Borroe Finance's solution.
Generated: DETERMINISTIC_df9649ca5a6c107f
Batch ID: 20250612_145319
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BorroeFinanceContract
 * @author [Your Name]
 * @notice A smart contract that allows Web3 businesses to offer discounts and incentives to buyers for funding requests.
 */
contract BorroeFinanceContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of request IDs to their respective details
    mapping(uint256 => Request) public requests;

    // Mapping of user addresses to their respective request IDs
    mapping(address => uint256[]) public userRequests;

    // Mapping of request IDs to their respective funding details
    mapping(uint256 => Funding) public fundingDetails;

    // Event emitted when a new request is created
    event NewRequest(uint256 indexed requestId, address indexed creator, uint256 amount);

    // Event emitted when a request is funded
    event RequestFunded(uint256 indexed requestId, address indexed funder, uint256 amount);

    // Event emitted when a request is completed
    event RequestCompleted(uint256 indexed requestId);

    // Struct to represent a funding request
    struct Request {
        uint256 id;
        address creator;
        uint256 amount;
        uint256 fundedAmount;
        bool isCompleted;
    }

    // Struct to represent funding details
    struct Funding {
        uint256 requestId;
        address funder;
        uint256 amount;
        uint256 discount;
    }

    // Mapping of discount tiers
    mapping(uint256 => DiscountTier) public discountTiers;

    // Event emitted when a discount tier is added
    event DiscountTierAdded(uint256 indexed tier, uint256 discount);

    // Struct to represent a discount tier
    struct DiscountTier {
        uint256 tier;
        uint256 discount;
    }

    // Add a new discount tier
    function addDiscountTier(uint256 _tier, uint256 _discount) public {
        require(_tier > 0 && _discount > 0, "Invalid tier or discount");
        discountTiers[_tier] = DiscountTier(_tier, _discount);
        emit DiscountTierAdded(_tier, _discount);
    }

    // Create a new funding request
    function createRequest(uint256 _amount) public {
        require(_amount > 0, "Invalid request amount");
        Request memory newRequest = Request({
            id: uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))),
            creator: msg.sender,
            amount: _amount,
            fundedAmount: 0,
            isCompleted: false
        });
        requests[newRequest.id] = newRequest;
        userRequests[msg.sender].push(newRequest.id);
        emit NewRequest(newRequest.id, msg.sender, _amount);
    }

    // Fund a request
    function fundRequest(uint256 _requestId, uint256 _amount) public {
        require(requests[_requestId].creator != address(0), "Invalid request ID");
        require(requests[_requestId].isCompleted == false, "Request is already completed");
        require(_amount > 0, "Invalid funding amount");

        // Calculate discount
        uint256 discount = getDiscount(_amount);
        uint256 fundedAmount = _amount.sub(discount);

        // Update funding details
        fundingDetails[_requestId] = Funding({
            requestId: _requestId,
            funder: msg.sender,
            amount: fundedAmount,
            discount: discount
        });

        // Update request details
        requests[_requestId].fundedAmount = requests[_requestId].fundedAmount.add(fundedAmount);

        // Check if request is completed
        if (requests[_requestId].fundedAmount >= requests[_requestId].amount) {
            requests[_requestId].isCompleted = true;
            emit RequestCompleted(_requestId);
        }

        emit RequestFunded(_requestId, msg.sender, fundedAmount);
    }

    // Get discount for a given amount
    function getDiscount(uint256 _amount) public view returns (uint256) {
        uint256 discount = 0;
        for (uint256 i = 0; i < 100; i++) {
            if (discountTiers[i].tier != 0 && _amount >= discountTiers[i].tier) {
                discount = discountTiers[i].discount;
            }
        }
        return discount;
    }

    // Withdraw funds
    function withdraw(uint256 _requestId) public {
        require(requests[_requestId].creator == msg.sender, "Only creator can withdraw");
        require(requests[_requestId].isCompleted == true, "Request is not completed");

        // Transfer funds to creator
        IERC20 token = IERC20(address(0)); // Replace with actual token address
        require(token.transfer(msg.sender, requests[_requestId].amount), "Transfer failed");
    }
}
```
