from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, String, BIGINT

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"Pets [name = {self.name}, type={self.type}]"