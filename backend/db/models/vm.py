from pydantic import BaseSettings

class VirtualMachine(BaseSettings):
    id: int
    name: str
    status: str
    vcpu: int
    ram_memory: int
    disk_memory: int
    created_at: str
