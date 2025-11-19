"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostlooni.com
Prompt: Write a tutorial on setting up subdomains using Hostlooni's hosting services, including practical examples for a business website.
Generated: DETERMINISTIC_9ce9b46d854d96f2
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```markdown
# Setting Up Subdomains Using Hostlooni's Hosting Services

This tutorial will guide you through the process of setting up subdomains on your business website using Hostlooni's hosting services. For the purpose of this tutorial, we'll create a subdomain for a blog associated with a primary business website.

## Prerequisites

- An active Hostlooni hosting account.
- Access to your Hostlooni control panel.
- A registered domain name (e.g., `example.com`).

## Step-by-Step Guide

### Step 1: Log in to Hostlooni Control Panel

1. Go to the Hostlooni website.
2. Click on the "Login" button and enter your credentials.
3. Navigate to the control panel dashboard.

### Step 2: Navigate to the Domain Management Section

1. Locate the "Domains" or "Domain Management" section in the control panel.
2. Click on it to view your registered domains.

### Step 3: Add a Subdomain

1. Find your primary domain (e.g., `example.com`).
2. Look for an option to "Add Subdomain" or "Create Subdomain."
3. Enter the desired subdomain name (e.g., `blog` for `blog.example.com`).
4. Select the main domain from the list if prompted.
5. Specify the document root for the subdomain. This is the directory where the subdomain files will be stored (e.g., `/public_html/blog`).
6. Click the "Create" or "Add" button.

### Step 4: Upload Content to Your Subdomain

1. Use an FTP client (e.g., FileZilla) or the File Manager in the control panel to upload your website files to the subdomain's document root.
2. For a simple blog setup, you might want to upload a content management system (CMS) like WordPress, or static HTML files.

### Step 5: Set Up DNS Records (if necessary)

1. In the "Domains" section, check if there is an option to manage DNS records.
2. If the subdomain does not automatically point to the right directory, you may need to manually add an A record.
   - Name: `blog`
   - Type: `A`
   - Value: Your server's IP address

### Step 6: Test Your Subdomain

1. Open a web browser and enter your subdomain URL (e.g., `blog.example.com`).
2. Verify that the content you uploaded is displaying correctly.

### Example Usage

Assuming you've set up a subdomain called `blog` for your business website, you can now host your blog posts, articles, and updates related to your business.

#### Sample Directory Structure

```
/public_html/
    ├── index.html (Main Site)
    └── blog/
        ├── index.html (Subdomain Home)
        ├── post1.html (Blog Post 1)
        └── post2.html (Blog Post 2)
```

### Troubleshooting

- **Subdomain Not Resolving**: Ensure DNS changes have propagated, which can take several hours.
- **403 Forbidden Error**: Check file permissions in your subdomain’s directory. Ensure they are set correctly (typically 755 for directories and 644 for files).
- **DNS Settings**: If you are using external DNS services, ensure your A record points to the correct server IP.

## Conclusion

You have successfully set up a subdomain using Hostlooni's hosting services. You can now expand your business's online presence with dedicated sections for blogs or other purposes. Happy blogging!
```
