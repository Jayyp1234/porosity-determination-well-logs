# Porosity Determination from Well Logs

## 📖 Overview
This repository contains Python-based tools and scripts to calculate **porosity** from well log data. It is part of the **"Python for Oil and Gas"** series and focuses on simplifying the process of well log analysis for reservoir evaluation. The project aims to help students, researchers, and professionals in the oil and gas industry.

## 🚀 Key Features
- **Porosity Calculation Models**: Supports porosity estimation using the Density Log, Neutron Log, and Sonic Log.
- **Data Preprocessing**: Handles noisy and incomplete well log data for improved analysis.
- **Visualization Tools**: Provides intuitive plots for porosity trends and cross-plots for analysis.
- **Industry Relevance**: Tailored to meet the needs of reservoir engineers and geoscientists.

## 🧪 Example Use Cases
- Determining porosity for sand and shale formations.
- Visualizing porosity-depth relationships for reservoir characterization.
- Comparing multiple log-derived porosity estimates.

## 📑 Table of Contents
1. [Introduction](#introduction)
2. [Methodology](#methodology)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Requirements](#data-requirements)
6. [Features](#features)
7. [Contributing](#contributing)
8. [License](#license)

---

## 🔬 Methodology
This tool calculates porosity using the following well log models:
1. **Density Log (ρ)**:
   \[
   \phi = \frac{\rho_{\text{ma}} - \rho_{\text{b}}}{\rho_{\text{ma}} - \rho_{\text{f}}}
   \]
   Where:
   - \( \rho_{\text{ma}} \): Matrix Density
   - \( \rho_{\text{b}} \): Bulk Density from the log
   - \( \rho_{\text{f}} \): Fluid Density
   
2. **Neutron Log**:
   Direct measurement of porosity based on neutron scattering.

3. **Sonic Log**:
   \[
   \phi = \frac{\Delta t - \Delta t_{\text{ma}}}{\Delta t_{\text{f}} - \Delta t_{\text{ma}}}
   \]
   Where:
   - \( \Delta t \): Measured transit time
   - \( \Delta t_{\text{ma}} \): Matrix transit time
   - \( \Delta t_{\text{f}} \): Fluid transit time

---

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/porosity-determination-well-logs.git
   cd porosity-determination-well-logs
