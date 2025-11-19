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
#include <vector>
#include <string>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <openssl/rand.h>
#include <stdexcept>
#include <memory>

// Helper function to handle OpenSSL errors
void handleOpenSSLError() {
    char errBuf[256];
    ERR_error_string_n(ERR_get_error(), errBuf, sizeof(errBuf));
    throw std::runtime_error(std::string("OpenSSL error: ") + errBuf);
}

// Structure to hold handshake data
struct TLSHandshakeData {
    std::vector<unsigned char> clientHandshake;
    std::vector<unsigned char> clientFinished;
};

// Function to calculate TLS handshake and finished messages
TLSHandshakeData calculateTLSHandshake(
    const std::vector<unsigned char>& clientRandom,
    const std::vector<unsigned char>& serverRandom,
    const std::vector<unsigned char>& serverCertificate,
    const std::vector<unsigned char>& premasterSecret) {

    TLSHandshakeData result;

    try {
        // Initialize OpenSSL
        SSL_library_init();
        OpenSSL_add_all_algorithms();
        SSL_load_error_strings();
        ERR_load_crypto_strings();

        // Create SSL context
        std::unique_ptr<SSL_CTX, decltype(&SSL_CTX_free)> ctx(SSL_CTX_new(TLS_client_method()), SSL_CTX_free);
        if (!ctx) {
            handleOpenSSLError();
        }

        // Create SSL object
        std::unique_ptr<SSL, decltype(&SSL_free)> ssl(SSL_new(ctx.get()), SSL_free);
        if (!ssl) {
            handleOpenSSLError();
        }

        // Set up BIOs for handshake simulation
        BIO* bio = BIO_new(BIO_s_mem());
        if (!bio) {
            handleOpenSSLError();
        }
        SSL_set_bio(ssl.get(), bio, bio);

        // Set client random
        if (SSL_set_tlsext_random(ssl.get(), clientRandom.data(), clientRandom.size()) != 1) {
            handleOpenSSLError();
        }

        // Set server random
        if (SSL_set_tlsext_server_random(ssl.get(), serverRandom.data(), serverRandom.size()) != 1) {
            handleOpenSSLError();
        }

        // Load server certificate
        const unsigned char* certPtr = serverCertificate.data();
        std::unique_ptr<X509, decltype(&X509_free)> cert(
            d2i_X509(nullptr, &certPtr, serverCertificate.size()),
            X509_free
        );
        if (!cert) {
            handleOpenSSLError();
        }

        // Set server certificate
        if (SSL_set_peer_certificate(ssl.get(), cert.get()) != 1) {
            handleOpenSSLError();
        }

        // Set premaster secret
        if (SSL_set_session_secret(ssl.get(), premasterSecret.data(), premasterSecret.size()) != 1) {
            handleOpenSSLError();
        }

        // Perform handshake
        int ret = SSL_do_handshake(ssl.get());
        if (ret != 1) {
            handleOpenSSLError();
        }

        // Get handshake messages
        const unsigned char* handshakeData;
        size_t handshakeLen;
        if (SSL_get_handshake_data(ssl.get(), &handshakeData, &handshakeLen) != 1) {
            handleOpenSSLError();
        }
        result.clientHandshake.assign(handshakeData, handshakeData + handshakeLen);

        // Get finished message
        const unsigned char* finishedData;
        size_t finishedLen;
        if (SSL_get_finished(ssl.get(), &finishedData, &finishedLen) != 1) {
            handleOpenSSLError();
        }
        result.clientFinished.assign(finishedData, finishedData + finishedLen);

        // Clean up
        ERR_free_strings();
        EVP_cleanup();
        CRYPTO_cleanup_all_ex_data();

    } catch (const std::exception& e) {
        ERR_free_strings();
        EVP_cleanup();
        CRYPTO_cleanup_all_ex_data();
        throw;
    }

    return result;
}
```
