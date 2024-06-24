{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "486e3abd-4229-4711-bccb-f81aca9305c9",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'input.json'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 12\u001b[0m\n\u001b[0;32m      9\u001b[0m csv_file \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124moutput.csv\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m     11\u001b[0m \u001b[38;5;66;03m# Load JSON data from a file\u001b[39;00m\n\u001b[1;32m---> 12\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43minput_json_file\u001b[49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m json_file:\n\u001b[0;32m     13\u001b[0m     data \u001b[38;5;241m=\u001b[39m json\u001b[38;5;241m.\u001b[39mload(json_file)\n\u001b[0;32m     15\u001b[0m \u001b[38;5;66;03m# Open the CSV file in write mode\u001b[39;00m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    322\u001b[0m     )\n\u001b[1;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'input.json'"
     ]
    }
   ],
   "source": [
    "# json and csv modules are installed by default, no need to install\n",
    "\n",
    "import json\n",
    "import csv\n",
    "\n",
    "\n",
    "# specify file path , along with extension\n",
    "input_json_file = 'input.json'\n",
    "csv_file = 'output.csv'\n",
    "\n",
    "# Load JSON data from a file\n",
    "with open(input_json_file) as json_file:\n",
    "    data = json.load(json_file)\n",
    "\n",
    "# Open the CSV file in write mode\n",
    "with open(csv_file, 'w', newline='') as csvfile:\n",
    "    # Create a CSV writer\n",
    "    writer = csv.writer(csvfile)\n",
    "\n",
    "    # Write the header row based on the keys of the first JSON object\n",
    "    writer.writerow(data[0].keys())\n",
    "\n",
    "    # Write the data rows\n",
    "    for item in data:\n",
    "        writer.writerow(item.values())\n",
    "\n",
    "printf(\"Conversion successfull. The output file is saved as : \" + csv_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c53f654-9020-4189-a362-eba64bbd75d0",
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
