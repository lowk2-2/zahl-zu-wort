# Zahl-zu-Wort Konverter

Ein einfaches Python-CLI-Tool, das ganze Zahlen in deutsche Wortform umwandelt.

```
256  →  Zweihundertsechsundfünfzig
```

## Verwendung

```bash
python zahl_zu_wort.py <zahl>
```

**Beispiele:**

```bash
python zahl_zu_wort.py 256
# Zweihundertsechsundfünfzig

python zahl_zu_wort.py 1000000
# Eine million

python zahl_zu_wort.py -42
# minus Zweiundvierzig

python zahl_zu_wort.py 1.000
# Eintausend
```

## Features

- Zahlen von **-999 Milliarden bis +999 Milliarden**
- Negative Zahlen
- Tausendertrennzeichen (`.` oder `,`) werden automatisch ignoriert
- Keine externen Abhängigkeiten – nur Python 3

## Voraussetzungen

- Python 3.6+
