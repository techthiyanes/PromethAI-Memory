from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, DateTime, String, JSON
from cognee.infrastructure.databases.relational import Base

class PipelineRun(Base):
    __tablename__ = "pipeline_runs"

    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid4)

    created_at = Column(DateTime(timezone = True), default = lambda: datetime.now(timezone.utc))

    run_name = Column(String, index = True)

    status = Column(String)

    run_info = Column(JSON)
