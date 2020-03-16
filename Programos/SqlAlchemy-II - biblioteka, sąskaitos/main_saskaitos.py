from sqlalchemy.orm import sessionmaker
from saskaitos import engine, Asmuo, Bankas, Saskaita

Session = sessionmaker(bind=engine)
session = Session()


# Įdedu asmenį, banką ir asmens sąskaitą

asmuo1 = Asmuo(vardas="Donatas", pavarde="Noreika", asmens_kodas=0000000000, tel_numeris="+370 000 00 000")
bankas1 = Bankas(pavadinimas="Swedbank", adresas="Konstitucijos pr. 20A, 03502 Vilnius", banko_kodas=73000, swift_kodas="HABALT22")
saskaita = Saskaita(numeris=0000000000000000, balansas=5000.45, asmuo=asmuo1, bankas=bankas1)

session.add(saskaita)
session.commit()