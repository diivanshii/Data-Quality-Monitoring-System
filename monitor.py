{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8b44781-d4bb-464c-a018-03920c3950ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Monitoring complete. Check issues_log.csv.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(\"marketing_campaign.csv\")\n",
    "\n",
    "# Initialize log list\n",
    "logs = []\n",
    "\n",
    "# 1. Null Value Check\n",
    "nulls = df.isnull().sum()\n",
    "null_issues = nulls[nulls > 0]\n",
    "for col, count in null_issues.items():\n",
    "    logs.append(f\"Nulls in '{col}': {count}\")\n",
    "\n",
    "# 2. Duplicate Check\n",
    "duplicate_count = df.duplicated().sum()\n",
    "if duplicate_count > 0:\n",
    "    logs.append(f\"Duplicate Rows: {duplicate_count}\")\n",
    "\n",
    "# 3. Outlier Detection (numeric columns)\n",
    "numeric_cols = df.select_dtypes(include='number').columns\n",
    "for col in numeric_cols:\n",
    "    outliers = df[df[col] > df[col].quantile(0.99)]\n",
    "    if not outliers.empty:\n",
    "        logs.append(f\"Outliers in '{col}': {len(outliers)} values above 99th percentile\")\n",
    "\n",
    "# 4. Schema Validation\n",
    "expected_cols = ['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income']\n",
    "for col in expected_cols:\n",
    "    if col not in df.columns:\n",
    "        logs.append(f\"Missing expected column: {col}\")\n",
    "\n",
    "# 5. Write issues to CSV\n",
    "with open(\"issues_log.csv\", \"w\") as f:\n",
    "    f.write(\"Issue\\n\")\n",
    "    for log in logs:\n",
    "        f.write(f\"{log}\\n\")\n",
    "\n",
    "print(\"Monitoring complete. Check issues_log.csv.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fc0bcc6-d258-43fd-825d-874ac238e47a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
