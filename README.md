# Nutrition_Fact_App 
( # python - tkinter, pandas, openpyxl, pyinstaller )

Build your own  nutrition fact database and calculate the nutrition value of your own recipe.

ps. It was a little tool that I make for my friend and also my ex-collegue Lulu to speed up her work as a functional food formula R&D. This explains why there are greetings in my apps, because it's a gift. ^___^

●I use tkinter to build the UI.

1.UI - Build Database 

![Database](https://user-images.githubusercontent.com/69572417/126296579-735ba5b8-5af0-4b22-a1a9-15d77641be4b.PNG)

2.UI - Do Calculations UI

![Calculator](https://user-images.githubusercontent.com/69572417/126296863-427830fc-32dc-456f-99e4-92369386af34.PNG)

3.Output file .xslx 

![Output](https://user-images.githubusercontent.com/69572417/126304959-de4fe968-c3f8-46a2-88a6-f6778504e817.PNG)

●Then I rearrange the file structure and use Pyinstaller to pack the apps.

pyinstaller -i img.ico  [-w] ./Database.py
pyinstaller -i img.ico  [-w] ./Calculator.py

ps.I decided to keep the log window for inspecting the process and error.

![file](https://user-images.githubusercontent.com/69572417/126459719-5b0544a3-352f-4aac-b51e-17496b10461a.PNG)
