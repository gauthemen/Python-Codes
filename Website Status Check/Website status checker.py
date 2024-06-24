{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1a095b7-b78c-4339-91f2-ccfe1ceb92a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the Website URL:   google.com\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond>\n",
      "Make sure you are entering a valid URL\n"
     ]
    }
   ],
   "source": [
    "import urllib.request\n",
    "\n",
    "\n",
    "def check_website_status():\n",
    "    prompt = \"Enter the Website URL:  \"\n",
    "    while True:\n",
    "        url = str(input(prompt))  # prompt\n",
    "        if url.startswith('https://'):\n",
    "            pass\n",
    "        elif url.startswith('http://'):\n",
    "            pass\n",
    "        else:\n",
    "            url = 'https://' + url\n",
    "        try:\n",
    "            headers = {}\n",
    "            headers['User-Agent'] = (\n",
    "                \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \\\n",
    "            (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36\")\n",
    "            req = urllib.request.Request(url, headers=headers)\n",
    "            page = urllib.request.urlopen(req)\n",
    "            code = str(page.getcode())\n",
    "            print('The website ' + url + ' has returned a ' + code + ' code')\n",
    "            break\n",
    "        except Exception as e:\n",
    "            print(str(e))\n",
    "            print(\"Make sure you are entering a valid URL\")\n",
    "            try_again = input(\"Do you want to try again (y/n): \")\n",
    "            try_again = try_again.lower()\n",
    "            if try_again == 'y':\n",
    "                continue\n",
    "            else:\n",
    "                break\n",
    "\n",
    "\n",
    "check_website_status()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee1c5c03-8a4f-4e44-8ba1-f15e75c4fd1b",
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
