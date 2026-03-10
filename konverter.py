"""
Zahl-zu-Wort Konverter (Deutsch)
Verwendung: python zahl_zu_wort.py <zahl>
Beispiel:   python zahl_zu_wort.py 256
"""

import sys

EINER = [
    "", "ein", "zwei", "drei", "vier", "fünf",
    "sechs", "sieben", "acht", "neun", "zehn",
    "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn",
    "sechzehn", "siebzehn", "achtzehn", "neunzehn"
]

ZEHNER = [
    "", "", "zwanzig", "dreißig", "vierzig", "fünfzig",
    "sechzig", "siebzig", "achtzig", "neunzig"
]


def konvertiere_unter_1000(n: int) -> str:
    """Konvertiert eine Zahl von 1 bis 999 in Wortform."""
    if n == 0:
        return ""

    if n < 20:
        return EINER[n]

    if n < 100:
        einer = n % 10
        zehner = n // 10
        if einer == 0:
            return ZEHNER[zehner]
        return EINER[einer] + "und" + ZEHNER[zehner]

    # 100–999
    hundert = n // 100
    rest = n % 100
    prefix = ("ein" if hundert == 1 else EINER[hundert]) + "hundert"
    return prefix + konvertiere_unter_1000(rest)


def zahl_zu_wort(n: int) -> str:
    """Konvertiert eine ganze Zahl in die deutsche Wortform."""
    if n < 0:
        return "minus " + zahl_zu_wort(-n)

    if n == 0:
        return "null"

    if n == 1:
        return "eins"

    teile = []

    # Milliarden
    if n >= 1_000_000_000:
        mrd = n // 1_000_000_000
        n %= 1_000_000_000
        if mrd == 1:
            teile.append("eine milliarde")
        else:
            teile.append(konvertiere_unter_1000(mrd) + " milliarden")

    # Millionen
    if n >= 1_000_000:
        mio = n // 1_000_000
        n %= 1_000_000
        if mio == 1:
            teile.append("eine million")
        else:
            teile.append(konvertiere_unter_1000(mio) + " millionen")

    # Tausender
    if n >= 1_000:
        tsd = n // 1_000
        n %= 1_000
        if tsd == 1:
            teile.append("eintausend")
        else:
            teile.append(konvertiere_unter_1000(tsd) + "tausend")

    # Rest (1–999)
    if n > 0:
        teile.append(konvertiere_unter_1000(n))

    wort = "".join(teile)
    return wort[0].upper() + wort[1:]


def main():
    if len(sys.argv) < 2:
        print("Verwendung: python zahl_zu_wort.py <zahl>")
        print("Beispiel:   python zahl_zu_wort.py 256")
        sys.exit(1)

    eingabe = sys.argv[1].replace(".", "").replace(",", "").replace(" ", "")

    try:
        zahl = int(eingabe)
    except ValueError:
        print(f"Fehler: '{sys.argv[1]}' ist keine gültige ganze Zahl.")
        sys.exit(1)

    if zahl < -999_999_999_999 or zahl > 999_999_999_999:
        print("Fehler: Zahl muss zwischen -999.999.999.999 und 999.999.999.999 liegen.")
        sys.exit(1)

    print(zahl_zu_wort(zahl))


if __name__ == "__main__":
    main()
