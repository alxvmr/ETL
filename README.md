# ETL

CSV файлы хранятся в:
- ETL\dagster\domain-project\domain_project\data
- ETL\prefect\data\original

___

Запуск окружения:
1. poetry install
2. poetry shell

___

Добавление глобальной переменной **pipelines** (для задания Prefect)
1. Перейти в папку ETL\prefect
2. Выполнить команду (в запущпенном окружении) **pip install .**

___

Для задания с prefect запустить команду:

piplines --data_path <путь к входному csv> --output_path <путь к выходному csv>

ПРИМЕР: piplines --data_path "C:\Users\alexe\Desktop\prefect_dagster\ETL\prefect\data\original\original.csv" --output_path "C:\Users\alexe\Desktop\prefect_dagster\ETL\prefect\data\original\original4.csv"

Для задания с Dagster:
1. Перейти в папку dagster -> domain-project
2. Вызвать команду dagit
3. Перейти в UI (http://127.0.0.1:3000)
4. Нажать на Materialize all на вкладке Deployment
5. Прописать в конфигурации пути к входному и выходному файлам
ПРИМЕР:
{'ops': {'load': {'config': {'DATA_PATH': 'C:\Users\alexe\Desktop\prefect_dagster\ETL\dagster\domain-project\domain_project\data\original.csv'}}, 'save': {'config': {'SAVE_PATH': 'C:\Users\alexe\Desktop\prefect_dagster\ETL\dagster\domain-project\domain_project\data\originalDag2.csv'}}}}
6. Материализуем

___

## Примеры работы
1. Prefect
<img src="https://sun9-east.userapi.com/sun9-43/s/v1/ig2/x7dyHIzwAphw1WEtvYuFfPWPdZwTMq2NRI1iXGEeG63lXHrEZPe-lVpKnrqQoLZPEuf9rRkz4CpCM4fTRlbLRLg9.jpg?size=1553x462&quality=96&type=album" height=200>

2. Dagster
<img src="https://sun9-west.userapi.com/sun9-4/s/v1/ig2/xDUHkDMbpst18KcR4genKHgfcod4UXZau7j3zK0E9_7i0lI3OXCcbD8-cZEj49Myt1q-hQgyeHVMYh8guEPyIeg5.jpg?size=634x218&quality=96&type=album" height=100>

<img src="https://sun9-west.userapi.com/sun9-6/s/v1/ig2/i8koDt_MDpI6GhsxTU2fv9AIkFYBxduD_hKDCQ5E_fta7QB3LlQI9i2FZoaWYCz7xejgu5s_fPPuFiJmw84RpBKE.jpg?size=618x766&quality=96&type=album" height=200>

<img src="https://sun9-west.userapi.com/sun9-54/s/v1/ig2/w47stpMBK-H1YfrzjSxz8pbRrHnX_Ya350DbEOtmi3St7mvns-bu9kuugZ-k8m42CV6vcm8be2d3LEtK-3Qy7orp.jpg?size=1889x145&quality=96&type=album" height=100>
