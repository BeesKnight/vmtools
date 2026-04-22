from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from db.session import SessionLocal

vm_router = APIRouter(prefix="/vms", tags=["VMs"])

@vm_router.post("/vms")
async def create_vm(vm_name: str) -> dict[str, int]:
    async with SessionLocal() as session:
        if session is None:
            raise HTTPException(status_code=500, detail="Database session not available")
        result = await session.execute(text("SELECT create_vm(:vm_name)"), {"vm_name": vm_name})
        vm_id = result.scalar()
        if vm_id is None:
            raise HTTPException(status_code=400, detail="Failed to create VM")
        return {"vm_id": vm_id}