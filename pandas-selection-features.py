{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "214bb2d9",
   "metadata": {
    "papermill": {
     "duration": 0.006344,
     "end_time": "2025-10-21T02:12:35.389209",
     "exception": false,
     "start_time": "2025-10-21T02:12:35.382865",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h1>📌 Explorando a Biblioteca Pandas em Python: seleção de dados</h1>\n",
    "\n",
    "<h3>📌 Um Guia Prático para Iniciantes</h3>\n",
    "\n",
    "<p style='font-size:16px;'>A biblioteca Pandas é uma das ferramentas mais poderosas e populares da linguagem Python para análise e manipulação de dados. Criada por Wes McKinney, ela se tornou essencial para cientistas de dados, analistas e desenvolvedores que trabalham com grandes volumes de informações.</p>\n",
    "\n",
    "<p>O Pandas (derivado de Panel Data) é uma biblioteca de código aberto voltada para trabalhar com dados estruturados, ou seja, dados organizados em tabelas.</p>\n",
    "\n",
    "<h3>📌 Seleção de dados</h3>\n",
    "\n",
    "<p style='font-size:16px;'>A seleção de dados é uma das tarefas mais importantes no uso do Pandas, pois permite acessar informações de forma flexível. No Pandas, a seleção é feita principalmente por indexação (usando colchetes [] - operador de indexação), usando os métodos .loc (para rótulos) e .iloc (para índices numéricos), entre outras formas. Você pode selecionar colunas específicas, múltiplas colunas, linhas baseadas em condições ou por posição, e até subconjuntos que combinam linhas e colunas.</p>\n",
    "\n",
    "📌Autor: Carlos da Costa<br>\n",
    "📌Recife, PE - Brasil<br>\n",
    "📌Telefone: +55 81 99712 9140<br>\n",
    "📌Telegram: @jcarlossc<br>\n",
    "📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>\n",
    "📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>\n",
    "📌Email: jcarlossc1977@gmail.com<br>\n",
    "📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>\n",
    "📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>\n",
    "📌GitHub: https://github.com/jcarlossc<br>\n",
    "📌Kaggle: https://www.kaggle.com/jcarlossc/<br>\n",
    "📌Twitter/X: https://x.com/jcarlossc1977"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "694a2673",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:35.401689Z",
     "iopub.status.busy": "2025-10-21T02:12:35.401338Z",
     "iopub.status.idle": "2025-10-21T02:12:37.581203Z",
     "shell.execute_reply": "2025-10-21T02:12:37.579950Z"
    },
    "papermill": {
     "duration": 2.188341,
     "end_time": "2025-10-21T02:12:37.583133",
     "exception": false,
     "start_time": "2025-10-21T02:12:35.394792",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Importando a biblioteca Pandas\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a6b91edc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.595900Z",
     "iopub.status.busy": "2025-10-21T02:12:37.595435Z",
     "iopub.status.idle": "2025-10-21T02:12:37.607614Z",
     "shell.execute_reply": "2025-10-21T02:12:37.606423Z"
    },
    "papermill": {
     "duration": 0.02065,
     "end_time": "2025-10-21T02:12:37.609369",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.588719",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Criando um DataFrame de exemplo\n",
    "dados = pd.DataFrame(\n",
    "    {\n",
    "    'nome': ['Teresa', 'Soares', 'Jose', 'Carlos', 'Maria', 'Teresa'],\n",
    "    'idade': [3, 35, 31, 48, 40, 56],\n",
    "    'cidade': ['Recife', 'Paulista', 'Olinda', 'Caruaru', 'Petrolina', 'Timbauba'],\n",
    "    'salario': [3200, 4500, 5000, 3700, 6000, 7000]\n",
    "    }\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c207a6f9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.622386Z",
     "iopub.status.busy": "2025-10-21T02:12:37.622060Z",
     "iopub.status.idle": "2025-10-21T02:12:37.658913Z",
     "shell.execute_reply": "2025-10-21T02:12:37.657776Z"
    },
    "papermill": {
     "duration": 0.045974,
     "end_time": "2025-10-21T02:12:37.660843",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.614869",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6 entries, 0 to 5\n",
      "Data columns (total 4 columns):\n",
      " #   Column   Non-Null Count  Dtype \n",
      "---  ------   --------------  ----- \n",
      " 0   nome     6 non-null      object\n",
      " 1   idade    6 non-null      int64 \n",
      " 2   cidade   6 non-null      object\n",
      " 3   salario  6 non-null      int64 \n",
      "dtypes: int64(2), object(2)\n",
      "memory usage: 324.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "# Informações sobre quantidade de observações(6), número de colunas(4),\n",
    "# uso de memória e tipos de dados.\n",
    "dados.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73a78b84",
   "metadata": {
    "papermill": {
     "duration": 0.005712,
     "end_time": "2025-10-21T02:12:37.672148",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.666436",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção de colunas</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ff0077c4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.684684Z",
     "iopub.status.busy": "2025-10-21T02:12:37.684310Z",
     "iopub.status.idle": "2025-10-21T02:12:37.691982Z",
     "shell.execute_reply": "2025-10-21T02:12:37.691113Z"
    },
    "papermill": {
     "duration": 0.01563,
     "end_time": "2025-10-21T02:12:37.693559",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.677929",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Teresa\n",
       "1    Soares\n",
       "2      Jose\n",
       "3    Carlos\n",
       "4     Maria\n",
       "5    Teresa\n",
       "Name: nome, dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Selecionar uma única coluna.\n",
    "dados['nome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "edcd1775",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.705869Z",
     "iopub.status.busy": "2025-10-21T02:12:37.705523Z",
     "iopub.status.idle": "2025-10-21T02:12:37.729381Z",
     "shell.execute_reply": "2025-10-21T02:12:37.728106Z"
    },
    "papermill": {
     "duration": 0.032121,
     "end_time": "2025-10-21T02:12:37.731290",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.699169",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Maria</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade\n",
       "0  Teresa      3\n",
       "1  Soares     35\n",
       "2    Jose     31\n",
       "3  Carlos     48\n",
       "4   Maria     40\n",
       "5  Teresa     56"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Selecionar multiplas colunas.\n",
    "dados[['nome', 'idade']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e786cf89",
   "metadata": {
    "papermill": {
     "duration": 0.005995,
     "end_time": "2025-10-21T02:12:37.743260",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.737265",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção por índices e posições com iloc.</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "59b651da",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.755647Z",
     "iopub.status.busy": "2025-10-21T02:12:37.755360Z",
     "iopub.status.idle": "2025-10-21T02:12:37.762457Z",
     "shell.execute_reply": "2025-10-21T02:12:37.761475Z"
    },
    "papermill": {
     "duration": 0.015266,
     "end_time": "2025-10-21T02:12:37.764172",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.748906",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nome       Teresa\n",
       "idade           3\n",
       "cidade     Recife\n",
       "salario      3200\n",
       "Name: 0, dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona a primeira linha.\n",
    "dados.iloc[0]        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2e978217",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.776884Z",
     "iopub.status.busy": "2025-10-21T02:12:37.776519Z",
     "iopub.status.idle": "2025-10-21T02:12:37.786445Z",
     "shell.execute_reply": "2025-10-21T02:12:37.785417Z"
    },
    "papermill": {
     "duration": 0.018243,
     "end_time": "2025-10-21T02:12:37.788229",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.769986",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>35</td>\n",
       "      <td>Paulista</td>\n",
       "      <td>4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>31</td>\n",
       "      <td>Olinda</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade    cidade  salario\n",
       "0  Teresa      3    Recife     3200\n",
       "1  Soares     35  Paulista     4500\n",
       "2    Jose     31    Olinda     5000"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Da 1ª à 3ª linha (exclusive)\n",
    "dados.iloc[0:3]      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c9e4c8af",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.802797Z",
     "iopub.status.busy": "2025-10-21T02:12:37.801625Z",
     "iopub.status.idle": "2025-10-21T02:12:37.808983Z",
     "shell.execute_reply": "2025-10-21T02:12:37.807837Z"
    },
    "papermill": {
     "duration": 0.015865,
     "end_time": "2025-10-21T02:12:37.810655",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.794790",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Teresa\n",
       "1    Soares\n",
       "2      Jose\n",
       "3    Carlos\n",
       "4     Maria\n",
       "5    Teresa\n",
       "Name: nome, dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona primeira coluna.\n",
    "dados.iloc[:, 0]     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4276ba80",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.824180Z",
     "iopub.status.busy": "2025-10-21T02:12:37.823856Z",
     "iopub.status.idle": "2025-10-21T02:12:37.833572Z",
     "shell.execute_reply": "2025-10-21T02:12:37.832636Z"
    },
    "papermill": {
     "duration": 0.018571,
     "end_time": "2025-10-21T02:12:37.835213",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.816642",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Maria</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade\n",
       "0  Teresa      3\n",
       "1  Soares     35\n",
       "2    Jose     31\n",
       "3  Carlos     48\n",
       "4   Maria     40\n",
       "5  Teresa     56"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Duas primeiras colunas\n",
    "dados.iloc[:, 0:2]   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a472baed",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.848574Z",
     "iopub.status.busy": "2025-10-21T02:12:37.848256Z",
     "iopub.status.idle": "2025-10-21T02:12:37.854446Z",
     "shell.execute_reply": "2025-10-21T02:12:37.853556Z"
    },
    "papermill": {
     "duration": 0.014632,
     "end_time": "2025-10-21T02:12:37.855974",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.841342",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Paulista'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona elemento linha 2, coluna 3\n",
    "dados.iloc[1, 2]     "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6909352e",
   "metadata": {
    "papermill": {
     "duration": 0.005713,
     "end_time": "2025-10-21T02:12:37.868132",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.862419",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção por rótulo(label) com loc.</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "033dd62e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.881982Z",
     "iopub.status.busy": "2025-10-21T02:12:37.881636Z",
     "iopub.status.idle": "2025-10-21T02:12:37.892499Z",
     "shell.execute_reply": "2025-10-21T02:12:37.891009Z"
    },
    "papermill": {
     "duration": 0.020173,
     "end_time": "2025-10-21T02:12:37.894179",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.874006",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>cidade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>Recife</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>Paulista</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>Olinda</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome    cidade\n",
       "0  Teresa    Recife\n",
       "1  Soares  Paulista\n",
       "2    Jose    Olinda"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona linhas com íntervalo de índices e nomes de colunas.\n",
    "dados.loc[0:2, ['nome', 'cidade']]                   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bb44394a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.909132Z",
     "iopub.status.busy": "2025-10-21T02:12:37.908779Z",
     "iopub.status.idle": "2025-10-21T02:12:37.914804Z",
     "shell.execute_reply": "2025-10-21T02:12:37.913716Z"
    },
    "papermill": {
     "duration": 0.015514,
     "end_time": "2025-10-21T02:12:37.916561",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.901047",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Definindo a coluna \"name\" como índice (rótulo das linhas).\n",
    "dados_loc = pd.DataFrame(dados).set_index('nome')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "57ab0521",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.930498Z",
     "iopub.status.busy": "2025-10-21T02:12:37.930225Z",
     "iopub.status.idle": "2025-10-21T02:12:37.941096Z",
     "shell.execute_reply": "2025-10-21T02:12:37.939982Z"
    },
    "papermill": {
     "duration": 0.019799,
     "end_time": "2025-10-21T02:12:37.942907",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.923108",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>nome</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Teresa</th>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Teresa</th>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        idade    cidade  salario\n",
       "nome                            \n",
       "Teresa      3    Recife     3200\n",
       "Teresa     56  Timbauba     7000"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona uma linha pelo rótulo.\n",
    "dados_loc.loc['Teresa']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "57bb398b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.957324Z",
     "iopub.status.busy": "2025-10-21T02:12:37.957037Z",
     "iopub.status.idle": "2025-10-21T02:12:37.966212Z",
     "shell.execute_reply": "2025-10-21T02:12:37.965312Z"
    },
    "papermill": {
     "duration": 0.018234,
     "end_time": "2025-10-21T02:12:37.967852",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.949618",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>nome</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Carlos</th>\n",
       "      <td>48</td>\n",
       "      <td>Caruaru</td>\n",
       "      <td>3700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Teresa</th>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Teresa</th>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        idade    cidade  salario\n",
       "nome                            \n",
       "Carlos     48   Caruaru     3700\n",
       "Teresa      3    Recife     3200\n",
       "Teresa     56  Timbauba     7000"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona uma linha pelo rótulo.\n",
    "dados_loc.loc[['Carlos', 'Teresa']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "38af2434",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:37.982793Z",
     "iopub.status.busy": "2025-10-21T02:12:37.982427Z",
     "iopub.status.idle": "2025-10-21T02:12:37.989443Z",
     "shell.execute_reply": "2025-10-21T02:12:37.988338Z"
    },
    "papermill": {
     "duration": 0.016644,
     "end_time": "2025-10-21T02:12:37.991214",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.974570",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4500"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona linha e coluna.\n",
    "dados_loc.loc['Soares', 'salario']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fa4ed30c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.006777Z",
     "iopub.status.busy": "2025-10-21T02:12:38.006424Z",
     "iopub.status.idle": "2025-10-21T02:12:38.021531Z",
     "shell.execute_reply": "2025-10-21T02:12:38.020374Z"
    },
    "papermill": {
     "duration": 0.024725,
     "end_time": "2025-10-21T02:12:38.023227",
     "exception": false,
     "start_time": "2025-10-21T02:12:37.998502",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>nome</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Soares</th>\n",
       "      <td>35</td>\n",
       "      <td>Paulista</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jose</th>\n",
       "      <td>31</td>\n",
       "      <td>Olinda</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        idade    cidade\n",
       "nome                   \n",
       "Soares     35  Paulista\n",
       "Jose       31    Olinda"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona linhas e colunas específicas.\n",
    "dados_loc.loc['Soares':'Jose', ['idade', 'cidade']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d501dbc2",
   "metadata": {
    "papermill": {
     "duration": 0.006597,
     "end_time": "2025-10-21T02:12:38.036647",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.030050",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção por valores nulos ou duplicados</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "675b95ab",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.051679Z",
     "iopub.status.busy": "2025-10-21T02:12:38.051380Z",
     "iopub.status.idle": "2025-10-21T02:12:38.060421Z",
     "shell.execute_reply": "2025-10-21T02:12:38.059323Z"
    },
    "papermill": {
     "duration": 0.018263,
     "end_time": "2025-10-21T02:12:38.061968",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.043705",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [nome, idade, cidade, salario]\n",
       "Index: []"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleção por dados nulos.\n",
    "dados[dados['idade'].isna()] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5634cc06",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.077702Z",
     "iopub.status.busy": "2025-10-21T02:12:38.076622Z",
     "iopub.status.idle": "2025-10-21T02:12:38.086660Z",
     "shell.execute_reply": "2025-10-21T02:12:38.085836Z"
    },
    "papermill": {
     "duration": 0.019408,
     "end_time": "2025-10-21T02:12:38.088244",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.068836",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>35</td>\n",
       "      <td>Paulista</td>\n",
       "      <td>4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>31</td>\n",
       "      <td>Olinda</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>48</td>\n",
       "      <td>Caruaru</td>\n",
       "      <td>3700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Maria</td>\n",
       "      <td>40</td>\n",
       "      <td>Petrolina</td>\n",
       "      <td>6000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade     cidade  salario\n",
       "0  Teresa      3     Recife     3200\n",
       "1  Soares     35   Paulista     4500\n",
       "2    Jose     31     Olinda     5000\n",
       "3  Carlos     48    Caruaru     3700\n",
       "4   Maria     40  Petrolina     6000\n",
       "5  Teresa     56   Timbauba     7000"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona linhas sem valores nulos.\n",
    "dados[dados['idade'].notna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a1a1c8b4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.103804Z",
     "iopub.status.busy": "2025-10-21T02:12:38.103443Z",
     "iopub.status.idle": "2025-10-21T02:12:38.113311Z",
     "shell.execute_reply": "2025-10-21T02:12:38.112521Z"
    },
    "papermill": {
     "duration": 0.019358,
     "end_time": "2025-10-21T02:12:38.114764",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.095406",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade    cidade  salario\n",
       "0  Teresa      3    Recife     3200\n",
       "5  Teresa     56  Timbauba     7000"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona valores duplicados.\n",
    "dados[dados.duplicated('nome', keep=False)]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba2b72a0",
   "metadata": {
    "papermill": {
     "duration": 0.007162,
     "end_time": "2025-10-21T02:12:38.129286",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.122124",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção e ordenação de dados</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e9f88a2d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.145348Z",
     "iopub.status.busy": "2025-10-21T02:12:38.145034Z",
     "iopub.status.idle": "2025-10-21T02:12:38.155067Z",
     "shell.execute_reply": "2025-10-21T02:12:38.154083Z"
    },
    "papermill": {
     "duration": 0.019858,
     "end_time": "2025-10-21T02:12:38.156527",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.136669",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>31</td>\n",
       "      <td>Olinda</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>35</td>\n",
       "      <td>Paulista</td>\n",
       "      <td>4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Maria</td>\n",
       "      <td>40</td>\n",
       "      <td>Petrolina</td>\n",
       "      <td>6000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>48</td>\n",
       "      <td>Caruaru</td>\n",
       "      <td>3700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade     cidade  salario\n",
       "0  Teresa      3     Recife     3200\n",
       "2    Jose     31     Olinda     5000\n",
       "1  Soares     35   Paulista     4500\n",
       "4   Maria     40  Petrolina     6000\n",
       "3  Carlos     48    Caruaru     3700\n",
       "5  Teresa     56   Timbauba     7000"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona e ordena por idade.\n",
    "dados.sort_values('idade', ascending=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ce0c7c3",
   "metadata": {
    "papermill": {
     "duration": 0.007146,
     "end_time": "2025-10-21T02:12:38.171041",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.163895",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção de célula única com .at[] e .iat[]</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "405c8545",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.186804Z",
     "iopub.status.busy": "2025-10-21T02:12:38.186464Z",
     "iopub.status.idle": "2025-10-21T02:12:38.192885Z",
     "shell.execute_reply": "2025-10-21T02:12:38.191873Z"
    },
    "papermill": {
     "duration": 0.016512,
     "end_time": "2025-10-21T02:12:38.194522",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.178010",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Olinda'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona Valor da coluna da terceira linha. \n",
    "dados.at[2, 'cidade']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "771ce79b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.210616Z",
     "iopub.status.busy": "2025-10-21T02:12:38.210309Z",
     "iopub.status.idle": "2025-10-21T02:12:38.216791Z",
     "shell.execute_reply": "2025-10-21T02:12:38.215731Z"
    },
    "papermill": {
     "duration": 0.016212,
     "end_time": "2025-10-21T02:12:38.218292",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.202080",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Olinda'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona o valor da terceira linha da terceira coluna.\n",
    "dados.iat[2, 2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "322b0353",
   "metadata": {
    "papermill": {
     "duration": 0.007235,
     "end_time": "2025-10-21T02:12:38.233093",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.225858",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Seleção com amostragem e limites</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "8c04a94e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.249815Z",
     "iopub.status.busy": "2025-10-21T02:12:38.248731Z",
     "iopub.status.idle": "2025-10-21T02:12:38.258264Z",
     "shell.execute_reply": "2025-10-21T02:12:38.257460Z"
    },
    "papermill": {
     "duration": 0.019252,
     "end_time": "2025-10-21T02:12:38.259722",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.240470",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>3</td>\n",
       "      <td>Recife</td>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Soares</td>\n",
       "      <td>35</td>\n",
       "      <td>Paulista</td>\n",
       "      <td>4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jose</td>\n",
       "      <td>31</td>\n",
       "      <td>Olinda</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade    cidade  salario\n",
       "0  Teresa      3    Recife     3200\n",
       "1  Soares     35  Paulista     4500\n",
       "2    Jose     31    Olinda     5000"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona as 3 primeiras linhas\n",
    "dados.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f8fd2167",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.276260Z",
     "iopub.status.busy": "2025-10-21T02:12:38.275706Z",
     "iopub.status.idle": "2025-10-21T02:12:38.285212Z",
     "shell.execute_reply": "2025-10-21T02:12:38.284201Z"
    },
    "papermill": {
     "duration": 0.019609,
     "end_time": "2025-10-21T02:12:38.287076",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.267467",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Maria</td>\n",
       "      <td>40</td>\n",
       "      <td>Petrolina</td>\n",
       "      <td>6000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade     cidade  salario\n",
       "4   Maria     40  Petrolina     6000\n",
       "5  Teresa     56   Timbauba     7000"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona as 2 últimas linhas.\n",
    "dados.tail(2)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "05722d4d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-21T02:12:38.304118Z",
     "iopub.status.busy": "2025-10-21T02:12:38.303486Z",
     "iopub.status.idle": "2025-10-21T02:12:38.312781Z",
     "shell.execute_reply": "2025-10-21T02:12:38.311933Z"
    },
    "papermill": {
     "duration": 0.019723,
     "end_time": "2025-10-21T02:12:38.314553",
     "exception": false,
     "start_time": "2025-10-21T02:12:38.294830",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>salario</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>48</td>\n",
       "      <td>Caruaru</td>\n",
       "      <td>3700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>56</td>\n",
       "      <td>Timbauba</td>\n",
       "      <td>7000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     nome  idade    cidade  salario\n",
       "3  Carlos     48   Caruaru     3700\n",
       "5  Teresa     56  Timbauba     7000"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Seleciona 2 linhas aleatórias.\n",
    "dados.sample(2)  "
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 31153,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.11.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 8.972443,
   "end_time": "2025-10-21T02:12:38.842702",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-10-21T02:12:29.870259",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
