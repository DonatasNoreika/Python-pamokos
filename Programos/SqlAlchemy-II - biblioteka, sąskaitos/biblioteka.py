from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

engine = create_engine('sqlite:///biblioteka.db')
Base = declarative_base()


class Skaitytojas(Base):
    __tablename__ = "skaitytojas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    adresas = Column("Adresas", String)

class Autorius(Base):
    __tablename__ = "autorius"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    tautybe = Column("Tautybė", String)
    gimimo_metai = Column("Gimimo metai", Integer)
    mirties_metai = Column("Mirties metai", Integer)
    trumpa_biografija = Column("Trumpa biografija", String)

class Knyga(Base):
    __tablename__ = "knyga"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    zanras = Column("Žanras", String)
    isleidimo_metai = Column("Išleidimo metai", Integer)
    isbn = Column("ISBN", String)
    fizine_bukle = Column("Fizinė būklė", String)
    autorius_id = Column(Integer, ForeignKey('autorius.id'))
    autorius = relationship("Autorius")

class NuomosSutartis(Base):
    __tablename__ = "nuomos_sutartis"
    id = Column(Integer, primary_key=True)
    paemimo_data = Column("Paėmimo data", DateTime, default=datetime.now())
    grazinimo_data = Column("Gražinimo data", DateTime)
    uzstatas = Column("Užstatas", String)
    pastabos = Column("Pastabos", String)
    skaitytojas_id = Column(Integer, ForeignKey('skaitytojas.id'))
    skaitytojas = relationship("Skaitytojas")
    knyga_id = Column(Integer, ForeignKey('knyga.id'))
    knyga = relationship("Knyga")


Base.metadata.create_all(engine)


