# Algorit-m-renditjeje-p-r-materiale-akademike-me-PageRank-relevanc-dhe-freski
# Motor i Renditjes për Materiale Akademike (Academic Ranking Engine)

## Qëllimi Shkencor
Ky projekt synon ndërtimin e një motori kërkimi të thjeshtëzuar për një koleksion materialesh akademike. Përtej modelit klasik PageRank, i cili bazohet vetëm në lidhjet midis dokumenteve, ky motor integron një qasje hibride që merr parasysh relevancën tekstuale, freskinë, cilësinë dhe penalizimin e përmbajtjes.

## Modeli Matematikor
Renditja përfundimtare e çdo dokumenti $i$ llogaritet përmes formulës së peshuar:

$$S_{i} = w_{P}P_{i} + w_{R}R_{i} + w_{F}F_{i} + w_{Q}Q_{i} - w_{Sp}Sp_{i}$$

Ku komponentët përfaqësojnë:
* **$P_{i}$**: PageRank (lidhjet midis dokumenteve).
* **$R_{i}$**: Relevanca ndaj pyetjes (TF-IDF e thjeshtuar).
* **$F_{i}$**: Freskia e dokumentit.
* **$Q_{i}$**: Cilësia e materialit.
* **$Sp_{i}$**: Penalizimi për përmbajtje të dobët ose të përsëritur.

## Struktura e Projektit
Repozitori është i organizuar sipas hierarkisë së këshilluar:
* `examples/materials.json`: Dataset-i me të paktën 20 dokumente akademike.
* `src/ranking/`: Modulet për PageRank, llogaritjen e tipareve dhe motorin kryesor.
* `src/visualization/`: Skripte për vizualizimin e grafit dhe rezultateve.
* `scripts/`: Skripte për ekzekutimin e pyetjeve dhe skanimin e peshave.

## Instalimi dhe Përdorimi
1. Instaloni bibliotekat e nevojshme (si `networkx`, `numpy`, `matplotlib`):
   ```bash
   pip install -r requirements.txt
## 🛠️ Moduli i Oshilatorit me Amortizim dhe Rezistencë (Kejsi)

Ky modul fut në lojë konceptet e fërkimit dhe forcave komplekse (si rezistenca e ajrit), duke i përafruar ekuacionet teorike me sistemet fizike reale. Fokusimi kryesor ka qenë modelimi i amortizimit (*damping*) dhe ndikimi i tij në sistem.

### 👥 Bashkëpunimi dhe Ndarja e Kontributeve

* **Ndihma për Azemin:** Kam ndihmuar Azemin që të zgjerojë projektin e tij ideal përmes futjes së konceptit të fërkimit. Kjo i dha mundësi atij të krijonte një variant të dytë të modelit ku krahasohet sjellja pa fërkim me atë në kushte reale.
* **Ndihma për Vjorisën:** Pasi kam studiuar sjelljen e forcave të fërkimit, kam asistuar Vjorisën në përcaktimin dhe kuptimin e parametrit kritik të amortizimit $\delta$. Ky parametër është thelbësor në modelin Duffing për të parandaluar daljen e sistemit jashtë kontrollit dhe për të mundësuar shfaqjen e strukturave në Seksionet Poincaré.
* **Asistenca e pranuar:** Azemi më ka ndihmuar në rishikimin e ekuacioneve të mia dhe në verifikimin e algoritmeve të integrimit numerik (Euler) në rastet kur fërkimi është zero. Vjorisa ka udhëhequr pjesën e vizualizimit, duke më mësuar se si të interpretoj "Portretin Fazor" kur trajektorja formon një spirale që mblidhet te pika e ekuilibrit fiks.

---

### 💻 Implementimi në Kod

Më poshtë ndodhet skripti në **Python** që integron numerikisht ekuacionet e lëvizjes duke përdorur **Metodën Euler**, duke shfaqur rënien e amplitudës dhe portretin fazor në formë spirale.

#### Parakushtet
```bash
pip install numpy matplotlib
