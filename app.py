import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
from adjustText import adjust_text
import matplotlib.font_manager as fm

# Make the page look nice and wide
st.set_page_config(page_title="Middle Earth Network Analysis", layout="wide")

# Start with a fresh graph - this will hold all our locations and paths
G = nx.DiGraph()

# This huge dictionary has all our locations and their info
# x,y coordinates are based on a reference map, and each place has a type
# (like haven, fortress, etc.) which we'll use for coloring later
locations = {
    # Classic good guy places
    'Shire': {'pos': (25, 52), 'type': 'haven'},        # Hobbit central!
    'Grey_Havens': {'pos': (15, 52), 'type': 'haven'},  # Elf port city
    'Rivendell': {'pos': (47, 52), 'type': 'haven'},    # Elrond's place
    'Bree': {'pos': (28, 52), 'type': 'town'},          # Where it all began...
    
    # Spooky abandoned places
    'Fornost': {'pos': (30, 57), 'type': 'ruin'},       # Old capital, now empty
    'Weathertop': {'pos': (32, 52), 'type': 'ruin'},    # That scary place with the Nazgul
    'Tharbad': {'pos': (35, 45), 'type': 'ruin'},       # Abandoned river crossing
    'Osgiliath': {'pos': (64, 23), 'type': 'ruin'},     # Gondor's old capital
    
    # Big important forests
    'Mirkwood': {'pos': (60, 55), 'type': 'forest'},    # Thranduil's sketchy woods
    'Fangorn': {'pos': (48, 38), 'type': 'forest'},     # Home of the Ents
    
    # Mountain stuff
    'Erebor': {'pos': (65, 62), 'type': 'mountain'},    # The Lonely Mountain!
    'Mount_Doom': {'pos': (69, 25), 'type': 'mountain'},# Where the ring goes bye-bye
    'Iron_Hills': {'pos': (75, 62), 'type': 'mountain'},# More dwarves here
    
    # Major cities and towns
    'Dale': {'pos': (65, 57), 'type': 'city'},          # City by Erebor
    'Esgaroth': {'pos': (68, 58), 'type': 'town'},      # Lake-town
    'Edoras': {'pos': (48, 28), 'type': 'city'},        # Horse bros
    'Minas_Tirith': {'pos': (62, 23), 'type': 'city'},  # White city
    'Pelargir': {'pos': (62, 18), 'type': 'city'},      # Harbor city
    'Dol_Guldur': {'pos': (62, 48), 'type': 'fortress'},# Sauron's vacation home
    'Minas_Morgul': {'pos': (66, 24), 'type': 'fortress'},# Super creepy city
    'Barad_dur': {'pos': (72, 26), 'type': 'fortress'}, # Sauron's main crib
    'Black_Gate': {'pos': (66, 29), 'type': 'gate'},    # Front door to Mordor
    
    # Other important spots
    'Moria': {'pos': (47, 43), 'type': 'ruin'},         # "You shall not pass!"
    'Lorien': {'pos': (52, 42), 'type': 'haven'},       # Galadriel's forest
    'Isengard': {'pos': (45, 35), 'type': 'fortress'},  # Saruman's tower
    'Dead_Marshes': {'pos': (62, 28), 'type': 'hazard'},# Spooky swamp
    'Paths_of_Dead': {'pos': (51, 24), 'type': 'pass'}, # Ghost shortcut
    'Cirith_Ungol': {'pos': (68, 24), 'type': 'pass'},  # Spider pass
    'Cair_Andros': {'pos': (61, 26), 'type': 'fortress'},# River fortress
    'Rhosgobel': {'pos': (55, 52), 'type': 'town'},     # Radagast's home
    'Gap_of_Rohan': {'pos': (45, 32), 'type': 'pass'},    # Gap in the White Mountains
    'Helms_Deep': {'pos': (46, 31), 'type': 'fortress'},  # Rohan's stronghold
}

# Add all our locations to the graph
for loc, data in locations.items():
    G.add_node(loc, pos=data['pos'], type=data['type'])

