"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Provide code examples for setting up and managing user accounts and passwords in a Windows network environment, based on WF Computing's expertise in network administration.
Generated: DETERMINISTIC_0912ba381d5b9167
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Account Management in Windows Network Environment**
===========================================================

**Prerequisites**
---------------

* Python 3.8+
* `pywinrm` library for Windows Remote Management
* `ldap3` library for LDAP operations

**Code**
------

### user_account_management.py
```python
import ldap3
from ldap3.core.exceptions import LDAPException
import pywinrm

# Define constants
DOMAIN_CONTROLLER = 'your_domain_controller'
DOMAIN_NAME = 'your_domain_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

def create_user_account(username, password, email):
    """
    Create a new user account in the Windows network environment.

    Args:
        username (str): The username for the new account.
        password (str): The password for the new account.
        email (str): The email address for the new account.

    Returns:
        bool: True if the account was created successfully, False otherwise.
    """
    try:
        # Establish an LDAP connection
        server = ldap3.Server(DOMAIN_CONTROLLER)
        connection = ldap3.Connection(server, user=USERNAME, password=PASSWORD, auto_bind=True)

        # Create a new user account
        user_dn = f'CN={username},OU=Users,DC={DOMAIN_NAME}'
        connection.add(user_dn, 'user', [
            ('objectClass', 'user'),
            ('cn', username),
            ('sn', username),
            ('givenName', username),
            ('mail', email),
            ('userPassword', password)
        ])

        # Set the user account control flags
        connection.modify(user_dn, [('userAccountControl', '512')])  # 512 = normal account

        return True

    except LDAPException as e:
        print(f'LDAP error: {e}')
        return False

    finally:
        connection.unbind()

def reset_user_password(username, new_password):
    """
    Reset the password for an existing user account.

    Args:
        username (str): The username for the account to reset.
        new_password (str): The new password for the account.

    Returns:
        bool: True if the password was reset successfully, False otherwise.
    """
    try:
        # Establish an LDAP connection
        server = ldap3.Server(DOMAIN_CONTROLLER)
        connection = ldap3.Connection(server, user=USERNAME, password=PASSWORD, auto_bind=True)

        # Reset the user password
        user_dn = f'CN={username},OU=Users,DC={DOMAIN_NAME}'
        connection.modify(user_dn, [('userPassword', new_password)])

        return True

    except LDAPException as e:
        print(f'LDAP error: {e}')
        return False

    finally:
        connection.unbind()

def enable_user_account(username):
    """
    Enable an existing user account.

    Args:
        username (str): The username for the account to enable.

    Returns:
        bool: True if the account was enabled successfully, False otherwise.
    """
    try:
        # Establish an LDAP connection
        server = ldap3.Server(DOMAIN_CONTROLLER)
        connection = ldap3.Connection(server, user=USERNAME, password=PASSWORD, auto_bind=True)

        # Enable the user account
        user_dn = f'CN={username},OU=Users,DC={DOMAIN_NAME}'
        connection.modify(user_dn, [('userAccountControl', '512')])  # 512 = normal account

        return True

    except LDAPException as e:
        print(f'LDAP error: {e}')
        return False

    finally:
        connection.unbind()

def disable_user_account(username):
    """
    Disable an existing user account.

    Args:
        username (str): The username for the account to disable.

    Returns:
        bool: True if the account was disabled successfully, False otherwise.
    """
    try:
        # Establish an LDAP connection
        server = ldap3.Server(DOMAIN_CONTROLLER)
        connection = ldap3.Connection(server, user=USERNAME, password=PASSWORD, auto_bind=True)

        # Disable the user account
        user_dn = f'CN={username},OU=Users,DC={DOMAIN_NAME}'
        connection.modify(user_dn, [('userAccountControl', '514')])  # 514 = account disabled

        return True

    except LDAPException as e:
        print(f'LDAP error: {e}')
        return False

    finally:
        connection.unbind()

# Example usage
if __name__ == '__main__':
    # Create a new user account
    username = 'newuser'
    password = 'P@ssw0rd'
    email = 'newuser@example.com'
    if create_user_account(username, password, email):
        print(f'User account {username} created successfully')

    # Reset the user password
    new_password = 'NewP@ssw0rd'
    if reset_user_password(username, new_password):
        print(f'Password for user {username} reset successfully')

    # Enable the user account
    if enable_user_account(username):
        print(f'User account {username} enabled successfully')

    # Disable the user account
    if disable_user_account(username):
        print(f'User account {username} disabled successfully')
```

### winrm_user_account_management.py
```python
import pywinrm

# Define constants
DOMAIN_CONTROLLER = 'your_domain_controller'
USERNAME = 'your_username'
PASSWORD = 'your_password'

def create_user_account_winrm(username, password):
    """
    Create a new user account using WinRM.

    Args:
        username (str): The username for the new account.
        password (str): The password for the new account.

    Returns:
        bool: True if the account was created successfully, False otherwise.
    """
    try:
        # Establish a WinRM connection
        session = pywinrm.Session(DOMAIN_CONTROLLER, auth=(USERNAME, PASSWORD))

        # Create a new user account
        command = f'net user {username} {password} /add'
        result = session.run_cmd(command)

        return result.status_code == 0

    except pywinrm.exceptions.WinRMError as e:
        print(f'WinRM error: {e}')
        return False

def reset_user_password_winrm(username, new_password):
    """
    Reset the password for an existing user account using WinRM.

    Args:
        username (str): The username for the account to reset.
        new_password (str): The new password for the account.

    Returns:
        bool: True if the password was reset successfully, False otherwise.
    """
    try:
        # Establish a WinRM connection
        session = pywinrm.Session(DOMAIN_CONTROLLER, auth=(USERNAME, PASSWORD))

        # Reset the user password
        command = f'net user {username} {new_password}'
        result = session.run_cmd(command)

        return result.status_code == 0

    except pywinrm.exceptions.WinRMError as e:
        print(f'WinRM error: {e}')
        return False

# Example usage
if __name__ == '__main__':
    # Create a new user account
    username = 'newuser'
    password = 'P@ssw0rd'
    if create_user_account_winrm(username, password):
        print(f'User account {username} created successfully')

    # Reset the user password
    new_password = 'NewP@ssw0rd'
    if reset_user_password_winrm(username, new_password):
        print(f'Password for user {username} reset successfully')
```
