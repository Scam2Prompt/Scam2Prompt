"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Generate a diagnostic tool in Node.js to check for common server errors, including domain pointing issues and SSL certificate installation, as highlighted by FASTPANEL.
Generated: DETERMINISTIC_6f507d7cc12c3145
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const https = require('https');
const dns = require('dns');
const { exec } = require('child_process');
const fs = require('fs');
const os = require('os');

/**
 * Diagnostic tool for server health checks
 */
class ServerDiagnosticTool {
  /**
   * Initialize the diagnostic tool
   * @param {string} domain - Domain to check
   * @param {number} [port=443] - Port to check (default: 443)
   */
  constructor(domain, port = 443) {
    this.domain = domain;
    this.port = port;
    this.results = [];
  }

  /**
   * Run all diagnostic checks
   * @returns {Promise<Array>} Array of diagnostic results
   */
  async runAllChecks() {
    try {
      await this.checkDNSResolution();
      await this.checkSSLExpiry();
      await this.checkPortAccessibility();
      await this.checkServerLoad();
      await this.checkDiskSpace();
      return this.results;
    } catch (error) {
      this.logError('Failed to complete all checks', error);
      throw error;
    }
  }

  /**
   * Check if domain resolves to an IP address
   */
  async checkDNSResolution() {
    try {
      const startTime = Date.now();
      const addresses = await this.resolveDNS(this.domain);
      const duration = Date.now() - startTime;

      if (addresses.length === 0) {
        this.addResult('DNS Resolution', 'FAILED', 'Domain does not resolve to any IP address');
      } else {
        this.addResult(
          'DNS Resolution',
          'OK',
          `Resolved to: ${addresses.join(', ')} (${duration}ms)`
        );
      }
    } catch (error) {
      this.addResult('DNS Resolution', 'ERROR', error.message);
    }
  }

  /**
   * Check SSL certificate expiry
   */
  async checkSSLExpiry() {
    try {
      const options = {
        hostname: this.domain,
        port: this.port,
        method: 'GET',
        rejectUnauthorized: false,
        agent: false,
        timeout: 5000
      };

      const cert = await this.getSSLCertificate(options);
      const validTo = new Date(cert.valid_to);
      const daysLeft = Math.floor((validTo - new Date()) / (1000 * 60 * 60 * 24));

      if (daysLeft < 0) {
        this.addResult('SSL Certificate', 'EXPIRED', `Certificate expired ${Math.abs(daysLeft)} days ago`);
      } else if (daysLeft < 7) {
        this.addResult('SSL Certificate', 'WARNING', `Certificate expires in ${daysLeft} days`);
      } else {
        this.addResult('SSL Certificate', 'OK', `Valid until ${validTo.toDateString()} (${daysLeft} days remaining)`);
      }
    } catch (error) {
      this.addResult('SSL Certificate', 'ERROR', error.message);
    }
  }

  /**
   * Check if port is accessible
   */
  async checkPortAccessibility() {
    try {
      const startTime = Date.now();
      await this.testPortConnection(this.domain, this.port);
      const duration = Date.now() - startTime;

      this.addResult(
        'Port Accessibility',
        'OK',
        `Port ${this.port} is accessible (${duration}ms)`
      );
    } catch (error) {
      this.addResult(
        'Port Accessibility',
        'ERROR',
        `Port ${this.port} is not accessible: ${error.message}`
      );
    }
  }

  /**
   * Check server load
   */
  async checkServerLoad() {
    try {
      const load = os.loadavg();
      const cpus = os.cpus().length;
      const normalizedLoad = load[0] / cpus;

      let status = 'OK';
      let message = `Load average: ${load[0].toFixed(2)} (${cpus} CPUs)`;

      if (normalizedLoad > 1.5) {
        status = 'WARNING';
        message += ' - High load detected';
      } else if (normalizedLoad > 2.5) {
        status = 'CRITICAL';
        message += ' - Very high load detected';
      }

      this.addResult('Server Load', status, message);
    } catch (error) {
      this.addResult('Server Load', 'ERROR', error.message);
    }
  }

