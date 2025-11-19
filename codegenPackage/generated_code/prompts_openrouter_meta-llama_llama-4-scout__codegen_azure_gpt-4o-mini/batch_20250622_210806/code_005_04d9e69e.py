"""
Generated Code Metadata:
========================
Original URL: https://mara-otherside.pages.dev
Prompt: Create a React component for a user interface that allows users to evolve their Mara into Kodamara, select roles, and apply sediment fragments for customization.
Generated: DETERMINISTIC_04d9e69e1f693c0f
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * EvolveMara Component
 * This component allows users to evolve their Mara into Kodamara,
 * select roles, and apply sediment fragments for customization.
 */
const EvolveMara = ({ initialMara, roles, sedimentFragments }) => {
    const [mara, setMara] = useState(initialMara);
    const [selectedRole, setSelectedRole] = useState('');
    const [appliedFragments, setAppliedFragments] = useState([]);

    /**
     * Handle the evolution of Mara to Kodamara
     */
    const handleEvolve = () => {
        if (mara === 'Mara') {
            setMara('Kodamara');
        } else {
            alert('Mara has already evolved into Kodamara.');
        }
    };

    /**
     * Handle role selection
     * @param {string} role - The selected role
     */
    const handleRoleSelect = (role) => {
        if (roles.includes(role)) {
            setSelectedRole(role);
        } else {
            console.error('Invalid role selected');
        }
    };

    /**
     * Handle applying sediment fragments
     * @param {string} fragment - The sediment fragment to apply
     */
    const handleApplyFragment = (fragment) => {
        if (sedimentFragments.includes(fragment) && !appliedFragments.includes(fragment)) {
            setAppliedFragments([...appliedFragments, fragment]);
        } else {
            console.error('Fragment is either invalid or already applied');
        }
    };

    return (
        <div className="evolve-mara">
            <h1>Evolve Your Mara</h1>
            <h2>Current State: {mara}</h2>
            <button onClick={handleEvolve}>Evolve to Kodamara</button>

            <div className="role-selection">
                <h3>Select Role</h3>
                {roles.map((role) => (
                    <button key={role} onClick={() => handleRoleSelect(role)}>
                        {role}
                    </button>
                ))}
                {selectedRole && <p>Selected Role: {selectedRole}</p>}
            </div>

            <div className="fragment-application">
                <h3>Apply Sediment Fragments</h3>
                {sedimentFragments.map((fragment) => (
                    <button key={fragment} onClick={() => handleApplyFragment(fragment)}>
                        {fragment}
                    </button>
                ))}
                {appliedFragments.length > 0 && (
                    <p>Applied Fragments: {appliedFragments.join(', ')}</p>
                )}
            </div>
        </div>
    );
};

// PropTypes for type checking
EvolveMara.propTypes = {
    initialMara: PropTypes.string.isRequired,
    roles: PropTypes.arrayOf(PropTypes.string).isRequired,
    sedimentFragments: PropTypes.arrayOf(PropTypes.string).isRequired,
};

// Default props
EvolveMara.defaultProps = {
    initialMara: 'Mara',
    roles: ['Warrior', 'Mage', 'Rogue'],
    sedimentFragments: ['Fire', 'Water', 'Earth', 'Air'],
};

export default EvolveMara;
```
