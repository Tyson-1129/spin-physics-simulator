# Spin Physics Simulator

## Overview
The Spin Physics Simulator is a machine learning and physics modeling project that simulates the angular momentum and velocity decay of a spinning top. It utilizes physics-based differential equations to generate synthetic spin data and applies a Random Forest Regressor to predict the precise stop times of the spinning object.

## Features
* **Physics Modeling:** Derives and calculates angular momentum and velocity decay over time.
* **Data Visualization:** Plots decay curves and spin behavior for clear physical analysis.
* **Machine Learning Integration:** Trains a predictive model to forecast total spin duration based on initial conditions.
* **Synthetic Data Generation:** Generates comprehensive datasets for model training and validation.

## Technologies Used
* **Python**
* **NumPy:** Numerical computations
* **SymPy:** Symbolic mathematics and differential equations
* **Matplotlib:** Data visualization and decay curves
* **Scikit-learn:** Random Forest Regressor for stop-time prediction
* **Jupyter Notebook:** Interactive environment for execution

## Repository Structure
* `simulator.ipynb`[cite: 5]: The primary Jupyter Notebook containing the simulation logic, mathematical derivations, data generation, and machine learning pipeline.

## Getting Started
1. Clone this repository to your local machine:
   `git clone https://github.com/Tyson-1129/spin-physics-simulator.git`
2. Install the required Python dependencies:
   `pip install numpy sympy matplotlib scikit-learn`
3. Launch Jupyter Notebook and open `simulator.ipynb`[cite: 5] to run the cells, view the plotted decay curves, and test the prediction model.
