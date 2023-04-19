class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.

    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, a, b):
        """Palauttaa kahden luvun summan.

        :param a: summan ensimmäinen luku
        :type a: Union[int, float]
        :param b: summan toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b summa
        :rtype: Union[int, float]
        """ 
        return sum([a, b])

    def kerro(self, a, b):
        """Palauttaa kahden luvun tulon.

        :param a: tulon ensimmäinen luku
        :type a: Union[int, float]
        :param b: tulon toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in [a, b]:
            tulo *= luku
        return tulo
    


class MonenLaskija(Laskija):
    """Luokka, joka toteuttaa eri laskutoimituksia useille luvuille.

    Korvaa Laskija-luokan metodit siten, että ne voivat ottaa vastaan kuinka monta lukua tahansa.
    """

    def summaa(self, *args):
        """Palauttaa lukujen summan.

        :param args: luvut, joiden summa halutaan laskea
        :type args: Union[int, float]
        :return: lukujen summa
        :rtype: Union[int, float]
        """
        return sum(args)

    def kerro(self, *args):
        """Palauttaa lukujen tulon.

        :param args: luvut, joiden tulo halutaan laskea
        :type args: Union[int, float]
        :return: lukujen tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo


def argumenttien_tulostaja(**kwargs):
    """Tulostaa annetut avainsana-argumentit avainsana ja arvo -muodossa."""
    for avainsana, arvo in kwargs.items():
        print(f'Argumentin "{avainsana}" arvo on {arvo}.')





### Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.

l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
