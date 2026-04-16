from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Bind9
from diagrams.onprem.client import Client
from diagrams.generic.network import Switch
from diagrams.generic.os import Ubuntu

# We add these attributes to force more space between elements
graph_attr = {
    "nodesep": "1.5",  # Horizontal space between nodes
    "ranksep": "2.0",  # Vertical space between layers
    "pad": "0.5"       # Padding around the whole diagram
}

with Diagram(
    "Architecture Technique BIND9", 
    filename="technique_bind9_fixed", 
    show=False, 
    direction="LR",
    graph_attr=graph_attr  # This is the key fix
):
    
    internet = Ubuntu("Internet / Root Servers\n(8.8.8.8)")

    with Cluster("Docker Host"):
        network_bridge = Switch("DNS_NET\nBridge Interne (172.20.0.0/24)")
        
        # We can add an empty label or padding to clusters if needed
        with Cluster("conteneur : ns-server"):
            authoritative = Bind9("BIND9 — Authoritative\n172.20.0.10")
            
        with Cluster("conteneur : ns-resolver"):
            resolver = Bind9("BIND9 — Recursive\n172.20.0.20")
            
        app_client = Client("Client App\n(NS: 172.20.0.20)")

    # Connections with explicit labels
    # Using 'minlen' in Edge can also force more vertical distance if needed
    app_client >> Edge(label="query", color="blue", minlen="2") >> network_bridge
    network_bridge >> Edge(color="blue", minlen="2") >> resolver
    
    # Recursive lookups
    resolver >> Edge(label="external forward", style="dashed", color="orange") >> internet
    resolver >> Edge(label="local zone lookup", color="green", style="bold") >> authoritative