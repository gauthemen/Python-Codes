{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04e62407-949c-4c40-832f-6a0b3f4e1705",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'for' statement on line 9 (1905915550.py, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 10\u001b[1;36m\u001b[0m\n\u001b[1;33m    for _file in fnmatch.filter(_files, _pattern):\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after 'for' statement on line 9\n"
     ]
    }
   ],
   "source": [
    "# searching_specific_files.py\n",
    "\n",
    "import fnmatch\n",
    "import os\n",
    "\n",
    "root_path = '/home/tuts/Documents'\n",
    "_pattern = '*.mp4'\n",
    "\n",
    "for _root, dirs, _files in os.walk(root_path):\n",
    "for _file in fnmatch.filter(_files, _pattern):\n",
    "print(os.path.join(_root, _file))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b27c5f65-07c7-41d4-ad8a-b62b6ebbd6b8",
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
