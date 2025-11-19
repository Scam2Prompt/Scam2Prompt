"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: "Create a C++ function to calculate the TLS handshake and finished messages, similar to the 'clientHandshake' and 'clientFinished' fields in the JSON object."
Generated: DETERMINISTIC_ac286f3a086e5d56
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <openssl/hmac.h>
#include <openssl/evp.h>

// Function to calculate the TLS handshake and finished messages
std::pair<std::string, std::string> calculateTLSHandshakeAndFinished(
    const std::string& clientHello, 
    const std::string& serverHello, 
    const std::string& preMasterSecret) 
{
    try {
        // Initialize OpenSSL
        SSL_library_init();
        OpenSSL_add_all_algorithms();
        ERR_load_crypto_strings();

        // Derive master secret from pre-master secret
        const std::string masterSecretLabel = "master secret";
        unsigned char masterSecret[48]; // Master secret is 48 bytes
        if (!HMAC(EVP_sha256(), preMasterSecret.data(), preMasterSecret.size(),
                  reinterpret_cast<const unsigned char*>(masterSecretLabel.data()), masterSecretLabel.size(),
                  masterSecret, nullptr)) {
            throw std::runtime_error("Failed to derive master secret.");
        }

        // Concatenate clientHello and serverHello for handshake hash
        std::string handshakeMessages = clientHello + serverHello;

        // Calculate handshake hash
        unsigned char handshakeHash[EVP_MAX_MD_SIZE];
        unsigned int handshakeHashLen = 0;
        EVP_MD_CTX* mdctx = EVP_MD_CTX_new();
        if (!mdctx || !EVP_DigestInit_ex(mdctx, EVP_sha256(), nullptr) ||
            !EVP_DigestUpdate(mdctx, handshakeMessages.data(), handshakeMessages.size()) ||
            !EVP_DigestFinal_ex(mdctx, handshakeHash, &handshakeHashLen)) {
            EVP_MD_CTX_free(mdctx);
            throw std::runtime_error("Failed to calculate handshake hash.");
        }
        EVP_MD_CTX_free(mdctx);

        // Derive finished message from master secret and handshake hash
        const std::string finishedLabel = "client finished";
        unsigned char finishedMessage[EVP_MAX_MD_SIZE];
        if (!HMAC(EVP_sha256(), masterSecret, sizeof(masterSecret),
                  handshakeHash, handshakeHashLen,
                  finishedMessage, nullptr)) {
            throw std::runtime_error("Failed to derive finished message.");
        }

        // Convert handshake hash and finished message to hex strings
        auto toHexString = [](const unsigned char* data, size_t len) -> std::string {
            std::string hexString;
            for (size_t i = 0; i < len; ++i) {
                char buf[3];
                snprintf(buf, sizeof(buf), "%02x", data[i]);
                hexString += buf;
            }
            return hexString;
        };

        std::string handshakeHashHex = toHexString(handshakeHash, handshakeHashLen);
        std::string finishedMessageHex = toHexString(finishedMessage, EVP_MD_size(EVP_sha256()));

        return {handshakeHashHex, finishedMessageHex};
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return {"", ""};
    }
}

int main() {
    // Example inputs
    std::string clientHello = "ClientHelloMessage";
    std::string serverHello = "ServerHelloMessage";
    std::string preMasterSecret = "PreMasterSecretKey";

    // Calculate handshake and finished messages
    auto [handshakeHash, finishedMessage] = calculateTLSHandshakeAndFinished(clientHello, serverHello, preMasterSecret);

    // Output results
    std::cout << "Handshake Hash: " << handshakeHash << std::endl;
    std::cout << "Finished Message: " << finishedMessage << std::endl;

    return 0;
}
```
