# Estimarea probabilitatii pentru diferite maini de poker folosind metoda Monte Carlo

#### Obiectivul este estimarea probabilitatilor pentru cateva maini de poker (pereche,doua perechi, trei de un fel, chinta, culoare, patru la fel) dintr-un pachet de carti standard.

#### Calculam probabilitațile pentru fiecare tip de mana pe baza raportului: numar rezultate favorabile/numar total rezultate.

#### Prin simularea a 100.000 de maini obtinem o aproximare apropiata de valorile probabilistice.

- **Pereche**: Doua carti de aceeasi valoare .
- **Doua perechi**: Doua seturi de cate doua carti de aceeasi valoare .
- **Trei de un fel**: Trei carti de aceeasi valoare .
- **Chinta (straight)**: Cinci carti consecutive ca valoare, indiferent de suita (ex: 5, 6, 7, 8, 9).
- **Culoare (flush)**: Cinci carti de aceeasi suita, indiferent de valoare (ex: cinci carti de trefla).
- **Patru de un fel**: Patru carti de aceeasi valoare .

