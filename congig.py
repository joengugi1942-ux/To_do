from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:password23345@localhost:5432/api"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(session) as session:
        yield session
