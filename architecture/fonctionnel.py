from diagrams import Diagram, Cluster, Edge
from diagrams.programming.flowchart import Action, Database, MultipleDocuments, Inspection

# This creates 'fonctionnel_bind9.png'
with Diagram("Schema Fonctionnel DNS", filename="fonctionnel_bind9", show=False, direction="LR"):
    
    inputs = MultipleDocuments("Entrées:\n- Requêtes DNS\n- Zone Files\n- Config")

    with Cluster("Traitement (BIND9 Logic)"):
        logic = Action("Résolution &\nRécursion")
        
        with Cluster("Contraintes"):
            security = Inspection("ACLs / Sécurité")
            docker_res = Database("Docker Limits")

    outputs = MultipleDocuments("Sorties:\n- Réponses IP\n- Logs\n- Cache")

    # Flow logic
    inputs >> logic
    security >> Edge(style="dashed", color="firebrick") >> logic
    docker_res >> Edge(style="dashed", color="gray") >> logic
    logic >> outputs