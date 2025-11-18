"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardtevara.xyz
Prompt: Create a smart contract to manage utility NFTs for a web3 gaming ecosystem, incorporating ZK Stack for enhanced performance.
Generated: DETERMINISTIC_8392629029bd02d4
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Importing OpenZeppelin libraries for ERC721 and AccessControl
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

// Importing Zero-Knowledge-related libraries
import "@zk-stack/contracts/ZKVerifier.sol"; // Replace with correct ZK library for your stack

/**
 * @title UtilityNFT
 * @dev A smart contract for managing utility NFTs in a web3 gaming ecosystem
 *      with Zero-Knowledge proof capabilities for enhanced performance.
 */
contract UtilityNFT is ERC721URIStorage, AccessControl {
    // Define roles for admin and minters
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

    // Event emitted when a ZK proof is verified
    event ZKProofVerified(address indexed user, uint256 indexed tokenId);

    // Reference to ZK Verifier contract
    ZKVerifier public zkVerifier;

    // Counter to assign unique token IDs
    uint256 private _tokenIdCounter;

    /**
     * @dev Constructor initializes the NFT contract with a name and symbol,
     *      sets the default admin, and configures the ZK Verifier.
     * @param name The name of the NFT collection.
     * @param symbol The symbol for the NFT collection.
     * @param verifierAddress Address of the ZK Verifier contract.
     */
    constructor(string memory name, string memory symbol, address verifierAddress) ERC721(name, symbol) {
        require(verifierAddress != address(0), "Verifier address cannot be zero");

        // Assign roles
        _setupRole(ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);

        // Set ZK Verifier contract
        zkVerifier = ZKVerifier(verifierAddress);

        // Initialize token counter
        _tokenIdCounter = 1; // Start token IDs from 1 (not 0)
    }

    /**
     * @dev Function for minting a new NFT.
     *      Only users with MINTER_ROLE can mint.
     * @param to Address to receive the NFT.
     * @param tokenURI URI pointing to the metadata for the NFT.
     */
    function mint(address to, string memory tokenURI) external onlyRole(MINTER_ROLE) {
        require(to != address(0), "Invalid recipient address");

        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter += 1;

        // Mint the NFT
        _safeMint(to, tokenId);

        // Set metadata URI
        _setTokenURI(tokenId, tokenURI);
    }

    /**
     * @dev Verifies a Zero-Knowledge proof for a user and emits an event if successful.
     * @param proof The Zero-Knowledge proof to verify.
     * @param user Address of the user providing the proof.
     * @param tokenId Associated token ID for which proof is verified.
     */
    function verifyZKProof(bytes calldata proof, address user, uint256 tokenId) external {
        require(user != address(0), "Invalid user address");
        require(_exists(tokenId), "Token does not exist");

        // Verify the Zero-Knowledge proof
        bool isValid = zkVerifier.verifyProof(proof);
        require(isValid, "Invalid ZK proof");

        // Emit event signaling proof verification
        emit ZKProofVerified(user, tokenId);
    }

    /**
     * @dev Override isApprovedForAll to allow the admin to bypass approvals.
     * @param owner NFT owner address.
     * @param operator Operator address.
     * @return True if the operator is approved for all NFTs, false otherwise.
     */
    function isApprovedForAll(address owner, address operator) public view override returns (bool) {
        // Allow admins to bypass approvals
        if (hasRole(ADMIN_ROLE, operator)) {
            return true;
        }

        return super.isApprovedForAll(owner, operator);
    }

    /**
     * @dev Modifier to restrict access to admin-only functionality.
     */
    modifier onlyAdmin() {
        require(hasRole(ADMIN_ROLE, msg.sender), "Caller is not an admin");
        _;
    }

    /**
     * @dev Allows the admin to set a new ZK Verifier contract address.
     * @param verifierAddress Address of the new ZK Verifier contract.
     */
    function setZKVerifier(address verifierAddress) external onlyAdmin {
        require(verifierAddress != address(0), "Verifier address cannot be zero");
        zkVerifier = ZKVerifier(verifierAddress);
    }
}
```
