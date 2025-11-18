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
	"fmt"
	"net"
	"net/http"
	"os"
	"time"
)

// MonitorConfig holds the configuration for monitoring servers
type MonitorConfig struct {
	servers []string
	timeout time.Duration
}

// NewMonitorConfig creates a new instance of MonitorConfig
func NewMonitorConfig(servers []string, timeout time.Duration) *MonitorConfig {
	return &MonitorConfig{servers: servers, timeout: timeout}
}

// CheckSSL checks if the server has a valid SSL certificate
func (mc *MonitorConfig) CheckSSL(server string) error {
	conn, err := tls.Dial("tcp", server, nil)
	if err != nil {
		return fmt.Errorf("Failed to connect to %s: %v", server, err)
	}
	defer conn.Close()

	if len(conn.ConnectionState().PeerCertificates) == 0 {
		return fmt.Errorf("No SSL certificate found for %s", server)
	}
	return nil
}

// CheckIPv4 checks if the server is accessible via IPv4
func (mc *MonitorConfig) CheckIPv4(server string) error {
	_, err := net.LookupIP(server)
	if err != nil {
		return fmt.Errorf("Failed to resolve %s: %v", server, err)
	}
	return nil
}

// CheckIPv6 checks if the server is accessible via IPv6
func (mc *MonitorConfig) CheckIPv6(server string) error {
	addrs, err := net.LookupIP(server)
	if err != nil {
		return fmt.Errorf("Failed to resolve %s: %v", server, err)
	}

	for _, addr := range addrs {
		if addr.To16() != nil && addr.To4() == nil {
			return nil // Found an IPv6 address
		}
	}
	return fmt.Errorf("No IPv6 address found for %s", server)
}

// Monitor performs the checks for each server and alerts if there are issues
func (mc *MonitorConfig) Monitor() {
	for _, server := range mc.servers {
		fmt.Printf("Checking server: %s\n", server)

		// Check SSL
		if err := mc.CheckSSL(server); err != nil {
			fmt.Printf("SSL Alert: %v\n", err)
		} else {
			fmt.Println("SSL Certificate is valid.")
		}

		// Check IPv4
		if err := mc.CheckIPv4(server); err != nil {
			fmt.Printf("IPv4 Alert: %v\n", err)
		} else {
			fmt.Println("IPv4 is reachable.")
		}

		// Check IPv6
		if err := mc.CheckIPv6(server); err != nil {
			fmt.Printf("IPv6 Alert: %v\n", err)
		} else {
			fmt.Println("IPv6 is reachable.")
		}

		fmt.Println("------------------------------------------------")
	}
}

func main() {
	// Define servers to monitor
	servers := []string{"example.com:443", "anotherexample.com:443"}
	timeout := 5 * time.Second

	// Create a new monitor configuration
	monitorConfig := NewMonitorConfig(servers, timeout)

	// Start monitoring
	monitorConfig.Monitor()
}
```
