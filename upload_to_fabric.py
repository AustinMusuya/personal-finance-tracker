import os
import requests
from azure.identity import InteractiveBrowserCredential

# Change these

# lakehouse_url = "https://onelake.dfs.fabric.microsoft.com/YourWorkspace.YourLakehouse.Lakehouse/files/finance_data.csv"

lakehouse_url = "https://onelake.dfs.fabric.microsoft.com/Finance-tracker.finance_data.Lakehouse/files/finance_data.csv"
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
