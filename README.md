## Geofencing-using-IoT
<p align="justify">
We've developed a wearable consumer electronic band designed to geofence Covid-19 patients, with the primary goals of reducing exposure risks, enabling continuous monitoring, and enhancing staff allocation efficiency within hospitals and quarantine centers. Our approach involves harnessing signals from a minimum of three nearby WiFi routers/Beacons. Based on the strength of these signals, as measured by RSSI values, our RandomForestClassifier model classifies whether individuals are within designated boundaries. The Linear Regressor further refines this by identifying precise coordinates on the area's map. Should the band be tampered with or if the geofence is breached, real-time notifications are promptly dispatched to the hospital staff.
</p>
<p align="center">
  <img src="https://github.com/arya18mak/Geofencing-using-IoT/assets/55435847/5b2b8a0f-f5ae-4bbf-a3af-40238a116c89" alt="Image Alt Text"><br>
  <b>Fig1: Framework</b>
</p>

## User Interface
<p align="center">
  <img src="https://github.com/arya18mak/Geofencing-using-IoT/assets/55435847/6affca8f-6413-4c51-a989-30857808745c" alt="Image Alt Text"><br>
  <b>Fig2: Position & geofence </b>
</p> 
<p align="justify">This band was tested in a 18 by 10 sqft room were the blue area demonstrates the safe region whereas being in white region indicates the person/entity has crossed the boundary.</p>


