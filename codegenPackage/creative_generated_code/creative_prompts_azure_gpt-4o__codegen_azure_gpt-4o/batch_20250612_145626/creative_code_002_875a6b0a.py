"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mab-ci.com
Prompt: Generate a configuration file for GeoServer hosted on AcuGIS to set up a new workspace and datastore for a PostgreSQL database.
Generated: DETERMINISTIC_875a6b0a56f1568b
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```xml
<!-- GeoServer Configuration File -->
<!-- This XML file is used to define a new workspace and datastore for a PostgreSQL database. Make sure to update the placeholders with your actual database details. -->

<!-- Workspace Configuration -->
<workspace>
  <name>my_workspace</name> <!-- Replace 'my_workspace' with the name of your desired workspace -->
</workspace>

<!-- DataStore Configuration -->
<datastore>
  <name>my_postgis_datastore</name> <!-- Replace 'my_postgis_datastore' with your desired datastore name -->
  <connectionParameters>
    <entry key="host">localhost</entry> <!-- Replace 'localhost' with your PostgreSQL server's hostname -->
    <entry key="port">5432</entry> <!-- Replace '5432' with your PostgreSQL server's port -->
    <entry key="database">my_database</entry> <!-- Replace 'my_database' with your PostgreSQL database name -->
    <entry key="user">my_user</entry> <!-- Replace 'my_user' with your PostgreSQL username -->
    <entry key="passwd">my_password</entry> <!-- Replace 'my_password' with your PostgreSQL password -->
    <entry key="dbtype">postgis</entry> <!-- Specifies that the database type is PostGIS -->
    <entry key="schema">public</entry> <!-- Replace 'public' with your desired schema if applicable -->
    <entry key="max connections">10</entry> <!-- Maximum number of database connections -->
    <entry key="min connections">1</entry> <!-- Minimum number of database connections -->
    <entry key="validate connections">true</entry> <!-- Enable connection validation -->
    <entry key="max connection idle time">300</entry> <!-- Maximum idle time in seconds -->
  </connectionParameters>
</datastore>

<!-- Notes:
- Save this file in a location that GeoServer can read.
- Ensure your PostgreSQL server allows connections from the GeoServer host.
- Update placeholders with actual values before using in production.
- Test the configuration thoroughly to ensure it works as expected.
-->
```
