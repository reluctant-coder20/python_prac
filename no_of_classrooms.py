{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOYEjZkwzihjL49xPPP6WoU",
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
        "<a href=\"https://colab.research.google.com/github/reluctant-coder20/python_prac/blob/main/no_of_classrooms.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d4RdKYjyhrCv",
        "outputId": "d0f157ac-51ef-434a-d5c2-3c29ddd39ada"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "number of classrooms:  5\n"
          ]
        }
      ],
      "source": [
        "\"\"\"you are given a list of subjects for students. assume 1 classroom for 1 subject.\n",
        " how many classrooms are required by all students\"\"\"\n",
        "\n",
        "subjects = {\"python\", \"java\",\"c++\",\"python\",\"javascript\",\"java\",\"python\",\"java\",\"c++\",\"c\"}\n",
        "a = len(subjects)\n",
        "print(\"number of classrooms: \", a)"
      ]
    }
  ]
}