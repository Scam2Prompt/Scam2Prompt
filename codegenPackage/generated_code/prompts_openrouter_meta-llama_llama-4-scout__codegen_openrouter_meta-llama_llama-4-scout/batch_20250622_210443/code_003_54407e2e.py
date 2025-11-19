"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Develop a Node.js application to manage and display a list of partners, similar to the "Nos partenaires" section on the Mêtis website.
Generated: DETERMINISTIC_54407e2e30248cbb
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Partner Management Application in Node.js**
====================================================

**partner.model.js**
```javascript
/**
 * Partner model
 * @typedef {Object} Partner
 * @property {number} id
 * @property {string} name
 * @property {string} description
 * @property {string} logoUrl
 */

class Partner {
  constructor(id, name, description, logoUrl) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.logoUrl = logoUrl;
  }
}

module.exports = Partner;
```

**partner.service.js**
```javascript
const Partner = require('./partner.model');

/**
 * Partner service
 * @class
 */
class PartnerService {
  constructor() {
    this.partners = [];
  }

  /**
   * Get all partners
   * @returns {Partner[]} partners
   */
  getAllPartners() {
    return this.partners;
  }

  /**
   * Get partner by id
   * @param {number} id
   * @returns {Partner|null} partner
   */
  getPartnerById(id) {
    return this.partners.find((partner) => partner.id === id) || null;
  }

  /**
   * Create new partner
   * @param {string} name
   * @param {string} description
   * @param {string} logoUrl
   * @returns {Partner} partner
   */
  createPartner(name, description, logoUrl) {
    const newPartner = new Partner(this.partners.length + 1, name, description, logoUrl);
    this.partners.push(newPartner);
    return newPartner;
  }

  /**
   * Update existing partner
   * @param {number} id
   * @param {string} name
   * @param {string} description
   * @param {string} logoUrl
   * @returns {Partner|null} partner
   */
  updatePartner(id, name, description, logoUrl) {
    const partnerIndex = this.partners.findIndex((partner) => partner.id === id);
    if (partnerIndex === -1) {
      return null;
    }
    this.partners[partnerIndex].name = name;
    this.partners[partnerIndex].description = description;
    this.partners[partnerIndex].logoUrl = logoUrl;
    return this.partners[partnerIndex];
  }

  /**
   * Delete partner by id
   * @param {number} id
   * @returns {boolean} success
   */
  deletePartner(id) {
    const partnerIndex = this.partners.findIndex((partner) => partner.id === id);
    if (partnerIndex === -1) {
      return false;
    }
    this.partners.splice(partnerIndex, 1);
    return true;
  }
}

module.exports = PartnerService;
```

**partner.controller.js**
```javascript
const express = require('express');
const PartnerService = require('./partner.service');

const partnerService = new PartnerService();

const router = express.Router();

/**
 * Get all partners
 * @route GET /partners
 */
router.get('/partners', (req, res) => {
  try {
    const partners = partnerService.getAllPartners();
    res.json(partners);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

/**
 * Get partner by id
 * @route GET /partners/:id
 */
router.get('/partners/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id, 10);
    const partner = partnerService.getPartnerById(id);
    if (!partner) {
      res.status(404).json({ message: 'Partner not found' });
    } else {
      res.json(partner);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

/**
 * Create new partner
 * @route POST /partners
 */
router.post('/partners', (req, res) => {
  try {
    const { name, description, logoUrl } = req.body;
    if (!name || !description || !logoUrl) {
      res.status(400).json({ message: 'Name, description, and logoUrl are required' });
    } else {
      const newPartner = partnerService.createPartner(name, description, logoUrl);
      res.json(newPartner);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

/**
 * Update existing partner
 * @route PUT /partners/:id
 */
router.put('/partners/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id, 10);
    const { name, description, logoUrl } = req.body;
    if (!name || !description || !logoUrl) {
      res.status(400).json({ message: 'Name, description, and logoUrl are required' });
    } else {
      const updatedPartner = partnerService.updatePartner(id, name, description, logoUrl);
      if (!updatedPartner) {
        res.status(404).json({ message: 'Partner not found' });
      } else {
        res.json(updatedPartner);
      }
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

/**
 * Delete partner by id
 * @route DELETE /partners/:id
 */
router.delete('/partners/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id, 10);
    const success = partnerService.deletePartner(id);
    if (!success) {
      res.status(404).json({ message: 'Partner not found' });
    } else {
      res.json({ message: 'Partner deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;
```

**app.js**
```javascript
const express = require('express');
const partnerController = require('./partner.controller');

const app = express();
app.use(express.json());

app.use('/api', partnerController);

const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**package.json**
```json
{
  "name": "partner-management",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```
