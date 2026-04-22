from fastapi import FastAPI, HTTPException
from api.v1.vm import vm_router
from core.config import settings

app = FastAPI(
    title=settings.api_name,
    version=settings.api_version, 
    description="API for managing virtual machines"
    )

app.include_router(vm_router, prefix="/api/v1")