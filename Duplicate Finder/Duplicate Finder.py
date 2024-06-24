{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "68cb76f4-fea8-4667-9ffb-77fd34514be0",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 71\u001b[0m\n\u001b[0;32m     68\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNo action taken.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     70\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m---> 71\u001b[0m     \u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[1;32mIn[1], line 33\u001b[0m, in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m     32\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmain\u001b[39m():\n\u001b[1;32m---> 33\u001b[0m     directory \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mEnter the directory to scan for duplicates: \u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     34\u001b[0m     min_size \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter the minimum file size to consider (in bytes, default is 0): \u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     36\u001b[0m     duplicates \u001b[38;5;241m=\u001b[39m find_duplicates(directory, min_size)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipykernel\\kernelbase.py:1282\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1280\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1281\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1282\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1283\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1284\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1285\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1286\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[0;32m   1287\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipykernel\\kernelbase.py:1325\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1322\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1323\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1324\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1325\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1326\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1327\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import hashlib\n",
    "\n",
    "def get_file_hash(filepath):\n",
    "    \"\"\"Return the MD5 hash of a file.\"\"\"\n",
    "    hasher = hashlib.md5()\n",
    "    with open(filepath, 'rb') as f:\n",
    "        buf = f.read()\n",
    "        hasher.update(buf)\n",
    "    return hasher.hexdigest()\n",
    "\n",
    "def find_duplicates(directory, min_size=0):\n",
    "    \"\"\"Find duplicate files in a directory.\"\"\"\n",
    "    hashes = {}\n",
    "    duplicates = {}\n",
    "\n",
    "    for dirpath, dirnames, filenames in os.walk(directory):\n",
    "        for filename in filenames:\n",
    "            filepath = os.path.join(dirpath, filename)\n",
    "            if os.path.getsize(filepath) >= min_size:\n",
    "                file_hash = get_file_hash(filepath)\n",
    "                if file_hash in hashes:\n",
    "                    duplicates.setdefault(file_hash, []).append(filepath)\n",
    "                    # Also ensure the original file is in the duplicates list\n",
    "                    if hashes[file_hash] not in duplicates[file_hash]:\n",
    "                        duplicates[file_hash].append(hashes[file_hash])\n",
    "                else:\n",
    "                    hashes[file_hash] = filepath\n",
    "\n",
    "    return {k: v for k, v in duplicates.items() if len(v) > 1}\n",
    "\n",
    "def main():\n",
    "    directory = input(\"Enter the directory to scan for duplicates: \")\n",
    "    min_size = int(input(\"Enter the minimum file size to consider (in bytes, default is 0): \") or \"0\")\n",
    "\n",
    "    duplicates = find_duplicates(directory, min_size)\n",
    "\n",
    "    if not duplicates:\n",
    "        print(\"No duplicates found.\")\n",
    "        return\n",
    "\n",
    "    print(\"\\nDuplicates found:\")\n",
    "    for _, paths in duplicates.items():\n",
    "        for path in paths:\n",
    "            print(path)\n",
    "        print(\"------\")\n",
    "\n",
    "    action = input(\"\\nChoose an action: (D)elete, (M)ove, (N)o action: \").lower()\n",
    "\n",
    "    if action == \"d\":\n",
    "        for _, paths in duplicates.items():\n",
    "            for path in paths[1:]:  # Keep the first file, delete the rest\n",
    "                os.remove(path)\n",
    "                print(f\"Deleted {path}\")\n",
    "\n",
    "    elif action == \"m\":\n",
    "        target_dir = input(\"Enter the directory to move duplicates to: \")\n",
    "        if not os.path.exists(target_dir):\n",
    "            os.makedirs(target_dir)\n",
    "\n",
    "        for _, paths in duplicates.items():\n",
    "            for path in paths[1:]:  # Keep the first file, move the rest\n",
    "                target_path = os.path.join(target_dir, os.path.basename(path))\n",
    "                os.rename(path, target_path)\n",
    "                print(f\"Moved {path} to {target_path}\")\n",
    "\n",
    "    else:\n",
    "        print(\"No action taken.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cafb6c58-f525-4f22-ac33-7745381dc5ea",
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
