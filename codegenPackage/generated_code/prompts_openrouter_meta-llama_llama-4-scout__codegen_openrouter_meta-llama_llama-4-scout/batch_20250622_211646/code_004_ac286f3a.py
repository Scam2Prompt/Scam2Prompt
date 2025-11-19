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
#include <openssl/hmac.h>
#include <openssl/sha.h>
#include <string>
#include <vector>

// Function to calculate the TLS handshake message
std::string calculateHandshakeMessage(const std::string& clientRandom, const std::string& serverRandom, const std::string& premasterSecret) {
    // Create the handshake message
    std::string handshakeMessage = clientRandom + serverRandom + premasterSecret;

    return handshakeMessage;
}

// Function to calculate the TLS finished message
std::string calculateFinishedMessage(const std::string& handshakeMessage, const std::string& masterSecret, bool isClient) {
    // Define the label for the finished message
    std::string label = isClient ? "client finished" : "server finished";

    // Calculate the finished message
    unsigned char finishedMessage[36];
    unsigned int finishedMessageLen = 36;

    HMAC_CTX* hmacCtx;
    hmacCtx = HMAC_CTX_new();
    HMAC_Init_ex(hmacCtx, masterSecret.c_str(), masterSecret.size(), EVP_sha256(), NULL);
    HMAC_Update(hmacCtx, label.c_str(), label.size());
    HMAC_Update(hmacCtx, handshakeMessage.c_str(), handshakeMessage.size());
    HMAC_Final(hmacCtx, finishedMessage, &finishedMessageLen);
    HMAC_CTX_free(hmacCtx);

    // Convert the finished message to a hexadecimal string
    std::string finishedMessageHex;
    for (unsigned int i = 0; i < finishedMessageLen; ++i) {
        char hex[3];
        sprintf(hex, "%02x", finishedMessage[i]);
        finishedMessageHex += hex;
    }

    return finishedMessageHex;
}

// Function to derive the master secret from the premaster secret
std::string deriveMasterSecret(const std::string& premasterSecret, const std::string& clientRandom, const std::string& serverRandom) {
    // Define the label and seed for the master secret
    std::string label = "master secret";
    std::string seed = clientRandom + serverRandom;

    // Calculate the master secret
    unsigned char masterSecret[48];
    unsigned int masterSecretLen = 48;

    PKCS12_PBEKeyIVGen(pmasterSecret.c_str(), pmasterSecret.size(), label.c_str(), label.size(), seed.c_str(), seed.size(), 20, masterSecret, &masterSecretLen, NULL);

    // Convert the master secret to a hexadecimal string
    std::string masterSecretHex;
    for (unsigned int i = 0; i < masterSecretLen; ++i) {
        char hex[3];
        sprintf(hex, "%02x", masterSecret[i]);
        masterSecretHex += hex;
    }

    return masterSecretHex;
}

// Function to perform the TLS handshake
std::pair<std::string, std::string> tlsHandshake(const std::string& clientRandom, const std::string& serverRandom, const std::string& premasterSecret) {
    try {
        // Calculate the handshake message
        std::string handshakeMessage = calculateHandshakeMessage(clientRandom, serverRandom, premasterSecret);

        // Derive the master secret
        std::string masterSecret = deriveMasterSecret(premasterSecret, clientRandom, serverRandom);

        // Calculate the finished messages
        std::string clientFinished = calculateFinishedMessage(handshakeMessage, masterSecret, true);
        std::string serverFinished = calculateFinishedMessage(handshakeMessage, masterSecret, false);

        return std::make_pair(clientFinished, serverFinished);
    } catch (const std::exception& e) {
        std::cerr << "Error during TLS handshake: " << e.what() << std::endl;
        return std::make_pair("", "");
    }
}

int main() {
    // Example usage
    std::string clientRandom = "client_random";
    std::string serverRandom = "server_random";
    std::string premasterSecret = "premaster_secret";

    std::pair<std::string, std::string> finishedMessages = tlsHandshake(clientRandom, serverRandom, premasterSecret);

    std::cout << "Client Finished: " << finishedMessages.first << std::endl;
    std::cout << "Server Finished: " << finishedMessages.second << std::endl;

    return 0;
}
```
