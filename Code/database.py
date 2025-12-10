# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, text

DATABASE_URL = "sqlite+aiosqlite:///./numbers.db"

Base = declarative_base()

class NumberEntry(Base):
    __tablename__ = "numbers"
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def check_number(number: int) -> str:
    async with async_session() as session: 
        result = await session.execute(
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
    async with async_session() as session:
        session.add(NumberEntry(value=number))
        await session.commit()
