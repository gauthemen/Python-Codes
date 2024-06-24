{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "397691e7-4b47-4249-9c3c-b3e0753d52b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a remote host to scan:  8888\n"
     ]
    },
    {
     "ename": "gaierror",
     "evalue": "[Errno 11001] getaddrinfo failed",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mgaierror\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 11\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m# Ask for input\u001b[39;00m\n\u001b[0;32m     10\u001b[0m remoteServer \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a remote host to scan: \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 11\u001b[0m remoteServerIP \u001b[38;5;241m=\u001b[39m \u001b[43msocket\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgethostbyname\u001b[49m\u001b[43m(\u001b[49m\u001b[43mremoteServer\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     13\u001b[0m \u001b[38;5;66;03m# Print a nice banner with information on which host we are about to scan\u001b[39;00m\n\u001b[0;32m     14\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m*\u001b[39m \u001b[38;5;241m60\u001b[39m)\n",
      "\u001b[1;31mgaierror\u001b[0m: [Errno 11001] getaddrinfo failed"
     ]
    }
   ],
   "source": [
    "import socket\n",
    "import subprocess\n",
    "import sys\n",
    "import asyncio\n",
    "from datetime import datetime\n",
    "\n",
    "subprocess.call('cls', shell=True)\n",
    "\n",
    "# Ask for input\n",
    "remoteServer = input(\"Enter a remote host to scan: \")\n",
    "remoteServerIP = socket.gethostbyname(remoteServer)\n",
    "\n",
    "# Print a nice banner with information on which host we are about to scan\n",
    "print(\"-\" * 60)\n",
    "print(\"Please wait, scanning remote host\", remoteServerIP)\n",
    "print(\"-\" * 60)\n",
    "\n",
    "# Check what time the scan started\n",
    "t1 = datetime.now()\n",
    "\n",
    "\n",
    "async def scan_port(port):\n",
    "    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
    "    sock.setblocking(False)\n",
    "    try:\n",
    "        await asyncio.wait_for(\n",
    "            asyncio.get_event_loop().sock_connect(sock, (remoteServerIP, port)),\n",
    "            timeout=1\n",
    "        )\n",
    "        print(\"Port {}: Open\".format(port))\n",
    "    except (socket.timeout, ConnectionRefusedError):\n",
    "        pass\n",
    "    finally:\n",
    "        sock.close()\n",
    "\n",
    "\n",
    "async def main():\n",
    "    tasks = []\n",
    "    for port in range(1, 1025):\n",
    "        tasks.append(scan_port(port))\n",
    "    await asyncio.gather(*tasks)\n",
    "\n",
    "try:\n",
    "    asyncio.run(main())\n",
    "except KeyboardInterrupt:\n",
    "    print(\"You pressed Ctrl+C\")\n",
    "    sys.exit()\n",
    "\n",
    "except socket.gaierror:\n",
    "    print('Hostname could not be resolved. Exiting')\n",
    "    sys.exit()\n",
    "\n",
    "except socket.error:\n",
    "    print(\"Couldn't connect to server\")\n",
    "    sys.exit()\n",
    "\n",
    "# Checking the time again\n",
    "t2 = datetime.now()\n",
    "\n",
    "# Calculates the difference of time, to see how long it took to run the script\n",
    "total = t2 - t1\n",
    "\n",
    "print('Scanning Completed in:', total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b97a6ff-48bc-4a3c-984d-776aac28b29e",
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
