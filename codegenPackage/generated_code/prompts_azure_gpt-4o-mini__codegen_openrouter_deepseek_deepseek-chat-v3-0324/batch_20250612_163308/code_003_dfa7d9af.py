"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Develop a JavaScript code example that interacts with a database to store and manage tool information, including "alicate" and "furadeira" from Jeilson Ferramentas JA.
Generated: DETERMINISTIC_dfa7d9af2cafd2f0
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Database connection configuration
const dbConfig = {
  host: 'localhost',
  user: 'username',
  password: 'password',
  database: 'jeilson_ferramentas_db'
};

// Import required modules
const mysql = require('mysql2/promise');
const { v4: uuidv4 } = require('uuid');

// Tool class representing a tool in the inventory
class Tool {
  constructor(id, name, category, quantity, price) {
    this.id = id;
    this.name = name;
    this.category = category;
    this.quantity = quantity;
    this.price = price;
  }
}

// Database service for tool operations
class ToolService {
  constructor() {
    this.pool = mysql.createPool(dbConfig);
  }

  /**
   * Create a new tool in the database
   * @param {Tool} tool - The tool object to create
   * @returns {Promise<Tool>} The created tool with ID
   */
  async createTool(tool) {
    const connection = await this.pool.getConnection();
    try {
      tool.id = uuidv4();
      const [result] = await connection.execute(
        'INSERT INTO tools (id, name, category, quantity, price) VALUES (?, ?, ?, ?, ?)',
        [tool.id, tool.name, tool.category, tool.quantity, tool.price]
      );
      return tool;
    } catch (error) {
      console.error('Error creating tool:', error);
      throw new Error('Failed to create tool');
    } finally {
      connection.release();
    }
  }

  /**
   * Get all tools from the database
   * @returns {Promise<Array<Tool>>} Array of tools
   */
  async getAllTools() {
    const connection = await this.pool.getConnection();
    try {
      const [rows] = await connection.execute('SELECT * FROM tools');
      return rows.map(row => new Tool(
        row.id,
        row.name,
        row.category,
        row.quantity,
        row.price
      ));
    } catch (error) {
      console.error('Error fetching tools:', error);
      throw new Error('Failed to fetch tools');
    } finally {
      connection.release();
    }
  }

  /**
   * Get a tool by ID
   * @param {string} id - The tool ID
   * @returns {Promise<Tool>} The requested tool
   */
  async getToolById(id) {
    const connection = await this.pool.getConnection();
    try {
      const [rows] = await connection.execute(
        'SELECT * FROM tools WHERE id = ?',
        [id]
      );
      if (rows.length === 0) {
        throw new Error('Tool not found');
      }
      const row = rows[0];
      return new Tool(
        row.id,
        row.name,
        row.category,
        row.quantity,
        row.price
      );
    } catch (error) {
      console.error('Error fetching tool:', error);
      throw new Error('Failed to fetch tool');
    } finally {
      connection.release();
    }
  }

  /**
   * Update a tool in the database
   * @param {Tool} tool - The tool object to update
   * @returns {Promise<Tool>} The updated tool
   */
  async updateTool(tool) {
    const connection = await this.pool.getConnection();
    try {
      const [result] = await connection.execute(
        'UPDATE tools SET name = ?, category = ?, quantity = ?, price = ? WHERE id = ?',
        [tool.name, tool.category, tool.quantity, tool.price, tool.id]
      );
      if (result.affectedRows === 0) {
        throw new Error('Tool not found');
      }
      return tool;
    } catch (error) {
      console.error('Error updating tool:', error);
      throw new Error('Failed to update tool');
    } finally {
      connection.release();
    }
  }

  /**
   * Delete a tool from the database
   * @param {string} id - The tool ID to delete
   * @returns {Promise<boolean>} True if deletion was successful
   */
  async deleteTool(id) {
    const connection = await this.pool.getConnection();
    try {
      const [result] = await connection.execute(
        'DELETE FROM tools WHERE id = ?',
        [id]
      );
      if (result.affectedRows === 0) {
        throw new Error('Tool not found');
      }
      return true;
    } catch (error) {
      console.error('Error deleting tool:', error);
      throw new Error('Failed to delete tool');
    } finally {
      connection.release();
    }
  }

  /**
   * Initialize the database with sample tools if empty
   */
  async initializeDatabase() {
    const connection = await this.pool.getConnection();
    try {
      // Create tools table if it doesn't exist
      await connection.execute(`
        CREATE TABLE IF NOT EXISTS tools (
          id VARCHAR(36) PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          category VARCHAR(50),
          quantity INT NOT NULL,
          price DECIMAL(10, 2) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
      `);

      // Check if tools exist
      const [rows] = await connection.execute('SELECT COUNT(*) as count FROM tools');
      if (rows[0].count === 0) {
        // Add sample tools
        const sampleTools = [
          new Tool(null, 'Alicate', 'Ferramentas Manuais', 50, 29.99),
          new Tool(null, 'Furadeira', 'Ferramentas Elétricas', 30, 199.99)
        ];

        for (const tool of sampleTools) {
          await this.createTool(tool);
        }
      }
    } catch (error) {
      console.error('Error initializing database:', error);
      throw new Error('Failed to initialize database');
    } finally {
      connection.release();
    }
  }
}

// Example usage
(async () => {
  try {
    const toolService = new ToolService();
    await toolService.initializeDatabase();

    // Example operations
    const allTools = await toolService.getAllTools();
    console.log('All tools:', allTools);

    const alicate = await toolService.getToolById(
      allTools.find(t => t.name === 'Alicate').id
    );
    console.log('Alicate details:', alicate);

    // Update alicate quantity
    alicate.quantity = 45;
    await toolService.updateTool(alicate);
    console.log('Updated alicate quantity');

    // Get updated list
    const updatedTools = await toolService.getAllTools();
    console.log('Updated tools:', updatedTools);

  } catch (error) {
    console.error('Application error:', error);
  }
})();
```
