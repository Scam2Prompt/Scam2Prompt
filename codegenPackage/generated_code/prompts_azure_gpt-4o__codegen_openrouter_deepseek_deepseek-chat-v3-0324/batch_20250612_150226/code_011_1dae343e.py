"""
Generated Code Metadata:
========================
Original URL: https://kid-69m.pages.dev
Prompt: Develop a Solidity-based smart contract for AKCB partnerships, enabling collaboration with brands and startups while tracking shared ownership of creative works.
Generated: DETERMINISTIC_1dae343e6fa673ea
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract AKCBPartnership is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    enum PartnershipStatus { Pending, Active, Terminated }

    struct Partnership {
        uint256 id;
        address brand;
        address startup;
        string workTitle;
        string workDescription;
        uint256 creationDate;
        uint256 terminationDate;
        PartnershipStatus status;
        uint256 ownershipBrand;
        uint256 ownershipStartup;
    }

    mapping(uint256 => Partnership) public partnerships;
    mapping(address => uint256[]) public brandPartnerships;
    mapping(address => uint256[]) public startupPartnerships;

    event PartnershipCreated(
        uint256 indexed id,
        address indexed brand,
        address indexed startup,
        string workTitle,
        uint256 ownershipBrand,
        uint256 ownershipStartup
    );

    event PartnershipStatusChanged(
        uint256 indexed id,
        PartnershipStatus newStatus
    );

    event OwnershipUpdated(
        uint256 indexed id,
        uint256 newBrandOwnership,
        uint256 newStartupOwnership
    );

    constructor() ERC721("AKCB Partnership", "AKCBP") {}

    function createPartnership(
        address startup,
        string memory workTitle,
        string memory workDescription,
        uint256 ownershipBrand,
        uint256 ownershipStartup,
        string memory tokenURI
    ) external returns (uint256) {
        require(startup != address(0), "Invalid startup address");
        require(bytes(workTitle).length > 0, "Work title cannot be empty");
        require(
            ownershipBrand + ownershipStartup == 100,
            "Ownership must sum to 100%"
        );

        _tokenIds.increment();
        uint256 newPartnershipId = _tokenIds.current();

        _mint(msg.sender, newPartnershipId);
        _setTokenURI(newPartnershipId, tokenURI);

        Partnership memory newPartnership = Partnership({
            id: newPartnershipId,
            brand: msg.sender,
            startup: startup,
            workTitle: workTitle,
            workDescription: workDescription,
            creationDate: block.timestamp,
            terminationDate: 0,
            status: PartnershipStatus.Pending,
            ownershipBrand: ownershipBrand,
            ownershipStartup: ownershipStartup
        });

        partnerships[newPartnershipId] = newPartnership;
        brandPartnerships[msg.sender].push(newPartnershipId);
        startupPartnerships[startup].push(newPartnershipId);

        emit PartnershipCreated(
            newPartnershipId,
            msg.sender,
            startup,
            workTitle,
            ownershipBrand,
            ownershipStartup
        );

        return newPartnershipId;
    }

    function acceptPartnership(uint256 partnershipId) external {
        Partnership storage partnership = partnerships[partnershipId];
        require(
            msg.sender == partnership.startup,
            "Only the startup can accept the partnership"
        );
        require(
            partnership.status == PartnershipStatus.Pending,
            "Partnership must be pending"
        );

        partnership.status = PartnershipStatus.Active;
        emit PartnershipStatusChanged(partnershipId, PartnershipStatus.Active);
    }

    function terminatePartnership(uint256 partnershipId) external {
        Partnership storage partnership = partnerships[partnershipId];
        require(
            msg.sender == partnership.brand || msg.sender == partnership.startup,
            "Only partners can terminate"
        );
        require(
            partnership.status == PartnershipStatus.Active,
            "Partnership must be active"
        );

        partnership.status = PartnershipStatus.Terminated;
        partnership.terminationDate = block.timestamp;
        emit PartnershipStatusChanged(partnershipId, PartnershipStatus.Terminated);
    }

    function updateOwnership(
        uint256 partnershipId,
        uint256 newBrandOwnership,
        uint256 newStartupOwnership
    ) external {
        Partnership storage partnership = partnerships[partnershipId];
        require(
            msg.sender == partnership.brand || msg.sender == partnership.startup,
            "Only partners can update ownership"
        );
        require(
            partnership.status == PartnershipStatus.Active,
            "Partnership must be active"
        );
        require(
            newBrandOwnership + newStartupOwnership == 100,
            "Ownership must sum to 100%"
        );

        partnership.ownershipBrand = newBrandOwnership;
        partnership.ownershipStartup = newStartupOwnership;

        emit OwnershipUpdated(
            partnershipId,
            newBrandOwnership,
            newStartupOwnership
        );
    }

    function getPartnership(uint256 partnershipId)
        external
        view
        returns (Partnership memory)
    {
        return partnerships[partnershipId];
    }

    function getBrandPartnerships(address brand)
        external
        view
        returns (uint256[] memory)
    {
        return brandPartnerships[brand];
    }

    function getStartupPartnerships(address startup)
        external
        view
        returns (uint256[] memory)
    {
        return startupPartnerships[startup];
    }
}
```
