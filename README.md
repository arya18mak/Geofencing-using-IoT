# 📡 Geofencing Using IoT

🏆 **Semi-Finalist — Deep Blue by Mastek (2020–21)**
Selected from ~600 abstracts submitted across India (spanning multiple problem statements). For our problem statement, 10 teams were chosen to compete — and we were one of only 3 to reach the semi-finals.

---

A wearable IoT wristband system for real-time indoor geofencing of COVID-19 patients in hospitals and quarantine centers. The system uses WiFi signal strength (RSSI) from nearby routers to classify and localize patients, triggering instant alerts to staff when a boundary is breached or the band is tampered with.

---

## 🧠 How It Works

Traditional GPS-based geofencing fails indoors. This system instead leverages **WiFi RSSI trilateration** — collecting signal strength readings from at least three nearby routers/beacons and running them through a two-stage ML pipeline:

1. **RandomForestClassifier** — determines whether the patient is inside or outside the designated safe zone.
2. **Linear Regressor** — estimates the patient's precise (x, y) coordinates on a floor map.

If the geofence is breached or the band is tampered with, **IFTTT webhooks** fire real-time notifications to hospital staff.

---

## 🖼️ System Architecture

<img src="https://github.com/arya18mak/Geofencing-using-IoT/assets/55435847/5b2b8a0f-f5ae-4bbf-a3af-40238a116c89" alt="Framework" width="800">

---

## 🖥️ User Interface

<img src="https://github.com/arya18mak/Geofencing-using-IoT/assets/55435847/6affca8f-6413-4c51-a989-30857808745c" alt="Position & Geofence">

The dashboard was tested in an **18 × 10 sq ft** room with **3 WiFi routers**:
- 🔵 **Blue area** — patient is within the safe zone
- ⬜ **White area** — boundary has been crossed

---

## 🗂️ Repository Structure

```
Geofencing-using-IoT/
├── app.py                    # Flask backend — receives RSSI data, runs inference, serves the UI
├── classifier                # Trained RandomForestClassifier (pickle)
├── x_cord                    # Trained Linear Regressor for X coordinate
├── y_cord                    # Trained Linear Regressor for Y coordinate
├── coordinatescapturexl.csv  # RSSI signal readings at labeled coordinates (training data)
├── chord.csv                 # Chord/boundary definition data
├── coo1.csv                  # Additional coordinate data
├── templates/                # HTML templates (Jinja2)
├── static/                   # CSS, JS, and image assets
├── style.css                 # Global styles
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku process declaration
└── .gitignore
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.7+
- Three WiFi routers/beacons deployed in your target area
- A PostgreSQL database (for storing readings — used via `psycopg2`)
- An [IFTTT](https://ifttt.com) account with a Webhooks applet for alerts

### 1. Clone the repository

```bash
git clone https://github.com/arya18mak/Geofencing-using-IoT.git
cd Geofencing-using-IoT
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Set the following environment variables before running the app:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `IFTTT_KEY` | Your IFTTT Webhooks API key |
| `IFTTT_EVENT` | Name of the IFTTT event to trigger on breach |

### 4. Run the Flask app locally

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🔧 Adapting to Your Own Space

The pre-trained models (`classifier`, `x_cord`, `y_cord`) were calibrated for an **18 × 10 sq ft** room with **3 specific routers**. To deploy in a different area:

1. **Collect RSSI training data** — walk through your space and record signal strengths from your routers at known coordinates. Save this to a CSV in the same format as `coordinatescapturexl.csv`.
2. **Retrain the models** — fit a new `RandomForestClassifier` for boundary detection and new `LinearRegressor` instances for X and Y coordinates.
3. **Replace the model files** — swap out `classifier`, `x_cord`, and `y_cord` with your newly trained versions.
4. **Update the floor map** — replace the map image in `static/` with a scaled image of your area.

---

## 🚀 Deployment (Heroku)

The app is Heroku-ready via the included `Procfile`.

```bash
heroku create your-app-name
heroku config:set DATABASE_URL=<your_db_url> IFTTT_KEY=<your_key> IFTTT_EVENT=<your_event>
git push heroku master
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask, Gunicorn |
| Machine Learning | scikit-learn (RandomForest, LinearRegression) |
| Data | pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Database | PostgreSQL (psycopg2) |
| Alerts | IFTTT Webhooks |
| Hosting | Heroku |

---

## 📌 Key Design Decisions

- **WiFi RSSI over GPS** — GPS is unreliable indoors; RSSI from existing infrastructure requires no additional hardware beyond the routers already present in a facility.
- **Two-stage ML** — The classifier gives a fast pass/fail boundary check, while the regressor provides finer location detail for the map display.
- **IFTTT for alerting** — Keeps the notification layer simple and configurable without building a custom messaging backend.

---

## 📄 License

This project does not currently specify a license. Please contact the repository owner before using or adapting this code in production.
