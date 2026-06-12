
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Dispute(Base):
    __tablename__='disputes'
    id: Mapped[int] = mapped_column(primary_key=True)
