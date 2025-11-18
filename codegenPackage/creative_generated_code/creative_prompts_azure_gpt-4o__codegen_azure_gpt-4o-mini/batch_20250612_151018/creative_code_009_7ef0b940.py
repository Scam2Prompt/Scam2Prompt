"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Implement functionality in a COVID-19 graph that allows users to hover over data points for more information, drag to zoom in, and double-click to zoom out, as described on the webpage.
Generated: DETERMINISTIC_7ef0b9404335e38f
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://d3js.org/d3.v7.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COVID-19 Data Graph</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        .tooltip {
            position: absolute;
            text-align: center;
            padding: 8px;
            font: 12px sans-serif;
            background: lightsteelblue;
            border: 0px;
            border-radius: 8px;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <svg id="covidGraph" width="800" height="400"></svg>
    <script>
        // Sample COVID-19 data
        const data = [
            { date: new Date('2023-01-01'), cases: 100 },
            { date: new Date('2023-01-02'), cases: 120 },
            { date: new Date('2023-01-03'), cases: 150 },
            { date: new Date('2023-01-04'), cases: 130 },
            // Add more data points as needed
        ];

        // Set up SVG dimensions and margins
        const margin = { top: 20, right: 30, bottom: 30, left: 40 };
        const width = +d3.select('#covidGraph').attr('width') - margin.left - margin.right;
        const height = +d3.select('#covidGraph').attr('height') - margin.top - margin.bottom;

        // Create scales and axes
        const x = d3.scaleTime().range([0, width]);
        const y = d3.scaleLinear().range([height, 0]);
        const xAxis = d3.axisBottom(x);
        const yAxis = d3.axisLeft(y);

        // Create tooltip
        const tooltip = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

        // Create SVG group element
        const svg = d3.select("#covidGraph")
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // Set the domains for the scales
        x.domain(d3.extent(data, d => d.date));
        y.domain([0, d3.max(data, d => d.cases)]);

        // Draw axes
        svg.append("g")
            .attr("class", "x-axis")
            .attr("transform", `translate(0,${height})`)
            .call(xAxis);

        svg.append("g")
            .attr("class", "y-axis")
            .call(yAxis);

        // Draw the line
        svg.append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "steelblue")
            .attr("stroke-width", 1.5)
            .attr("d", d3.line()
                .x(d => x(d.date))
                .y(d => y(d.cases))
            );

        // Draw points and add interactivity
        svg.selectAll(".dot")
            .data(data)
            .enter().append("circle")
            .attr("class", "dot")
            .attr("cx", d => x(d.date))
            .attr("cy", d => y(d.cases))
            .attr("r", 5)
            .on("mouseover", (event, d) => {
                tooltip.transition().duration(200).style("opacity", .9);
                tooltip.html(`Date: ${d.date.toDateString()}<br>Cases: ${d.cases}`)
                    .style("left", (event.pageX + 5) + "px")
                    .style("top", (event.pageY - 28) + "px");
            })
            .on("mouseout", () => {
                tooltip.transition().duration(500).style("opacity", 0);
            });

        // Zoom functionality
        const zoom = d3.zoom()
            .scaleExtent([1, 10])
            .on("zoom", (event) => {
                const new_xScale = event.transform.rescaleX(x);
                const new_yScale = event.transform.rescaleY(y);

                svg.select(".x-axis").call(xAxis.scale(new_xScale));
                svg.select(".y-axis").call(yAxis.scale(new_yScale));
                svg.selectAll(".dot")
                    .attr("cx", d => new_xScale(d.date))
                    .attr("cy", d => new_yScale(d.cases));
                svg.select("path")
                    .attr("d", d3.line()
                        .x(d => new_xScale(d.date))
                        .y(d => new_yScale(d.cases))
                    );
            });

        // Attach zoom behavior to the SVG
        svg.call(zoom)
            .on("dblclick.zoom", null); // Disable double-click zoom

        // Handle double-click zoom out
        svg.on("dblclick", (event) => {
            const transform = d3.zoomIdentity;
            svg.transition()
                .duration(750)
                .call(zoom.transform, transform);
        });

    </script>
</body>
</html>
```
