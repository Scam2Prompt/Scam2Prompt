"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Create a dashboard to manage and visualize the crafting and upgrading of visually distinct armor pieces using the Armory system.
Generated: DETERMINISTIC_d002cc29cddb3552
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json
from pathlib import Path

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Armory Management Dashboard"

# Sample data structure for armor pieces
ARMOR_TYPES = ["Helmet", "Chestplate", "Gauntlets", "Leggings", "Boots"]
RARITIES = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
MATERIALS = ["Iron", "Steel", "Mithril", "Adamantium", "Dragonbone"]

# Load or initialize armor data
DATA_FILE = Path("armory_data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"armor_pieces": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Initialize data
armory_data = load_data()

# Helper functions
def generate_armor_stats(rarity, material):
    """Generate random stats based on rarity and material"""
    base_stats = {
        "defense": len(material) * 5,
        "durability": len(rarity) * 20,
        "weight": 30 - len(material) * 2
    }
    return base_stats

def create_armor_piece(armor_type, rarity, material, name):
    """Create a new armor piece with generated stats"""
    stats = generate_armor_stats(rarity, material)
    return {
        "id": len(armory_data["armor_pieces"]) + 1,
        "name": name,
        "type": armor_type,
        "rarity": rarity,
        "material": material,
        "stats": stats,
        "level": 1,
        "upgrade_cost": len(rarity) * 100
    }

# Dashboard layout
app.layout = dbc.Container([
    html.H1("Armory Management Dashboard", className="mb-4 text-center"),
    
    dbc.Tabs([
        dbc.Tab(label="Armory Overview", children=[
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="armor-distribution-chart")
                ], width=6),
                dbc.Col([
                    dcc.Graph(id="material-distribution-chart")
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="rarity-distribution-chart")
                ], width=12)
            ]),
            html.Hr(),
            html.H3("Armory Inventory"),
            dash_table.DataTable(
                id="armor-table",
                columns=[
                    {"name": "ID", "id": "id"},
                    {"name": "Name", "id": "name"},
                    {"name": "Type", "id": "type"},
                    {"name": "Rarity", "id": "rarity"},
                    {"name": "Material", "id": "material"},
                    {"name": "Level", "id": "level"},
                    {"name": "Defense", "id": "stats.defense"},
                    {"name": "Durability", "id": "stats.durability"},
                    {"name": "Weight", "id": "stats.weight"},
                ],
                data=armory_data["armor_pieces"],
                filter_action="native",
                sort_action="native",
                page_size=10,
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "left", "padding": "10px"}
            )
        ]),
        
        dbc.Tab(label="Craft New Armor", children=[
            dbc.Card([
                dbc.CardBody([
                    html.H4("Craft New Armor Piece", className="card-title"),
                    dbc.Form([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Armor Type"),
                                dcc.Dropdown(
                                    id="armor-type-dropdown",
                                    options=[{"label": t, "value": t} for t in ARMOR_TYPES],
                                    value=ARMOR_TYPES[0]
                                )
                            ], width=4),
                            dbc.Col([
                                dbc.Label("Rarity"),
                                dcc.Dropdown(
                                    id="rarity-dropdown",
                                    options=[{"label": r, "value": r} for r in RARITIES],
                                    value=RARITIES[0]
                                )
                            ], width=4),
                            dbc.Col([
                                dbc.Label("Material"),
                                dcc.Dropdown(
                                    id="material-dropdown",
                                    options=[{"label": m, "value": m} for m in MATERIALS],
                                    value=MATERIALS[0]
                                )
                            ], width=4)
                        ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Armor Name"),
                                dbc.Input(
                                    id="armor-name-input",
                                    type="text",
                                    placeholder="Enter armor name"
                                )
                            ], width=12)
                        ], className="mt-3"),
                        dbc.Button(
                            "Craft Armor",
                            id="craft-armor-button",
                            color="primary",
                            className="mt-3"
                        )
                    ])
                ])
            ])
        ]),
        
        dbc.Tab(label="Upgrade Armor", children=[
            dbc.Row([
                dbc.Col([
                    html.H4("Select Armor to Upgrade"),
                    dcc.Dropdown(
                        id="upgrade-armor-dropdown",
                        options=[{"label": f"{a['name']} (Lvl {a['level']})", "value": a["id"]} 
                                for a in armory_data["armor_pieces"]],
                        placeholder="Select armor piece"
                    ),
                    html.Div(id="upgrade-armor-stats", className="mt-3"),
                    dbc.Button(
                        "Upgrade Armor",
                        id="upgrade-armor-button",
                        color="success",
                        className="mt-3",
                        disabled=True
                    )
                ], width=6),
                dbc.Col([
                    html.H4("Upgrade Preview"),
                    html.Div(id="upgrade-preview-stats")
                ], width=6)
            ])
        ])
    ]),
    
    dcc.Store(id="armory-data-store", data=armory_data)
], fluid=True)

# Callbacks for updating data and visualizations
@app.callback(
    Output("armory-data-store", "data"),
    Input("craft-armor-button", "n_clicks"),
    State("armor-type-dropdown", "value"),
    State("rarity-dropdown", "value"),
    State("material-dropdown", "value"),
    State("armor-name-input", "value"),
    State("armory-data-store", "data"),
    prevent_initial_call=True
)
def craft_armor(n_clicks, armor_type, rarity, material, name, data):
    if not name:
        return dash.no_update
    
    new_armor = create_armor_piece(armor_type, rarity, material, name)
    data["armor_pieces"].append(new_armor)
    save_data(data)
    return data

@app.callback(
    Output("armor-table", "data"),
    Output("armor-distribution-chart", "figure"),
    Output("material-distribution-chart", "figure"),
    Output("rarity-distribution-chart", "figure"),
    Input("armory-data-store", "data")
)
def update_dashboard(data):
    df = pd.DataFrame(data["armor_pieces"])
    
    # Update table
    table_data = df.to_dict("records")
    
    # Update charts
    type_fig = px.pie(
        df, names="type", title="Armor Type Distribution",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    material_fig = px.bar(
        df, x="material", title="Material Distribution",
        color="rarity", barmode="group",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    rarity_fig = px.histogram(
        df, x="rarity", title="Rarity Distribution",
        color="type", barmode="group",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    return table_data, type_fig, material_fig, rarity_fig

@app.callback(
    Output("upgrade-armor-dropdown", "options"),
    Input("armory-data-store", "data")
)
def update_upgrade_dropdown(data):
    return [{"label": f"{a['name']} (Lvl {a['level']})", "value": a["id"]} 
            for a in data["armor_pieces"]]

@app.callback(
    Output("upgrade-armor-stats", "children"),
    Output("upgrade-armor-button", "disabled"),
    Input("upgrade
