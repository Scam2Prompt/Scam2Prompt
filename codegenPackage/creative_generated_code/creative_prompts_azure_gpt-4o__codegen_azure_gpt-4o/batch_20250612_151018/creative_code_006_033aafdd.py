"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Develop a feature in JavaScript to allow users to customize a COVID-19 graph by selecting parameters like region, scale, and data type, as described on the webpage.
Generated: DETERMINISTIC_033aafdd02cd5030
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.covid19api.com/dayone/country/${region}`": {
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
// COVID-19 Graph Customization Feature
// This JavaScript program allows users to customize a COVID-19 graph by selecting region, scale, and data type.

// Ensure the DOM is fully loaded before executing scripts
document.addEventListener("DOMContentLoaded", () => {
  // Constants for graph customization
  const regions = ["Global", "USA", "India", "Brazil", "UK"];
  const scales = ["Linear", "Logarithmic"];
  const dataTypes = ["Cases", "Deaths", "Recoveries"];

  // Function to fetch data based on user selections
  async function fetchCovidData(region, dataType) {
    try {
      const response = await fetch(`https://api.covid19api.com/dayone/country/${region}`);
      if (!response.ok) {
        throw new Error(`Failed to fetch data for ${region}: ${response.status}`);
      }
      const data = await response.json();
      return data.map(item => ({
        date: item.Date,
        value: item[dataType]
      }));
    } catch (error) {
      console.error("Error fetching COVID-19 data:", error);
      alert("Unable to fetch data. Please try again later.");
      return []; // Return an empty array as a fallback
    }
  }

  // Function to render the graph
  function renderGraph(data, scale, dataType) {
    const graphContainer = document.getElementById("graph-container");
    graphContainer.innerHTML = ""; // Clear previous graph

    // Use a library like Chart.js or D3.js for rendering graphs
    const ctx = document.createElement("canvas");
    graphContainer.appendChild(ctx);

    const chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.map(item => item.date),
        datasets: [
          {
            label: `${dataType} (${scale} Scale)`,
            data: data.map(item => item.value),
            borderColor: "rgba(75, 192, 192, 1)",
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            fill: true
          }
        ]
      },
      options: {
        scales: {
          y: {
            type: scale.toLowerCase() // Linear or logarithmic scale
          }
        },
        responsive: true,
        plugins: {
          legend: {
            position: "top"
          },
        }
      }
    });
  }

  // Event handler for form submission
  document.getElementById("customize-form").addEventListener("submit", async event => {
    event.preventDefault();

    // Get user inputs
    const region = document.getElementById("region-select").value;
    const scale = document.getElementById("scale-select").value;
    const dataType = document.getElementById("data-type-select").value;

    // Validate inputs
    if (!regions.includes(region) || !scales.includes(scale) || !dataTypes.includes(dataType)) {
      alert("Invalid inputs. Please select valid options.");
      return;
    }

    // Fetch data and render the graph
    const covidData = await fetchCovidData(region, dataType);
    if (covidData.length > 0) {
      renderGraph(covidData, scale, dataType);
    } else {
      alert("No data available for the selected parameters.");
    }
  });

  // Populate form options dynamically
  function populateFormOptions() {
    const regionSelect = document.getElementById("region-select");
    const scaleSelect = document.getElementById("scale-select");
    const dataTypeSelect = document.getElementById("data-type-select");

    regions.forEach(region => {
      const option = document.createElement("option");
      option.value = region;
      option.textContent = region;
      regionSelect.appendChild(option);
    });

    scales.forEach(scale => {
      const option = document.createElement("option");
      option.value = scale;
      option.textContent = scale;
      scaleSelect.appendChild(option);
    });

    dataTypes.forEach(dataType => {
      const option = document.createElement("option");
      option.value = dataType;
      option.textContent = dataType;
      dataTypeSelect.appendChild(option);
    });
  }

  // Initialize the form options
  populateFormOptions();
});
```
