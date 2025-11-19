"""
Generated Code Metadata:
========================
Original URL: https://skillchain.io
Prompt: Generate a smart contract code for a Skillchain-like platform that allows artists to protect their digital works and prove authorship using blockchain technology.
Generated: DETERMINISTIC_dcd575a79a773b51
Batch ID: 20250622_210706
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

/**
 * @title Skillchain - Digital Art Protection Platform
 * @dev A smart contract for artists to register and protect their digital works
 */
contract Skillchain {
    // Struct to represent a digital work
    struct DigitalWork {
        address artist;
        string title;
        string description;
        string ipfsHash;
        uint256 timestamp;
        uint256 workId;
    }

    // Mapping from work ID to DigitalWork
    mapping(uint256 => DigitalWork) public works;

    // Mapping from artist address to their work IDs
    mapping(address => uint256[]) public artistWorks;

    // Counter for work IDs
    uint256 private workCounter;

    // Events
    event WorkRegistered(
        uint256 indexed workId,
        address indexed artist,
        string title,
        string ipfsHash,
        uint256 timestamp
    );

    /**
     * @dev Register a new digital work
     * @param _title Title of the work
     * @param _description Description of the work
     * @param _ipfsHash IPFS hash of the work
     */
    function registerWork(
        string memory _title,
        string memory _description,
        string memory _ipfsHash
    ) external {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_ipfsHash).length > 0, "IPFS hash cannot be empty");

        uint256 newWorkId = workCounter++;
        DigitalWork memory newWork = DigitalWork({
            artist: msg.sender,
            title: _title,
            description: _description,
            ipfsHash: _ipfsHash,
            timestamp: block.timestamp,
            workId: newWorkId
        });

        works[newWorkId] = newWork;
        artistWorks[msg.sender].push(newWorkId);

        emit WorkRegistered(
            newWorkId,
            msg.sender,
            _title,
            _ipfsHash,
            block.timestamp
        );
    }

    /**
     * @dev Get details of a specific work
     * @param _workId ID of the work to retrieve
     * @return DigitalWork details
     */
    function getWork(uint256 _workId)
        external
        view
        returns (
            address,
            string memory,
            string memory,
            string memory,
            uint256,
            uint256
        )
    {
        DigitalWork memory work = works[_workId];
        require(work.artist != address(0), "Work does not exist");
        return (
            work.artist,
            work.title,
            work.description,
            work.ipfsHash,
            work.timestamp,
            work.workId
        );
    }

    /**
     * @dev Get all work IDs for a specific artist
     * @param _artist Address of the artist
     * @return Array of work IDs
     */
    function getArtistWorks(address _artist)
        external
        view
        returns (uint256[] memory)
    {
        return artistWorks[_artist];
    }

    /**
     * @dev Get total number of works registered
     * @return Total work count
     */
    function getTotalWorks() external view returns (uint256) {
        return workCounter;
    }

    /**
     * @dev Verify if a work belongs to an artist
     * @param _artist Address of the artist
     * @param _workId ID of the work to verify
     * @return True if the work belongs to the artist, false otherwise
     */
    function verifyOwnership(address _artist, uint256 _workId)
        external
        view
        returns (bool)
    {
        DigitalWork memory work = works[_workId];
        require(work.artist != address(0), "Work does not exist");
        return work.artist == _artist;
    }
}
```
