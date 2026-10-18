# Raport Tehnic - Etapa 1
## SmartDent Kids: Platformă AI pentru Analiza Radiografiilor Panoramice Pediatrice

**Echipa MIRPR:**
- Morar Luciana Denisa
- Marcu Roxana Vanesa

---

### 1. Introducere
Prezentul raport descrie stadiul actual al proiectului **SmartDent Kids**, dezvoltat în cadrul disciplinei MIRPR. Scopul final este dezvoltarea unei platforme bazate pe Inteligență Artificială (AI) capabilă să detecteze și să caracterizeze leziunile odontale la copii, folosind radiografii panoramice (OPT).

În această primă etapă, ne-am concentrat pe realizarea unui prototip funcțional (Proof of Concept) care să demonstreze fluxul de lucru al aplicației. Întrucât modelul AI nu este încă antrenat, rezultatele analizei sunt simulate (hard-codate), urmând a fi înlocuite cu predicțiile reale în etapele ulterioare.

### 2. Descrierea Problemei Rezolvate cu Ajutorul AI

#### 2.1. Descrierea Plastică (Context și Importanță)
Caria dentară și complicațiile acesteia reprezintă una dintre cele mai frecvente afecțiuni în rândul copiilor. Evaluarea severității leziunilor și alegerea tratamentului optim (conservator vs. extracție) depind de interpretarea corectă a investigațiilor radiologice. Interpretarea manuală a radiografiilor panoramice la copii este dificilă din cauza suprapunerilor, a anatomiei specifice dinților temporari și a variabilității inter-observator.

Proiectul își propune să ofere un sistem automat de suport decizional pentru **stomatologii pediatri și radiologii dentari**, reducând timpul de analiză și oferind o evaluare obiectivă a riscului de afectare pulpară și a prognosticului dintelui.

#### 2.2. Descrierea Formală (Date de Intrare, Ieșire și Metrici)
- **Date de intrare (Input):** O radiografie panoramică (matrice de pixeli). Opțional, pot fi incluși parametri clinici (ex: vârsta pacientului).
- **Date de ieșire (Output):**
  - *Detecție:* Coordonate spațiale (bounding boxes), clasa leziunii (ex: CAR - carie, OBT - obturație, FUR - implicare furcație), profunzime (smalț, dentină superficială, dentină profundă) și gradul de distrucție coronară.
  - *Predicție:* Probabilitatea de afectare pulpară (0-100%) și rata de supraviețuire a dintelui (tratament conservator vs. extracție).
- **Metrici de performanță:**
  - *Detecție:* mAP (mean Average Precision), IoU (Intersection over Union), Precision, Recall.
  - *Predicție:* AUC-ROC, Acuratețe, F1-Score.

### 3. Related Work & Tools
Pentru fundamentarea teoretică, au fost analizate următoarele lucrări relevante:
- **Mutlu et al. (2026):** Utilizează YOLOv11 și YOLOv12 pe 2.297 radiografii. Modelul YOLOv11 a obținut un mAP@0.5 de 0.857. Tehnologii: Ultralytics, PyTorch.
- **Mahizha et al. (2026) (SwinDent-Seg):** Propune o arhitectură hibridă Swin Transformer-CNN pe 1.018 radiografii, obținând un mAP50 de 0.8947. Tehnologii: PyTorch.
- **Zhou et al. (2023):** Folosește un Swin Transformer îmbunătățit cu informații despre tipul dintelui pe 6.028 dinți ai **copiilor**. A obținut o acuratețe de 0.8557, depășind medicii rezidenți.
- **Mureșanu et al. (2024):** Lucrarea aferentă dataset-ului de pe Zenodo (1.628 radiografii, format YOLO). Oferă adnotări realizate cu *MakeSense.ai* (ICC de 0.91).

### 4. Arhitectura și Funcționalitățile Aplicației
#### 4.1. Fluxul de Bază
Aplicația demonstrează următorul flux de lucru:
1. **Încărcarea fișierului:** Utilizatorul selectează o radiografie (fișier imagine).
2. **Vizualizarea:** Imaginea este afișată în interfață.
3. **Declanșarea analizei:** Un buton simulează trimiterea imaginii către modulul AI.
4. **Afișarea rezultatelor simulate:** Sunt afișate date hard-codate sub formă de tabel (detecții) și indicatori grafici (predicții), demonstrând cum va arăta interfața finală.

#### 4.2. Tehnologii Utilizate și Justificarea Alegerii
Aplicația este dezvoltată în Python, folosind:
- **Streamlit:** Pentru viteza de dezvoltare a interfeței web (widget-uri de upload, layout pe coloane) fără a scrie cod HTML/CSS.
- **Pandas:** Pentru a structura rezultatele detecției sub formă de tabel (DataFrame), ușor de afișat și manipulat.
- **Pillow (PIL):** Pentru deschiderea și manipularea fișierelor de tip imagine înainte de a fi afișate.

### 5. Concluzii și Pași Următori
În această etapă, a fost pusă baza aplicației software și s-a demonstrat fluxul funcțional al platformei. Deși rezultatele sunt momentan simulate, structura este pregătită pentru integrarea unui model de deep learning.
În Etapa 2, ne propunem explorarea vizuală a datelor (EDA) și antrenarea unui model inițial (ex: YOLOv8n) pe un subset mic de imagini.