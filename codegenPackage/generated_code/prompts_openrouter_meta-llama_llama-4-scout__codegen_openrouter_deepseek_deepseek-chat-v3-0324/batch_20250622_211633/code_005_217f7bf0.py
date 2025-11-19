"""
Generated Code Metadata:
========================
Original URL: https://galmudugmof.so
Prompt: "Design a basic financial dashboard for the Galmudug Ministry of Finance using a library like D3.js, displaying key financial indicators, budget performance, and revenue trends."
Generated: DETERMINISTIC_217f7bf0418c9e3c
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Financial Dashboard for Galmudug Ministry of Finance using D3.js

// Main Dashboard Class
class FinancialDashboard {
  constructor(containerId, data) {
    this.containerId = containerId;
    this.data = data;
    this.margin = { top: 20, right: 20, bottom: 50, left: 50 };
    this.width = 800 - this.margin.left - this.margin.right;
    this.height = 400 - this.margin.top - this.margin.bottom;
    this.colors = d3.scaleOrdinal(d3.schemeCategory10);
  }

  // Initialize the dashboard
  init() {
    try {
      this.createContainer();
      this.renderKPIs();
      this.renderBudgetPerformance();
      this.renderRevenueTrends();
    } catch (error) {
      console.error("Error initializing dashboard:", error);
      this.showError("Failed to initialize dashboard. Please try again.");
    }
  }

  // Create main container
  createContainer() {
    d3.select(`#${this.containerId}`)
      .append("div")
      .attr("class", "dashboard-container")
      .style("width", "100%")
      .style("max-width", "1200px")
      .style("margin", "0 auto");
  }

  // Render Key Performance Indicators
  renderKPIs() {
    const container = d3.select(".dashboard-container")
      .append("div")
      .attr("class", "kpi-container")
      .style("display", "flex")
      .style("justify-content", "space-between")
      .style("margin-bottom", "30px");

    const kpis = [
      { title: "Total Revenue", value: this.data.totalRevenue, change: this.data.revenueChange },
      { title: "Budget Utilization", value: this.data.budgetUtilization, change: this.data.utilizationChange },
      { title: "Deficit/Surplus", value: this.data.deficitSurplus, change: this.data.deficitChange }
    ];

    kpis.forEach(kpi => {
      const card = container.append("div")
        .attr("class", "kpi-card")
        .style("padding", "20px")
        .style("border-radius", "5px")
        .style("background", "#f5f5f5")
        .style("width", "30%");

      card.append("h3")
        .text(kpi.title)
        .style("margin", "0 0 10px 0")
        .style("font-size", "16px");

      card.append("div")
        .text(kpi.value)
        .style("font-size", "24px")
        .style("font-weight", "bold")
        .style("margin-bottom", "5px");

      const changeClass = kpi.change >= 0 ? "positive" : "negative";
      card.append("div")
        .text(`${kpi.change >= 0 ? '+' : ''}${kpi.change}%`)
        .attr("class", changeClass)
        .style("font-size", "14px");
    });
  }

  // Render Budget Performance Chart
  renderBudgetPerformance() {
    const container = d3.select(".dashboard-container")
      .append("div")
      .attr("class", "chart-container")
      .style("margin-bottom", "30px");

    container.append("h2")
      .text("Budget Performance")
      .style("margin-bottom", "10px");

    const svg = container.append("svg")
      .attr("width", this.width + this.margin.left + this.margin.right)
      .attr("height", this.height + this.margin.top + this.margin.bottom)
      .append("g")
      .attr("transform", `translate(${this.margin.left},${this.margin.top})`);

    // X axis
    const x = d3.scaleBand()
      .range([0, this.width])
      .domain(this.data.budgetPerformance.map(d => d.department))
      .padding(0.2);

    svg.append("g")
      .attr("transform", `translate(0,${this.height})`)
      .call(d3.axisBottom(x))
      .selectAll("text")
      .attr("transform", "rotate(-45)")
      .style("text-anchor", "end");

    // Y axis
    const y = d3.scaleLinear()
      .domain([0, d3.max(this.data.budgetPerformance, d => Math.max(d.allocated, d.utilized))])
      .range([this.height, 0]);

    svg.append("g")
      .call(d3.axisLeft(y));

    // Bars for allocated budget
    svg.selectAll("allocated")
      .data(this.data.budgetPerformance)
      .enter()
      .append("rect")
      .attr("x", d => x(d.department))
      .attr("y", d => y(d.allocated))
      .attr("width", x.bandwidth())
      .attr("height", d => this.height - y(d.allocated))
      .attr("fill", "#4e79a7");

    // Bars for utilized budget
    svg.selectAll("utilized")
      .data(this.data.budgetPerformance)
      .enter()
      .append("rect")
      .attr("x", d => x(d.department))
      .attr("y", d => y(d.utilized))
      .attr("width", x.bandwidth())
      .attr("height", d => this.height - y(d.utilized))
      .attr("fill", "#f28e2b");

    // Legend
    const legend = svg.append("g")
      .attr("transform", `translate(${this.width - 150},0)`);

    legend.append("rect")
      .attr("x", 0)
      .attr("y", 0)
      .attr("width", 15)
      .attr("height", 15)
      .attr("fill", "#4e79a7");

    legend.append("text")
      .attr("x", 20)
      .attr("y", 12)
      .text("Allocated")
      .style("font-size", "12px");

    legend.append("rect")
      .attr("x", 0)
      .attr("y", 20)
      .attr("width", 15)
      .attr("height", 15)
      .attr("fill", "#f28e2b");

    legend.append("text")
      .attr("x", 20)
      .attr("y", 32)
      .text("Utilized")
      .style("font-size", "12px");
  }

  // Render Revenue Trends Line Chart
  renderRevenueTrends() {
    const container = d3.select(".dashboard-container")
      .append("div")
      .attr("class", "chart-container")
      .style("margin-bottom", "30px");

    container.append("h2")
      .text("Revenue Trends (Last 12 Months)")
      .style("margin-bottom", "10px");

    const svg = container.append("svg")
      .attr("width", this.width + this.margin.left + this.margin.right)
      .attr("height", this.height + this.margin.top + this.margin.bottom)
      .append("g")
      .attr("transform", `translate(${this.margin.left},${this.margin.top})`);

    // Parse dates
    const parseTime = d3.timeParse("%Y-%m");

    // Format data
    const formattedData = this.data.revenueTrends.map(d => {
      return {
        date: parseTime(d.month),
        revenue: d.revenue
      };
    });

    // X axis
    const x = d3.scaleTime()
      .domain(d3.extent(formattedData, d => d.date))
      .range([0, this.width]);

    svg.append("g")
      .attr("transform", `translate(0,${this.height})`)
      .call(d3.axisBottom(x));

    // Y axis
    const y = d3.scaleLinear()
      .domain([0, d3.max(formattedData, d => d.revenue)])
      .range([this.height, 0]);

    svg.append("g")
      .call(d3.axisLeft(y));

    // Line generator
    const line = d3.line()
      .x(d => x(d.date))
      .y(d => y(d.revenue));

    // Add the line
    svg.append("path")
      .datum(formattedData)
      .attr("fill", "none")
      .attr("stroke", "#e15759")
      .attr("stroke-width", 2)
      .attr("d", line);

    // Add dots
    svg.selectAll("dot")
      .data(formattedData)
      .enter()
      .append("circle")
      .attr("cx", d => x(d.date))
      .attr("cy", d => y(d.revenue))
      .attr("r", 4)
      .attr("fill", "#e15759");
  }

  // Show error message
  showError(message) {
    d3.select(`#${this.containerId}`)
      .append("div")
      .attr("class", "error-message")
      .
