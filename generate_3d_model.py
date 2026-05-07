import plotly.graph_objects as go

# Create a 3D building model for Vishwanath Construction villa experience
# Building structure: Ground floor with living room, bedroom, balcony, and garden area

# Define colors
wall_color = 'lightblue'
floor_color = 'beige'
roof_color = 'brown'
garden_color = 'green'

# Create figure
fig = go.Figure()

# Ground floor base (10x10x0.5)
fig.add_trace(go.Mesh3d(
    x=[0, 10, 10, 0, 0, 10, 10, 0],
    y=[0, 0, 10, 10, 0, 0, 10, 10],
    z=[0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5],
    i=[0, 0, 0, 1, 4, 4, 6, 6, 4, 0, 3, 6],
    j=[1, 2, 4, 2, 1, 2, 5, 5, 5, 7, 2, 2],
    k=[2, 3, 1, 3, 2, 6, 2, 4, 6, 6, 7, 7],
    color=floor_color,
    name='Ground Floor'
))

# Living Room (4x6x3) - front left
fig.add_trace(go.Mesh3d(
    x=[0, 4, 4, 0, 0, 4, 4, 0],
    y=[0, 0, 6, 6, 0, 0, 6, 6],
    z=[0.5, 0.5, 0.5, 0.5, 3.5, 3.5, 3.5, 3.5],
    i=[0, 0, 0, 1, 4, 4, 6, 6, 4, 0, 3, 6],
    j=[1, 2, 4, 2, 1, 2, 5, 5, 5, 7, 2, 2],
    k=[2, 3, 1, 3, 2, 6, 2, 4, 6, 6, 7, 7],
    color=wall_color,
    opacity=0.7,
    name='Living Room'
))

# Bedroom (4x4x3) - back left
fig.add_trace(go.Mesh3d(
    x=[0, 4, 4, 0, 0, 4, 4, 0],
    y=[6, 6, 10, 10, 6, 6, 10, 10],
    z=[0.5, 0.5, 0.5, 0.5, 3.5, 3.5, 3.5, 3.5],
    i=[0, 0, 0, 1, 4, 4, 6, 6, 4, 0, 3, 6],
    j=[1, 2, 4, 2, 1, 2, 5, 5, 5, 7, 2, 2],
    k=[2, 3, 1, 3, 2, 6, 2, 4, 6, 6, 7, 7],
    color=wall_color,
    opacity=0.7,
    name='Bedroom'
))

# Balcony (2x4x2) - front right
fig.add_trace(go.Mesh3d(
    x=[4, 6, 6, 4, 4, 6, 6, 4],
    y=[0, 0, 4, 4, 0, 0, 4, 4],
    z=[0.5, 0.5, 0.5, 0.5, 2.5, 2.5, 2.5, 2.5],
    i=[0, 0, 0, 1, 4, 4, 6, 6, 4, 0, 3, 6],
    j=[1, 2, 4, 2, 1, 2, 5, 5, 5, 7, 2, 2],
    k=[2, 3, 1, 3, 2, 6, 2, 4, 6, 6, 7, 7],
    color='lightgray',
    opacity=0.8,
    name='Balcony'
))

# Garden area (4x6x0.2) - back right
fig.add_trace(go.Mesh3d(
    x=[4, 10, 10, 4, 4, 10, 10, 4],
    y=[4, 4, 10, 10, 4, 4, 10, 10],
    z=[0.5, 0.5, 0.5, 0.5, 0.7, 0.7, 0.7, 0.7],
    i=[0, 0, 0, 1, 4, 4, 6, 6, 4, 0, 3, 6],
    j=[1, 2, 4, 2, 1, 2, 5, 5, 5, 7, 2, 2],
    k=[2, 3, 1, 3, 2, 6, 2, 4, 6, 6, 7, 7],
    color=garden_color,
    opacity=0.9,
    name='Garden'
))

