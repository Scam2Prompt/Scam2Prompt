"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layeralorg.pages.dev
Prompt: Write code to mint and redeem LayerAI Data Capsules as NFTs, ensuring compatibility with both ERC-20 and BEP-20 token standards.
Generated: DETERMINISTIC_8fcc7353d7ec6a65
Batch ID: 20250612_151141
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

// Import OpenZeppelin libraries for ERC721, ERC20, and Access Control.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract LayerAIDataCapsuleNFT is ERC721, AccessControl {
    // Define constants for roles
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant REDEEMER_ROLE = keccak256("REDEEMER_ROLE");

    uint256 private _currentTokenId; // Tracks the last minted token ID
    mapping(uint256 => string) private _capsuleData; // Stores data associated with each NFT

    // Address of the ERC-20/BEP-20 token for payments (e.g., LayerAI Tokens)
    IERC20 private paymentToken;

    // Event emitted when a data capsule NFT is minted
    event DataCapsuleMinted(address indexed recipient, uint256 tokenId, string data);

    // Event emitted when a data capsule NFT is redeemed
    event DataCapsuleRedeemed(address indexed owner, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract.
     * @param _paymentTokenAddress Address of the ERC-20/BEP-20 compatible token.
     */
    constructor(address _paymentTokenAddress) ERC721("LayerAI Data Capsule", "LADC") {
        require(_paymentTokenAddress != address(0), "Invalid token address");
        paymentToken = IERC20(_paymentTokenAddress);

        // Grant default admin role to the contract deployer
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /**
     * @dev Mint a new LayerAI Data Capsule NFT.
     * @param recipient Address of the recipient.
     * @param data Associated data for the NFT.
     * @param paymentAmount Amount of ERC-20/BEP-20 tokens for payment.
     */
    function mintDataCapsule(
        address recipient,
        string memory data,
        uint256 paymentAmount
    ) external onlyRole(MINTER_ROLE) {
        require(recipient != address(0), "Invalid recipient address");
        require(paymentAmount > 0, "Payment amount must be greater than zero");

        // Transfer payment tokens from the sender to the contract
        bool success = paymentToken.transferFrom(msg.sender, address(this), paymentAmount);
        require(success, "Payment token transfer failed");

        // Increment the token ID counter and mint the NFT
        _currentTokenId++;
        _safeMint(recipient, _currentTokenId);

        // Store associated data for the capsule
        _capsuleData[_currentTokenId] = data;

        emit DataCapsuleMinted(recipient, _currentTokenId, data);
    }

    /**
     * @dev Redeem an existing LayerAI Data Capsule NFT.
     * @param tokenId ID of the NFT to redeem.
     */
    function redeemDataCapsule(uint256 tokenId) external onlyRole(REDEEMER_ROLE) {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");

        // Burn the NFT
        _burn(tokenId);

        // Clear associated data
        delete _capsuleData[tokenId];

        emit DataCapsuleRedeemed(msg.sender, tokenId);
    }

    /**
     * @dev Get the data associated with a specific NFT.
     * @param tokenId ID of the NFT.
     * @return Associated data for the NFT.
     */
    function getCapsuleData(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _capsuleData[tokenId];
    }

    /**
     * @dev Override supportsInterface to include AccessControl interfaces.
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override(ERC721, AccessControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
