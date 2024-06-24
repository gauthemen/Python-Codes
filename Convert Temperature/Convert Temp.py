{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0549f671-8e6a-4103-9391-b9b7c0667a0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What would you like to convert from? (input no.): \n",
      " (1)Celsius (2)fahrenheit (3)Kelvin  1\n",
      "Enter Temperature:  25\n",
      "You want to convert it into: \n",
      " (a)fahrenheit (b)Kelvin  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The temperature is: 77.0 °F\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def from_cel():    \n",
    "    x = float(input(\"Enter Temperature: \"))\n",
    "    y = input(\"You want to convert it into: \\n (a)fahrenheit (b)Kelvin \")\n",
    "    \n",
    "    if y == 'a':\n",
    "        final = (x*(9/5)) + 32\n",
    "        print(f\"The temperature is: {final} °F\")\n",
    "\n",
    "    else:\n",
    "        final = x + 273.15\n",
    "        print(f\"The temperature is: {final} K\")\n",
    "\n",
    "        \n",
    "\n",
    "def from_fah():\n",
    "    x = float(input(\"Enter Temperature: \"))\n",
    "    y = input(\"You want to convert it into: \\n (a)celsius (b)Kelvin \")\n",
    "    \n",
    "    if y == 'a':\n",
    "        final = (x - 32)*(5/9)\n",
    "        print(f\"The temperature is: {final} °C\")\n",
    "\n",
    "\n",
    "    else:\n",
    "        final = (x - 32)*(5/9) + 273.15\n",
    "        print(f\"The temperature is: {final} K\")\n",
    "\n",
    "\n",
    "def from_Kel():\n",
    "    x = float(input(\"Enter Temperature: \"))\n",
    "    y = input(\"You want to convert it into: \\n (a)celsius (b)fahrenheit \")\n",
    "    \n",
    "    if y == 'a':\n",
    "        final = x - 273.15\n",
    "        print(f\"The temperature is: {final} °C\")\n",
    "\n",
    "    else:\n",
    "        final = (x - 273.15)*(5/9) + 32\n",
    "        print(f\"The temperature is: {final} °F\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def get_temp():\n",
    "    global t\n",
    "    t = input(\"What would you like to convert from? (input no.): \\n (1)Celsius (2)fahrenheit (3)Kelvin \")\n",
    "\n",
    "get_temp()\n",
    "\n",
    "\n",
    "if t == \"1\":\n",
    "    from_cel()\n",
    "\n",
    "elif t == '2':\n",
    "    from_fah()\n",
    "\n",
    "elif t == '3':\n",
    "    from_Kel()\n",
    "\n",
    "else:\n",
    "    print(\"please enter a correct input\")\n",
    "    get_temp()\n"
   ]
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
