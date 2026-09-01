{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPPH+gaTUNL1xoM6vbUn74q",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mynenisailikitha2827/Computer_vision/blob/main/CV_LAB5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "htp2LVCc6x8W"
      },
      "outputs": [],
      "source": [
        "import cv2\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "img = cv2.imread(\"/content/loki.jpg\", cv2.IMREAD_GRAYSCALE)\n",
        "if img is None:\n",
        "    print(\"error: image not found\")\n",
        "else:\n",
        "    fig, axes = plt.subplots(3, 3, figsize=(8,6))\n",
        "    axes = axes.flatten()\n",
        "    axes[0].imshow(img, cmap=\"gray\")\n",
        "    axes[0].set_title(\"Original Image\")\n",
        "    axes[0].axis(\"off\")\n",
        "    for i in range(8):\n",
        "        bit_plane = (img >> i) & 1\n",
        "        axes[i + 1].imshow(bit_plane * 255, cmap=\"gray\")\n",
        "        axes[i + 1].set_title(f\"Bit Plane {i}\")\n",
        "        axes[i + 1].axis(\"off\")\n",
        "    plt.tight_layout()\n",
        "    plt.show()"
      ]
    }
  ]
}