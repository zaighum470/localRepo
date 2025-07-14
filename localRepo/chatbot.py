import pyautogui
import pyperclip
import time
import openai as OpenAI

time.sleep(3)

client = OpenAI(
  api_key="<Your Key Here>",
)

# Step 1: Click at (448, 1029)
pyautogui.click(695, 1044)
time.sleep(1)

# Step 2: Click and drag from (914, 494) to (1122, 915)
pyautogui.moveTo(966, 504)
pyautogui.mouseDown()
pyautogui.moveTo(1970, 897, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Press Ctrl+C to copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
pyautogui.click(921,585)
"""copied_text =pyperclip.paste()
print(copied_text)"""





def is_last_message_from_sender(chat_log, sender_name="jazz"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)

    copied_text = pyperclip.paste()

    # Print the copied text to verify
    print(copied_text)
    print(is_last_message_from_sender(copied_text))
    if is_last_message_from_sender(copied_text):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named zaighum who speaks hindi as well as english. You are from pakistan and you are a coder. You analyze chat messages and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] : "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')