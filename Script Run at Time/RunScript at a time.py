{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "066a309e-6a63-494b-8aa9-08ca464c6670",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import datetime library in python\n",
    "from datetime import datetime\n",
    "# Saves a .txt file with file name\n",
    "# as 2020-01-11-10-20-23.txt  at current time indicated by now function of datetime library\n",
    "with open(datetime.now().strftime(\"%Y-%m-%d-%H-%M-%S\"), \"w\") as myfile:\n",
    "    # instead of now i could also initialse with datetime(1999, 12, 12, 12, 12, 12, 342380) to give the time values to datetime constructor\n",
    "    # Content of the file (it can be any script in python which we want to run at a particular time )\n",
    "    myfile.write(\"hii guys ,your Lunch time begins ! \")"
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
