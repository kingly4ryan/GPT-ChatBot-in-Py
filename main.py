import openai

# openai.api_key = "sk-proj-cFiI2I9jW8fcDSoULzpTT3BlbkFJBQbZe37mKj31Ula21bBL"

def chatWithGPT(prompt) :
    res = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )
    
    return res.choices[0].message.content.strip()

if __name__ == "__main__":
    while True :
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit", "bye"] :
            break
        
        res = chatWithGPT(userInput)
        print("ChatBot: ", res)