# Now we're setting up all the paths between places
# weight = how dangerous it is (1 = safe, 10 = super dangerous)
# type = what kind of path (road, mountain_pass, etc.)
routes = [
    ('Bree', 'Weathertop', {'weight': 3, 'type': 'road'}),
    ('Weathertop', 'Rivendell', {'weight': 4, 'type': 'road'}),
    ('Rivendell', 'Moria', {'weight': 7, 'type': 'mountain_pass'}),
    ('Moria', 'Lorien', {'weight': 5, 'type': 'forest_path'}),
    ('Lorien', 'Fangorn', {'weight': 4, 'type': 'forest_path'}),
    ('Fangorn', 'Isengard', {'weight': 3, 'type': 'road'}),
    ('Isengard', 'Helms_Deep', {'weight': 2, 'type': 'road'}),
    ('Helms_Deep', 'Edoras', {'weight': 2, 'type': 'road'}),
    ('Edoras', 'Minas_Tirith', {'weight': 4, 'type': 'road'}),
    ('Minas_Tirith', 'Osgiliath', {'weight': 3, 'type': 'road'}),
    ('Osgiliath', 'Dead_Marshes', {'weight': 7, 'type': 'hazardous_path'}),
    ('Dead_Marshes', 'Black_Gate', {'weight': 8, 'type': 'dangerous_path'}),
    ('Black_Gate', 'Barad_dur', {'weight': 9, 'type': 'dangerous_path'}),
    ('Barad_dur', 'Mount_Doom', {'weight': 10, 'type': 'dangerous_path'}),
    ('Rivendell', 'Mirkwood', {'weight': 5, 'type': 'forest_path'}),
    ('Mirkwood', 'Dale', {'weight': 4, 'type': 'forest_path'}),
    ('Dale', 'Erebor', {'weight': 2, 'type': 'road'}),
    ('Gap_of_Rohan', 'Isengard', {'weight': 3, 'type': 'road'}),
    ('Edoras', 'Paths_of_Dead', {'weight': 6, 'type': 'mountain_pass'}),
    ('Grey_Havens', 'Shire', {'weight': 2, 'type': 'road'}),
    ('Shire', 'Bree', {'weight': 2, 'type': 'road'}),
    ('Shire', 'Fornost', {'weight': 3, 'type': 'road'}),
    ('Bree', 'Fornost', {'weight': 3, 'type': 'road'}),
    ('Bree', 'Tharbad', {'weight': 4, 'type': 'road'}),
    ('Tharbad', 'Moria', {'weight': 5, 'type': 'road'}),
    ('Mirkwood', 'Dol_Guldur', {'weight': 6, 'type': 'dangerous_path'}),
    ('Dol_Guldur', 'Lorien', {'weight': 7, 'type': 'dangerous_path'}),
    ('Dale', 'Iron_Hills', {'weight': 4, 'type': 'road'}),
    ('Dale', 'Esgaroth', {'weight': 2, 'type': 'road'}),
    ('Mirkwood', 'Rhosgobel', {'weight': 3, 'type': 'forest_path'}),
    ('Rhosgobel', 'Lorien', {'weight': 4, 'type': 'forest_path'}),
    ('Osgiliath', 'Minas_Morgul', {'weight': 5, 'type': 'dangerous_path'}),
    ('Minas_Morgul', 'Cirith_Ungol', {'weight': 8, 'type': 'dangerous_path'}),
    ('Cirith_Ungol', 'Mount_Doom', {'weight': 7, 'type': 'dangerous_path'}),
    ('Minas_Tirith', 'Pelargir', {'weight': 3, 'type': 'road'}),
    ('Osgiliath', 'Cair_Andros', {'weight': 3, 'type': 'road'}),
    ('Cair_Andros', 'Dead_Marshes', {'weight': 5, 'type': 'hazardous_path'}),
    ('Tharbad', 'Gap_of_Rohan', {'weight': 5, 'type': 'road'}),
]

