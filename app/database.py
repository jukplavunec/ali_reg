from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    func,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
from sqlalchemy import NullPool
from app.config import settings

class BaseModel:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

database_params = {"poolclass": NullPool}
engine = create_async_engine(settings.db_url, **database_params, echo=False)
async_session_factory = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base(cls=BaseModel)
