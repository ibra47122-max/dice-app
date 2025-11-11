1. Comando buid: docker build -t dice-app .
2. Comando build sin env: docker run -p 8888:5000 dice-app 
3. Comando build con env: docker run -p 8888:5000 -e DICE_SIDES=20 dice-app

![Captura sin env](dice-roller.png)
![Captura con env](dice-roller-env.png)
