# Reaktywny system zapory sieciowej

> Reaktywny system zapory sieciowej oparty na silniku Snort (tbd narzędzie). Projekt realizowany w ramach zajęć Sieci Sterownych Programowo na uczelni AGH

---

## O projekcie

Projekt implementujący reaktywny mechanizm obrony sieciowej. Narzędzie łączy możliwości inspekcji ruchu w czasie rzeczywistym oferowane przez Snort z mechanizmami aktywnej odpowiedzi (**Active Response**) oraz dynamiczną integracją z regułami zapory sieciowej (np. `nftables`/`iptables`).

### Główne założenia i funkcjonalności:
* **Analiza ruchu w czasie rzeczywistym:** Wykrywanie nieautoryzowanych prób dostępu, skanowania portów oraz znanych sygnatur ataków.
* **Aktywne zerwanie sesji:** Wykorzystanie techniki obronnego podszywania się pod adres IP celu (IP Spoofing) do natychmiastowego zrywania złośliwych połączeń TCP lub wysyłania odpowiedzi ICMP.
* **Dynamiczne blokowanie:** Automatyczna reakcja na incydenty i tymczasowe izolowanie adresów IP atakujących na poziomie firewalla
* (TPD czy do zrobienia) **Rejestrowanie zdarzeń:** Centralne logowanie alertów w formacie ułatwiającym analizę powłamaniową.

---

## Zespół projektowy

| Imię i nazwisko | GitHub |
| :--- | :--- |
| **Maciej Kucharski** | [@kucharzky](https://github.com/kucharzky) |
| **Adrian Homa** | [@AH-repo](https://github.com/AH-repo) |
| **Michał Górka** | [@migorka](https://github.com/migorka) |
| **Mateusz Kosek** | [@Mateusz-AGH](https://github.com/Mateusz-AGH) |
| **Mikołaj Zielniok** | [@w1nn3t0u-o7](https://github.com/w1nn3t0u-o7) |

---

## Szybki start

### Wymagania wstępne
* System operacyjny: 
* Zainstalowane pakiety: `snort`, `iptables` / `nftables`, `libpcap`

### Uruchomienie (przykład)
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/kucharzky/ssp-projekt.git
   ```

2. Kolejne etapy będą dodane podczas realizacji projektu

---

## Licencja

Projekt udostępniany na licencji MIT. Szczegóły w pliku [LICENSE](LICENSE).
