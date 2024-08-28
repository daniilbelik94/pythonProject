# Eingabe des Stundenlohns und Umwandlung in einen Float-Wert
stundenlohn = float(input("Bitte Stundenlohn eingeben: €"))

# Definieren von Konstanten
stundenProTag = 8
arbeitstageProMonat = 23
monateProJahr = 12
urlaubstage = 30

# Zusätzliche Vergütung
zuschlagUeberstunden = 0.25  # +25% für Überstunden
zuschlagSamstag = 0.50  # +50% für Samstag
zuschlagSonntag = 1.00  # +100% für Sonntag
zuschlagUrlaub = 0.50  # +50% für Urlaub

# Eingabe der Anzahl der Überstunden und Wochenendtage
ueberstunden = float(input("Wie viele Überstunden (über 8 Stunden pro Tag) machen Sie im Monat? "))
samstage = int(input("An wie vielen Samstagen im Monat arbeiten Sie? "))
sonntage = int(input("An wie vielen Sonntagen im Monat arbeiten Sie? "))

# Berechnungen
monatslohn = stundenlohn * stundenProTag * arbeitstageProMonat
ueberstundenLohn = ueberstunden * stundenlohn * (1 + zuschlagUeberstunden)
samstagsLohn = samstage * stundenProTag * stundenlohn * (1 + zuschlagSamstag)
sonntagsLohn = sonntage * stundenProTag * stundenlohn * (1 + zuschlagSonntag)
urlaubLohn = urlaubstage * stundenProTag * stundenlohn * (1 + zuschlagUrlaub)

jahreslohn = (monatslohn * monateProJahr) + ueberstundenLohn + samstagsLohn + sonntagsLohn
jahreslohnInklUrlaub = jahreslohn + urlaubLohn

# Ausgabe der Ergebnisse
print("\n--- Gehaltsübersicht ---")
print(f"Stundenlohn: €{stundenlohn:.2f}")
print(f"Monatlicher Lohn ohne Zuschläge: €{monatslohn:.2f}")
print(f"Lohn für Überstunden: €{ueberstundenLohn:.2f}")
print(f"Lohn für Samstage: €{samstagsLohn:.2f}")
print(f"Lohn für Sonntage: €{sonntagsLohn:.2f}")
print(f"Jahreslohn ohne Urlaub: €{jahreslohn:.2f}")
print(f"Jahreslohn inkl. Urlaub: €{jahreslohnInklUrlaub:.2f}")

# Optionale Gehaltserhöhung
antwort = input("\nMöchten Sie eine Gehaltserhöhung simulieren? (ja/nein): ").strip().lower()

if antwort == "ja":
    erhoehungProzent = float(input("Geben Sie den Prozentsatz der Erhöhung ein: "))
    neuerStundenlohn = stundenlohn * (1 + erhoehungProzent / 100)
    neuerMonatslohn = neuerStundenlohn * stundenProTag * arbeitstageProMonat
    neuerUeberstundenLohn = ueberstunden * neuerStundenlohn * (1 + zuschlagUeberstunden)
    neuerSamstagsLohn = samstage * stundenProTag * neuerStundenlohn * (1 + zuschlagSamstag)
    neuerSonntagsLohn = sonntage * stundenProTag * neuerStundenlohn * (1 + zuschlagSonntag)
    neuerUrlaubLohn = urlaubstage * stundenProTag * neuerStundenlohn * (1 + zuschlagUrlaub)

    neuerJahreslohn = (neuerMonatslohn * monateProJahr) + neuerUeberstundenLohn + neuerSamstagsLohn + neuerSonntagsLohn
    neuerJahreslohnInklUrlaub = neuerJahreslohn + neuerUrlaubLohn

    print("\n--- Gehaltsübersicht nach Erhöhung ---")
    print(f"Neuer Stundenlohn: €{neuerStundenlohn:.2f}")
    print(f"Neuer monatlicher Lohn ohne Zuschläge: €{neuerMonatslohn:.2f}")
    print(f"Neuer Lohn für Überstunden: €{neuerUeberstundenLohn:.2f}")
    print(f"Neuer Lohn für Samstage: €{neuerSamstagsLohn:.2f}")
    print(f"Neuer Lohn für Sonntage: €{neuerSonntagsLohn:.2f}")
    print(f"Neuer Jahreslohn ohne Urlaub: €{neuerJahreslohn:.2f}")
    print(f"Neuer Jahreslohn inkl. Urlaub: €{neuerJahreslohnInklUrlaub:.2f}")
else:
    print("Keine Gehaltserhöhung vorgenommen.")
