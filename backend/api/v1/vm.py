from fastapi import APIRouter, FastAPI, HTTPException

vm_router = APIRouter(prefix="/vms", tags=["VMs"])

@vm_router.post("/vms")
async def create_vm(vm_name: str):
    # Placeholder for VM creation logic
    if vm_name == "existing_vm":
        raise HTTPException(status_code=400, detail="VM already exists")
    return {"message": f"VM '{vm_name}' created successfully"}