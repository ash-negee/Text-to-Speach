import pyttsx3

engine = pyttsx3.init()

# Set the voice ID or name provided by the third-party engine
voice_id = "vHKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

# Increase speech rate by 20%
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

text = input("Enter the text: ")

# Split the text into words
words = text.split()

grouped_words = []
current_group = []
for word in words:
    current_group.append(word)
    # Check if the combined character length of current group exceeds 10
    if len(' '.join(current_group)) >= 10:
        grouped_words.append(current_group)
        current_group = []

# Add any remaining words to the last group
if current_group:
    grouped_words.append(current_group)

# Read the grouped words
for group in grouped_words:
    engine.say(' '.join(group))
    engine.runAndWait()
    input("Press Enter to continue...")