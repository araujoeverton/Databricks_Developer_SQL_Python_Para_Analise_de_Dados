{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "9e60a032-f3e1-46a9-9c0c-16aa5eb2f656",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Renomeando Colunas withColumnRenamed e Alias"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "f61d2091-3659-4fb8-ad8b-5c9d23c88e1c",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "# sintaxe\n",
    "df = df.withColumnRenamed(\"coluna_antiga\", \"coluna_nova\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "41da6975-966d-4c08-8cc7-52fbd0feb1f1",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df = spark.read.json(\"dbfs:/FileStore/tables/Anac/V_OCORRENCIA_AMPLA.json\")\n",
    "display(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2eb8dfa6-37dd-44ad-ae74-362857632ebe",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c840efb3-a775-4ab7-8ac7-466bcdf1d2c3",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "renomeado = df.withColumnRenamed('Aerodromo_de_Destino', 'Destino') \\\n",
    "    .withColumnRenamed('Aerodromo_de_Origem', 'Origem') \\\n",
    "    .withColumnRenamed('Danos_a_Aeronave', 'Danos')\\\n",
    "    .withColumnRenamed('UF', 'Estado')\n",
    "    \n",
    "\n",
    "display(renomeado)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "50f0fae8-9cf9-458a-a6e1-b9af3381c295",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "print(renomeado.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3d3500d4-2184-4d86-b0fe-431d192b9777",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "445ee36b-a9db-4266-9f14-62876f343707",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#selecionando apenas algumas colunas e ja renomeando com .alias\n",
    "\n",
    "Teste = df.select(df.Aerodromo_de_Destino.alias('Destino'),\n",
    "                  df.Nome_do_Fabricante,\n",
    "                  df.Aerodromo_de_Origem.alias('Origem'),\n",
    "                  df.UF.alias('Estado'),\n",
    "                  df.Numero_da_Ocorrencia,\n",
    "                  df.Matricula.alias(\"Registro\")\n",
    "\n",
    "\n",
    "        )\n",
    "display(Teste)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "bdf6fc05-9b1c-4621-9b17-e70d86f5076b",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Conversão de Dados método cast + withColumn "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "a727bd77-42d2-45bc-bc42-e061c5c5a537",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Resumo\n",
    "#A função cast no PySpark aceita vários tipos de dados para a conversão\n",
    "\"\"\"\n",
    "string ou varchar: Texto.\n",
    "integer ou int:    Numero inteiro.\n",
    "long:              Numero inteiro longo.\n",
    "double:            precisão dupla.\n",
    "float:             precisão simples.\n",
    "decimal:           decimal.\n",
    "timestamp:         Data e hora.\n",
    "date:              Somente a Data.\n",
    "boolean:           booleana (True e False) 0=False e 1=True.\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8d9e46c3-9dca-48ac-9464-72d7b3c943f3",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Curiosidades\n",
    "\"\"\"\n",
    "Qual diferença entre esses que trazem numeros decimais no geral\n",
    "double:            precisão dupla.\n",
    "float:             precisão simples.\n",
    "decimal:           decimal.\n",
    "\n",
    "----- numeros com longas casas decimais \n",
    "float (Precisão Simples 32 bits na memória):\n",
    "Mínimo: 1.40129846432 x 10^-45\n",
    "Máximo: 3.40282346639 x 10^38\n",
    "\n",
    "double (Precisão Dupla 64 bits na memória):\n",
    "Mínimo: 4.94065645841 x 10^-324\n",
    "Máximo: 1.79769313486 x 10^308\n",
    "\n",
    "decimal : pode escolher quantas casas decimais aparece no resultado \n",
    "O decimal usa uma representação decimal, o que permite maior precisão e evita muitos dos problemas de arredondamento associados ao float\n",
    "\n",
    "Decimal ou Float são mais ultilizados\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "db1c7339-315f-4029-b1fd-377d7ee73f95",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Carga Df sem .option(\"inferSchema\", \"true\") sendo assim virá tudo como string, vamor ver na prática \n",
    "orders_df       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "4099fbba-dd35-464d-8bed-b251398171ff",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b1377db0-dfea-4ddd-964a-205830ade6e8",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Converter Dados com withColumn\n",
    "orders_df = orders_df.withColumn('order_id',orders_df.order_id.cast('int') ) \n",
    "orders_df = orders_df.withColumn('customer_id',orders_df.customer_id.cast('integer') ) \n",
    "orders_df = orders_df.withColumn('order_date',orders_df.order_date.cast('date'))\n",
    "orders_df = orders_df.withColumn('required_date',orders_df.required_date.cast('date'))\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2754b9bd-2b56-4f9d-865a-8b2ac11079fd",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Converter Dados com .Select  \n",
    "orders_df2       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b8bd50c1-be5b-4b66-a814-760508c0e3eb",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#.Select (Converte e ja seleciona as colunas , pode renomear com Alias tambem)\n",
    "Conversao = orders_df2.select(\n",
    "    orders_df2.order_id.cast(\"integer\"),\n",
    "    orders_df2.order_date.cast(\"date\"),\n",
    "    orders_df2.store_id.cast(\"int\"),\n",
    "    orders_df2.staff_id.cast(\"int\").alias(\"IdLoja\"),\n",
    "    orders_df2.order_status.cast(\"int\").alias(\"Status_Entrega\"),\n",
    ")\n",
    "display(Conversao)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8972fe3e-aa3e-46dc-a340-9e70847f5d14",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Conversões númericas Avançadas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "43fffe3e-7989-4e8a-b16a-252074b099cc",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "\n",
    "Items = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .option(\"inferSchema\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/order_items.csv\")\n",
    "display(Items)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "73d452c5-08e5-4165-ba84-079eb693b65e",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "print(Items.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "f7c3dbef-60d1-4133-ab2a-22cc3070972d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#formato double\n",
    "fracionado = Items.withColumn('Fracao',Items.list_price/2.03)\n",
    "display(fracionado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "5ff513da-fe4b-46e7-99ea-11496310e399",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Criando novas colunas ja convertidas \n",
    "fracionado2 = fracionado\\\n",
    "    .withColumn('double' ,fracionado.Fracao)\\\n",
    "    .withColumn('Int'    ,fracionado.Fracao.cast('integer') )\\\n",
    "    .withColumn('Float'  ,fracionado.Fracao.cast('float') )\\\n",
    "    .withColumn('Decimal',fracionado.Fracao.cast('decimal(10,2)'))\n",
    "display(fracionado2)\n",
    "\n",
    "\n",
    "\"\"\"\n",
    "Obs : 'decimal(10,2)'  \n",
    "o valor decimal terá um máximo de 10 dígitos no total (incluindo os dígitos à esquerda e à direita do ponto decimal) e 2 dígitos à direita do ponto decimal.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "bb1209aa-ef0e-4038-814a-deb6f003f94c",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Substituindo o duble por decimal no Df\n",
    "display(fracionado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "08033aa3-279a-4c37-a6db-741588222dcc",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "\n",
    "SubDouble =  fracionado.withColumn('Fracao',fracionado.Fracao.cast('decimal(10,2)'))\n",
    "display(SubDouble)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "ccbe7d1a-f9fd-4433-a26b-548257142511",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Arredondamento de Numeros"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "a5894994-f8c4-4f09-b938-c868c7969da3",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(fracionado2) # Rodar ate gerar o DF fracionado2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "9423369a-f673-4af3-9a25-7be7373987e0",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Aproveitar  script fracionado2 para Treinar \n",
    "\"\"\"\n",
    "floor (arredondamento para baixo)\n",
    "ceil  (arredondamento para cima)\n",
    "round (arredondamento Automatico)\n",
    "\"\"\"\n",
    "\n",
    "from pyspark.sql.functions import floor, ceil , round\n",
    "Arred = fracionado2\\\n",
    "    .withColumn('ArredAcima', ceil(fracionado2.double))\\\n",
    "    .withColumn('ArredAbaixo',floor(fracionado2.double))\\\n",
    "    .withColumn('ArredAutomatico',round(fracionado2.double))\n",
    "display(Arred)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d813e42a-bbc8-451b-a55e-a6ec62126a51",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Trabalhando com Datas\n",
    "https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html\n",
    "\n",
    "https://spark.apache.org/docs/latest/sql-ref-datatypes.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "45b21aa2-c700-47ba-a107-b3695721c9d7",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .option(\"inferSchema\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "9e7e0089-3f85-45f5-a62b-b8f8d48ccf19",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "a8273895-6ff6-4433-a3ca-317b266acf86",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Extraindo uma fração de uma data em novas Colunas\n",
    "from pyspark.sql.functions import year, month, dayofmonth\n",
    "\n",
    "orders_df = orders_df\\\n",
    "                     .withColumn(\"ano_pedido\", year(\"order_date\")) \\\n",
    "                     .withColumn(\"mes_pedido\", month(\"order_date\")) \\\n",
    "                     .withColumn(\"dia_pedido\", dayofmonth(\"order_date\")) \n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ccf17bec-4a07-4ff3-b9fb-f9872826d07e",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#usando a classe datetime\n",
    "from pyspark.sql.functions import expr\n",
    "from datetime import datetime\n",
    "orders_df2 = orders_df\\\n",
    "                     .withColumn(\"ano_pedido\", expr(\"year(order_date)\")) \\\n",
    "                     .withColumn(\"mes_pedido\", expr(\"month(order_date)\")) \\\n",
    "                     .withColumn(\"dia_pedido\", expr(\"day(order_date)\"))\n",
    "display(orders_df2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b474efb0-9677-4e3f-be96-f77a1ce0875f",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Simulando mater registro de quando os dados foram carregados (Muito comum no dia a dia para rastreio se os dados foram atualizados ou nao )\n",
    "\n",
    "from pyspark.sql.functions import current_date,current_timestamp ,expr\n",
    "\n",
    "orders_df = orders_df \\\n",
    "    .withColumn(\"data_atual\", current_date()) \\\n",
    "    .withColumn(\"data_hora_atual\", current_timestamp()) \\\n",
    "    .withColumn(\"data_hora_br\", expr(\"from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')\"))\n",
    "\n",
    "display(orders_df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e9f973f4-3e0b-45b3-9797-97a278d09eac",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#formato brasil -3h\n",
    "#   .withColumn(\"data_hora_br\", expr(\"from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')\"))\n",
    "from pyspark.sql.functions import current_date,current_timestamp ,expr\n",
    "\n",
    "orders_df = orders_df \\\n",
    "    .withColumn(\"data_atual\", current_date()) \\\n",
    "    .withColumn(\"data_hora_atual\", current_timestamp()) \\\n",
    "    .withColumn(\"data_hora_br\", expr(\"from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')\"))\n",
    "\n",
    "display(orders_df)\n",
    "\n",
    "\"\"\"\n",
    "referencias \n",
    "https://docs.databricks.com/en/sql/language-manual/functions/from_utc_timestamp.html\n",
    "https://spark.apache.org/docs/3.1.2/api/python/reference/api/pyspark.sql.functions.from_utc_timestamp.html\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "32b0a3ae-cbcc-4a5c-ae88-4b29bec004ad",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Extraindo horas minutos e Segundos \n",
    "from pyspark.sql.functions import year, month, dayofmonth, hour, minute, second\n",
    "orders_df = orders_df\\\n",
    "                     .withColumn(\"hora_carga\", hour(\"data_hora_br\")) \\\n",
    "                     .withColumn(\"minuto_carga\", minute(\"data_hora_br\")) \\\n",
    "                     .withColumn(\"segundo_carga\", second(\"data_hora_br\"))\n",
    "\n",
    "display(orders_df)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c135995a-1919-401c-9075-06c96a3a14cc",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "313425ad-d28d-4c0a-80cd-43462fb64a7d",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### Comandos e Formatos de Datas avançado \n",
    "https://docs.databricks.com/en/sql/language-manual/functions/cast.html\n",
    "\n",
    "https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3135763c-54ec-4de7-b014-de70667479c8",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .option(\"inferSchema\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c40f6696-ed20-46e6-a10a-d7f9897a160f",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Formato PT-Br\n",
    "\n",
    "from pyspark.sql.functions import  date_format\n",
    "orders_df = orders_df.withColumn(\"data_formatada\", date_format(orders_df.order_date, \"dd/MM/yyyy\"))\n",
    "display(orders_df)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "6ebd0a0b-a39e-4d51-b882-82cbf56cd3b5",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Exemplos outros formatos\n",
    "from pyspark.sql.functions import date_format \n",
    "\n",
    "orders_df = orders_df\\\n",
    "        .withColumn(\"Exemplo1\", date_format(orders_df.order_date,\"yyyy MM dd\"))\\\n",
    "        .withColumn(\"Exemplo2\", date_format(orders_df.order_date,\"MM/dd/yyyy HH:mm\"))\\\n",
    "        .withColumn(\"Exemplo3\", date_format(orders_df.order_date,\"MM-yyyy\"))\\\n",
    "        .withColumn(\"Exemplo4\", date_format(orders_df.order_date,\"yyyy MMM dd\"))\\\n",
    "        .withColumn(\"Exemplo5\", date_format(orders_df.order_date,\"yyyy MMMM dd E\"))\\\n",
    "        .withColumn(\"Exemplo6\", date_format(orders_df.order_date,\"MMM\"))\\\n",
    "        .withColumn(\"Exemplo7\", date_format(orders_df.order_date,\"MMM-yyyy\"))   \n",
    "\n",
    "display(orders_df)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "4ca8f0cc-e097-49b6-80f9-8927b3c3345f",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### Traduçoes para portugues\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b6dc4961-389b-43c7-8139-2c451d03d796",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#conversao para portugues método when \n",
    "from pyspark.sql.functions import when\n",
    "orders_df2 = orders_df.withColumn(\"Exemplo6\",\n",
    "                                    when(orders_df.Exemplo6 ==\"Jan\",\"Jan\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Feb\",\"Fev\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Mar\",\"Mar\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Apr\",\"Abr\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"May\",\"Mai\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Jun\",\"Jun\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Jul\",\"Jul\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Aug\",\"Ago\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Sep\",\"Set\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Oct\",\"Out\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Nov\",\"Nov\")\n",
    "                                   .when(orders_df.Exemplo6 ==\"Dec\",\"Dez\")\n",
    "                                   .otherwise(orders_df.Exemplo6))\n",
    "\n",
    "display(orders_df2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "94a5b17a-d7d4-4df0-b90c-63b9253a7d84",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Colinha marota\n",
    "\"\"\"\n",
    "MMM >mes abrev \n",
    "\"Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec\",\n",
    "\"Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez\"\n",
    "\n",
    "MMMM > mes completo\n",
    "\"January February March April May June July August September October November December\",\n",
    "\"Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro\"\n",
    "\n",
    "\n",
    "E > dia da semana \n",
    "\"Sun Mon Tue Wed Thu Fri Sat\", \n",
    "\"Dom Seg Ter Qua Qui Sex Sáb\"\n",
    "\n",
    "EEEE > dia da semana completo\n",
    "\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\", \n",
    "\"Domingo Segunda-feira Terça-feira Quarta-feira Quinta-feira Sexta-feira Sábado\"\n",
    "\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "230c767d-e12a-4377-acbd-3321bab5e592",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Diferença entre Datas Adição e Subtração"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "43a3a404-028b-48fc-b8cb-4c78ece130d7",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .option(\"inferSchema\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "1c5f8dc4-45e5-40a5-a11f-b12c721b81e0",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import datediff, months_between, year\n",
    "\n",
    "\n",
    "orders_df = orders_df.withColumn(\"diferenca_dias\", datediff(\"required_date\", \"order_date\")) \\\n",
    "                     .withColumn(\"diferenca_meses\", months_between(\"required_date\", \"order_date\")) \\\n",
    "                     .withColumn(\"diferenca_anos\", year(\"required_date\") - year(\"order_date\"))\n",
    "\n",
    "display(orders_df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2cc4892e-ada0-43dc-8ff7-5a54699693be",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Simulando diferença de alguma coluna de data com a data Atual \n",
    "from pyspark.sql.functions import datediff, months_between, year ,current_date\n",
    "\n",
    "orders_df = orders_df.withColumn(\"diferenca_dias\", datediff( current_date(),\"required_date\",)) \\\n",
    "                     .withColumn(\"diferenca_meses\", months_between(current_date(),\"required_date\")) \\\n",
    "                     .withColumn(\"diferenca_anos\", year(current_date()) -  year(\"required_date\"))\n",
    "\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "f70b8486-aeb3-4e7d-bac3-2acfef2e5971",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### Adicionar intervalos em Datas\n",
    "\n",
    "https://docs.databricks.com/en/sql/language-manual/functions/cast.html\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "59372279-bb07-4d10-8f15-abb647e05c11",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .option(\"inferSchema\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "7a7c8727-d15e-43f9-9f4c-216c1959b7e8",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import expr\n",
    "\n",
    "# Adicionar coluna 'previsao_entrega' com 5 dias adicionados à 'order_date'\n",
    "# Adicionar coluna 'pagamento' com 1 mês adicionado à 'order_date'\n",
    "# Adicionar coluna 'devolucao' com 1 Ano adicionado à 'order_date'\n",
    "\n",
    "orders_df = orders_df\\\n",
    "                     .withColumn(\"previsao_entrega\", expr(\"order_date + interval 5 days\"))\\\n",
    "                     .withColumn(\"pagamento\", expr(\"order_date + interval 1 month\"))\\\n",
    "                     .withColumn(\"max_devolucao\", expr(\"order_date + interval 1 year\"))\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "4195cc6d-6acf-492f-930c-0f0e410ed697",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#simulação rápida tirando intervalos\n",
    "orders_df = orders_df\\\n",
    "                     .withColumn(\"previsao_entrega\", expr(\"order_date - interval 5 days\"))\\\n",
    "                     .withColumn(\"pagamento\", expr(\"order_date - interval 1 month\"))\\\n",
    "                     .withColumn(\"max_devolucao\", expr(\"order_date - interval 1 year\"))\n",
    "display(orders_df)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d709c480-c568-47c1-84ac-91b0c36adb5e",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### Datas em SQL\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "6728aa4f-8e6d-425f-8657-373767269ee5",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df       = spark.read.\\\n",
    "    format(\"csv\")\\\n",
    "    .option(\"header\", \"true\")\\\n",
    "    .option(\"inferSchema\", \"true\")\\\n",
    "    .load(\"/FileStore/tables/Bikes/orders.csv\")\n",
    "display(orders_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "225006c9-7f1e-4137-bf0d-b782c181e216",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders_df.createOrReplaceTempView(\"tabela_ordens\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "4b92b94f-6211-4b64-bd45-d76d06d8c0c2",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "select * from tabela_ordens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d7e16719-d876-4369-bec2-7cb79c0a341b",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "-- extraindo partes de uma data \n",
    "SELECT *,\n",
    "       YEAR(order_date) AS Ano,\n",
    "       MONTH(order_date) AS Mes,\n",
    "       DAY(order_date) AS Dia\n",
    "      FROM tabela_ordens\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "4161d631-88a2-4e16-8f16-6a1b7456c022",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "-- para treinar   \n",
    "-- traduções: now ou  current_timestamp  = carimbo de data/hora atual\n",
    "-- muito usado para ter coluna ou colunas de quando os daos foram carregados para base, arquivos banco de dados etc\n",
    "--  converter fuso horário from_utc_timestamp\n",
    "\n",
    "select * ,\n",
    "now() as agora,\n",
    "current_timestamp() AS agora2,\n",
    "from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo') AS agora_PTBR,\n",
    "date_format(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo'), 'yyyy-MM-dd HH:mm:ss') AS agora_formatado,\n",
    "date_format(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo'), 'dd/MM/yyyy') AS agora_formatado_brasil,\n",
    "date_format(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo'), 'dd/MM/yyyy HH:mm:ss') AS agora_formatado_brasil_Completo,\n",
    "year(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')) as ano,\n",
    "month(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')) as mes,\n",
    "day(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')) as dia,\n",
    "hour(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')) as hora,\n",
    "minute(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')) as minuto,\n",
    "second(from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo')) as segundo\n",
    "from tabela_ordens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "66cfdd41-2c05-4818-a1be-001cdff8e8d6",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "-- dados maior que certa data \n",
    " SELECT * FROM tabela_ordens WHERE order_date >= '2016-01-01' -- Obs o padrao é ano-mes-dia\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "e41f9cb6-014f-4b4e-95e9-3fb17861df38",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "-- quantos anos tenho de registro na base?\n",
    " SELECT distinct \n",
    " year(order_date) \n",
    " FROM tabela_ordens "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "10e995fa-4cdb-41e5-abe3-ab5e06459072",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "--Dados entre 2017  e 2018\n",
    "SELECT * FROM tabela_ordens\n",
    " WHERE year(order_date) BETWEEN 2017 and 2018"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2f026850-7a05-4cb3-a165-cd8074627a6f",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "--Dados entre datas espesificas \n",
    "SELECT * FROM tabela_ordens\n",
    "WHERE order_date BETWEEN '2017-01-04' and '2018-01-01' \n",
    " -- Obs o padrao é ano-mes-dia "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "867bcc54-0f79-415a-a5e3-f164054d2f2e",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "select * ,\n",
    "date_format(order_date, 'yyyy-MM-dd HH:mm:ss') AS ptbr,\n",
    "date_format(order_date, 'dd/MM/yyyy') AS dataformatada,\n",
    "date_format(order_date, 'dd/MM/yyyy HH:mm:ss') AS datahora\n",
    "\n",
    "from tabela_ordens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "0de0d93e-6fc5-48ef-a48e-0b392550ec2c",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Salvar consulta em um Df para trabalhar com Python ou salvar como qualqer tipo de arquivo \n",
    "\n",
    "resultado = spark.sql(\n",
    "    \n",
    "\"\"\"\n",
    "select * ,\n",
    "date_format(order_date, 'yyyy-MM-dd HH:mm:ss') AS ptbr,\n",
    "date_format(order_date, 'dd/MM/yyyy') AS dataformatada,\n",
    "date_format(order_date, 'dd/MM/yyyy HH:mm:ss') AS datahora\n",
    "\n",
    "from tabela_ordens                \n",
    "\n",
    "\n",
    "\n",
    "\"\"\")\n",
    "\n",
    "\n",
    "display(resultado)\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "dashboards": [],
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 1001953215070996,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "12. Conversão de Dados",
   "widgets": {}
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
