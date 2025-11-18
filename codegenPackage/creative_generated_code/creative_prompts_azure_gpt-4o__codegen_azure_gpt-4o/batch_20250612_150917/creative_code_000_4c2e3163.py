"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Write a smart contract example using the Data Ownership Protocol (DOP) to selectively disclose ERC20 token holdings while maintaining privacy for other assets.
Generated: DETERMINISTIC_4c2e3163ef95d776
Batch ID: 20250612_150917
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
 * @title SelectiveDisclosure
 * @dev Smart contract to enable selective disclosure of ERC20 token holdings
 * using the Data Ownership Protocol (DOP) principles, while maintaining privacy
 * for other assets.
 */
contract SelectiveDisclosure {
    // Struct to store disclosure requests
    struct DisclosureRequest {
        address requester;
        address tokenAddress;
        bool approved;
    }

    // Mapping of token holder to disclosure requests
    mapping(address => DisclosureRequest[]) public disclosureRequests;

    /**
     * @dev Event triggered when a disclosure request is created.
     * @param requester Address of the requester.
     * @param holder Address of the token holder.
     * @param tokenAddress Address of the ERC20 token requested.
     */
    event DisclosureRequested(
        address indexed requester,
        address indexed holder,
        address indexed tokenAddress
    );

    /**
     * @dev Event triggered when a disclosure request is approved.
     * @param requester Address of the requester.
     * @param holder Address of the token holder.
     * @param tokenAddress Address of the ERC20 token approved for disclosure.
     * @param balance The disclosed token balance.
     */
    event DisclosureApproved(
        address indexed requester,
        address indexed holder,
        address indexed tokenAddress,
        uint256 balance
    );

    /**
     * @dev Allows a requester to create a disclosure request for a token holder's ERC20 balance.
     * @param holder Address of the token holder.
     * @param tokenAddress Address of the ERC20 token.
     */
    function requestDisclosure(address holder, address tokenAddress) external {
        require(holder != address(0), "Invalid holder address.");
        require(tokenAddress != address(0), "Invalid token address.");

        DisclosureRequest memory newRequest = DisclosureRequest({
            requester: msg.sender,
            tokenAddress: tokenAddress,
            approved: false
        });

        disclosureRequests[holder].push(newRequest);

        emit DisclosureRequested(msg.sender, holder, tokenAddress);
    }

    /**
     * @dev Allows a token holder to approve a disclosure request, revealing their balance.
     * @param index Index of the disclosure request in the holder's array.
     */
    function approveDisclosure(uint256 index) external {
        require(index < disclosureRequests[msg.sender].length, "Invalid index.");

        DisclosureRequest storage request = disclosureRequests[msg.sender][index];
        require(!request.approved, "Request already approved.");

        request.approved = true;

        uint256 balance = getERC20Balance(msg.sender, request.tokenAddress);

        emit DisclosureApproved(request.requester, msg.sender, request.tokenAddress, balance);
    }

    /**
     * @dev Retrieves the ERC20 token balance of a given holder.
     * @param holder Address of the token holder.
     * @param tokenAddress Address of the ERC20 token.
     * @return balance The token holder's balance.
     */
    function getERC20Balance(address holder, address tokenAddress) internal view returns (uint256 balance) {
        try IERC20(tokenAddress).balanceOf(holder) returns (uint256 tokenBalance) {
            return tokenBalance;
        } catch {
            return 0; // Return 0 if the call fails (e.g., non-compliant ERC20 contract)
        }
    }
}

/**
 * @dev Minimal interface for ERC20 token contract.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
