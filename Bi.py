{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Dhwani123p/CL-4/blob/main/Bi.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wf5KrEb6vrkR"
      },
      "source": [
        "# Welcome to Colab!"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from sqlalchemy import create_engine\n",
        "\n",
        "# Extract\n",
        "df = pd.DataFrame({\n",
        "    \"id\":     [1, 2, 3, 4, 5],\n",
        "    \"name\":   [\"Alice\", \"Bob\", None, \"Dave\", \"Alice\"],\n",
        "    \"dept\":   [\"HR\", \"IT\", \"Finance\", \"Sales\", \"HR\"],\n",
        "    \"salary\": [50000, 60000, 55000, None, 50000]\n",
        "})\n",
        "\n",
        "# Transform\n",
        "df.dropna(inplace=True)\n",
        "df.drop_duplicates(inplace=True)\n",
        "print(\"After Transform:\\n\", df)\n",
        "\n",
        "# Load to SQLite (creates a local .db file — no installation needed)\n",
        "engine = create_engine(\"sqlite:///etl_database.db\")\n",
        "df.to_sql(\"ETL_Output\", engine, if_exists=\"replace\", index=False)\n",
        "print(\"✅ Database created: etl_database.db\")\n",
        "\n",
        "# Verify — read back from DB\n",
        "verify = pd.read_sql(\"SELECT * FROM ETL_Output\", engine)\n",
        "print(\"\\nData in Database:\\n\", verify)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "poooV9LRFJ0K",
        "outputId": "fb7f1e5f-8ae2-41ea-a6e2-a19509ca49b2"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "After Transform:\n",
            "    id   name dept   salary\n",
            "0   1  Alice   HR  50000.0\n",
            "1   2    Bob   IT  60000.0\n",
            "4   5  Alice   HR  50000.0\n",
            "✅ Database created: etl_database.db\n",
            "\n",
            "Data in Database:\n",
            "    id   name dept   salary\n",
            "0   1  Alice   HR  50000.0\n",
            "1   2    Bob   IT  60000.0\n",
            "2   5  Alice   HR  50000.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# ── 1. SIMULATE ETL DATA ────────────────\n",
        "raw = pd.DataFrame({\n",
        "    \"name\":   [\"Alice\", \"Bob\", None, \"Dave\", \"Alice\", \"Eve\"],\n",
        "    \"dept\":   [\"HR\", \"IT\", None, \"Sales\", \"HR\", \"IT\"],\n",
        "    \"salary\": [50000, 60000, 55000, None, 50000, 70000]\n",
        "})\n",
        "\n",
        "# ── 2. TRANSFORM ────────────────────────\n",
        "clean = raw.copy()\n",
        "clean.dropna(inplace=True)       # remove nulls\n",
        "clean.drop_duplicates(inplace=True)  # remove duplicates\n",
        "\n",
        "# ── 3. VISUALIZE ETL STATS ──────────────\n",
        "\n",
        "# Chart 1 - Before vs After (rows)\n",
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "plt.subplot(2, 2, 1)\n",
        "plt.bar([\"Before ETL\", \"After ETL\"], [len(raw), len(clean)], color=[\"red\", \"green\"])\n",
        "plt.title(\"Row Count: Before vs After ETL\")\n",
        "plt.ylabel(\"Rows\")\n",
        "\n",
        "# Chart 2 - Null values per column\n",
        "plt.subplot(2, 2, 2)\n",
        "raw.isnull().sum().plot(kind=\"bar\", color=\"orange\")\n",
        "plt.title(\"Null Values per Column (Before ETL)\")\n",
        "plt.ylabel(\"Null Count\")\n",
        "\n",
        "# Chart 3 - Salary by Department (after ETL)\n",
        "plt.subplot(2, 2, 3)\n",
        "clean.groupby(\"dept\")[\"salary\"].mean().plot(kind=\"bar\", color=\"blue\")\n",
        "plt.title(\"Avg Salary by Department (After ETL)\")\n",
        "plt.ylabel(\"Salary\")\n",
        "\n",
        "# Chart 4 - Pie chart of departments\n",
        "plt.subplot(2, 2, 4)\n",
        "clean[\"dept\"].value_counts().plot(kind=\"pie\", autopct=\"%1.0f%%\")\n",
        "plt.title(\"Department Distribution\")\n",
        "plt.ylabel(\"\")\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.savefig(\"etl_visualization.png\")\n",
        "plt.show()\n",
        "print(\"Done! Chart saved.\")"
      ],
      "metadata": {
        "id": "f24toZ_ZFifI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "2SKAYa5eFRAj"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}