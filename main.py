from openai import OpenAI
import os
import json

# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))

# Knowledge base for AI Learning.

KNOWLEDGE_BASE ="""
IYF We Can Academy student knowledge base

Artificial Intelligence(AI):

Artificial Intelligence (AI) it is anything that mimic human intelligence by automating human task.


SCHOOL PROGRAM INFORMATION:

1.Classes run only on Saturdays and Sundays.
2.We have two classes per day for this course.
        -10:00 AM to 12:00 PM
        -2:00 PM to 4:00 PM.
3.Class duration is 2 hours per session.
4.The class room is found in the MIB main building, second floor room 205.
5.You teachers name is Mr. Daniel Chacha but you can call him Chacha. He is a very friendly and approachable teacher.
6.You can reach him through his email: daniel.chacha@we-can-academy.org or personal cell: +254 796 280 700.
7.Chapel classes are held on saturdays only from 08:00 AM to 10:00 AM.
8.The chapel is located on the first floor, conference room where by it is mandatory for all students and is part of the curriculum.
9.For this course a students should have:
        -a book.
        - pen.
        - a laptop.
10.Chapel class duration is 2 hours per session.
11.Each student must attend four chaplain consultation sessions during the three-month program, attendance will be recorded by scanning of the passport.
12.For enrollment a registration/commitment fee of Kes. 1000 is required, whis includes a class passport booklet.


"""
def save_output(result):
    """Save the AI response to output.txt."""

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(result)

    print("\nsuccessfully saved")

#ASK THE AI A QUESTION

def ask_question():
    """Student asks a question."""

    question = input("\nStudent:").strip()

    if not question:
        print("\nquestion.")

        return

    if question.lower() =="exit":
        return "exit"

    prompt = f"""

You are the IYF We Can Academy Student Support Bot.


Your job is to help students using ONLY the knowledge base provided below.


KNOWLEDGE BASE:
{KNOWLEDGE_BASE}

STUDENT QUESTION:
{question}

Rules:

- Do NOT add explanation beyound the KNOWLEDGE_BASE
- If the answer is not explicitly found in the KNOWLEDGE_BASE respond exactly with:"Not information about this"


"""

    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt
        )

        result = response.output_text

        print("\n===== ANSWER =====")
        print(result)

        save_output(result)

        return result

    except Exception as error:
        print("\nAn error occurred while contacting OpenAI.")
        print(error)
        return None


#ARTIFICIAL INTELLIGENCE EXPLANATION

def artificial_intelligence_json():
    """Explain AI and return the response in JSON format."""

    prompt = f"""
You are an AI learning tutor at IYF We Can Academy.

Use the following knowledge base:

{KNOWLEDGE_BASE}

Using ONLY the exact information from the knowledge base:

Return ONLY valid JSON using exactly these two fields:

{{
    "topic": "...",
    "definition": "...",

}}

Requirements:

- Topic must be "Artificial Intelligence (AI)"
- Definition must be simple and beginner-friendly
- Use information consistent with the knowledge base
- Do not include Markdown
- Do not include explanations outside the JSON
- Do not add examples

"""

    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt
        )

        result = response.output_text

        # Parse JSON
        data = json.loads(result)

        print("\n===== ARTIFICIAL INTELLIGENCE =====")

        print("\nTopic:")
        print(data["topic"])

        print("\nDefinition:")
        print(data["definition"])

    
        # Save formatted JSON
        save_output(json.dumps(data, indent=3))

    except json.JSONDecodeError:
        print("\nThe AI returned an invalid JSON response.")
        print("Raw response:")
        print(result)

    except Exception as error:
        print("\nAn error occurred while explaining AI.")
        print(error)

        print("\n===== IYF WE CAN ACADEMY INFORMATION =====")

        print("\nClass Days:")
        print("Saturday and Sunday")

        print("\nClass Times:")
        print("10:00 AM - 12:00 PM")
        print("2:00 PM - 4:00 PM")

        print("\nClassroom:")
        print("Main Building, Second Floor, Room 205")

        print("\nTeacher:")
        print("Mr. Daniel Chacha (Chacha)")

        print("\nChapel:")
        print("Saturday, 8:00 AM - 10:00 AM")
        print("First Floor, Conference Room")

        print("\nEnrollment Fee:")
        print("KES 1,000")

        print("\nRequired Equipment:")
        print("Book, pen, and laptop")


#MAIN MENU

def main():

       print("==========================================")
       print("       IYF EXPOUNDER STUDENT BOT")
       print("==========================================")

       print("\nWelcome to the IYF We Can Academy Support Bot!")

       while True:

        print("\n===== MENU =====")
        print("1. What is Artificial Intelligence (AI)?")
        print("2. Ask a Student Support Question")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            artificial_intelligence_json()

        elif choice == "2":

            result = ask_question()

            if result == "exit":
                print("\nThank you for using IYF Expounder!")
                break


        elif choice == "3":

            print("\nThank you for using IYF Expounder!")
            print("GoodLuck!")
            break

        else:

            print("\nInvalid choice.")
            print("Please choose 1, 2, or 3.")

#START PROGRAM
if __name__ == "__main__":
    main()  