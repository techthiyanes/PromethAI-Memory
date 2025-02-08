from cognee.infrastructure.engine import DataPoint


class EdgeType(DataPoint):
    __tablename__ = "edge_type"
    relationship_name: str
    number_of_edges: int

    metadata: dict = {"index_fields": ["relationship_name"]}
