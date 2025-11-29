import google.generativeai as genai
genai.configure(api_key="YOUR API KEY")   
model = genai.GenerativeModel("gemini-2.5-flash")
def chat_with_gemini():
    print("Chat with Gemini 2.5 Flash! Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break


        response = model.generate_content(user_input)


        print("Gemini:", response.text)
        print()


chat_with_gemini()
