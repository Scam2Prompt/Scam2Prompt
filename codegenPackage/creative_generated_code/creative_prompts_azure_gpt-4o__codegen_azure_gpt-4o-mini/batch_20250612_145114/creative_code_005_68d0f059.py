"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: Implement a DNS resolver in Go that uses Google Public DNS servers (8.8.8.8 and 2001:4860:4860::8844) to resolve domain names.
Generated: DETERMINISTIC_68d0f059bf4d9704
Batch ID: 20250612_145114
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
	"context"
	"fmt"
	"net"
	"time"
)

// DNSResolver is a struct that holds the DNS servers to be used for resolution.
type DNSResolver struct {
	servers []string
}

// NewDNSResolver creates a new DNSResolver with the provided DNS servers.
func NewDNSResolver(servers []string) *DNSResolver {
	return &DNSResolver{servers: servers}
}

// Resolve resolves a domain name to its IP addresses using the configured DNS servers.
func (r *DNSResolver) Resolve(ctx context.Context, domain string) ([]net.IP, error) {
	var ips []net.IP

	// Iterate over each configured DNS server
	for _, server := range r.servers {
		// Create a custom DNS resolver with a timeout
		resolver := &net.Resolver{
			PreferGo: true,
			Dial: func(ctx context.Context, network, addr string) (net.Conn, error) {
				// Set a timeout for the DNS resolution
				ctx, cancel := context.WithTimeout(ctx, 2*time.Second)
				defer cancel()
				return net.Dialer{Timeout: 2 * time.Second}.DialContext(ctx, network, addr)
			},
		}

		// Perform the DNS resolution
		ips, err := resolver.LookupIP(ctx, "ip", domain)
		if err != nil {
			// Log the error and continue to the next server
			fmt.Printf("Error resolving %s with server %s: %v\n", domain, server, err)
			continue
		}

		// If successful, return the resolved IPs
		return ips, nil
	}

	return nil, fmt.Errorf("all DNS servers failed to resolve %s", domain)
}

func main() {
	// Define Google Public DNS servers
	dnsServers := []string{"8.8.8.8:53", "2001:4860:4860::8844:53"}

	// Create a new DNS resolver
	resolver := NewDNSResolver(dnsServers)

	// Define the domain to resolve
	domain := "example.com"

	// Create a context for the resolution
	ctx := context.Background()

	// Resolve the domain
	ips, err := resolver.Resolve(ctx, domain)
	if err != nil {
		fmt.Printf("Failed to resolve domain %s: %v\n", domain, err)
		return
	}

	// Print the resolved IP addresses
	fmt.Printf("Resolved IPs for %s: %v\n", domain, ips)
}
```
