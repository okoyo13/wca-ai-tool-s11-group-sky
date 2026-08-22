from openai import OpenAI
from dotenv import load_dotenv
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
2.We have two classes per day for this course: 
        -10:00 AM to 12:00 PM.
        - 2:00 PM to 4:00 PM.
3.Class duration is 2 hours per session.
4.The class room is found in the MIS building, second floor room 205.
5.You teachers name is Mr. Daniel Chacha but you can call him Chacha. He is a very friendly and approachable teacher.
6.You can reach him through his email: daniel.chacha@we-can-academy.org or personal cell: +254 796 280 700.
7.Chapel classes are held on saturdays only from 08:00 AM to 10:00 AM.
8.The chapel is located on the first floor, conference room where by it is mandatory for students and is part of the curriculum.
9.For this course a students should have:
        -a book.
        -a pen.
        -a laptop.
10.Chapel class duration is 2 hours per session.
11.Each student must attend four chaplain consultation sessions during the three-month program, attendance will be recorded by scanning of the passport.
12.For enrollment a registration/commitment fee of Kes. 1000 is required, whis includes a class passport booklet.
13.A graduation fee will be payable by all students who successfully complete the program.
14.We only accept cash payment only were a receipt will be given to you as a proff of payment, wherebye every receipt should be kept safe until graduation.
15.Three absence will result in expulsion.
16.Missed classed can be recovered by meeting your chaplain.
17.Any attempt to scan another student's QR code to record false attendance is considered fraud and will result in immediate expulsion.
18.You need to scan your passport:
        -At the entrance.
        -After every class.
        -After Chapel class sessions.
        -After Chaplain consultation.
19.A link we be provided to you by your class teacher that will help you track your attendance.
20.You need to know at least one programming languange,a good laptop for this course and positive mind that is ready to learn.
21.Head Chaplain is known as Mika and you can reach him through +254 768 653 081.
22.Mr. Kennedy is the one in charge of the chapel class.
23.The course take 3 month for complition.

"""
def save_output(result):
    """Save the AI response to output.txt."""

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(result)

    print("\nOutput saved successfully to output.txt")

#ASK THE AI A QUESTION

def ask_question():
    """Allow the student to have a continuous conversation."""
    print("\n=====STUDENT SUPPORT=====")
    print("Welcome to AI course")
    print("Type 'exit' to end the convenversation.\n")

    while True:

        question = input("Student:").strip()

    #Exit the conversation and return to the main menu

        if question.lower() == "exit":
            return "exit"
        #Check for empty input 
    
        if not question:
            print("\nPlease Enter a Question.\n")
            continue

        prompt = f"""
ROLE:
You are the IYF We Can Academy Student Support Bot.

TASK:
Your job is to help students using ONLY the knowledge base provided below.

CONTENT:
KNOWLEDGE BASE:
{KNOWLEDGE_BASE}

STUDENT QUESTION:
{question}

CONSTRAINTS:
Rules:
- Use ONLY information that appears in the KNOWLEDGE_BASE
- Do NOT use your own knowledge or make assumptions.
- Do NOT generate examples unless they appear in the KNOWLEDGE_BASE
- Do NOT add explanation beyound the KNOWLEDGE_BASE
- If the answer is not explicitly found in the KNOWLEDGE_BASE respond exactly with:"I'm Sorry,this information is not available please clarify or call +254 708 333 444 for further assistance.
- Do not invent information that is not contained in the knowledge base.
- If the question is unrelated to the knowledge base, do not make up an answer.
- If the question requires a decision, special permission, personal assistance, orinformation that is not contained in the knowledge base, tell the student that human intervention is required.
- If the question is unclear or ambiguous, ask the student to clarify it.
- Be polite and helpful.
- For questions about school rules, fees, attendance, classes,Chapel, the teacher, location, or equipment, use the knowledge base.
- Never invent school policies,fees, schedules, contacts locations or attendance rules.

OUTPUT:
- Give a clear and concise answer
- Use simple English suitable for students.
"""

        try:
            print("\nThinking...")

            response = client.responses.create(
                model="gpt-5.4-mini",
                input=prompt
            )

            result = response.output_text

            print("\n===== ANSWER =====")
            print(result)

            save_output(result)

            print()

        except Exception as error:
            print("\n=====ERRROR=====")
            print("The bot could not generate a response.")
            print(error)


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
        print("MIS Building, Second Floor, Room 205")

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
        

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            artificial_intelligence_json()

        elif choice == "2":
            result = ask_question()

            if result == "exit":
                print("\nThank you for using IYF Expounder!")
                print("GoodLuck!")
                break


        else:

            print("\nInvalid choice.")
            print("Please choose 1, or 2.")

#START PROGRAM
if __name__ == "__main__":
    main()  