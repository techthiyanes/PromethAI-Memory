from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, DateTime, String, JSON
from cognee.infrastructure.databases.relational import Base

class TaskRun(Base):
    __tablename__ = "task_runs"

    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid4)

    task_name = Column(String)

    created_at = Column(DateTime(timezone = True), default = lambda: datetime.now(timezone.utc))

    status = Column(String)

    run_info = Column(JSON)
