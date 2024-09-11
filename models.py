"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
db = SQLAlchemy()


DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Base(DeclarativeBase):
    pass

"""
class Cupcake(db.Model):
    ""Cupcake.""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def to_dict(self):
        ""Serialize cupcake to a dict of cupcake info.""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }
"""




class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcakes"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    flavor: Mapped[str] = mapped_column(db.Text, nullable=False)
    size: Mapped[str] = mapped_column(db.Text, nullable=False)
    rating: Mapped[int] = mapped_column(db.Float, nullable=False)
    image: Mapped[str] = mapped_column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def to_dict(self):
        """Serialize cupcake to a dict of cupcake info."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
