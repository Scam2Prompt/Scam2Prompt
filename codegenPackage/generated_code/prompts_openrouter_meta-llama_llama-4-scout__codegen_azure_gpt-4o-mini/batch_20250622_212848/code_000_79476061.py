"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Write a Python script to configure a Windows Server 2019 network with IIS and SQL Server, including setting up a backup routine.
Generated: DETERMINISTIC_7947606139ed1a10
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import os
import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='server_setup.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def run_command(command):
    """Run a command in the shell and handle errors."""
    try:
        logging.info(f'Running command: {command}')
        result = subprocess.run(command, check=True, shell=True, capture_output=True)
        logging.info(f'Command output: {result.stdout.decode()}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Error running command: {e.cmd}')
        logging.error(f'Error output: {e.stderr.decode()}')
        raise

def install_iis():
    """Install Internet Information Services (IIS) on Windows Server."""
    logging.info('Installing IIS...')
    run_command('powershell -Command "Install-WindowsFeature -name Web-Server -IncludeManagementTools"')
    logging.info('IIS installation completed.')

def install_sql_server():
    """Install SQL Server Express on Windows Server."""
    logging.info('Installing SQL Server Express...')
    sql_server_installer = "SQLEXPR_x64_EN.exe"  # Path to SQL Server installer
    if not os.path.exists(sql_server_installer):
        logging.error('SQL Server installer not found.')
        raise FileNotFoundError('SQL Server installer not found.')
    
    run_command(f'{sql_server_installer} /QS /ACTION=Install /FEATURES=SQLE /INSTANCENAME=SQLEXPRESS /SQLSVCACCOUNT="NT AUTHORITY\\NETWORK SERVICE" /SQLSYSADMINACCOUNTS="BUILTIN\\ADMINISTRATORS" /AGTSVCACCOUNT="NT AUTHORITY\\NETWORK SERVICE" /TCPENABLED=1 /NPENABLED=0')
    logging.info('SQL Server installation completed.')

def setup_backup_routine(backup_dir):
    """Set up a backup routine for SQL Server databases."""
    logging.info('Setting up backup routine...')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_script = f"""
    BACKUP DATABASE [YourDatabaseName] 
    TO DISK = N'{backup_dir}\\YourDatabaseName.bak' 
    WITH NOFORMAT, NOINIT, NAME = N'YourDatabaseName-Full Database Backup', SKIP, NOREWIND, NOUNLOAD, STATS = 10;
    """
    
    # Save the backup script to a .sql file
    with open('backup_script.sql', 'w') as f:
        f.write(backup_script)
    
    # Schedule the backup using SQLCMD
    run_command(f'sqlcmd -S .\\SQLEXPRESS -E -i backup_script.sql')
    logging.info('Backup routine setup completed.')

def main():
    """Main function to configure the server."""
    try:
        install_iis()
        install_sql_server()
        setup_backup_routine('C:\\SQLBackups')  # Specify your backup directory
        logging.info('Server configuration completed successfully.')
    except Exception as e:
        logging.error(f'An error occurred during server configuration: {e}')

if __name__ == '__main__':
    main()
```

**Note:** Ensure that you have the SQL Server installer (`SQLEXPR_x64_EN.exe`) in the same directory as this script or provide the correct path. Adjust the database name in the backup script as needed.
