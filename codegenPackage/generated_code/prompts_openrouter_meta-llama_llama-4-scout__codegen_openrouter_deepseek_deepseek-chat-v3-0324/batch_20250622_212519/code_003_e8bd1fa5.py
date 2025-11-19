"""
Generated Code Metadata:
========================
Original URL: https://make1518999.cc
Prompt: Generate a code example for batch processing multiple assets, including ERC20 tokens, NFTs, and native tokens, using a blockchain asset management platform.
Generated: DETERMINISTIC_e8bd1fa53dc4460f
Batch ID: 20250622_212519
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title BatchAssetProcessor
 * @dev A contract for batch processing multiple asset types (ERC20, ERC721, native tokens)
 */
contract BatchAssetProcessor is ReentrancyGuard {
    using Address for address payable;

    event BatchTransferCompleted(address indexed sender, uint256 totalTransactions);
    event AssetTransferFailed(address indexed asset, address indexed recipient, uint256 amountOrTokenId, string reason);

    /**
     * @dev Batch transfer ERC20 tokens to multiple recipients
     * @param token The ERC20 token contract address
     * @param recipients Array of recipient addresses
     * @param amounts Array of amounts to transfer (1:1 mapping with recipients)
     */
    function batchTransferERC20(
        IERC20 token,
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external nonReentrant {
        require(recipients.length == amounts.length, "Mismatched arrays");
        require(recipients.length > 0, "No recipients");

        uint256 totalAmount = 0;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        require(token.transferFrom(msg.sender, address(this), totalAmount), "Initial transfer failed");

        for (uint256 i = 0; i < recipients.length; i++) {
            try token.transfer(recipients[i], amounts[i]) {
                // Success
            } catch Error(string memory reason) {
                emit AssetTransferFailed(address(token), recipients[i], amounts[i], reason);
            } catch {
                emit AssetTransferFailed(address(token), recipients[i], amounts[i], "Unknown error");
            }
        }

        emit BatchTransferCompleted(msg.sender, recipients.length);
    }

    /**
     * @dev Batch transfer ERC721 tokens to multiple recipients
     * @param nft The ERC721 token contract address
     * @param recipients Array of recipient addresses
     * @param tokenIds Array of token IDs to transfer (1:1 mapping with recipients)
     */
    function batchTransferERC721(
        IERC721 nft,
        address[] calldata recipients,
        uint256[] calldata tokenIds
    ) external nonReentrant {
        require(recipients.length == tokenIds.length, "Mismatched arrays");
        require(recipients.length > 0, "No recipients");

        for (uint256 i = 0; i < recipients.length; i++) {
            try nft.safeTransferFrom(msg.sender, recipients[i], tokenIds[i]) {
                // Success
            } catch Error(string memory reason) {
                emit AssetTransferFailed(address(nft), recipients[i], tokenIds[i], reason);
            } catch {
                emit AssetTransferFailed(address(nft), recipients[i], tokenIds[i], "Unknown error");
            }
        }

        emit BatchTransferCompleted(msg.sender, recipients.length);
    }

    /**
     * @dev Batch transfer native tokens (ETH) to multiple recipients
     * @param recipients Array of recipient addresses
     * @param amounts Array of amounts to transfer (1:1 mapping with recipients)
     */
    function batchTransferNative(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external payable nonReentrant {
        require(recipients.length == amounts.length, "Mismatched arrays");
        require(recipients.length > 0, "No recipients");

        uint256 totalAmount = 0;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        require(msg.value == totalAmount, "Incorrect ETH amount");

        for (uint256 i = 0; i < recipients.length; i++) {
            try payable(recipients[i]).sendValue(amounts[i]) {
                // Success
            } catch Error(string memory reason) {
                emit AssetTransferFailed(address(0), recipients[i], amounts[i], reason);
            } catch {
                emit AssetTransferFailed(address(0), recipients[i], amounts[i], "Unknown error");
            }
        }

        emit BatchTransferCompleted(msg.sender, recipients.length);
    }

    /**
     * @dev Batch transfer mixed assets (ERC20, ERC721, native) in a single transaction
     * @param erc20Data Tuple of (token, recipients, amounts) for ERC20 transfers
     * @param erc721Data Tuple of (nft, recipients, tokenIds) for ERC721 transfers
     * @param nativeData Tuple of (recipients, amounts) for native transfers
     * @param nativeValue Total native token value to be sent
     */
    function batchTransferMixed(
        (IERC20 token, address[] recipients, uint256[] amounts) calldata erc20Data,
        (IERC721 nft, address[] recipients, uint256[] tokenIds) calldata erc721Data,
        (address[] recipients, uint256[] amounts) calldata nativeData,
        uint256 nativeValue
    ) external payable nonReentrant {
        require(msg.value == nativeValue, "Incorrect ETH amount");

        // Process ERC20 transfers
        if (erc20Data.recipients.length > 0) {
            batchTransferERC20(erc20Data.token, erc20Data.recipients, erc20Data.amounts);
        }

        // Process ERC721 transfers
        if (erc721Data.recipients.length > 0) {
            batchTransferERC721(erc721Data.nft, erc721Data.recipients, erc721Data.tokenIds);
        }

        // Process native transfers
        if (nativeData.recipients.length > 0) {
            batchTransferNative(nativeData.recipients, nativeData.amounts);
        }
    }
}
```
