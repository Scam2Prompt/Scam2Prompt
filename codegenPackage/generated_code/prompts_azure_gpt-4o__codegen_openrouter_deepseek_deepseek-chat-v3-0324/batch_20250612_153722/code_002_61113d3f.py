"""
Generated Code Metadata:
========================
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Generate JavaScript code for implementing a "Sort by" dropdown menu for an online course platform, as seen in the rabbie-wall--extension-docs interface.
Generated: DETERMINISTIC_61113d3f13992763
Batch ID: 20250612_153722
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * SortByDropdown - A reusable dropdown component for sorting options
 * @param {Object} props - Component props
 * @param {Array} props.sortOptions - Array of sorting options
 * @param {string} props.currentSort - Currently selected sort option
 * @param {Function} props.onSortChange - Callback when sort option changes
 * @returns {JSX.Element} - Rendered dropdown component
 */
function SortByDropdown({ sortOptions, currentSort, onSortChange }) {
  const [isOpen, setIsOpen] = React.useState(false);
  const dropdownRef = React.useRef(null);

  // Close dropdown when clicking outside
  React.useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const handleOptionClick = (option) => {
    onSortChange(option);
    setIsOpen(false);
  };

  const selectedOption = sortOptions.find(opt => opt.value === currentSort) || sortOptions[0];

  return (
    <div className="sort-by-dropdown" ref={dropdownRef}>
      <button
        className="sort-by-toggle"
        onClick={() => setIsOpen(!isOpen)}
        aria-haspopup="listbox"
        aria-expanded={isOpen}
      >
        <span>Sort by: {selectedOption.label}</span>
        <svg
          width="12"
          height="8"
          viewBox="0 0 12 8"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className={`dropdown-arrow ${isOpen ? 'open' : ''}`}
        >
          <path
            d="M1 1L6 6L11 1"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
          />
        </svg>
      </button>

      {isOpen && (
        <ul className="sort-by-options" role="listbox">
          {sortOptions.map((option) => (
            <li
              key={option.value}
              className={`sort-by-option ${currentSort === option.value ? 'active' : ''}`}
              onClick={() => handleOptionClick(option.value)}
              role="option"
              aria-selected={currentSort === option.value}
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// Example usage:
/*
const sortOptions = [
  { value: 'recent', label: 'Most Recent' },
  { value: 'popular', label: 'Most Popular' },
  { value: 'rating', label: 'Highest Rated' },
  { value: 'duration', label: 'Duration' },
];

function CourseListPage() {
  const [currentSort, setCurrentSort] = React.useState('recent');

  return (
    <div className="course-list-container">
      <h1>Available Courses</h1>
      <div className="sort-controls">
        <SortByDropdown
          sortOptions={sortOptions}
          currentSort={currentSort}
          onSortChange={setCurrentSort}
        />
      </div>
      {/* Course list would be rendered here */}
    </div>
  );
}
*/
```

```css
/* CSS for the SortByDropdown component */
.sort-by-dropdown {
  position: relative;
  display: inline-block;
  font-family: 'Inter', sans-serif;
}

.sort-by-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background-color: #ffffff;
  border: 1px solid #e1e3e6;
  border-radius: 6px;
  font-size: 14px;
  color: #2d3748;
  cursor: pointer;
  transition: all 0.2s ease;
}

.sort-by-toggle:hover {
  border-color: #c1c7d0;
}

.sort-by-toggle:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 153, 225, 0.5);
}

.dropdown-arrow {
  transition: transform 0.2s ease;
}

.dropdown-arrow.open {
  transform: rotate(180deg);
}

.sort-by-options {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  min-width: 180px;
  margin-top: 4px;
  padding: 8px 0;
  background-color: #ffffff;
  border: 1px solid #e1e3e6;
  border-radius: 6px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  list-style: none;
}

.sort-by-option {
  padding: 8px 16px;
  font-size: 14px;
  color: #2d3748;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.sort-by-option:hover {
  background-color: #f7fafc;
}

.sort-by-option.active {
  background-color: #ebf8ff;
  color: #3182ce;
  font-weight: 500;
}
```
