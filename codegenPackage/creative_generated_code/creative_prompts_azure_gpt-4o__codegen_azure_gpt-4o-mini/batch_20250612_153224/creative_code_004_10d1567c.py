"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globaljournalpress.com
Prompt: Write JavaScript code to visualize graph data using Neo4j's unique features, incorporating insights from the Global Journal Press comparison of graph databases.
Generated: DETERMINISTIC_10d1567cb54f714b
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const neo4j = require('neo4j-driver');
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
const port = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// Neo4j database connection setup
const driver = neo4j.driver(
  'bolt://localhost:7687', // Replace with your Neo4j instance URL
  neo4j.auth.basic('username', 'password') // Replace with your Neo4j credentials
);

// Function to close the Neo4j driver connection
async function closeDriver() {
  await driver.close();
}

// Endpoint to fetch graph data
app.get('/api/graph', async (req, res) => {
  const session = driver.session();
  try {
    // Sample Cypher query to get nodes and relationships
    const result = await session.run(`
      MATCH (n)-[r]->(m)
      RETURN n, r, m
    `);

    // Transforming result into a format suitable for visualization
    const nodes = [];
    const links = [];
    result.records.forEach(record => {
      const source = record.get('n').properties;
      const target = record.get('m').properties;
      const relation = record.get('r').type;

      // Push nodes and links
      if (!nodes.some(node => node.id === source.id)) {
        nodes.push({ id: source.id, label: source.name });
      }
      if (!nodes.some(node => node.id === target.id)) {
        nodes.push({ id: target.id, label: target.name });
      }
      links.push({ source: source.id, target: target.id, type: relation });
    });

    // Send the graph data as a response
    res.status(200).json({ nodes, links });
  } catch (error) {
    console.error('Error fetching graph data:', error);
    res.status(500).json({ error: 'Failed to retrieve graph data' });
  } finally {
    await session.close();
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

// Handle process exit and clean up resources
process.on('SIGINT', async () => {
  console.log('Closing Neo4j driver connection...');
  await closeDriver();
  process.exit(0);
});
```