# Add bidirectional edges
# Make all paths two-way (you can go there AND back again... get it?)
for (src, dst, data) in routes:
    G.add_edge(src, dst, **data)
    G.add_edge(dst, src, **data)

def scale_coordinates(locations, original_width, original_height, new_width, new_height):
    """
    Makes our coordinates match the map size - just boring math stuff
    Think of it like resizing a photo but for coordinates
    """
    scaled_locations = {}
    for loc, data in locations.items():
        x, y = data['pos']
        # Basic cross multiplication to scale coordinates
        new_x = (x / original_width) * new_width
        new_y = (y / original_height) * new_height
        scaled_locations[loc] = {'pos': (new_x, new_y), 'type': data['type']}
    return scaled_locations

def create_visualization():
    """
    This is where the magic happens - creates the whole map visualization
    It's like drawing the map but with code instead of a pencil
    """
    # Set up our canvas with a dark theme (because it looks cool)
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 10), facecolor='#222222')
    
    # Make space for our map
    ax_map = fig.add_subplot(111)
    ax_map.set_facecolor('#222222')
    
    # Try to load the fancy map background
    try:
        map_img = mpimg.imread('middle_earth_map_optimized.png')
        img_height, img_width = map_img.shape[:2]
        
        # Make the coordinates match the map size
        desired_width = 50
        desired_height = int(desired_width * (img_height/img_width))
        scaled_locations = scale_coordinates(locations, 100, 75, desired_width, desired_height)
        
        # Update all our location coordinates
        for loc, data in scaled_locations.items():
            G.nodes[loc]['pos'] = data['pos']
        
        # Show the map
        ax_map.imshow(map_img, extent=[0, desired_width, 0, desired_height], aspect='auto', alpha=0.8)
    except FileNotFoundError:
        st.error("Couldn't find the map image :( Using blank background instead")
    
    # Get node positions
    pos = nx.get_node_attributes(G, 'pos')
    
    # Define node colors
    node_colors = {
        'city': '#ffd700',      # Gold
        'haven': '#90EE90',     # Light green
        'fortress': '#8B0000',  # Dark red
        'mountain': '#4a4a4a',  # Dark gray
        'forest': '#228B22',    # Forest green
        'ruin': '#8B4513',      # Saddle brown
        'town': '#FFA500',      # Orange
        'gate': '#000000',      # Black
        'hazard': '#800080',    # Purple
        'pass': '#A9A9A9'       # Gray
    }
    
    # Draw edges
    edge_colors = []
    edge_styles = []
    for (u, v) in G.edges():
        if G[u][v]['type'] in ['dangerous_path', 'hazardous_path']:
            edge_colors.append('#FF0000')
            edge_styles.append('dotted')
        else:
            edge_colors.append('#463E3F')
            edge_styles.append('solid')
    
    nx.draw_networkx_edges(G, pos,
                          edge_color=edge_colors,
                          style=edge_styles,
                          width=1.5,
                          alpha=0.7,
                          ax=ax_map)
    
    # Draw nodes
    for node_type in set(nx.get_node_attributes(G, 'type').values()):
        node_list = [node for node in G.nodes() if G.nodes[node]['type'] == node_type]
        nx.draw_networkx_nodes(G, pos,
                             nodelist=node_list,
                             node_color=node_colors[node_type],
                             node_size=700,
                             edgecolors='black',
                             linewidths=2,
                             alpha=0.8,
                             ax=ax_map)
    
    # Add labels
    texts = []
    for node, (x, y) in pos.items():
        texts.append(ax_map.text(x, y, node.replace('_', ' '),
                               fontsize=12,
                               horizontalalignment='center',
                               verticalalignment='center'))
    
    adjust_text(texts,
               arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5, lw=0.5),
               ax=ax_map)
    
    # Create legend
    legend_elements = []
    for loc_type, color in node_colors.items():
        legend_elements.append(
            mpatches.Patch(facecolor=color, edgecolor='black',
                          label=loc_type.replace('_', ' ').title())
        )
    
    legend_elements.extend([
        plt.Line2D([0], [0], color='#463E3F', linestyle='-',
                  label='Safe Path'),
        plt.Line2D([0], [0], color='#FF0000', linestyle=':',
                  label='Dangerous Path')
    ])
    
    ax_map.legend(handles=legend_elements,
                 title='Map Legend',
                 title_fontsize=12,
                 fontsize=10,
                 loc='lower center',
                 bbox_to_anchor=(0.5, -0.1),
                 ncol=3,
                 borderaxespad=0,
                 labelcolor='white')
    
    plt.tight_layout()
    return fig

