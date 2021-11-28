# Multi
Федоров Александр
![image](https://user-images.githubusercontent.com/81014175/143781147-cfd3e9b3-065a-428c-b4fd-ed57d39cdd00.png) 
синхронная обработка ссылок заняла 831.1016318798065 секунд 
ансинхронная работа при 5 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782025-307defe8-6052-4411-be2d-2c4dbb362311.png) 
![image](https://user-images.githubusercontent.com/81014175/143782203-09597556-c6e2-4c93-8ee9-612817a1ef99.png) 
ансинхронная работа при 10 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782278-4c145414-d7ca-4473-8cab-250000c4a1c5.png) 
![image](https://user-images.githubusercontent.com/81014175/143782347-aa32686c-9b48-4c5a-b408-c3a3cba60e1f.png) 
ансинхронная работа при 100 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782366-a599685d-321e-4e69-b387-e92c40af7e20.png) 
![image](https://user-images.githubusercontent.com/81014175/143782429-1f83aca1-91dc-400a-b0f1-03e31db26bc6.png) 
Смотря на скрины обработки при разном количестве воркеров мы делаем вывод, чем больше воркеров тем быстрее обрабатываются ссылкки, но тем сильнее нагружается процессов, оперативная память и нагрузка на сеть растёт 
![image](https://user-images.githubusercontent.com/81014175/143782730-08b59b2b-f76c-4bc6-a156-3f2c181a69f4.png) 
CPU-bound. Генерируем монетки 
На одном ядре генерации монеты заняла 117 cекунд 
Время генерации монеты при использовании ProcessPoolExecutor при 2 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782873-107763fe-7f1c-44eb-be00-11566c8e30f1.png) 
![image](https://user-images.githubusercontent.com/81014175/143782880-e784e4f0-35ee-4a02-aefc-6b34993e5a70.png) 
Время генерации монеты при использовании ProcessPoolExecutor при 4 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782890-162eb84c-c4ea-4356-aea1-194fa66a2b4d.png) 
![image](https://user-images.githubusercontent.com/81014175/143782935-365498bf-332c-4f7b-abb1-d027e475e34b.png) 
Время генерации монеты при использовании ProcessPoolExecutor при 5 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782952-098b9b27-2612-4298-b5d9-bb60c0de1b7d.png) 
![image](https://user-images.githubusercontent.com/81014175/143782973-07fd6e41-fbf4-4df4-91b7-39a4a3ae02c2.png) 
Время генерации монеты при использовании ProcessPoolExecutor при 10 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143782982-f35bdfd8-9b46-440c-b61d-ee53c1819312.png) 
![image](https://user-images.githubusercontent.com/81014175/143783010-ef78be9a-dc1a-4fb2-86be-04915e5bb18d.png) 
Время генерации монеты при использовании ProcessPoolExecutor при 100 воркерах 
![image](https://user-images.githubusercontent.com/81014175/143783031-efb8b165-e2d8-4eeb-9848-d431d7981639.png) 
![image](https://user-images.githubusercontent.com/81014175/143783041-40481084-fba6-40aa-a452-cda2e0ce3d4a.png) 
При использовании ProcessPoolExecutor основываясь на скринах, можно увидеть что время генерации одного токена никак не зависит от количества воркеров, а также не увеличивается нагрузка на процессор, оперативную память и на сеть 
