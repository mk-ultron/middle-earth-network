# Middle Earth Network Analysis

## Overview
This project implements a network analysis of Middle Earth's transportation system using Python's NetworkX library. The graph represents key locations from Tolkien's world as nodes and the paths between them as edges, with weights representing the difficulty/danger of travel.

## Features
- Interactive visualization of Middle Earth's transportation network
- 20 key locations (nodes) including cities, fortresses, forests, and landmarks
- 38 bidirectional paths (edges) with weighted difficulty levels
- Color-coded location types and path safety indicators
- Three network analysis algorithms:
  1. Shortest (safest) path finding
  2. Strategic location analysis using betweenness centrality
  3. Regional grouping detection using community detection

## Prerequisites
- Python 3.7+
- NetworkX
- Matplotlib
- Adjustext

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/middle-earth-network.git
cd middle-earth-network
```

2. Install required packages:
```bash
pip install networkx matplotlib adjustText
```

3. (Optional) Install the Middle Earth font for authentic styling:
   - Place `middle_earth_font.ttf` in the project directory
   - The program will fallback to serif font if not available

## Usage
Run the main program:
```bash
python middle_earth_network.py
```

The program will:
1. Display an interactive map visualization
2. Print network analysis results to the console
3. Show the safest path from Bree to Mount Doom
4. Identify strategic locations
5. Display regional groupings

## Network Structure

### Location Types
- Cities (Gold): Major population centers
- Havens (Light Green): Elven refuges
- Fortresses (Dark Red): Military strongholds
- Mountains (Dark Gray): Major peaks
- Forests (Forest Green): Wooded regions
- Ruins (Saddle Brown): Ancient remnants
- Towns (Orange): Smaller settlements
- Gates (Black): Strategic passageways
- Hazards (Purple): Dangerous areas
- Passes (Gray): Mountain passages

### Path Types
- Safe Paths (Solid Gray): Normal travel routes
- Dangerous Paths (Dotted Red): High-risk routes

### Edge Weights
Paths are weighted on a scale of 1-10 based on difficulty/danger:
- 1-3: Safe, well-traveled routes
- 4-6: Moderate difficulty
- 7-8: Dangerous passages
- 9-10: Extremely perilous routes

## Analysis Features

### 1. Shortest Path Analysis
Identifies the safest route between locations using Dijkstra's algorithm, taking into account path difficulty weights.

### 2. Strategic Locations
Uses betweenness centrality to identify key strategic positions in the network, highlighting locations that are important for controlling movement through Middle Earth.

### 3. Regional Groupings
Employs community detection to identify natural groupings of locations, revealing the underlying regional structure of Middle Earth.

## Visualization
The visualization includes:
- Interactive map with background image
- Color-coded locations by type
- Path representations showing safety levels
- Comprehensive legend
- Non-overlapping location labels

## Acknowledgments
- J.R.R. Tolkien for creating the rich world of Middle Earth
- NetworkX team for the excellent graph analysis library
- Middle Earth maps used for reference ([this reddit post/user](https://www.reddit.com/r/lotr/comments/bcvzaz/map_of_middle_earth_without_labels_enjoy/))

## Contact
Your Name - [@yourusername](https://github.com/mk-ultron)
Project Link: [https://github.com/mk-ultron/middle-earth-network](https://github.com/mk-ultron/middle-earth-network)