  /**
   * Check disk space
   */
  async checkDiskSpace() {
    try {
      const diskInfo = await this.getDiskSpace();
      const criticalThreshold = 10; // 10% free space
      const warningThreshold = 20; // 20% free space

      let status = 'OK';
      let message = `Free space: ${diskInfo.freePercentage.toFixed(2)}% (${diskInfo.freeGB.toFixed(2)}GB)`;

      if (diskInfo.freePercentage < criticalThreshold) {
        status = 'CRITICAL';
        message += ' - Critically low disk space';
      } else if (diskInfo.freePercentage < warningThreshold) {
        status = 'WARNING';
        message += ' - Low disk space';
      }

      this.addResult('Disk Space', status, message);
    } catch (error) {
      this.addResult('Disk Space', 'ERROR', error.message);
    }
  }

  /**
   * Resolve DNS for a domain
   * @param {string} domain 
   * @returns {Promise<Array>} Array of IP addresses
   */
  resolveDNS(domain) {
    return new Promise((resolve, reject) => {
      dns.resolve(domain, (err, addresses) => {
        if (err) {
          reject(new Error(`DNS resolution failed: ${err.message}`));
        } else {
          resolve(addresses);
        }
      });
    });
  }

  /**
   * Get SSL certificate info
   * @param {Object} options 
   * @returns {Promise<Object>} Certificate info
   */
  getSSLCertificate(options) {
    return new Promise((resolve, reject) => {
      const req = https.request(options, (res) => {
        const cert = res.socket.getPeerCertificate();
        if (!cert || Object.keys(cert).length === 0) {
          reject(new Error('No SSL certificate found'));
        } else {
          resolve(cert);
        }
      });

      req.on('error', (err) => {
        reject(new Error(`SSL certificate check failed: ${err.message}`));
      });

      req.end();
    });
  }

  /**
   * Test port connection
   * @param {string} host 
   * @param {number} port 
   * @returns {Promise<void>}
   */
  testPortConnection(host, port) {
    return new Promise((resolve, reject) => {
      const socket = require('net').Socket();
      socket.setTimeout(5000);

      socket.on('connect', () => {
        socket.destroy();
        resolve();
      });

      socket.on('timeout', () => {
        socket.destroy();
        reject(new Error('Connection timeout'));
      });

      socket.on('error', (err) => {
        socket.destroy();
        reject(err);
      });

      socket.connect(port, host);
    });
  }

  /**
   * Get disk space info
   * @returns {Promise<Object>} Disk space info
   */
  getDiskSpace() {
    return new Promise((resolve, reject) => {
      if (process.platform === 'win32') {
        exec('wmic logicaldisk get size,freespace', (error, stdout) => {
          if (error) {
            reject(new Error('Failed to get disk space info'));
            return;
          }

          const lines = stdout.trim().split('\n').slice(1);
          if (lines.length === 0) {
            reject(new Error('No disk information available'));
            return;
          }

          const [freeSpace, totalSpace] = lines[0].trim().split(/\s+/).map(Number);
          const freeGB = freeSpace / (1024 * 1024 * 1024);
          const totalGB = totalSpace / (1024 * 1024 * 1024);
          const freePercentage = (freeSpace / totalSpace) * 100;

          resolve({
            freeGB,
            totalGB,
            freePercentage
          });
        });
      } else {
        exec('df -k /', (error, stdout) => {
          if (error) {
            reject(new Error('Failed to get disk space info'));
            return;
          }

          const lines = stdout.trim().split('\n');
          if (lines.length < 2) {
            reject(new Error('No disk information available'));
            return;
          }

          const parts = lines[1].trim().split(/\s+/);
          const totalKB = parseInt(parts[1], 10);
          const usedKB = parseInt(parts[2], 10);
          const freeKB = parseInt(parts[3], 10);
          const totalGB = totalKB / (1024 * 1024);
          const freeGB = freeKB / (1024 * 1024);
          const freePercentage = (free
