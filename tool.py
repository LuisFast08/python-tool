import time
import random
import requests
import os
import string

def clear_screen():
    if os.name == 'nt':
        os.system('cls')     
    else:                          
        os.system('clear')     

while True:                   

    clear_screen()           

    print("  _                  _           _       ")
    print(" | |                | |         | |      ")
    print(" | |    _   _  _ __ | |_   __ _ | |_ ___ ")
    print(" | |   | | | || '__|| __| / _ || __/ _ \\")       # Von ChatGPT generiert soll ein cooles design sein.
    print(" | |___| |_| || |   | |_ | (_| || ||  __/")
    print(" |____|\\__,_||_|    \\__| \\__,_| \\__\\___|")
    print("                                         ")
    print("             L U I S   T O O L           ")

    print("")
    print("Wähle ein Tool!")
    print("")

    print("📦 (1) - Barcode überprüfer.")
    print("⏱️ (2) - Timer.")
    print("🔢 (3) - Primzahl Tester.")
    print("➕ (4) - Alle zahlen bis zu deiner Addieren.")
    print("🔍 (5) - Alle Teiler einer Zahl.")
    print("🎯 (6) - Zahlen Raten Spiel.")
    print("🌦️ (7) - Wetter Abfragen einer PLZ.")
    print("⚖️ (8) - BMI Rechner.")
    print("🌐 (9) - IP Checker")
    print("📝(10) - To-Dos")
    print("🔐(11) - Passwort generator.")
    print("👋(99) - Programm beenden.")
    print("")
    try:
        option = int(input("Welches Tool möchtest du benutzen? "))
    except ValueError:
        print(f"Bitte gib nur Zahlen ein!\n")
        input("Drücke Enter ...")
        continue

    if option == 1:
        print("Willkommen zum Barcode überprüfer.")
        print("")
        barcode = input("Gebe eine 13-stellige EAN Nr. an: ")
        print("")

        if len(barcode) == 13 and barcode.isdigit():
            ungerade_summe = 0
            gerade_summe = 0

            for i, c in enumerate(barcode[:-1]):
                if i % 2 == 0:
                    ungerade_summe += int(c)
                else:
                    gerade_summe += int(c) * 3

            gesammt_summe = ungerade_summe + gerade_summe
            prüfziffer = (10 - (gesammt_summe % 10)) % 10

            eingegebene_prüfziffer = int(barcode[-1])

            if prüfziffer == eingegebene_prüfziffer:
                print("")
                print("Der eingegebene Barcode ist gültig!")
                print("")
            else:
                print("")
                print("Der eingegebene Barcode ist leider ungültig!")
                print("")
        else:
            print("")
            print("Die EAN-Nummer ist nicht gültig. Stelle bitte sicher, dass sie 13 Ziffern hat.")
            print("")

        input("Drücke Enter ...")

    elif option == 2:
        print("Willkommen zum Timer.")
        print("")
        try:
            zeit = int(input("Wie lange soll der Timer in Sekunden gehen? "))
        except ValueError:
            print("Bitte gib nur Zahlen ein.")
            input("Drücke Enter ...")
            continue
        print("")
        for i in range(zeit, 0, -1):
            print(f"Noch {i} Sekunden ...")
            time.sleep(1)
        print("")
        print(f"Die Zeit von {zeit} Sekunde(n) ist abgelaufen!\n")
        print("")

        input("Drücke Enter ...")

    elif option == 3:
        print("Willkommen zum Primzahl tester.")
        print("")
        try:
            zahl = int(input("Welche Zahl möchtest du überprüfen? "))
        except ValueError:
            print("Bitte gib nur Zahlen ein.")
            input("Drücke Enter ...")
            continue
        if zahl < 2:
            print("")
            print(f"{zahl} ist keine Primzahl.")
            print("")
        else:
            for i in range(2, zahl):
                if zahl % i == 0:
                    print("")
                    print(f"{zahl} ist keine Primzahl.")
                    print("")
                    break
            else:
                print("")
                print(f"{zahl} ist eine Primzahl.")
                print("")

        input("Drücke Enter ...")

    elif option == 4:
        while True:
            print("Willkommen zum Adierer.")
            print("")
            try:
                zahl = int(input("Wähle eine gerade Zahl bis zu der alles addiert wird: "))
            except ValueError:
                print("Bitte gib nur Zahlen ein.")
                input("Drücke Enter ...")
                continue

            if zahl % 2 == 0:
                summe = sum(range(0, zahl + 1))
                print("")
                print(f"Alle Zahlen bis {zahl} addiert ergibt: {summe}")
                print("")
                break
            else:
                print("")
                print("Bitte nenne eine gerade Zahl.")
                print("")

        input("Drücke Enter ...")

    elif option == 5:
        print("Willkommen zum, Teiler einsehen tool.")
        print("")
        try:
            zahl = int(input("Von welcher Zahl möchtest du die Teiler einsehen? "))
        except ValueError:
            print("Bitte gib nur Zahlen ein.")
            input("Drücke Enter ...")
            continue
        print("\nDie Teiler sind:")
        for i in range(1, zahl + 1):
            if zahl % i == 0:
                print(i)
        print("")

        input("Drücke Enter ...")

    elif option == 6:
        def generate_number():
            return random.randint(1, 100)

        zahl = generate_number()
        versuche = 0

        print("Willkommen zum Zahlen Spiel.")
        print("")

        while True:
            try:
                gues = int(input("Welche Zahl von 1 - 100 könnte ich mir ausgedacht haben? "))
            except ValueError:
                print("Bitte gib nur Zahlen ein.")
                input("Drücke Enter ...")
                continue
            versuche += 1

            if gues == zahl:
                print("")
                print(f"Du hast die Zahl erraten.\nDu hast {versuche} Versuche gebraucht. Die ausgedachte Zahl war: {zahl}")
                print("")
                break
            elif gues > zahl:
                print("")
                print("Die Zahl ist kleiner!")
                print("")
            else:
                print("")
                print("Die Zahl ist größer!")
                print("")

        input("Drücke Enter ...")

    elif option == 7:
        api_key = "113622db9c00d5fabdf8f525f5ca143a"

        print("Willkommen Bei der Wetter App")
        print("")

        def get_weather_by_zip(zip_code):
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},de&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                main = data['main']
                weather = data['weather'][0]
                temperature = main['temp']
                humidity = main['humidity']
                weather_description = weather['description']

                print("")
                print(f"Wetter für PLZ {zip_code}:")
                print(f"Temperatur: {temperature}°C")
                print(f"Luftfeuchtigkeit: {humidity}%")
                print(f"Beschreibung: {weather_description.capitalize()}")
                print("")

            else: 
                print("")
                print("Fehler, überprüfe die PLZ oder versuche es später erneut!")
                print("")

        zip_code = input("Gib eine PLZ ein, von der das wetter überprüft werden soll: ")
        print("")

        get_weather_by_zip(zip_code)

        input("Drücke Enter ...")

    elif option == 8:
        print("Willkommen bei dem BMI Rechner")
        print("")

        try:
            gewicht = int(input("Wieviel kg wiegst du? "))
            größe = float(input("Wie groß bist du in Metern? "))
        except ValueError:
            print("Bitte gib nur Zahlen ein.")
            input("Drücke Enter ...")
            continue

        bmi = gewicht / (größe ** 2)

        if bmi < 18.5:
            status = "Untergewicht"
        elif bmi < 25:
            status = "Normalgewicht"
        elif bmi < 30:
            status = "Übergewicht"
        else:
            status = "Adipositas"

        print("")
        print(f"Dein BMI beträgt: {bmi:.2f}")
        print("")
        print(f" Du hast: {status}")
        print("")


        input("Drücke Enter ...")

    elif option == 9:
        print("")
        print("Wilkommen zum IP checker.")
        print("")

        ip = input("Von welcher IP willst du öffentliche infos erhalten? ")
        print("")


        def get_ip_info(ip):
            api_key = "2ff23e262143cf" 
            api_url = f"https://ipinfo.io/{ip}/json?token={api_key}" 
            try:
                response = requests.get(api_url)
                response.raise_for_status()  
                data = response.json()
            
                print(f"Informationen für IP-Adresse: {ip}")
                print(f"IP: {data.get('ip')}")
                print(f"Stadt: {data.get('city')}")
                print(f"Region: {data.get('region')}")
                print(f"Land: {data.get('country')}")
                print(f"Organisation: {data.get('org')}")

            except requests.exceptions.RequestException as e:
                print("")
                print(f"Fehler beim Abrufen der IP-Informationen: {e}")
                print("")

        get_ip_info(ip)
        input("Enter Drücken ...")

    elif option == 10:
        ToDos = []
        print("Willkommen bei dem To-Do tool.")

        print("")
        print("")

        while True:
            print("")
            print("(1) - ToDo Hinzufügen")
            print("(2) - ToDos Anzeigen")
            print("(3) - ToDos schließen")
            print("")
            
            try:
                option = int(input("Was möchtest du Tuhen? "))
            except ValueError:
                print("Bitte gib nur Zahlen ein.")
                input("Drücke Enter ...")
                continue

            if option == 1:
                print("")
                todo = input("Welche To-Do steht an? ")
                ToDos.append(todo)
                print("")

            elif option == 2:
                print("Meine To-Dos:")
                print("")
                for liste in ToDos:
                    print(f"- {liste}")
                    print("")

            elif option == 3:
                print("")
                print("")
                print("Auf wieder sehen.")
                input("Enter Drücken ...")
                break

            else: 
                print("")
                print("Entscheide dich zwischen option 1 oder 2")
                print("")


    elif option == 11:
        print("Willkommen bei dem Passowort Generator.")
        print("")

        while True:

            print("Wähle eine der folgenden optionen.")
            print("")
            print("(1) - Passwort generieren.")
            print("(2) - Programm schließen.")
            print("")

            try:
                option = int(input("Was möchtest du tun? "))
            except ValueError:
                print("Bitte gebe nur Zahlen ein!")
                input("Enter drücken ...")
                continue

            if option == 1:
                print("")
                try:
                    zeichen = int(input("Wie viele Zeichen soll dein Passwort enthalten?"))
                except ValueError:
                    print("Bitte gebe nur Zahlen ein!")
                    input("Enter drücken ...")
                    continue

                zeichenliste = string.ascii_letters + string.digits + string.punctuation # Gibt an welche zeichen im Passwort generiert werden.
                passwort = ''.join(random.choice(zeichenliste) for _ in range(zeichen))  # Generiert das Passwort mit der länge wie oben angegeben.

                print("")
                print(f"Dein generiertes Passwort lautet: {passwort}")
                print("")
                input("Enter um ins Menü zurück zu kommen ...")
                

            elif option == 2:
                print("")
                print("Auf Wiedersehen.")
                input("Enter drücken ...")
                break

            else:
                print("")
                print("Wähle eine gültige option.")
                print("")


    elif option == 99:
        print("")
        print("")
        print("Auf Wiedersehen!")
        input("Enter zum Schließen ...")
        break

    else:
        print("")
        print("Ungültige Option! Bitte wähle eine der genannten Optionen.")
        print("")