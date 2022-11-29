import pywhatkit


# Send Message to a whatsapp number
# --> sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None

pywhatkit.sendwhatmsg('+2347037761887', 'From: SoluTion PyBot....... I used python for it', 14, 52, 10)


# Send Message to a whatsapp group
# --> sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None

pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "hello everyone", 12, 12, 30, True, 5)

# Send Message to a whatsapp number instantly
# --> sendwhatmsg_instantly(phone_no: str, message: str, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None

pywhatkit.sendwhatmsg_instantly("+2347037761887", "I love you isaac from python", 4, True, 2)

# Send image alongside caption
# --> sendwhats_image(receiver: str, img_path: str, caption: str = "", wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None

pywhatkit.sendwhats_image("+2347037761887", "C:\\Image.png", "Here is the image caption", 10, True, 5)
