# <img src="https://github.com/user-attachments/assets/766015ee-bc96-422c-8ca1-098d9d2f86c8" alt="InVision Logo" width="40"/> InVision - Machine Learning Regression Tool

Version: 1.0
Author: Kshitij K Sawant
---



## Overview

**InVision** is an intuitive machine learning regression tool designed to simplify the analysis and prediction of trends using CSV datasets. By integrating an interactive user interface, InVision empowers users to load data, select features, and perform regression analysis with minimal effort. This tool is particularly suited for financial and cryptocurrency market analysis but is flexible for a variety of domains.

---

## Features

- **Drag-and-Drop CSV Upload**: Easily load datasets for analysis.  
- **Column and Target Selection**: Dynamically select input features and target variables.  
- **Interactive UI**: User-friendly design for seamless data exploration and manipulation.  
- **Machine Learning Insights**: Leverages regression models to calculate metrics like Mean Squared Error (MSE) and R².  
- **Real-Time Results**: Display key regression metrics in an accessible format.  

---

## How It Works

1. **Upload Dataset**  
   Drag and drop your CSV file into the designated area of the application.

2. **Select Target and Features**  
   - View the column details from your CSV.
   - Highlight and select the column to be used as the target variable.  
   - Choose relevant features for the regression model.

3. **Run Regression Analysis**  
   - Click the "Run Regression" button.
   - View results including:
     - **MSE (Mean Squared Error):** A measure of prediction accuracy.
     - **R² Score:** An indication of the model's fit to the data.

4. **Analyze Results**  
   - Use the regression insights to interpret trends and correlations in your data.

---

## Requirements

- **Python 3.8+**  
- **Libraries**:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `tkinter`
  - `matplotlib`

---

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/username/InVision.git
   ```

2. Navigate to the project directory:  
   ```bash
   cd InVision
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:  
   ```bash
   python InVision.py
   ```

---

## Example Dataset

The sample CSV dataset (`BTC-2017min.csv`) provided includes historical Bitcoin prices, volumes, and other trading metrics. Example columns:
- **Date**: Timestamp of data collection.  
- **Open, High, Low, Close**: Cryptocurrency trading prices.  
- **Volume BTC, Volume USD**: Trading volumes in Bitcoin and USD.

This dataset is ideal for exploring regression on cryptocurrency market trends.

---

## Screenshots

### Application UI
<img width="1020" alt="InVision (Close X Open , Low , High)" src="https://github.com/user-attachments/assets/f8bf20f5-e424-4bc7-b6ea-d13210bfbdf5" />

### Application Logo
<img width="500" alt="InVision Logo" src="[https://github.com/user-attachments/assets/f8bf20f5-e424-4bc7-b6ea-d13210bfbdf5](https://github.com/user-attachments/assets/766015ee-bc96-422c-8ca1-098d9d2f86c8)" />




## Future Enhancements

- Incorporate support for classification models.  
- Add additional visualizations like scatter plots and line graphs.  
- Enable support for exporting results to a report or spreadsheet.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact

For inquiries or contributions, reach out to **Kshitij K Sawant** via [sawantkshitij1@gmail.com](mailto:email@example.com).  
