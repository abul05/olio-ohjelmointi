import random
import time


                        
class Olento:           
    #class muodostaa luokan tämän classin sisällä arvotaan numeroita/vahvuustasoa eri tyypeille esim nimi ja rohkeus.
    def __init__(self, nimi, rohkeus, katseen_voima):
        self.nimi = nimi
        self.rohkeus = rohkeus + random.randint(1,8)
        
        self.katseen_voima = katseen_voima + random.randint(katseen_voima,8)
        
        

        

class Peikko(Olento):
    
    """Luokka, joka kuvaa Peikon.

    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int

    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")


    def __init__(self, rohkeus = 4, katseen_voima = 4):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = rohkeus
        katseen_voima = katseen_voima
        super().__init__(nimi, rohkeus, katseen_voima)


    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)


### Kirjoita luokka Sankari tähän.
class Sankari (Olento):
    """
    Luokka edustaa sankarihahmoa pelissä. Sankarilla on nimi, rohkeus ja katseen voima. 
    Lisäksi hänellä on metodi arvo_hurraus, joka palauttaa satunnaisen merkkijonon. 
    """
    def __init__(self, nimi, rohkeus = 4, katseen_voima = 4):
        """
        Luo uuden sankari-olion annetulla nimellä, satunnaisella rohkeudella ja satunnaisella katseen voimalla.
        """
        self.nimi = nimi
        self.rohkeus = rohkeus
        self.katseen_voima = katseen_voima
        super().__init__(nimi, rohkeus, katseen_voima)

    def arvo_hurraus(self):
        """
        Palauta satunnainen hurrausmerkkijono.
        """
        hurraukset = ["Eläköön!", "Hurrraa!", "Voitto on meidän!", "Jes, me teimme sen!", "Hienoa työtä!"]
        return random.choice(hurraukset)
    
class Vuorenpeikko(Peikko):
    
    NIMITAVUT = ("moi", "hui", "hai", "loi", "hei", "poi", "leima", "siansaksa", "heprea", "moikka")
    RIEMUTAVUT = ("zaza", "koi", "ra", "tsa", "hehehe", "Suiii", "Limfao", "Raah", "suomi", "Raaste")
    
    def __init__(self, rohkeus = 3, katseen_voima = 6):
        #super viee tietoa peikko luokkaan
        super().__init__( rohkeus, katseen_voima)
        


class Luolapeikko(Peikko):

    NIMITAVUT = ("ai","ou","auts","jiik","ouh","eih","kääk")
    RIEMUTAVUT = ("bout", "to", "cum", "buuussss", "im", "bauta", "blow", "gaah", "bus", "yaaz", "haram bro")
   
    def __init__(self, rohkeus = 2, katseen_voima = 8):
         #super viee tietoa peikko luokkaan
        super().__init__( rohkeus, katseen_voima)

def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.

    :param olio: hurraava olio
    """
    print('%s: "%s!"' % (olio.nimi, olio.arvo_hurraus()))


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.

    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print("ja %s räpäyttää!" % rapayttaja.nimi)
        else:
            print("ja %s karkaa!" % rapayttaja.nimi)
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea


sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print("Sankarimme %s kävelee kohti seikkailua." % sankarin_tiedot)
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.
    peikkoilijat = [Peikko, Luolapeikko, Vuorenpeikko]
    valitut_peikot = random.choice(peikkoilijat)
    #arpoo vasustajan nimen 
    peikko = valitut_peikot()
    peikon_tiedot = peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print("Vastaan tulee hurja %s!" % peikon_tiedot)
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print("%s herää sängystään hikisenä - onneksi se oli vain unta!" % sankari.nimi)
