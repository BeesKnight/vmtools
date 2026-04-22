from fastapi import FastAPI, HTTPException
from api.v1.vm import vm_router

app = FastAPI(title="VM Tools API", version="1.0", description="API for managing virtual machines")

app.include_router(vm_router, prefix="/api/v1")