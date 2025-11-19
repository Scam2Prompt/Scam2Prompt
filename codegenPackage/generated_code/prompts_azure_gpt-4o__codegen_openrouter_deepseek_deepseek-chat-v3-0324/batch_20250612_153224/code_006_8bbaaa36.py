"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Provide a Python script to test internet connection speed (400/10Mbps Ethernet) and ensure stable live connections for voiceover work, as outlined on Eric Navarro's website.
Generated: DETERMINISTIC_8bbaaa363eb040a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import speedtest
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('connection_test.log'),
        logging.StreamHandler()
    ]
)

def test_speed():
    """Test download and upload speed using speedtest.net"""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        logging.info("Testing download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        logging.info(f"Download speed: {download_speed:.2f} Mbps")
        
        logging.info("Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        logging.info(f"Upload speed: {upload_speed:.2f} Mbps")
        
        return download_speed, upload_speed
    except Exception as e:
        logging.error(f"Speed test failed: {str(e)}")
        return None, None

def check_latency(host="8.8.8.8", count=5):
    """Check network latency by pinging a host"""
    try:
        import subprocess
        output = subprocess.run(
            ["ping", "-c", str(count), host],
            capture_output=True,
            text=True
        )
        
        if output.returncode == 0:
            lines = output.stdout.split('\n')
            latency_line = lines[-2]
            latency_values = latency_line.split('=')[1].split('/')
            min_latency = float(latency_values[0].strip().split(' ')[0])
            avg_latency = float(latency_values[1].strip())
            max_latency = float(latency_values[2].strip().split(' ')[0])
            
            logging.info(f"Latency (min/avg/max): {min_latency:.2f}/{avg_latency:.2f}/{max_latency:.2f} ms")
            return avg_latency
        else:
            logging.error(f"Ping failed with return code {output.returncode}")
            return None
    except Exception as e:
        logging.error(f"Latency check failed: {str(e)}")
        return None

def check_packet_loss(host="8.8.8.8", count=20):
    """Check packet loss by pinging a host"""
    try:
        import subprocess
        output = subprocess.run(
            ["ping", "-c", str(count), host],
            capture_output=True,
            text=True
        )
        
        if output.returncode == 0:
            lines = output.stdout.split('\n')
            stats_line = lines[-2]
            packet_loss = float(stats_line.split(',')[2].split('%')[0].strip())
            logging.info(f"Packet loss: {packet_loss}%")
            return packet_loss
        else:
            logging.error(f"Ping failed with return code {output.returncode}")
            return None
    except Exception as e:
        logging.error(f"Packet loss check failed: {str(e)}")
        return None

def check_jitter(host="8.8.8.8", count=20):
    """Calculate jitter (variation in latency)"""
    try:
        import subprocess
        output = subprocess.run(
            ["ping", "-c", str(count), host],
            capture_output=True,
            text=True
        )
        
        if output.returncode == 0:
            lines = output.stdout.split('\n')
            latency_line = lines[-2]
            latency_values = latency_line.split('=')[1].split('/')
            jitter = float(latency_values[3].strip().split(' ')[0])
            logging.info(f"Jitter: {jitter:.2f} ms")
            return jitter
        else:
            logging.error(f"Ping failed with return code {output.returncode}")
            return None
    except Exception as e:
        logging.error(f"Jitter calculation failed: {str(e)}")
        return None

def evaluate_connection(download_speed, upload_speed, avg_latency, packet_loss, jitter):
    """Evaluate if connection meets requirements for voiceover work"""
    requirements_met = True
    issues = []
    
    # Check download speed (minimum 10Mbps recommended)
    if download_speed < 10:
        requirements_met = False
        issues.append(f"Download speed ({download_speed:.2f} Mbps) below recommended 10Mbps")
    
    # Check upload speed (minimum 1Mbps recommended)
    if upload_speed < 1:
        requirements_met = False
        issues.append(f"Upload speed ({upload_speed:.2f} Mbps) below recommended 1Mbps")
    
    # Check latency (maximum 100ms recommended)
    if avg_latency > 100:
        requirements_met = False
        issues.append(f"Latency ({avg_latency:.2f} ms) above recommended 100ms")
    
    # Check packet loss (maximum 1% recommended)
    if packet_loss > 1:
        requirements_met = False
        issues.append(f"Packet loss ({packet_loss}%) above recommended 1%")
    
    # Check jitter (maximum 30ms recommended)
    if jitter > 30:
        requirements_met = False
        issues.append(f"Jitter ({jitter:.2f} ms) above recommended 30ms")
    
    if requirements_met:
        logging.info("Connection meets requirements for professional voiceover work")
    else:
        logging.warning("Connection does NOT meet requirements:")
        for issue in issues:
            logging.warning(f"- {issue}")
    
    return requirements_met, issues

def main():
    """Main function to run connection tests"""
    logging.info("Starting connection quality test...")
    
    # Run speed test
    download_speed, upload_speed = test_speed()
    if download_speed is None or upload_speed is None:
        logging.error("Aborting further tests due to speed test failure")
        return
    
    # Run latency test
    avg_latency = check_latency()
    if avg_latency is None:
        logging.error("Aborting further tests due to latency test failure")
        return
    
    # Run packet loss test
    packet_loss = check_packet_loss()
    if packet_loss is None:
        logging.error("Aborting further tests due to packet loss test failure")
        return
    
    # Run jitter test
    jitter = check_jitter()
    if jitter is None:
        logging.error("Aborting further tests due to jitter test failure")
        return
    
    # Evaluate results
    evaluate_connection(download_speed, upload_speed, avg_latency, packet_loss, jitter)
    
    logging.info("Connection quality test completed")

if __name__ == "__main__":
    main()
```