def shortest_path_analysis(G, start='Bree', end='Mount_Doom'):
    """
    Finds the safest path between two places - like Google Maps for Middle Earth!
    Uses something called Dijkstra's algorithm, but don't worry too much about that.
    Just know it's really good at finding the best path when each step has a "cost".
    """
    try:
        # Find the path with the lowest danger score
        path = nx.shortest_path(G, start, end, weight='weight')
        # Calculate total danger score for the whole journey
        distance = nx.shortest_path_length(G, start, end, weight='weight')
        
        # Let's get some details about each step of the journey
        path_details = []
        for i in range(len(path)-1):
            current = path[i]
            next_loc = path[i+1]
            # Look up info about the path between these two places
            edge_data = G[current][next_loc]
            
            # Store all the juicy details
            path_details.append({
                'from': current.replace('_', ' '),  # Make it look prettier
                'to': next_loc.replace('_', ' '),
                'danger_level': edge_data['weight'],
                'path_type': edge_data['type'].replace('_', ' ')
            })
        
        return {
            'path': [p.replace('_', ' ') for p in path],  # Full journey
            'total_danger': distance,                      # Total danger score
            'path_details': path_details                   # Step-by-step details
        }
    except nx.NetworkXNoPath:
        # Uh oh, no path found! (like trying to walk into Mordor... oh wait)
        return None

def strategic_locations_analysis(G, top_n=5):
    """
    Figures out which places are the most important for controlling Middle Earth.
    Kind of like finding the most popular intersections in a city, but for fantasy!
    
    The 'betweenness_centrality' thing is just a fancy way of saying:
    "How often do you HAVE to go through this place to get anywhere else?"
    """
    # This calculates how important each location is based on paths going through it
    centrality = nx.betweenness_centrality(G, weight='weight')
    
    # Sort locations by importance score (highest to lowest)
    sorted_locations = sorted(
        centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]
    
    # Let's get more info about each important place
    strategic_details = []
    for loc, score in sorted_locations:
        # Count how many paths connect to this place
        connections = len(G.edges(loc))
        
        # Calculate average danger of paths around this place
        danger_levels = [G[loc][neighbor]['weight'] 
                        for neighbor in G.neighbors(loc)]
        avg_danger = sum(danger_levels) / len(danger_levels)
        
        # Combine all the stats
        strategic_details.append({
            'location': loc.replace('_', ' '),
            'strategic_value': round(score * 100, 2),  # Make it a percentage
            'num_paths': connections,
            'avg_danger': round(avg_danger, 2)
        })
    
    return strategic_details

