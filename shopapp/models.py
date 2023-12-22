from shopapp import db
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

class User(db.Model):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, unique=True, nullable=False)
    password = mapped_column(String, nullable=False)

class Listing(db.Model):
    __tablename__ = "listing"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String)
    desc:Mapped[str] = mapped_column(Text)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    image_url:Mapped[str] = mapped_column(String, nullable=False)

class Tag(db.Model):
    __tablename__ = "tag"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String)

# many to many relationship (many listings can share the same tags)
class ListingTag(db.Model):
    __tablename__ = "listingTag"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    listing_id:Mapped[int] = mapped_column(ForeignKey("listing.id"), nullable=False)
    tag_id:Mapped[int] = mapped_column(ForeignKey("tag.id"), nullable=False)