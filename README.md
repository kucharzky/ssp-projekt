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

## Literatura

1. REFLO: Reactive Firewall System with OpenFlow and Flow Monitoring System

Artykuł przedstawia system monitorowania przepływów sieciowych w SDN, który wykorzystuje kontroler Floodlight i protokół OpenFlow do analizowania ruchu oraz kierowania wybranych pakietów do firewalla Snort. W kontekście naszego projektu najważniejsza jest możliwość monitorowania adresów IP źródłowych i docelowych oraz dynamicznego kierowania podejrzanego ruchu do analizy przez firewall, co może posłużyć jako podstawa wykrywania IP Spoofing.

V. Visoottiviseth, S. Lertviriyasawat, P. Suppiyatrakoon, P. Chitkornkitsil and N. Yamai, "REFLO: Reactive firewall system with OpenFlow and flow monitoring system," TENCON 2017 - 2017 IEEE Region 10 Conference, Penang, Malaysia, 2017, pp. 2273-2278, doi: 10.1109/TENCON.2017.8228240. keywords: {Firewalls (computing);Control systems;Monitoring;Ports (Computers);Databases;Payloads;Software-Defined Network;Openflow;Firewall;Network Monitoring},


2. Attacking Network Isolation in Software-Defined Networks: New Attacks and Countermeasures
   
Artykuł przedstawia mechanizm SpoofDefender, który wykrywa i blokuje próby podszywania się pod inne urządzenia w sieci SDN poprzez weryfikację zgodności adresów IP, MAC oraz portu przełącznika przypisanego do danego użytkownika. W kontekście naszego projektu szczególnie istotne jest sprawdzanie, czy źródłowy adres IP pakietu odpowiada wcześniej zarejestrowanemu urządzeniu, co pozwala wykrywać i blokować pakiety zawierające sfałszowane adresy IP.

R. Xiao, H. Zhu, C. Song, X. Liu, J. Dong and H. Li, "Attacking Network Isolation in Software-Defined Networks: New Attacks and Countermeasures," 2018 27th International Conference on Computer Communication and Networks (ICCCN), Hangzhou, China, 2018, pp. 1-9, doi: 10.1109/ICCCN.2018.8487340. keywords: {IP networks;Control systems;Protocols;Cloud computing;Data centers;Monitoring;Security},

## Topologia

Scenariusz badawczy zostanie zweryfikowany z użyciem topologii Spine-Leaf, która została wybrana ze względu na swoją powszechność w nowoczesnych centrach danych oraz sieciach korporacyjnych. Próby ataków IP spoofing będą przeprowadzane z przejętego hosta końcowego (h1), natomiast weryfikacja i filtrowanie ruchu będą realizowane na brzegowym przełączniku warstwy dostępowej (Leaf) za pośrednictwem kontrolera SDN.

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