def regional_groups_analysis(G):
    """
    Groups nearby locations together to find natural "regions" of Middle Earth.
    Like finding cliques in high school, but for fantasy locations!
    
    Uses the Louvain method - it's pretty smart about grouping things.
    It looks at how places are connected and groups them based on their relationships.
    """
    # Convert our graph to undirected (paths work both ways)
    G_undirected = G.to_undirected()
    
    # Find communities using the Louvain algorithm
    # Don't worry too much about the math - it's basically magic
    communities = list(nx.community.louvain_communities(
        G_undirected,
        weight='weight',
        resolution=1.0  # How picky we are about making groups
    ))
    
    # Let's analyze each group we found
    region_analysis = []
    for i, community in enumerate(communities):
        # Get a mini-graph of just this community
        subgraph = G_undirected.subgraph(community)
        
        # Calculate how connected this region is internally
        internal_edges = subgraph.number_of_edges()
        possible_edges = len(community) * (len(community) - 1) / 2
        density = internal_edges / possible_edges if possible_edges > 0 else 0
        
        # Find the average danger level within the region
        danger_levels = [G_undirected[u][v]['weight'] 
                        for u, v in subgraph.edges()]
        avg_danger = sum(danger_levels) / len(danger_levels) if danger_levels else 0
        
        # Get the most central location in this region
        # (like finding the capital city)
        subgraph_centrality = nx.degree_centrality(subgraph)
        capital = max(subgraph_centrality.items(), key=lambda x: x[1])[0]
        
        region_analysis.append({
            'region_number': i + 1,
            'locations': [loc.replace('_', ' ') for loc in sorted(community)],
            'size': len(community),
            'connectivity': round(density * 100, 2),  # Make it a percentage
            'avg_danger': round(avg_danger, 2),
            'regional_capital': capital.replace('_', ' ')
        })
    
    return region_analysis

def display_results(results, analysis_type):
    """
    Shows the results in a nice way in our Streamlit app
    Because no one likes reading raw Python dictionaries!
    """
    if analysis_type == "path":
        st.write("### 🚶‍♂️ Journey Details")
        st.write(f"Total Danger Score: {results['total_danger']:.2f}")
        
        # Show the path as a cool journey
        path_str = " → ".join(results['path'])
        st.write(f"Complete Path: {path_str}")
        
        # Make a nice table for the step-by-step details
        st.write("### Step by Step Breakdown:")
        for step in results['path_details']:
            with st.expander(f"{step['from']} to {step['to']}"):
                st.write(f"Path Type: {step['path_type']}")
                st.write(f"Danger Level: {step['danger_level']}/10")
                
    elif analysis_type == "strategic":
        st.write("### 🗺️ Strategic Locations Identified")
        for loc in results:
            with st.expander(f"{loc['location']} (Score: {loc['strategic_value']}%)"):
                st.write(f"Connected Paths: {loc['num_paths']}")
                st.write(f"Average Danger: {loc['avg_danger']}/10")
                
    elif analysis_type == "regions":
        st.write("### 🏰 Regional Analysis")
        for region in results:
            with st.expander(f"Region {region['region_number']} - Capital: {region['regional_capital']}"):
                st.write(f"Member Locations: {', '.join(region['locations'])}")
                st.write(f"Regional Connectivity: {region['connectivity']}%")
                st.write(f"Average Danger Level: {region['avg_danger']}/10")

def main():
    """
    This is where everything comes together!
    Like the Council of Elrond, but for code.
    """
    st.title("Middle Earth Network Analysis")
    st.write("Analyzing the paths and places of Middle Earth, because walking into Mordor actually requires some planning!")
    
    # Create two columns - map on left, analysis on right
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Show our awesome map
        fig = create_visualization()
        st.pyplot(fig)
    
    with col2:
        # Add analysis options
        analysis_type = st.selectbox(
            "What would you like to analyze?",
            ["Path Finder", "Strategic Locations", "Regional Groups"]
        )
        
        if analysis_type == "Path Finder":
            # Let users pick start and end points
            start = st.selectbox("Start Location", sorted(G.nodes()))
            end = st.selectbox("End Location", sorted(G.nodes()))
            
            if st.button("Find Path"):
                results = shortest_path_analysis(G, start, end)
                if results:
                    display_results(results, "path")
                else:
                    st.error("No safe path found! Maybe try taking the eagles? 🦅")
                    
        elif analysis_type == "Strategic Locations":
            n_locations = st.slider("Number of locations to analyze", 3, 10, 5)
            
            if st.button("Analyze Strategic Points"):
                results = strategic_locations_analysis(G, n_locations)
                display_results(results, "strategic")
                
        else:  # Regional Groups
            if st.button("Analyze Regions"):
                results = regional_groups_analysis(G)
                display_results(results, "regions")

if __name__ == '__main__':
    main()