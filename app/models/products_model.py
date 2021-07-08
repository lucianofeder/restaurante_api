from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float, Text
from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

@dataclass
class ProductsModel(db.Model):
    id: int
    recipe: str
    price: int
    calories: int
    section: str
    is_veggie: bool

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)

    name = Column(Text(150), nullable=False)
    price = Column(Float, nullable=False)
    calories = Column(Float)
    section = Column(String(150))
    is_veggie = Column(Boolean, default=False)
