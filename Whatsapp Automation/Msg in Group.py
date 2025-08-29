import pywhatkit
group_id = "E9HUUeote6J2SDkqVCxRYA" # Replace with your actual group ID
massege = "Hello, This is a test message from Python script."
#pywhatkit.sendwhatmsg_to_group(group_id, massege, 6, 2, 15, True, 2)
#pywhatkit.sendwhats_image(group_id, "img.png", "Hello")


# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly(group_id, "Hey All!")