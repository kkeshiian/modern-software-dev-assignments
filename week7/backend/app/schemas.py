from datetime import datetime

from pydantic import BaseModel

from typing import Optional

class CategoryCreate(BaseModel):
    name: str

class CategoryRead(CategoryCreate):
    id: int

    class Config:
        from_attributes = True

class NoteCreate(BaseModel):
    id: int
    title: str
    content: str
    category_id: Optional[int] = None # Tambahkan field ini
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None


class ActionItemCreate(BaseModel):
    description: str


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: str | None = None
    completed: bool | None = None


