# Middle Earth Network Analysis

## Overview
This project implements a network analysis of Middle Earth's travel system using Python's NetworkX library. The graph represents key locations from Tolkien's world as nodes and the paths between them as edges, with weights representing the difficulty/danger of travel.

## Key Features
- Interactive map visualization with 32 key locations
- Three powerful analysis tools:
  - Path Finder: Find the safest route between any two locations
  - Strategic Points Analyzer: Identify key control points in Middle Earth
  - Regional Groups Detective: Discover natural geographic communities
- Color-coded locations and paths showing different types and danger levels
- Detailed journey breakdowns with danger scores and path types

![image](https://github.com/user-attachments/assets/a56dc8b3-9ce2-469a-a3c2-5daa8d2b06ce)

## Prerequisites
```bash
# Core requirements
streamlit       # For the web interface
networkx        # The brain behind our network analysis
matplotlib      # Makes everything look pretty
adjustText      # Keeps our labels from overlapping
```

## Quick Start
1. Clone the repo and install dependencies:
```bash
git clone https://github.com/mk-ultron/middle-earth-network.git
cd middle-earth-network
pip install -r requirements.txt
```

2. Add your map image:
- Place 'middle_earth_map_optimized.png' in the project directory
- Don't worry, the app works without it too!

3. Fire it up:
```bash
streamlit run app.py
```

## Network Structure

### Location Types
Each location in Middle Earth is categorized:
- 🏰 Cities (Gold): Major population centers like Minas Tirith
- 🌳 Havens (Light Green): Safe spots like Rivendell
- 🗼 Fortresses (Dark Red): The scary places like Barad-dûr
- ⛰️ Mountains (Dark Gray): Where dragons sleep
- 🌲 Forests (Forest Green): Watch out for spiders!
- 🏛️ Ruins (Brown): Abandoned but important
- 🏘️ Towns (Orange): Cozy places like Bree
- 🚪 Gates (Black): Important entrances
- ⚠️ Hazards (Purple): The Dead Marshes and such
- 🏔️ Passes (Gray): Mountain crossings

### Path Types and Danger Levels
- Safe Roads (1-3): Well-traveled paths, like Shire to Bree
- Standard Routes (4-5): Regular roads with some risk
- Tricky Paths (6-7): Forest paths and mountain passes
- Dangerous Routes (8-10): The "don't go alone" paths

## Analysis Features

### 1. Path Finder
```python
def shortest_path_analysis(G, start='Bree', end='Mount_Doom'):
    # Finds the safest path between locations
    # Returns: Complete route, danger scores, and path details
```
- Uses Dijkstra's algorithm (fancy path-finding math)
- Considers both distance and danger
- Provides step-by-step journey breakdown
- Calculates total danger score

### 2. Strategic Locations Analyzer
```python
def strategic_locations_analysis(G, top_n=5):
    # Identifies key control points in Middle Earth
    # Returns: Important locations and their strategic values
```
- Uses betweenness centrality (finds important crossroads)
- Ranks locations by strategic importance
- Analyzes connection patterns
- Calculates regional influence

### 3. Regional Groups Detective
```python
def regional_groups_analysis(G):
    # Finds natural geographic communities
    # Returns: Region details with capitals and characteristics
```
- Implements Louvain community detection
- Identifies natural borders and regions
- Calculates regional characteristics:
  - Internal connectivity
  - Average danger levels
  - Regional capitals

## Usage Examples

### Finding a Safe Path
```python
# Through the web interface:
1. Select "Path Finder"
2. Choose start and end points
3. Click "Find Path"
4. Get detailed journey breakdown
```

### Analyzing Strategic Points
```python
# Through the web interface:
1. Select "Strategic Locations"
2. Choose number of locations to analyze
3. Get ranked list of key positions
```

### Discovering Regions
```python
# Through the web interface:
1. Select "Regional Groups"
2. Click "Analyze Regions"
3. Explore natural territory divisions
```

## Visualization Features
- Interactive Streamlit interface
- Color-coded map with location markers
- Path highlighting
- Danger level indicators
- Region grouping visualization
- Expandable details for each analysis

## Implementation Notes
- Built with Streamlit for easy web interaction
- NetworkX handles the heavy lifting of graph analysis
- Matplotlib creates the visualizations

## Acknowledgments
- J.R.R. Tolkien for creating Middle Earth
- NetworkX team for the graph tools
- Streamlit team for making web apps easy
- The community for map resources

## Contact
[@mk-ultron](https://github.com/mk-ultron)
Project Link: [https://github.com/mk-ultron/middle-earth-network](https://github.com/mk-ultron/middle-earth-network)
