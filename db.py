import settings
import databases
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from datetime import datetime


DATABASE_URL = settings.settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

product = sqlalchemy.Table("product", metadata,
                           sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                           sqlalchemy.Column("name", sqlalchemy.String(100)),
                           sqlalchemy.Column("description", sqlalchemy.String(200)),
                           sqlalchemy.Column("price", sqlalchemy.Float)
                           )

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(100), nullable=False),
                         sqlalchemy.Column("lastname", sqlalchemy.String(200), nullable=False),
                         sqlalchemy.Column("mail", sqlalchemy.String(100)),
                         sqlalchemy.Column("password", sqlalchemy.String(100))
                         )

orders = sqlalchemy.Table("orders", metadata,
                          sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                          sqlalchemy.Column("user_id", ForeignKey("users.id")),
                          sqlalchemy.Column("product_id", ForeignKey('product.id')),
                          sqlalchemy.Column("time_order", sqlalchemy.String(200)),
                          sqlalchemy.Column("status", sqlalchemy.Boolean)
                          )

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
