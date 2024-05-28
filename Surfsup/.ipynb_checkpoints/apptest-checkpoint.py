{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8ed3d978",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a822ad6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5cdb8d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def home():\n",
    "    print(\"Server received request from homepage...\")\n",
    "    return \"Welcome to my homepage\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (DataScience)",
   "language": "python",
   "name": "datascience"
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
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
