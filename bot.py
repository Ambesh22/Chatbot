# 655 247 to 1857 917 - Insta
# 738 278 to 1818 902
# 734 233 to 1859 916 - Whatsapp
import pyautogui
import time
import pyperclip
from openai import OpenAI
client = OpenAI(
    api_key = API KEY
)

def is_last_message_from_sender(chat_text , sender_name ="Harsh Gupta (JDC)"):
    message = chat_text.strip().split("/2025] ")[-1]
    if sender_name in message:
        return True
    return False

# Step 1: Click the icon at (1053, 1045)
pyautogui.moveTo(1434, 1052, duration=0.5)
pyautogui.click()

# Step 2: Wait for the app to open or UI to be ready
time.sleep(2)

while True:
    # Start drag with mouse down
    pyautogui.moveTo(734 ,233)
    time.sleep(2)

        # Drag to new location
    pyautogui.dragTo(1854, 933, duration=1,button="left")

        # Release mouse to finish selection
    time.sleep(1)


        # Step 4: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) # Allow clipboard to update
    pyautogui.click(1856, 935)

        # Step 5: Get text from clipboard
    copied_text = pyperclip.paste()

        # Step 6: Print or use the variable
    print("Copied text:")
    print(copied_text)

    print(is_last_message_from_sender(copied_text))
    if is_last_message_from_sender(copied_text):
        completion = client.chat.completions.create(
        model="gpt-4.1",
        messages = [
                {"role":"system" , "content":"you are a person named Ambesh M. who speaks in hindi as well as english. you are from india and you are a analyst. you analyse the chat history and respond like Ambesh M. Output should be the next chat response (text message only)"},
                {"role":"user" , "content":copied_text}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        #step 7: click at cordinates
        pyautogui.click(1245 , 966)
        time.sleep(1)

        #step8: paste the key
        pyautogui.hotkey('ctrl' , 'v')
        time.sleep(1)

        #step9: press enter
        pyautogui.hotkey('enter')