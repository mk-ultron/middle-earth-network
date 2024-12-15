import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from adjustText import adjust_text

# Create a new directed graph
G = nx.DiGraph()

# Define locations with updated coordinates
locations = {
    'Erebor': {'pos': (88, 58), 'type': 'mountain'},
    'Dale': {'pos': (87, 57), 'type': 'city'},
    'Rivendell': {'pos': (47, 52), 'type': 'haven'},
    'Mirkwood': {'pos': (70, 53), 'type': 'forest'},
    'Weathertop': {'pos': (32, 52), 'type': 'ruin'},
    'Bree': {'pos': (28, 52), 'type': 'town'},
    'Moria': {'pos': (47, 43), 'type': 'ruin'},
    'Lorien': {'pos': (52, 42), 'type': 'haven'},
    'Fangorn': {'pos': (48, 38), 'type': 'forest'},
    'Isengard': {'pos': (45, 35), 'type': 'fortress'}, 
    'Helms_Deep': {'pos': (48, 33), 'type': 'fortress'},
    'Gap_of_Rohan': {'pos': (35, 32), 'type': 'pass'},
    'Edoras': {'pos': (52, 30), 'type': 'city'},
    'Minas_Tirith': {'pos': (62, 23), 'type': 'city'},
    'Osgiliath': {'pos': (64, 23), 'type': 'ruin'},
    'Dead_Marshes': {'pos': (68, 28), 'type': 'hazard'},
    'Black_Gate': {'pos': (72, 23), 'type': 'gate'},
    'Mount_Doom': {'pos': (78, 18), 'type': 'mountain'},
    'Barad_dur': {'pos': (75, 20), 'type': 'fortress'},
    'Paths_of_Dead': {'pos': (38, 25), 'type': 'pass'}
}


# Add nodes to the graph
for loc, data in locations.items():
    G.add_node(loc, pos=data['pos'], type=data['type'])

# Define routes with weights (1-10 scale for difficulty/danger)
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
    ('Edoras', 'Paths_of_Dead', {'weight': 6, 'type': 'mountain_pass'})
]

# Add edges to the graph
for (src, dst, data) in routes:
    G.add_edge(src, dst, **data)
    G.add_edge(dst, src, **data)  # Add reverse route

# Load the custom font
try:
    font_path = 'middle_earth_font.ttf'
    fm.fontManager.addfont(font_path)
    custom_font = fm.FontProperties(fname=font_path)
    font_family = custom_font.get_name()
except:
    print("Warning: Custom font not loaded, using default font")
    font_family = 'serif'

def visualize_middle_earth():
    plt.figure(figsize=(20, 15))
    
    # Load and display the background map
    map_img = mpimg.imread('middle_earth_map.png')
    plt.imshow(map_img, extent=[0, 100, 0, 75], aspect='auto', alpha=0.8)
    
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
    
    # Draw edges with style based on type
    edge_colors = []
    edge_styles = []
    for (u, v) in G.edges():
        if G[u][v]['type'] in ['dangerous_path', 'hazardous_path']:
            edge_colors.append('#FF0000')  # Red for dangerous paths
            edge_styles.append('dotted')
        else:
            edge_colors.append('#463E3F')  # Dark gray for normal paths
            edge_styles.append('solid')
    
    # Draw edges
    nx.draw_networkx_edges(G, pos,
                          edge_color=edge_colors,
                          style=edge_styles,
                          width=1.5,
                          alpha=0.7)
    
    # Draw nodes
    for node_type in set(nx.get_node_attributes(G, 'type').values()):
        node_list = [node for node in G.nodes() if G.nodes[node]['type'] == node_type]
        nx.draw_networkx_nodes(G, pos,
                             nodelist=node_list,
                             node_color=node_colors[node_type],
                             node_size=700,
                             edgecolors='black',
                             linewidths=2,
                             alpha=0.8)
    
    # Create text objects for all labels
    texts = []
    for node, (x, y) in pos.items():
        texts.append(plt.text(x, y, node.replace('_', ' '),
                            fontsize=12,
                            fontfamily=font_family,
                            horizontalalignment='center',
                            verticalalignment='center'))
    
    # Adjust label positions to avoid overlap
    adjust_text(texts,
               arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5, lw=0.5),
               expand_points=(1.2, 1.2),
               force_points=(0.5, 0.5))
    
    # Add title
    plt.title("Realms of Middle Earth - Network Analysis",
             fontfamily=font_family,
             size=24,
             pad=20)
    
    plt.axis('off')
    plt.tight_layout()
    plt.show()


# Add analysis function
def analyze_network():
    print("\nNetwork Analysis Results:")
    
    # Shortest Path Analysis
    print("\n1. Shortest (Safest) Path Analysis (Bree to Mount Doom):")
    path = nx.shortest_path(G, 'Bree', 'Mount_Doom', weight='weight')
    distance = nx.shortest_path_length(G, 'Bree', 'Mount_Doom', weight='weight')
    print(f"Safest route: {' -> '.join(path)}")
    print(f"Total danger score: {distance}")
    
    # Strategic Locations Analysis
    print("\n2. Strategic Locations (Betweenness Centrality):")
    centrality = nx.betweenness_centrality(G)
    sorted_locations = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 most strategic locations:")
    for loc, score in sorted_locations[:5]:
        print(f"{loc}: {score:.3f}")
    
    # Regional Analysis
    print("\n3. Regional Groupings:")
    communities = list(nx.community.greedy_modularity_communities(G))
    print(f"Number of distinct regions: {len(communities)}")
    for i, community in enumerate(communities, 1):
        print(f"Region {i}: {', '.join(community)}")

# Run visualization and analysis
visualize_middle_earth()
analyze_network()