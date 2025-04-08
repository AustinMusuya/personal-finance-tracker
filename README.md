# 💰 Personal Finance Tracker CLI

This is a simple command-line tool, **Personal Finance Tracker** built using Python. It allows users to:

- Record income and expense transactions.
- View summaries within a selected date range.
- Visualize financial trends over time using line plots.

This app uses **CSV** for data storage and provides a basic command-line interface (CLI).

---

## 📦 Features

- ✅ Add new transactions (Income or Expense)
- ✅ View transactions within a date range
- ✅ Summary report showing:
  - Total Income
  - Total Expenses
  - Net Savings
- ✅ Line plot visualization of income and expense over time
- ✅ Stores data in a CSV file for easy access and portability

---

## 🛠️ Technologies Used

- **Python** (Standard Library)
- **Pandas** for data manipulation
- **Matplotlib** for visualization
- **CSV** module for file handling

---

## 📁 Project Structure

```
personal-finance-tracker/
│
├── main.py                # Main application file
├── data_entry.py          # User input validation functions
├── finance_data.csv       # CSV file to store transactions
└── README.md              # Project documentation
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AustinMusuya/personal-finance-tracker.git
cd personal-finance-tracker
```

### 2. Install Dependencies

All dependencies are standard Python libraries. However, make sure you have `pandas` and `matplotlib` installed:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

---

## 🧑‍💻 How to Use

### ➕ Add a Transaction

1. Choose option `1` in the menu.
2. Enter the date in `dd/mm/yyyy` format or press `Enter` for today's date.
3. Enter the amount (positive number).
4. Select the category: `I` for Income or `E` for Expense.
5. Enter an optional description.

### 📊 View Transactions and Summary

1. Choose option `2` in the menu.
2. Enter the start and end dates in `dd/mm/yyyy` format.
3. A table of filtered transactions and summary is shown.
4. Optionally, visualize income/expenses over time using a line chart.

### 📊 View Expense and Summary

1. Choose option `3` in the menu.
2. Enter the start and end dates in `dd/mm/yyyy` format.
3. A table of filtered transactions and summary is shown.
4. Optionally, visualize income/expenses over time using a pie chart.

### ❌ Exit

- Choose option `4` to exit the program.

---

## 📌 Example Transaction

```
Date: 06/04/2025
Amount: 5000
Category: I
Description: Freelance project
```

---

## 📈 Visualization Example

- Green Line: Income
- Red Line: Expenses
- X-axis: Date
- Y-axis: Amount

A helpful visual to monitor your spending/saving habits!

---

## 🧪 Future Improvements

- Category breakdown pie chart
- Monthly or weekly summaries
- Export to PDF
- GUI version using Tkinter or PyQt

---

## 👨‍💻 Author

**Austin Musuya**

---

## 📃 License

This project is licensed under the MIT License. You’re free to use, modify, and distribute it as you like.

---

## 🧑‍💻 Uploading and Using Data on Microsoft Fabric

### 1. Go to Microsoft Fabric

- Open your browser and go to: [Microsoft Fabric](https://app.fabric.microsoft.com)
- Sign in using your Microsoft or organizational account.

### 2. Create a Workspace (or pick an existing one)

- On the left sidebar, click “Workspaces”.
- Click “New workspace” (top-right).
- Name it something like: **Personal Finance Tracker**
- Click “Create”

### Make sure this workspace is assigned to a Fabric Capacity:

- In workspace settings, under **“Premium / Fabric capacity”**, toggle it to **On**.

### 3. Create a Lakehouse

- Inside the workspace, click **New** > **Lakehouse**
- Give it a name: **FinanceLakehouse**
- Click **Create**

This sets up the data storage environment where your CSV will live.

### 4. Upload `finance_data.csv` to the Lakehouse

- After creating the Lakehouse, it opens the Lakehouse view.
- You’ll see **“Files”** and **“Tables”** tabs.
- Click the **Files** tab.
- Click **Upload → Upload files**.
- Select your `finance_data.csv` file from your local system.
- Confirm the upload.

✅ **Done!** You’ve now uploaded the CSV to your Lakehouse.

### Optional: Convert CSV to a Table (Recommended)

To use your data in reports, it’s best to promote it to a table:

- In **Files**, right-click your `finance_data.csv`.
- Choose **“Create table”**.
- Fabric will infer headers and create a SQL-compatible table from your CSV.

You can now:

- Use Power BI to build reports from this table.
- Query the table in Fabric notebooks.
- Set refresh schedules later via pipelines or Dataflows.

---

## 📤 Upload to OneLake via Python Script

You can also upload your `finance_data.csv` file directly to OneLake using the following script.

```python
import os
import requests
from azure.identity import InteractiveBrowserCredential

# Change these
lakehouse_url = "https://onelake.dfs.fabric.microsoft.com/YourWorkspace.YourLakehouse.Lakehouse/files/finance_data.csv"
local_file = "./finance_data.csv"  # adjust path if needed

# Authenticate (this opens a browser window for login)
credential = InteractiveBrowserCredential()
token = credential.get_token("https://storage.azure.com/.default").token

# Upload
headers = {
    "Authorization": f"Bearer {token}",
    "x-ms-blob-type": "BlockBlob"
}

with open(local_file, "rb") as f:
    response = requests.put(lakehouse_url, data=f, headers=headers)

if response.status_code in [200, 201]:
    print("✅ Upload successful!")
else:
    print(f"❌ Upload failed: {response.status_code} — {response.text}")
```

This script will authenticate via your Microsoft account, and then upload the `finance_data.csv` file to OneLake.

---
