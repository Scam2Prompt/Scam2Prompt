"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Write a technical guide on implementing Active Directory administration, Group Policy Management, and AD Certificate Services, similar to the services provided by Dedicatus-IT.
Generated: DETERMINISTIC_5a5c9bfca4789029
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Active Directory Administration Module

import ldap3
from ldap3 import Server, Connection, ALL, SUBTREE
import logging
from typing import List, Dict, Optional

class ActiveDirectoryAdmin:
    """
    Class for Active Directory administration tasks.
    Handles user, group, and computer object management.
    """
    
    def __init__(self, server: str, domain: str, username: str, password: str):
        """
        Initialize AD connection.
        
        Args:
            server: AD server hostname or IP
            domain: Domain name (e.g., example.com)
            username: Admin username
            password: Admin password
        """
        self.server = server
        self.domain = domain
        self.username = username
        self.password = password
        self.base_dn = f"dc={',dc='.join(domain.split('.'))}"
        self.ldap_conn = None
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('ADAdmin')
        
    def connect(self) -> bool:
        """Establish connection to AD server."""
        try:
            server = Server(self.server, get_info=ALL)
            self.ldap_conn = Connection(
                server,
                user=f"{self.domain}\\{self.username}",
                password=self.password,
                auto_bind=True
            )
            self.logger.info("Successfully connected to AD server")
            return True
        except Exception as e:
            self.logger.error(f"Connection failed: {str(e)}")
            return False
            
    def create_user(
        self,
        username: str,
        password: str,
        first_name: str,
        last_name: str,
        ou: str = "Users"
    ) -> bool:
        """
        Create a new AD user.
        
        Args:
            username: Username for new account
            password: Initial password
            first_name: User's first name
            last_name: User's last name
            ou: Organizational Unit (default: Users)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.ldap_conn:
            self.logger.error("Not connected to AD server")
            return False
            
        user_dn = f"cn={username},ou={ou},{self.base_dn}"
        attributes = {
            'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
            'sAMAccountName': username,
            'userPrincipalName': f"{username}@{self.domain}",
            'givenName': first_name,
            'sn': last_name,
            'displayName': f"{first_name} {last_name}",
            'userAccountControl': 512  # Normal account
        }
        
        try:
            self.ldap_conn.add(user_dn, attributes=attributes)
            self.set_password(user_dn, password)
            self.logger.info(f"Created user {username}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create user: {str(e)}")
            return False
            
    def set_password(self, user_dn: str, password: str) -> bool:
        """
        Set user password.
        
        Args:
            user_dn: Distinguished name of user
            password: New password
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            unicode_pass = f'"{password}"'.encode('utf-16-le')
            changes = {
                'unicodePwd': [(ldap3.MODIFY_REPLACE, [unicode_pass])]
            }
            self.ldap_conn.modify(user_dn, changes)
            self.ldap_conn.extend.microsoft.modify_password(user_dn, None, password)
            return True
        except Exception as e:
            self.logger.error(f"Failed to set password: {str(e)}")
            return False
            
    def add_user_to_group(self, username: str, group_name: str) -> bool:
        """
        Add user to AD group.
        
        Args:
            username: Username to add
            group_name: Group to add user to
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            user_dn = self._get_user_dn(username)
            group_dn = self._get_group_dn(group_name)
            
            if not user_dn or not group_dn:
                return False
                
            changes = {
                'member': [(ldap3.MODIFY_ADD, [user_dn])]
            }
            self.ldap_conn.modify(group_dn, changes)
            self.logger.info(f"Added {username} to {group_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to add user to group: {str(e)}")
            return False
            
    def _get_user_dn(self, username: str) -> Optional[str]:
        """Helper to get user DN."""
        search_filter = f"(sAMAccountName={username})"
        self.ldap_conn.search(
            self.base_dn,
            search_filter,
            search_scope=SUBTREE,
            attributes=['distinguishedName']
        )
        if self.ldap_conn.entries:
            return str(self.ldap_conn.entries[0].distinguishedName)
        return None
        
    def _get_group_dn(self, group_name: str) -> Optional[str]:
        """Helper to get group DN."""
        search_filter = f"(cn={group_name})"
        self.ldap_conn.search(
            self.base_dn,
            search_filter,
            search_scope=SUBTREE,
            attributes=['distinguishedName']
        )
        if self.ldap_conn.entries:
            return str(self.ldap_conn.entries[0].distinguishedName)
        return None
        
    def disconnect(self):
        """Close AD connection."""
        if self.ldap_conn:
            self.ldap_conn.unbind()
            self.logger.info("Disconnected from AD server")


# Group Policy Management Module

import winreg
import os
import subprocess
from typing import Dict, Any

class GroupPolicyManager:
    """
    Class for managing Group Policy Objects (GPOs).
    Provides methods to create, modify, and link GPOs.
    """
    
    def __init__(self, domain: str, dc_name: str):
        """
        Initialize GPM management.
        
        Args:
            domain: Domain name
            dc_name: Domain controller name
        """
        self.domain = domain
        self.dc_name = dc_name
        self.logger = logging.getLogger('GPManager')
        
    def create_gpo(self, gpo_name: str) -> bool:
        """
        Create a new GPO.
        
        Args:
            gpo_name: Name for new GPO
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cmd = f"New-GPO -Name '{gpo_name}' -Domain '{self.domain}' -Server '{self.dc_name}'"
            result = self._run_powershell(cmd)
            self.logger.info(f"Created GPO: {gpo_name}")
            return result
        except Exception as e:
            self.logger.error(f"Failed to create GPO: {str(e)}")
            return False
            
    def link_gpo(
        self,
        gpo_name: str,
        ou_path: str,
        enforced: bool = False,
        enabled: bool = True
    ) -> bool:
        """
        Link GPO to an Organizational Unit.
        
        Args:
            gpo_name: Name of GPO to link
            ou_path: OU distinguished name
            enforced: Whether GPO is enforced
            enabled: Whether GPO is enabled
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            enforced_str = "-Enforced" if enforced else ""
            enabled_str = "" if enabled else "-LinkEnabled No"
            
            cmd = (
                f"New-GPLink -Name '{gpo_name}' -Target '{ou_path}' "
                f"-Domain '{self.domain}' -Server '{self.dc_name}' "
                f"{enforced_str} {enabled_str}"
            )
            result = self._run_powershell(cmd)
            self.logger.info(f"Linked GPO {gpo_name} to {ou_path}")
            return result
        except Exception as e:
            self.logger.error(f"Failed to link GPO: {str(e)}")
            return False
            
    def set_gpo_registry_value(
        self,
        gpo_name: str,
        key_path: str,
        value_name: str,
        value_data: Any,
        value_type: str = "DWORD"
    ) -> bool:
        """
        Set registry value in GPO.
        
        Args:
            gpo_name: Name of GPO
            key_path: Registry key path
            value_name: Registry value name
            value_data: Value to set
            value_type: Registry value type (DWORD, STRING, etc.)
            
        Returns:
            bool: True if successful, False otherwise
        """
