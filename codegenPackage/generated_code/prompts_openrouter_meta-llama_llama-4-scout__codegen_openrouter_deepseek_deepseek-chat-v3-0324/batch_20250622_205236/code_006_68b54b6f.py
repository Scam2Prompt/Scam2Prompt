"""
Generated Code Metadata:
========================
Original URL: https://dfcloudpbx.com
Prompt: Create a simple EPP (Extensible Provisioning Protocol) client to manage domain registrations and configurations for a Cloud PBX provider.
Generated: DETERMINISTIC_68b54b6f83a8471f
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
import xml.etree.ElementTree as ET
from datetime import datetime

class EPPClient:
    """
    A simple EPP client for domain registration and management.
    Handles connection, login, domain operations, and logout.
    """
    
    def __init__(self, host, port, cert_file, key_file, ca_file):
        """
        Initialize EPP client with connection details and certificates.
        
        Args:
            host (str): EPP server hostname
            port (int): EPP server port
            cert_file (str): Path to client certificate file
            key_file (str): Path to client private key file
            ca_file (str): Path to CA certificate file
        """
        self.host = host
        self.port = port
        self.cert_file = cert_file
        self.key_file = key_file
        self.ca_file = ca_file
        self.socket = None
        self.context = None
        self.transaction_id = 1
        
    def connect(self):
        """
        Establish a secure connection to the EPP server.
        
        Raises:
            ssl.SSLError: If SSL handshake fails
            socket.error: If connection fails
        """
        try:
            self.context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            self.context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)
            self.context.load_verify_locations(cafile=self.ca_file)
            self.context.verify_mode = ssl.CERT_REQUIRED
            
            sock = socket.create_connection((self.host, self.port))
            self.socket = self.context.wrap_socket(sock, server_hostname=self.host)
            
            # Read greeting message
            self._read_response()
            
        except (ssl.SSLError, socket.error) as e:
            raise Exception(f"Connection failed: {str(e)}")
    
    def login(self, client_id, password):
        """
        Authenticate with the EPP server.
        
        Args:
            client_id (str): EPP client ID
            password (str): EPP password
            
        Returns:
            bool: True if login successful, False otherwise
        """
        login_xml = f"""
        <epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
            <command>
                <login>
                    <clID>{client_id}</clID>
                    <pw>{password}</pw>
                    <options>
                        <version>1.0</version>
                        <lang>en</lang>
                    </options>
                    <svcs>
                        <objURI>urn:ietf:params:xml:ns:domain-1.0</objURI>
                        <svcExtension>
                            <extURI>urn:ietf:params:xml:ns:secDNS-1.1</extURI>
                        </svcExtension>
                    </svcs>
                </login>
            </command>
            <clTRID>TRID-{self.transaction_id}</clTRID>
        </epp>
        """
        self.transaction_id += 1
        response = self._send_command(login_xml)
        return 'code="1000"' in response
    
    def logout(self):
        """
        Logout from the EPP server.
        
        Returns:
            bool: True if logout successful, False otherwise
        """
        logout_xml = """
        <epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
            <command>
                <logout/>
            </command>
            <clTRID>TRID-{}</clTRID>
        </epp>
        """.format(self.transaction_id)
        self.transaction_id += 1
        response = self._send_command(logout_xml)
        return 'code="1500"' in response
    
    def check_domain(self, domain_name):
        """
        Check domain availability.
        
        Args:
            domain_name (str): Domain name to check
            
        Returns:
            dict: Dictionary with domain availability status
        """
        check_xml = """
        <epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
            <command>
                <check>
                    <domain:check xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
                        <domain:name>{}</domain:name>
                    </domain:check>
                </check>
                <clTRID>TRID-{}</clTRID>
            </command>
        </epp>
        """.format(domain_name, self.transaction_id)
        self.transaction_id += 1
        response = self._send_command(check_xml)
        
        root = ET.fromstring(response)
        ns = {'domain': 'urn:ietf:params:xml:ns:domain-1.0'}
        avail = root.find('.//domain:cd/domain:name', ns).get('avail')
        
        return {
            'domain': domain_name,
            'available': avail == 'true'
        }
    
    def register_domain(self, domain_name, period, registrant, contacts, nameservers, ds_data=None):
        """
        Register a new domain.
        
        Args:
            domain_name (str): Domain name to register
            period (int): Registration period in years
            registrant (str): Registrant contact ID
            contacts (dict): Dictionary of contact IDs (admin, tech, billing)
            nameservers (list): List of nameserver hostnames
            ds_data (list): Optional list of DS records
            
        Returns:
            bool: True if registration successful, False otherwise
        """
        # Build nameservers XML
        ns_xml = ""
        for ns in nameservers:
            ns_xml += f"<domain:hostAttr><domain:hostName>{ns}</domain:hostName></domain:hostAttr>"
        
        # Build contacts XML
        contacts_xml = f"""
        <domain:registrant>{registrant}</domain:registrant>
        <domain:contact type="admin">{contacts.get('admin')}</domain:contact>
        <domain:contact type="tech">{contacts.get('tech')}</domain:contact>
        <domain:contact type="billing">{contacts.get('billing')}</domain:contact>
        """
        
        # Build DS data XML if provided
        sec_dns_xml = ""
        if ds_data:
            sec_dns_xml = """
            <secDNS:create xmlns:secDNS="urn:ietf:params:xml:ns:secDNS-1.1">
                <secDNS:dsData>
            """
            for ds in ds_data:
                sec_dns_xml += f"""
                <secDNS:dsData>
                    <secDNS:keyTag>{ds['key_tag']}</secDNS:keyTag>
                    <secDNS:alg>{ds['alg']}</secDNS:alg>
                    <secDNS:digestType>{ds['digest_type']}</secDNS:digestType>
                    <secDNS:digest>{ds['digest']}</secDNS:digest>
                </secDNS:dsData>
                """
            sec_dns_xml += """
                </secDNS:dsData>
            </secDNS:create>
            """
        
        register_xml = f"""
        <epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
            <command>
                <create>
                    <domain:create xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
                        <domain:name>{domain_name}</domain:name>
                        <domain:period unit="y">{period}</domain:period>
                        {contacts_xml}
                        <domain:ns>{ns_xml}</domain:ns>
                    </domain:create>
                </create>
                {sec_dns_xml}
                <clTRID>TRID-{self.transaction_id}</clTRID>
            </command>
        </epp>
        """
        self.transaction_id += 1
        response = self._send_command(register_xml)
        return 'code="1000"' in response
    
    def renew_domain(self, domain_name, current_expiry, period):
        """
        Renew a domain registration.
        
        Args:
            domain_name (str): Domain name to renew
            current_expiry (str): Current expiry date in YYYY-MM-DD format
            period (int): Renewal period in years
            
        Returns:
            bool: True if renewal successful, False otherwise
        """
        renew_xml = f"""
        <epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
            <command>
                <renew>
                    <domain:renew xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
                        <domain:name>{domain_name}</domain:name>
                        <domain:curExpDate>{current_expiry}</domain:curExpDate>
                        <domain:period unit="y">{period}</domain:period>
                    </domain:renew>
                </renew>
                <clTRID>TRID-{self.transaction_id}</clTR
