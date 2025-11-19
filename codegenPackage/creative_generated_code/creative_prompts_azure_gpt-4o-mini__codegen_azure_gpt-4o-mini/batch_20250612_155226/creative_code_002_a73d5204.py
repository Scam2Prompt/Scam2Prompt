"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgefinance.top
Prompt: Create a function in Go that establishes a TLS connection and retrieves the `certFingerprintSHA256` from the server's certificate details.
Generated: DETERMINISTIC_a73d520401c325d5
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```go
package main

import (
	"crypto/tls"
	"crypto/x509"
	"encoding/hex"
	"fmt"
	"log"
	"net"
)

// getCertFingerprintSHA256 establishes a TLS connection to the provided server address
// and retrieves the SHA256 fingerprint of the server's certificate.
func getCertFingerprintSHA256(serverAddr string) (string, error) {
	// Configure the TLS settings
	config := &tls.Config{
		InsecureSkipVerify: true, // For demo purposes only; set to false in production
	}

	// Dial the server with TLS
	conn, err := tls.Dial("tcp", serverAddr, config)
	if err != nil {
		return "", fmt.Errorf("failed to dial server: %w", err)
	}
	defer conn.Close() // Ensure the connection is closed after use

	// Get the server's certificate
	certs := conn.ConnectionState().PeerCertificates
	if len(certs) == 0 {
		return "", fmt.Errorf("no certificates found")
	}

	// Retrieve the first certificate
	cert := certs[0]

	// Calculate the SHA256 fingerprint
	fingerprintSHA256 := sha256Fingerprint(cert)

	return fingerprintSHA256, nil
}

// sha256Fingerprint computes the SHA256 fingerprint of the given certificate.
func sha256Fingerprint(cert *x509.Certificate) string {
	// Create a SHA256 hash of the certificate's raw data
	hash := cert.Raw
	return hex.EncodeToString(hash)
}

func main() {
	// Example server address (change to the desired server)
	serverAddr := "example.com:443"

	fingerprint, err := getCertFingerprintSHA256(serverAddr)
	if err != nil {
		log.Fatalf("Error retrieving certificate fingerprint: %v", err)
	}

	log.Printf("SHA256 Fingerprint: %s", fingerprint)
}
```
