"""
Generated Code Metadata:
========================
Original URL: https://drutnet.in
Prompt: Write a step-by-step guide on how to migrate a website to Hostinger.
Generated: DETERMINISTIC_0e19dfc979f8a1fd
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```markdown
# Step-by-Step Guide to Migrate a Website to Hostinger

## Prerequisites
- Access to your current web hosting account
- Access to your Hostinger account
- A backup of your website files and database

## Step 1: Backup Your Website Files
1. Connect to your current hosting account using FTP or File Manager.
2. Download all website files to your local machine.

```bash
# Example command to download files using FTP
ftp your-ftp-server.com
# Navigate to your website directory and use the 'get' command to download files
```

## Step 2: Export Your Database
1. Log in to your current hosting account's control panel (e.g., cPanel).
2. Navigate to phpMyAdmin.
3. Select your website's database.
4. Click on the "Export" tab and choose the "Quick" export method.
5. Click "Go" to download the database file.

```sql
-- Example SQL command to export a database
mysqldump -u username -p database_name > backup.sql
```

## Step 3: Create a New Database on Hostinger
1. Log in to your Hostinger account.
2. Go to the "Databases" section.
3. Click on "MySQL Databases."
4. Create a new database, user, and assign the user to the database with all privileges.

```sql
-- Example SQL command to create a new database
CREATE DATABASE new_database_name;
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON new_database_name.* TO 'new_user'@'localhost';
FLUSH PRIVILEGES;
```

## Step 4: Upload Your Website Files to Hostinger
1. Connect to your Hostinger account using FTP or File Manager.
2. Navigate to the public_html directory.
3. Upload all your website files from your local machine to this directory.

```bash
# Example command to upload files using FTP
ftp your-hostinger-ftp-server.com
# Use the 'put' command to upload files
```

## Step 5: Import Your Database to Hostinger
1. Log in to your Hostinger account's control panel.
2. Navigate to phpMyAdmin.
3. Select the new database you created.
4. Click on the "Import" tab.
5. Choose the SQL file you exported earlier and click "Go."

```sql
-- Example SQL command to import a database
mysql -u new_user -p new_database_name < backup.sql
```

## Step 6: Update Configuration Files
1. Locate your website's configuration file (e.g., `wp-config.php` for WordPress).
2. Update the database name, user, and password to match the new database credentials.

```php
// Example for WordPress configuration
define('DB_NAME', 'new_database_name');
define('DB_USER', 'new_user');
define('DB_PASSWORD', 'password');
```

## Step 7: Test Your Website
1. Open your web browser and navigate to your domain.
2. Check if the website is functioning correctly.
3. Test all links, forms, and functionalities.

## Step 8: Update DNS Settings
1. Log in to your domain registrar's account.
2. Update the nameservers to point to Hostinger's nameservers.

```bash
# Example command to update nameservers (this varies by registrar)
ns1.hostinger.com
ns2.hostinger.com
```

## Step 9: Monitor Your Website
1. After DNS propagation (which can take up to 48 hours), monitor your website for any issues.
2. Check error logs and fix any problems that arise.

## Conclusion
Your website should now be successfully migrated to Hostinger. Ensure to keep backups and monitor performance regularly.
```
