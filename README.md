# 🦷 SmartDent-Kids

## Despre Proiect 
**SmartDent Kids** este o platformă bazată pe Inteligență Artificială concepută pentru a sprijini stomatologii pediatri în diagnosticarea și evaluarea leziunilor odontale la copii. Proiectul utilizează radiografii panoramice (OPT) pentru a detecta automat afecțiuni precum cariile, obturațiile sau leziunile de furcație, oferind totodată predicții privind prognosticul dintelui. 

## Echipa
- Morar Luciana Denisa
- Marcu Roxana Vanesa

## Problema Abordată
Caria dentară la copii este o afecțiune frecventă, iar interpretarea radiografiilor panoramice poate fi subiectivă și consumatoare de timp. Proiectul își propune să ofere un sistem automat de suport decizional care să reducă timpul de analiză și să crească acuratețea diagnosticului.


` SmartDent Kids` 


## Datele Utilizate
Pentru antrenarea și testarea modelelor, se utilizează dataset-ul public [Dataset for Automating Dental Condition Detection on Panoramic Radiographs](https://zenodo.org/records/15487430) (disponibil pe Zenodo).
- **Conținut:** 1.628 radiografii panoramice cu adnotări în format YOLO pentru 14 clase dentare.
- **Limitare cunoscută:** Dataset-ul curent conține imagini de la pacienți adulți. Pentru scopul proiectului (copii), se va aplica strategia de Transfer Learning.

## Tehnologii Utilizate
- **Python 3.10+**
- **Streamlit** (interfața web)
- **Pandas** (procesarea tabelelor de date)
- **Pillow** (procesarea imaginilor)

## Cum se rulează aplicația local

1. Clonează repository-ul

2. Creează și activează un mediu virtual:
  ` python -m venv .venv
   .venv\Scripts\Activate.ps1`

3. Instalează dependențele
` pip install streamlit pandas pillow`

4. Rulează aplicația
` streamlit run software-solution/app.py`
