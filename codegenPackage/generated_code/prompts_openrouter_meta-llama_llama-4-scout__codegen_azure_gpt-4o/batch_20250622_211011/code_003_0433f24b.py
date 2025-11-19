"""
Generated Code Metadata:
========================
Original URL: https://umbrella-d96b1.web.app
Prompt: What are the key features of a digital asset management platform that offers ultimate control to users, and how can they be implemented using JavaScript?
Generated: DETERMINISTIC_0433f24b4f56339a
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Digital Asset Management Platform
 * Key Features:
 * 1. Asset Upload
 * 2. Asset Organization (folders, tags, categories)
 * 3. Access Control (user roles and permissions)
 * 4. Search and Filter
 * 5. Version Control
 * 6. Asset Preview
 * 7. Audit Logs
 * 8. Download and Sharing
 * 
 * Implementation using JavaScript
 */

// Mock database for assets and users
const database = {
  assets: [],
  users: [],
  auditLogs: [],
};

// Utility function for error handling
function handleError(message) {
  console.error(`Error: ${message}`);
  throw new Error(message);
}

// Feature 1: Asset Upload
function uploadAsset(userId, asset) {
  if (!userId || !asset) {
    handleError("User ID and asset are required for upload.");
  }

  const user = database.users.find((u) => u.id === userId);
  if (!user || !user.permissions.includes("upload")) {
    handleError("User does not have permission to upload assets.");
  }

  const newAsset = {
    id: Date.now(),
    name: asset.name,
    type: asset.type,
    size: asset.size,
    uploadedBy: userId,
    createdAt: new Date(),
    tags: asset.tags || [],
    version: 1,
  };

  database.assets.push(newAsset);
  logAudit(userId, `Uploaded asset: ${asset.name}`);
  return newAsset;
}

// Feature 2: Asset Organization
function organizeAsset(assetId, tags = [], category = "") {
  const asset = database.assets.find((a) => a.id === assetId);
  if (!asset) {
    handleError("Asset not found.");
  }

  asset.tags = tags;
  asset.category = category;
  logAudit(asset.uploadedBy, `Organized asset: ${asset.name}`);
  return asset;
}

// Feature 3: Access Control
function setUserPermissions(userId, permissions) {
  const user = database.users.find((u) => u.id === userId);
  if (!user) {
    handleError("User not found.");
  }

  user.permissions = permissions;
  logAudit(userId, `Updated permissions: ${permissions.join(", ")}`);
}

// Feature 4: Search and Filter
function searchAssets(query) {
  return database.assets.filter((asset) =>
    asset.name.toLowerCase().includes(query.toLowerCase())
  );
}

function filterAssetsByTag(tag) {
  return database.assets.filter((asset) => asset.tags.includes(tag));
}

// Feature 5: Version Control
function updateAssetVersion(assetId, newVersion) {
  const asset = database.assets.find((a) => a.id === assetId);
  if (!asset) {
    handleError("Asset not found.");
  }

  asset.version = newVersion;
  logAudit(asset.uploadedBy, `Updated asset version: ${asset.name} to ${newVersion}`);
  return asset;
}

// Feature 6: Asset Preview
function previewAsset(assetId) {
  const asset = database.assets.find((a) => a.id === assetId);
  if (!asset) {
    handleError("Asset not found.");
  }

  return `Previewing asset: ${asset.name}`;
}

// Feature 7: Audit Logs
function logAudit(userId, action) {
  database.auditLogs.push({
    userId,
    action,
    timestamp: new Date(),
  });
}

function getAuditLogs() {
  return database.auditLogs;
}

// Feature 8: Download and Sharing
function downloadAsset(assetId) {
  const asset = database.assets.find((a) => a.id === assetId);
  if (!asset) {
    handleError("Asset not found.");
  }

  logAudit(asset.uploadedBy, `Downloaded asset: ${asset.name}`);
  return `Downloading asset: ${asset.name}`;
}

function shareAsset(assetId, recipientEmail) {
  const asset = database.assets.find((a) => a.id === assetId);
  if (!asset) {
    handleError("Asset not found.");
  }

  logAudit(asset.uploadedBy, `Shared asset: ${asset.name} with ${recipientEmail}`);
  return `Asset ${asset.name} shared with ${recipientEmail}`;
}

// Example Usage
try {
  // Add a user
  const userId = Date.now();
  database.users.push({ id: userId, name: "Admin", permissions: ["upload", "organize"] });

  // Upload an asset
  const asset = uploadAsset(userId, {
    name: "Image1.png",
    type: "image/png",
    size: "2MB",
    tags: ["image", "png"],
  });

  // Organize the asset
  organizeAsset(asset.id, ["image", "high-res"], "Images");

  // Search for assets
  const searchResults = searchAssets("Image");
  console.log(searchResults);

  // Preview the asset
  console.log(previewAsset(asset.id));

  // Download the asset
  console.log(downloadAsset(asset.id));

  // Share the asset
  console.log(shareAsset(asset.id, "recipient@example.com"));

  // Get audit logs
  console.log(getAuditLogs());
} catch (error) {
  console.error(error.message);
}
```
