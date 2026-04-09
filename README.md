# 🚗 SI Engine PV Diagram Simulation

A Python-based simulation of the Pressure–Volume (PV) diagram for a Spark Ignition (SI) Engine using the **Otto Cycle**.
This project helps visualize thermodynamic processes like compression, heat addition, expansion, and heat rejection.

---

## 📊 Output

![PV Diagram](images/pv_diagram.png)

---

## ⚙️ Features

* 📉 **Isentropic Compression (1 → 2)**
* 🔥 **Constant Volume Heat Addition (2 → 3)**
* 📈 **Isentropic Expansion (3 → 4)**
* ❄️ **Constant Volume Heat Rejection (4 → 1)**
* 🔧 Adjustable parameters:

  * Compression Ratio
  * Initial Pressure
  * Initial Volume
* 📊 Clean and labeled PV diagram using Matplotlib

---

## 🛠️ Tech Stack

* **Python**
* **NumPy**
* **Matplotlib**

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/shreechaturvedi/si-engine-pv-diagram-simulation.git
cd si-engine-pv-diagram-simulation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Simulation

```bash
python pv_simulation.py
```

---

## 📁 Project Structure

```
si-engine-pv-diagram-simulation/
│── pv_simulation.py      # Main simulation script
│── animation.py          # (Optional) animation logic
│── README.md             # Project documentation
│── requirements.txt      # Dependencies
└── images/
    └── pv_diagram.png    # Output graph
```

---

## ⚡ Key Concepts Used

* Otto Cycle Thermodynamics
* Isentropic Processes (PV^γ = constant)
* Heat Addition & Rejection
* Data Visualization using Matplotlib

---

## 📌 Future Improvements

* 🎞️ Add animated PV cycle (piston motion)
* 🖥️ Build GUI using PyQt
* 📊 Add efficiency & work calculations
* 🌐 Deploy as a web app

---

## 🤝 Contribution

Feel free to fork this repo and improve it. Suggestions and contributions are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Author

Developed by **Shreechaturvedi**
Mechanical Engineering + Coding Project 🚀

      
