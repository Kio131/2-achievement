# database.py
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, text

DATABASE_URL = "sqlite:///./numbers.db"

Base = declarative_base()

class NumberEntry(Base):
    __tablename__ = "numbers"
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def check_number(number: int) -> str:
    with SessionLocal() as session: 
        result = session.execute(
            text("SELECT value FROM numbers WHERE value IN (:number, :number_minus_1) ORDER BY id DESC LIMIT 2"),
            {"number": number, "number_minus_1": number - 1}
        )

        rows = [row[0] for row in result.fetchall()]  # получаем список найденных чисел

        if number in rows:
            return "number_found"
        elif (number - 1) in rows:
            return "number-1_found"
        else:
            return "nothing_found"

async def save_number(number: int):
    with SessionLocal() as session:
        entry = NumberEntry(value=number)
        session.add(entry)
        session.commit()
