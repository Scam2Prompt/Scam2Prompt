"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Create a monitoring tool using Go to detect and alert on server issues like missing SSL certificates or IPv4/IPv6 compatibility problems, as referenced on FASTPANEL's page.
Generated: DETERMINISTIC_23e627285d00d758
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
package main

import (
	"crypto/tls"
	"fmt"
	"net"
	"net/http"
	"time"
)

// ServerMonitor is a struct that holds the configuration for monitoring.
type ServerMonitor struct {
	Host string
	Port string
}

// NewServerMonitor creates a new instance of ServerMonitor.
func NewServerMonitor(host, port string) *ServerMonitor {
	return &ServerMonitor{
		Host: host,
		Port: port,
	}
}

// CheckSSL checks if the server has a valid SSL certificate.
func (sm *ServerMonitor) CheckSSL() error {
	conn, err := tls.Dial("tcp", fmt.Sprintf("%s:%s", sm.Host, sm.Port), nil)
	if err != nil {
		return fmt.Errorf("SSL check failed: %v", err)
	}
	defer conn.Close()

	// Check the certificate's validity
	for _, cert := range conn.ConnectionState().PeerCertificates {
		if time.Now().After(cert.NotAfter) {
			return fmt.Errorf("SSL certificate expired: %s", cert.Subject.CommonName)
		}
	}
	return nil
}

// CheckIPv4 checks if the server is reachable via IPv4.
func (sm *ServerMonitor) CheckIPv4() error {
	_, err := net.LookupIP(sm.Host)
	if err != nil {
		return fmt.Errorf("IPv4 check failed: %v", err)
	}
	return nil
}

// CheckIPv6 checks if the server is reachable via IPv6.
func (sm *ServerMonitor) CheckIPv6() error {
	ips, err := net.LookupIP(sm.Host)
	if err != nil {
		return fmt.Errorf("IPv6 check failed: %v", err)
	}

	for _, ip := range ips {
		if ip.To4() == nil {
			return nil // Found an IPv6 address
		}
	}
	return fmt.Errorf("No IPv6 address found for host: %s", sm.Host)
}

// Monitor performs the checks and alerts if any issues are found.
func (sm *ServerMonitor) Monitor() {
	if err := sm.CheckSSL(); err != nil {
		fmt.Println("Alert:", err)
	}

	if err := sm.CheckIPv4(); err != nil {
		fmt.Println("Alert:", err)
	}

	if err := sm.CheckIPv6(); err != nil {
		fmt.Println("Alert:", err)
	}
}

func main() {
	// Define the server to monitor
	host := "example.com" // Replace with the actual host
	port := "443"         // Default HTTPS port

	monitor := NewServerMonitor(host, port)

	// Run the monitoring tool
	monitor.Monitor()
}
```
