# Jornada Python - Hashtag Treinamentos

Projetos desenvolvidos no evento Jornada Python da Hashtag Programação, nele desenvolvi conhecimentos em automação de tarefas, análise/visualização de dados e machine learning preditivo.
Adicionei comentários detalhados em cada linha do código para fixar bem os conceitos e facilitar revisões futuras.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

⚠️ DADOS UTILIZADOS
Todos os dados são fictícios, disponibilizados pelo evento para estudo e prática.

## Projetos

### Automação de Cadastro
O projeto automatiza o cadastro manual de produtos em sistema web lendo planilha Excel.  
Utilizei pandas para ler e manipular a planilha de dados, pyautogui para simular cliques e digitação no navegador, e time para pausas humanizadas entre ações.  

### Análise de Cancelamentos (Churn)
O projeto analisa padrões de cancelamento em base de 800k clientes, identificando motivos principais para reduzir inativos.  
pandas manipula e limpa os dados, plotly.express cria gráficos interativos e dashboards para insights visuais.  

### Score de Crédito (ML)
O projeto cria modelo preditivo para classificar score de crédito (Ruim/Ok/Bom) de clientes bancários.  
pandas prepara dados, sklearn com LabelEncoder, train_test_split, RandomForestClassifier, KNeighborsClassifier e accuracy_score treinam e avaliam o modelo.  
