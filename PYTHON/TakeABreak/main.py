import time
import webbrowser as wb


print("Started:",time.ctime())
while True:
    for i in range(3):
        wb.open('https://www.youtube.com/watch?v=Rsn9VnoeNrs&list=PLD9E0B6A354DE4E4D')
        time.sleep(10)
    break
