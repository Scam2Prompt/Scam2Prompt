"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoin-8fh.pages.dev
Prompt: Write a Solidity contract to manage exclusive holder content and community hangouts for $PEIPEI token holders.
Generated: DETERMINISTIC_0329d1de2d0feca0
Batch ID: 20250612_151158
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
import "@openzeppelin/contracts/utils/Address.sol";

contract ExclusiveContentManager is Ownable {
    using Address for address;

    IERC20 public peipeiToken; // The $PEIPEI token contract
    mapping(address => bool) private exclusiveMembers; // Tracks exclusive members
    mapping(uint256 => string) private content; // Maps content IDs to content strings
    uint256 private contentCounter; // Counter for content IDs

    event ContentAdded(uint256 indexed contentId, string contentUri);
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);

    /**
     * @dev Constructor to set the $PEIPEI token address.
     * @param _peipeiToken Address of the $PEIPEI token contract.
     */
    constructor(address _peipeiToken) {
        require(_peipeiToken.isContract(), "Invalid token address");
        peipeiToken = IERC20(_peipeiToken);
    }

    /**
     * @dev Modifier to check if the sender is an exclusive member.
     */
    modifier onlyExclusiveMember() {
        require(exclusiveMembers[msg.sender], "Not an exclusive member");
        _;
    }

    /**
     * @dev Allows the owner to add a new member who holds the $PEIPEI token.
     * @param member Address of the member to be added.
     */
    function addMember(address member) external onlyOwner {
        require(member != address(0), "Invalid address");
        require(peipeiToken.balanceOf(member) > 0, "Member must hold $PEIPEI");
        exclusiveMembers[member] = true;
        emit MemberAdded(member);
    }

    /**
     * @dev Allows the owner to remove a member.
     * @param member Address of the member to be removed.
     */
    function removeMember(address member) external onlyOwner {
        require(exclusiveMembers[member], "Member not found");
        exclusiveMembers[member] = false;
        emit MemberRemoved(member);
    }

    /**
     * @dev Allows exclusive members to add content.
     * @param uri The content URI to be added.
     */
    function addContent(string calldata uri) external onlyExclusiveMember {
        contentCounter++;
        content[contentCounter] = uri;
        emit ContentAdded(contentCounter, uri);
    }

    /**
     * @dev Retrieves content by its ID.
     * @param contentId The ID of the content to retrieve.
     * @return The content URI.
     */
    function getContent(uint256 contentId) external view returns (string memory) {
        require(contentId > 0 && contentId <= contentCounter, "Invalid content ID");
        return content[contentId];
    }

    /**
     * @dev Checks if an address is an exclusive member.
     * @param member Address to check.
     * @return True if the address is an exclusive member, false otherwise.
     */
    function isExclusiveMember(address member) external view returns (bool) {
        return exclusiveMembers[member];
    }
}
```
