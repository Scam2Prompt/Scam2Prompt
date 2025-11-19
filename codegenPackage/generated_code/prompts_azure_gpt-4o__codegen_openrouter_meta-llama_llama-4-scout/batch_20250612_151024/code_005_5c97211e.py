"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Generate a Solidity contract for managing artist token presales on the GrooveUP platform. Include functionality for seed funding and token allocation based on the provided tokenomics.
Generated: DETERMINISTIC_5c97211ebcbea0cf
Batch ID: 20250612_151024
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GrooveUP Presale Contract
 * @author [Your Name]
 * @notice This contract manages artist token presales on the GrooveUP platform.
 */
contract GrooveUPPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of artist addresses to their presale information
    mapping(address => PresaleInfo) public presales;

    // Mapping of token addresses to their allocation information
    mapping(address => TokenAllocation) public tokenAllocations;

    // Event emitted when a new presale is created
    event PresaleCreated(address indexed artist, uint256 seedFunding, uint256 tokenAllocation);

    // Event emitted when a presale is funded
    event PresaleFunded(address indexed artist, uint256 amount);

    // Event emitted when tokens are allocated
    event TokensAllocated(address indexed artist, address indexed token, uint256 amount);

    // Struct to store presale information
    struct PresaleInfo {
        uint256 seedFunding;
        uint256 tokenAllocation;
        uint256 fundedAmount;
        bool isActive;
    }

    // Struct to store token allocation information
    struct TokenAllocation {
        uint256 allocatedAmount;
        uint256 claimedAmount;
    }

    /**
     * @notice Creates a new presale for an artist.
     * @param _artist The address of the artist.
     * @param _seedFunding The seed funding amount.
     * @param _tokenAllocation The token allocation amount.
     */
    function createPresale(address _artist, uint256 _seedFunding, uint256 _tokenAllocation) public {
        require(_artist != address(0), "Artist address cannot be zero");
        require(_seedFunding > 0, "Seed funding must be greater than zero");
        require(_tokenAllocation > 0, "Token allocation must be greater than zero");

        presales[_artist] = PresaleInfo(_seedFunding, _tokenAllocation, 0, true);
        emit PresaleCreated(_artist, _seedFunding, _tokenAllocation);
    }

    /**
     * @notice Funds a presale for an artist.
     * @param _artist The address of the artist.
     * @param _amount The amount to fund.
     */
    function fundPresale(address _artist, uint256 _amount) public nonReentrant {
        require(_artist != address(0), "Artist address cannot be zero");
        require(presales[_artist].isActive, "Presale is not active");
        require(_amount > 0, "Funding amount must be greater than zero");

        presales[_artist].fundedAmount = presales[_artist].fundedAmount.add(_amount);
        emit PresaleFunded(_artist, _amount);
    }

    /**
     * @notice Allocates tokens to an artist.
     * @param _artist The address of the artist.
     * @param _token The address of the token.
     * @param _amount The amount of tokens to allocate.
     */
    function allocateTokens(address _artist, address _token, uint256 _amount) public {
        require(_artist != address(0), "Artist address cannot be zero");
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Token amount must be greater than zero");

        TokenAllocation storage allocation = tokenAllocations[_token];
        allocation.allocatedAmount = allocation.allocatedAmount.add(_amount);
        emit TokensAllocated(_artist, _token, _amount);
    }

    /**
     * @notice Claims allocated tokens for an artist.
     * @param _artist The address of the artist.
     * @param _token The address of the token.
     * @param _amount The amount of tokens to claim.
     */
    function claimTokens(address _artist, address _token, uint256 _amount) public {
        require(_artist != address(0), "Artist address cannot be zero");
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Token amount must be greater than zero");

        TokenAllocation storage allocation = tokenAllocations[_token];
        require(allocation.allocatedAmount >= _amount, "Not enough allocated tokens");
        require(allocation.claimedAmount.add(_amount) <= allocation.allocatedAmount, "Cannot claim more than allocated");

        allocation.claimedAmount = allocation.claimedAmount.add(_amount);

        // Transfer tokens to artist
        ERC20(_token).transfer(_artist, _amount);
    }

    /**
     * @notice Deactivates a presale for an artist.
     * @param _artist The address of the artist.
     */
    function deactivatePresale(address _artist) public {
        require(_artist != address(0), "Artist address cannot be zero");
        require(presales[_artist].isActive, "Presale is not active");

        presales[_artist].isActive = false;
    }
}
```
