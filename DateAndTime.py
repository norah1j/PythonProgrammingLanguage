import time

timenow = time.localtime(time.time())
print("Current time :", timenow)

print("Year:", timenow[0])
print("Month:", timenow[1])
print("Day:", timenow[2])


timenow = time.asctime(time.localtime(time.time()))
print(timenow)
