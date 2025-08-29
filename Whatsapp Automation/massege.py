import pywhatkit
what_np = "+923302358711"
massege = "Hello, This is a test message from Python script."
#pywhatkit.sendwhatmsg_instantly(what_np, massege, wait_time=10, tab_close=True, close_time=3)
# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg(what_np,massege, 5,5, 15, True, 2)