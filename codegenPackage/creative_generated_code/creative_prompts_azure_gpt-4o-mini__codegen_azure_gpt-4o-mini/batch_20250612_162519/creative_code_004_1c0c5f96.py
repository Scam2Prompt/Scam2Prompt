"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinconectswap.blogspot.com
Prompt: Write a SQL query to retrieve all shoe types from a database that includes 'chuteira' and 'sandalias femininas', reflecting the categories found on the Lara Sapatos em Geral webpage.
Generated: DETERMINISTIC_1c0c5f963283c502
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve shoe types that match specific categories
SELECT DISTINCT shoe_type
FROM shoes
WHERE shoe_type IN ('chuteira', 'sandalias femininas')
ORDER BY shoe_type;
```
