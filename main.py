from fastapi import FastAPI
from app.routes import auth
from app.core.database import engine, Base
from app.models import task
from app.routes import tasks
from app.routes import user_routes
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(auth.router, prefix="/api/auth")
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(user_routes.router, prefix="/api/users")


@app.get("/")
def home():
    return {"message": "API funcionando correctamente :)"}
