"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Create a monitoring tool using Go to detect and alert on server issues like missing SSL certificates or IPv4/IPv6 compatibility problems, as referenced on FASTPANEL's page.
Generated: DETERMINISTIC_23e627285d00d758
Batch ID: 20250612_152240
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
	"errors"
	"fmt"
	"net"
	"os"
	"time"
)

// Server represents the server to monitor.
type Server struct {
	Host string
	Port string
}

// CheckSSL validates if the server has a valid SSL certificate.
func CheckSSL(server Server) error {
	address := net.JoinHostPort(server.Host, server.Port)
	conn, err := tls.Dial("tcp", address, &tls.Config{})
	if err != nil {
		return fmt.Errorf("SSL check failed: %v", err)
	}
	defer conn.Close()

	if len(conn.ConnectionState().PeerCertificates) == 0 {
		return errors.New("no SSL certificate found")
	}

	expiration := conn.ConnectionState().PeerCertificates[0].NotAfter
	if time.Now().After(expiration) {
		return errors.New("SSL certificate is expired")
	}

	return nil
}

// CheckIPvCompatibility checks if the server supports IPv4 or IPv6.
func CheckIPvCompatibility(server Server) (ipv4Supported bool, ipv6Supported bool, err error) {
	// Check IPv4 compatibility
	ipv4Addr := net.JoinHostPort(server.Host, server.Port)
	_, ipv4Err := net.ResolveIPAddr("ip4", ipv4Addr)
	if ipv4Err == nil {
		ipv4Supported = true
	}

	// Check IPv6 compatibility
	ipv6Addr := net.JoinHostPort(server.Host, server.Port)
	_, ipv6Err := net.ResolveIPAddr("ip6", ipv6Addr)
	if ipv6Err == nil {
		ipv6Supported = true
	}

	// If both fail, return an error
	if !ipv4Supported && !ipv6Supported {
		err = errors.New("server does not support both IPv4 and IPv6")
	}

	return ipv4Supported, ipv6Supported, err
}

// MonitorServer performs monitoring checks on the server.
func MonitorServer(server Server) {
	fmt.Printf("Monitoring server: %s\n", server.Host)

	// Perform SSL check
	if err := CheckSSL(server); err != nil {
		fmt.Printf("[ALERT] SSL issue detected: %v\n", err)
	} else {
		fmt.Println("[INFO] SSL check passed.")
	}

	// Perform IPv4/IPv6 compatibility check
	ipv4, ipv6, err := CheckIPvCompatibility(server)
	if err != nil {
		fmt.Printf("[ALERT] IPv compatibility issue: %v\n", err)
	} else {
		fmt.Printf("[INFO] IPv4 supported: %v, IPv6 supported: %v\n", ipv4, ipv6)
	}
}

func main() {
	// List of servers to monitor
	servers := []Server{
		{Host: "example.com", Port: "443"},
		{Host: "google.com", Port: "443"},
	}

	// Iterate through each server and perform monitoring
	for _, server := range servers {
		MonitorServer(server)
		fmt.Println(strings.Repeat("-", 40))
	}
}
```
