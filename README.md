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
