"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Design a Solana-based NFT project with a unique tokenomics system, including token allocation tiers and NFT airdrops.
Generated: DETERMINISTIC_d66e91ec160b118e
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SolanaNFTProject is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Tokenomics parameters
    struct Tier {
        uint256 allocation;
        uint256 price;
        uint256 maxSupply;
        uint256 minted;
    }

    // NFT metadata
    struct NFTMetadata {
        string name;
        string description;
        string imageURI;
        uint256 tier;
    }

    // Project parameters
    IERC20 public paymentToken;
    mapping(uint256 => Tier) public tiers;
    mapping(uint256 => NFTMetadata) public nftMetadata;
    mapping(address => bool) public whitelist;
    mapping(address => uint256) public userAllocation;
    mapping(uint256 => address) public tokenOwners;
    bool public airdropActive;
    uint256 public airdropAmount;
    uint256 public totalAirdropped;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, uint256 tier);
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event WhitelistUpdated(address indexed user, bool status);
    event TierAdded(uint256 tierId, uint256 allocation, uint256 price, uint256 maxSupply);

    constructor(
        string memory name,
        string memory symbol,
        address _paymentToken
    ) ERC721(name, symbol) {
        paymentToken = IERC20(_paymentToken);
        airdropActive = false;
    }

    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Not whitelisted");
        _;
    }

    function addTier(
        uint256 tierId,
        uint256 allocation,
        uint256 price,
        uint256 maxSupply
    ) external onlyOwner {
        require(tiers[tierId].allocation == 0, "Tier already exists");
        tiers[tierId] = Tier(allocation, price, maxSupply, 0);
        emit TierAdded(tierId, allocation, price, maxSupply);
    }

    function updateWhitelist(address user, bool status) external onlyOwner {
        whitelist[user] = status;
        emit WhitelistUpdated(user, status);
    }

    function mintNFT(uint256 tierId) external onlyWhitelisted {
        Tier storage tier = tiers[tierId];
        require(tier.allocation > 0, "Tier does not exist");
        require(tier.minted < tier.maxSupply, "Tier max supply reached");
        require(
            paymentToken.transferFrom(msg.sender, address(this), tier.price),
            "Payment failed"
        );

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        tier.minted += 1;
        userAllocation[msg.sender] += tier.allocation;
        tokenOwners[tokenId] = msg.sender;

        emit NFTMinted(msg.sender, tokenId, tierId);
    }

    function setNFTMetadata(
        uint256 tokenId,
        string memory name,
        string memory description,
        string memory imageURI,
        uint256 tier
    ) external onlyOwner {
        require(_exists(tokenId), "NFT does not exist");
        nftMetadata[tokenId] = NFTMetadata(name, description, imageURI, tier);
    }

    function startAirdrop(uint256 amount) external onlyOwner {
        airdropAmount = amount;
        airdropActive = true;
    }

    function stopAirdrop() external onlyOwner {
        airdropActive = false;
    }

    function claimAirdrop() external {
        require(airdropActive, "Airdrop not active");
        require(userAllocation[msg.sender] > 0, "No allocation");

        uint256 amount = (userAllocation[msg.sender] * airdropAmount) / 100;
        require(
            paymentToken.transfer(msg.sender, amount),
            "Airdrop transfer failed"
        );

        totalAirdropped += amount;
        emit AirdropClaimed(msg.sender, amount);
    }

    function withdrawFunds() external onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        require(
            paymentToken.transfer(owner(), balance),
            "Withdrawal failed"
        );
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        NFTMetadata memory metadata = nftMetadata[tokenId];
        return string(abi.encodePacked(
            "data:application/json;base64,",
            base64Encode(bytes(string(abi.encodePacked(
                '{"name":"', metadata.name, '",',
                '"description":"', metadata.description, '",',
                '"image":"', metadata.imageURI, '",',
                '"tier":"', Strings.toString(metadata.tier), '"}'
            ))))
        ));
    }

    function base64Encode(bytes memory data) internal pure returns (string memory) {
        if (data.length == 0) return "";
        bytes memory table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        uint256 encodedLen = 4 * ((data.length + 2) / 3);
        bytes memory result = new bytes(encodedLen + 32);
        assembly {
            let tablePtr := add(table, 1)
            let resultPtr := add(result, 32)
            for {
                let i := 0
            } lt(i, data.length) {
            } {
                i := add(i, 3)
                let input := mload(add(data, i))
                mstore8(resultPtr, mload(add(tablePtr, and(shr(18, input), 0x3F))))
                mstore8(add(resultPtr, 1), mload(add(tablePtr, and(shr(12, input), 0x3F))))
                mstore8(add(resultPtr, 2), mload(add(tablePtr, and(shr(6, input), 0x3F))))
                mstore8(add(resultPtr, 3), mload(add(tablePtr, and(input, 0x3F))))
                resultPtr := add(resultPtr, 4)
            }
            switch mod(data.length, 3)
            case 1 {
                mstore8(sub(resultPtr, 2), 0x3d)
                mstore8(sub(resultPtr, 1), 0x3d)
            }
            case 2 {
                mstore8(sub(resultPtr, 1), 0x3d)
            }
        }
        return string(result);
    }
}
```
