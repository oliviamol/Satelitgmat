

# 🛰️ Misiune GMAT

Acest proiect reprezintă o simulare orbitală care transformă date complexe de inginerie aerospațială într-o experiență vizuală 3D interactivă.

## Conceptul Proiectului
Misiunea a fost configurată în **NASA GMAT** (General Mission Analysis Tool) pentru a simula traiectoria unui satelit pe o durată de **2 ore**. 

**Punctul forte:** Parametrii orbitali au fost ajustați special pentru ca, în acest interval, satelitul să efectueze o trecere peste regiunea **României**, oferind o perspectivă simulată de monitorizare teritorială.

## 🛠️ Cum a fost construit?
1. **Simulare GMAT:** Am generat toate traseele (stările de ephemeris) într-un fișier `.e`, calculând poziția și viteza satelitului la fiecare pas temporal.
2. **Motor de Conversie Python:** Un script personalizat care transformă coordonatele brute în format **CZML**, pregătindu-le pentru web.
3. **Vizualizare 3D:** Datele sunt redate pe globul virtual **CesiumJS**, utilizând un algoritm de interpolare pentru a vedea satelitul „alunecând” lin pe orbită.

## 🚀 Demo în Cesium Sandcastle
Dacă vrei să vezi magia în acțiune fără să instalezi nimic:
1. Copiază codul din `sandcastle_code.js`.
2. Mergi pe [Cesium Sandcastle](https://sandcastle.cesium.com/).
3. Șterge tot și dă-i **Paste**.

Vei vedea satelitul trecând peste Glob atingând și România într-un mediu 3D spectaculos, cu hărți de înaltă rezoluție. Este modul perfect de a vedea cum datele matematice se transformă în realitate vizuală.

## 🎥 Vizualizare Video
  Se poate vedea în video-ul atașat acestui repository
---
*Proiect realizat cu pasiune pentru spațiu și cod*





