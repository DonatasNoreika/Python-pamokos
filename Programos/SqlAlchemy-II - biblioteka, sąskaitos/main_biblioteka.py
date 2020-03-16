from sqlalchemy.orm import sessionmaker
from biblioteka import engine, Autorius, Knyga, Skaitytojas, NuomosSutartis
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

# Įdedu autorių, knygą, skaitytojų ir nuomos sutartį

autorius1 = Autorius(vardas="George", pavarde="Orwell", tautybe="Anglas", gimimo_metai=1903, mirties_metai=1950, trumpa_biografija="https://lt.wikipedia.org/wiki/George_Orwell")
knyga1 = Knyga(pavadinimas="1984-ieji", zanras="Antiutopinis romanas", isleidimo_metai=1949, isbn=576767, fizine_bukle="Gera", autorius = autorius1)
skaitytojas1 = Skaitytojas(vardas="Donatas", pavarde="Noreika", adresas="Kairėnai")
nuomos_sutartis = NuomosSutartis(grazinimo_data= datetime(2020, 3, 31), uzstatas="100 Eur", pastabos="Nėra", skaitytojas=skaitytojas1, knyga = knyga1)

session.add(nuomos_sutartis)
session.commit()