# Roof (10x10x0.3) - on top
fig.add_trace(go.Mesh3d(
    x=[0, 10, 10, 0, 0, 10, 10, 0],
    y=[0, 0, 10, 10, 0, 0, 10, 10],
    z=[3.5, 3.5, 3.5, 3.5, 3.8, 3.8, 3.8, 3.8],
    i=[0, 0, 0, 1, 4, 4, 6, 6, 4, 0, 3, 6],
    j=[1, 2, 4, 2, 1, 2, 5, 5, 5, 7, 2, 2],
    k=[2, 3, 1, 3, 2, 6, 2, 4, 6, 6, 7, 7],
    color=roof_color,
    name='Roof'
))

# Update layout for better viewing
fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=4, range=[-2,12]),
        yaxis=dict(nticks=4, range=[-2,12]),
        zaxis=dict(nticks=4, range=[-1,5]),
        aspectmode='data'
    ),
    title="",
    width=800,
    height=600,
    margin=dict(r=10, l=10, b=10, t=40),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Generate the Plotly HTML
plot_html = fig.to_html(include_plotlyjs='cdn', full_html=False)

# Wrap in AutoCAD-like interface
cad_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vishwanath Construction - 3D CAD Villa Experience</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #2d2d30;
            color: #ffffff;
            overflow: hidden;
        }}
        .cad-toolbar {{
            background-color: #3c3c3c;
            padding: 5px;
            border-bottom: 1px solid #555;
            display: flex;
            align-items: center;
        }}
        .cad-toolbar button {{
            background-color: #4c4c4c;
            border: 1px solid #666;
            color: #fff;
            padding: 5px 10px;
            margin: 0 2px;
            cursor: pointer;
            border-radius: 3px;
        }}
        .cad-toolbar button:hover {{
            background-color: #5c5c5c;
        }}
        .cad-main {{
            display: flex;
            height: calc(100vh - 40px);
        }}
        .cad-sidebar {{
            width: 200px;
            background-color: #252526;
            border-right: 1px solid #555;
            padding: 10px;
        }}
        .cad-sidebar h3 {{
            margin-top: 0;
            color: #cccccc;
        }}
        .cad-sidebar ul {{
            list-style: none;
            padding: 0;
        }}
        .cad-sidebar li {{
            padding: 5px 0;
            cursor: pointer;
        }}
        .cad-sidebar li:hover {{
            background-color: #37373d;
        }}
        .cad-viewport {{
            flex: 1;
            background-color: #1e1e1e;
            display: flex;
            flex-direction: column;
        }}
        .cad-model-space {{
            flex: 1;
            padding: 10px;
        }}
        .cad-command-line {{
            background-color: #3c3c3c;
            border-top: 1px solid #555;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }}
        .cad-title {{
            text-align: center;
            padding: 10px;
            background-color: #007acc;
            color: white;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="cad-title">Vishwanath Construction - 3D CAD Villa Experience</div>
    <div class="cad-toolbar">
        <button>🏠 Home</button>
        <button>🔍 Zoom</button>
        <button>↻ Rotate</button>
        <button>📏 Measure</button>
        <button>💾 Save</button>
        <button>📤 Export</button>
    </div>
    <div class="cad-main">
        <div class="cad-sidebar">
            <h3>Model Tree</h3>
            <ul>
                <li>🏠 Ground Floor</li>
                <li>🛋️ Living Room</li>
                <li>🛏️ Bedroom</li>
                <li>🌅 Balcony</li>
                <li>🌳 Garden</li>
                <li>🏠 Roof</li>
            </ul>
            <h3>Properties</h3>
            <p>Dimensions: 10x10m<br>Height: 3.8m<br>Rooms: 2</p>
        </div>
        <div class="cad-viewport">
            <div class="cad-model-space">
                {plot_html}
            </div>
            <div class="cad-command-line">
                Command: Ready | Click and drag to rotate view | Scroll to zoom
            </div>
        </div>
    </div>
</body>
</html>
"""

# Save the custom HTML
with open("3d_building_model.html", "w", encoding="utf-8") as f:
    f.write(cad_html)

print("3D CAD-style building model generated and saved as 3d_building_model.html")